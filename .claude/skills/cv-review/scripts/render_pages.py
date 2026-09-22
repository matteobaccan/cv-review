#!/usr/bin/env python
"""Renderizza le pagine di un CV (PDF, DOCX, ODT, RTF, HTML) in PNG per la valutazione grafica.

Uso:
    python render_pages.py <file> [--out DIR] [--dpi 110]

Output: <DIR>/<nome>-p1.png, -p2.png ... (default DIR = ./render). Stampa i percorsi
generati e le informazioni tipografiche rilevabili dal PDF (numero pagine, font usati
con dimensioni e numero di caratteri, margini del blocco di testo).

I formati diversi da PDF vengono convertiti in PDF con LibreOffice (soffice); se non
e' disponibile, lo script termina con errore e la valutazione grafica va segnata N/A.

Dipendenze: pymupdf (fitz). Per DOCX/ODT/RTF/HTML anche LibreOffice.
"""
import argparse
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

CONVERTIBLE = {".docx", ".doc", ".odt", ".rtf", ".html", ".htm"}

SOFFICE_CANDIDATES = [
    "soffice",
    r"C:\Program Files\LibreOffice\program\soffice.exe",
    r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
    "/Applications/LibreOffice.app/Contents/MacOS/soffice",
    "/usr/bin/soffice",
    "/usr/lib/libreoffice/program/soffice",
]


def find_soffice() -> str | None:
    for c in SOFFICE_CANDIDATES:
        if shutil.which(c) or Path(c).exists():
            return c
    return None


def to_pdf(path: Path, workdir: Path) -> Path:
    soffice = find_soffice()
    if not soffice:
        raise RuntimeError("LibreOffice (soffice) non trovato: impossibile convertire in PDF")
    r = subprocess.run(
        [soffice, "--headless", "--convert-to", "pdf", "--outdir", str(workdir), str(path)],
        capture_output=True, text=True, timeout=180,
    )
    pdf = workdir / f"{path.stem}.pdf"
    if r.returncode != 0 or not pdf.exists():
        raise RuntimeError(f"conversione fallita: {r.stderr.strip() or r.stdout.strip()}")
    return pdf


def typography_report(doc) -> str:
    import fitz  # noqa: F401  (pymupdf)

    fonts: Counter = Counter()
    sizes: Counter = Counter()
    lines = [f"pagine: {doc.page_count}"]
    for i, page in enumerate(doc, 1):
        w, h = page.rect.width, page.rect.height
        text_rect = None
        for b in page.get_text("dict")["blocks"]:
            if b.get("type") != 0:
                continue
            for l in b["lines"]:
                for s in l["spans"]:
                    if not s["text"].strip():
                        continue
                    fonts[s["font"]] += len(s["text"])
                    sizes[round(s["size"], 1)] += len(s["text"])
                    r = fitz_rect(s["bbox"])
                    text_rect = r if text_rect is None else text_rect | r
        if text_rect is not None:
            pt = 72 / 25.4  # punti per mm
            lines.append(
                f"pagina {i}: {w/pt:.0f}x{h/pt:.0f} mm; margini testo (mm) "
                f"sx {text_rect.x0/pt:.0f}, dx {(w-text_rect.x1)/pt:.0f}, "
                f"alto {text_rect.y0/pt:.0f}, basso {(h-text_rect.y1)/pt:.0f}"
            )
    lines.append("font (caratteri): " + ", ".join(f"{f} ({n})" for f, n in fonts.most_common()))
    lines.append("dimensioni pt (caratteri): " + ", ".join(f"{s} ({n})" for s, n in sorted(sizes.items())))
    families = {f.split("-")[0].split(",")[0] for f in fonts}
    lines.append(f"famiglie distinte (stima): {len(families)} -> {', '.join(sorted(families))}")

    groups, wanted = pages_to_inspect(doc)
    lines.append("gruppi strutturali: " + " | ".join(as_ranges(g) for g in groups))
    lines.append(
        "pagine da esaminare: " + as_ranges(wanted)
        + f" (su {doc.page_count}; una per gruppo, piu' prima e ultima). "
        "Dichiara nel report quali pagine hai guardato."
    )
    return "\n".join(lines)


def fitz_rect(bbox):
    import fitz
    return fitz.Rect(*bbox)


def page_signature(page) -> tuple:
    """Impronta strutturale di una pagina: colonna di testo, corpo, immagini.

    Due pagine con la stessa impronta hanno lo stesso impianto grafico: guardarne
    una sola basta per compilare il blocco C.

    Entra solo cio' che dipende dall'impianto: i margini laterali (dove sta la
    colonna di testo), la dimensione del corpo dominante, la presenza di immagini.
    Restano fuori il margine superiore e l'insieme dei corpi presenti, che dipendono
    da dove cade il testo e da quali titoli capitano su quella pagina: sono
    contenuto, non struttura, e spezzerebbero il raggruppamento senza motivo.
    """
    pt = 72 / 25.4
    w = page.rect.width
    rect = None
    sizes: Counter = Counter()
    for b in page.get_text("dict")["blocks"]:
        if b.get("type") != 0:
            continue
        for line in b["lines"]:
            for s in line["spans"]:
                if not s["text"].strip():
                    continue
                sizes[round(s["size"], 1)] += len(s["text"])
                r = fitz_rect(s["bbox"])
                rect = r if rect is None else rect | r
    if rect is None:
        return ("vuota",)

    def mm5(v):  # margini arrotondati a 5 mm: sotto e' rumore di impaginazione
        return round(v / pt / 5) * 5

    return (
        mm5(rect.x0), mm5(w - rect.x1),
        sizes.most_common(1)[0][0],
        bool(page.get_images()),
    )


def pages_to_inspect(doc):
    """Raggruppa le pagine per impronta e indica quali vanno guardate.

    Una per gruppo, piu' sempre la prima e l'ultima: la prima porta testata e
    contatti, l'ultima e' dove si vede se il documento finisce mezzo vuoto (C9).
    """
    groups: dict = {}
    for i, page in enumerate(doc, 1):
        groups.setdefault(page_signature(page), []).append(i)
    ordered = sorted(groups.values(), key=lambda g: g[0])
    wanted = {g[0] for g in ordered} | {1, doc.page_count}
    return ordered, sorted(wanted)


def as_ranges(pages) -> str:
    out, start, prev = [], pages[0], pages[0]
    for n in pages[1:] + [None]:
        if n != prev + 1:
            out.append(str(start) if start == prev else f"{start}-{prev}")
            start = n
        prev = n
    return ", ".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--out", default="render")
    ap.add_argument("--dpi", type=int, default=110)
    args = ap.parse_args()

    try:
        import fitz
    except ImportError:
        print("[errore] pymupdf non installato: pip install pymupdf", file=sys.stderr)
        return 1

    src = Path(args.file)
    if not src.exists():
        print(f"[errore] non trovato: {src}", file=sys.stderr)
        return 1

    if src.suffix.lower() not in CONVERTIBLE | {".pdf"}:
        print(f"[errore] formato non renderizzabile: {src.suffix} (blocco C = N/A)", file=sys.stderr)
        return 2

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        try:
            pdf = src if src.suffix.lower() == ".pdf" else to_pdf(src, Path(tmp))
        except Exception as e:  # noqa: BLE001
            print(f"[errore] {e}", file=sys.stderr)
            return 2

        doc = fitz.open(pdf)
        zoom = args.dpi / 72
        for i, page in enumerate(doc, 1):
            target = out / f"{src.stem}-p{i}.png"
            page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False).save(str(target))
            print(f"ok  pagina {i} -> {target}")
        print(typography_report(doc))
        doc.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
