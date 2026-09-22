#!/usr/bin/env python
"""Converte un CV riscritto (Markdown) in DOCX e PDF su una pagina.

Uso:
    python cv_to_pdf.py <cv.md> [--out <cv.pdf>] [--compact] [--no-docx]

Catena: Markdown -> DOCX (pandoc, con stili generati qui) -> PDF (LibreOffice),
poi conteggio pagine e riempimento della prima pagina (pymupdf).

L'impaginazione rispetta il blocco C della rubrica: una sola famiglia di
caratteri, tutto allineato a sinistra, corpo 10 pt, margini 20 mm, un solo
colore oltre al nero, grassetto usato come segnalibro.

A differenza di report_to_pdf.py, il PDF prodotto non porta logo, intestazione
ne' pie' di pagina: e' il CV del candidato, non un documento della skill.

Due profili di spaziatura, entrambi sopra i minimi tipografici (corpo 10 pt,
interlinea 1.0, margini 18 mm):
    default     interlinea 1.12, stacco fra sezioni 9 pt
    --compact   interlinea 1.04, stacco fra sezioni 7 pt

Codici di uscita: 0 una pagina, 2 piu' di una pagina, 1 errore.

Dipendenze: pandoc, LibreOffice (soffice), pymupdf, python-docx.
"""
import argparse
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

BODY_FONT = "Calibri"       # LibreOffice sostituisce con Carlito se assente
INK = "1A1A1A"
ACCENT = "153E4C"           # unico colore oltre al nero (coerente con il logo)

# Minimi tipografici: sotto questi valori non si scende per far stare il CV
# in una pagina. Si toglie contenuto (voce C9 della rubrica).
MIN_BODY_PT = 10.0
MIN_LINE_SPACING = 1.0
MIN_MARGIN_CM = 1.8

PROFILES = {
    "default": {"line": 1.12, "para_after": 4, "h1_before": 9, "h1_after": 3},
    "compact": {"line": 1.04, "para_after": 3, "h1_before": 7, "h1_after": 2},
}

SOFFICE_CANDIDATES = [
    "soffice",
    r"C:\Program Files\LibreOffice\program\soffice.exe",
    r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
    "/Applications/LibreOffice.app/Contents/MacOS/soffice",
    "/usr/bin/soffice",
]


def find_soffice() -> str:
    for c in SOFFICE_CANDIDATES:
        if shutil.which(c) or Path(c).exists():
            return c
    raise RuntimeError("LibreOffice (soffice) non trovato")


def build_reference_docx(target: Path, profile: dict) -> None:
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import parse_xml
    from docx.oxml.ns import nsdecls
    from docx.shared import Cm, Pt, RGBColor

    assert profile["line"] >= MIN_LINE_SPACING, "interlinea sotto il minimo"

    r = subprocess.run(
        ["pandoc", "-o", str(target), "--print-default-data-file", "reference.docx"],
        capture_output=True,
    )
    if r.returncode != 0 or not target.exists():
        raise RuntimeError("pandoc non disponibile o reference.docx non generato")

    doc = Document(str(target))
    st = doc.styles
    W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

    def font(style, size, bold=None, color=None, name=BODY_FONT):
        s = st[style]
        s.font.name = name
        s.font.size = Pt(size)
        if bold is not None:
            s.font.bold = bold
        if color is not None:
            s.font.color.rgb = RGBColor.from_string(color)
        rpr = s.element.get_or_add_rPr()
        rfonts = rpr.find(f"{W}rFonts")
        if rfonts is None:
            rfonts = parse_xml(f'<w:rFonts {nsdecls("w")}/>')
            rpr.append(rfonts)
        for attr in ("ascii", "hAnsi", "cs", "eastAsia"):
            rfonts.set(f"{W}{attr}", name)
            # gli stili titolo di pandoc puntano al font del tema: se il
            # riferimento al tema resta, vince lui e il font impostato qui
            # viene ignorato (i titoli escono in Arial Black).
            rfonts.attrib.pop(f"{W}{attr}Theme", None)
        s.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        return s

    def spacing(style, before=None, after=None, line=None):
        pf = st[style].paragraph_format
        if before is not None:
            pf.space_before = Pt(before)
        if after is not None:
            pf.space_after = Pt(after)
        if line is not None:
            pf.line_spacing = line

    # corpo
    for s in ("Normal", "Body Text", "First Paragraph"):
        font(s, MIN_BODY_PT, color=INK)
        spacing(s, before=0, after=profile["para_after"], line=profile["line"])
    font("Compact", MIN_BODY_PT, color=INK)
    spacing("Compact", before=0, after=2, line=profile["line"])

    # testata: nome, ruolo, contatti
    font("Title", 22, bold=True, color=ACCENT)
    spacing("Title", before=0, after=1)
    font("Subtitle", 12.5, bold=False, color=ACCENT)
    spacing("Subtitle", before=0, after=1)
    font("Author", 9.5, bold=False, color="4A4A4A")
    spacing("Author", before=0, after=8)

    # sezioni
    font("Heading 1", 11.5, bold=True, color=ACCENT)
    spacing("Heading 1", before=profile["h1_before"], after=profile["h1_after"])
    font("Heading 2", 10.5, bold=True, color=INK)
    spacing("Heading 2", before=6, after=2)

    # filetto sotto i titoli di sezione: con la spaziatura sono i due soli
    # segnali di separazione, mai tre (voce C6)
    h1 = st["Heading 1"].element.get_or_add_pPr()
    h1.append(parse_xml(
        f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="4" w:space="2" w:color="B8CCD3"/></w:pBdr>'
    ))

    for sec in doc.sections:
        sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
        sec.top_margin = sec.bottom_margin = Cm(2.0)
        sec.left_margin = sec.right_margin = Cm(2.0)

    doc.save(str(target))


def use_body_font_for_bullets(docx_path: Path) -> None:
    """Riporta i punti elenco al font del corpo.

    pandoc genera il proprio numbering.xml (non lo eredita dal reference) e usa
    Symbol per i bullet: e' una seconda famiglia di caratteri nel documento e
    fa fallire la voce C10 sul CV prodotto dalla skill stessa.
    """
    with zipfile.ZipFile(docx_path) as z:
        items = {n: z.read(n) for n in z.namelist()}
    if "word/numbering.xml" not in items:
        return

    xml = items["word/numbering.xml"].decode("utf-8")
    for bad in ("Symbol", "Courier New", "Wingdings"):
        xml = xml.replace(f'w:ascii="{bad}"', f'w:ascii="{BODY_FONT}"')
        xml = xml.replace(f'w:hAnsi="{bad}"', f'w:hAnsi="{BODY_FONT}"')
    # glifi dell'area a uso privato di Symbol, assenti nel font del corpo
    xml = xml.replace('w:val="\uf0b7"', 'w:val="\u2022"')
    xml = xml.replace('w:val="\uf0a7"', 'w:val="\u2013"')
    items["word/numbering.xml"] = xml.encode("utf-8")

    with zipfile.ZipFile(docx_path, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in items.items():
            z.writestr(name, data)


def md_to_pdf(src: Path, out_pdf: Path, profile_name: str, keep_docx: bool) -> tuple[int, float]:
    with tempfile.TemporaryDirectory() as tmp:
        td = Path(tmp)
        ref = td / "reference.docx"
        build_reference_docx(ref, PROFILES[profile_name])

        docx = td / (src.stem + ".docx")
        r = subprocess.run(
            ["pandoc", str(src), "-o", str(docx), f"--reference-doc={ref}", "--standalone"],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            print(r.stderr, file=sys.stderr)
            raise RuntimeError("pandoc: conversione in DOCX fallita")
        use_body_font_for_bullets(docx)

        r = subprocess.run(
            [find_soffice(), "--headless", "--convert-to", "pdf", "--outdir", str(td), str(docx)],
            capture_output=True, text=True,
        )
        produced = td / (docx.stem + ".pdf")
        if not produced.exists():
            print(r.stdout, r.stderr, file=sys.stderr)
            raise RuntimeError("LibreOffice: conversione in PDF fallita")

        out_pdf.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(produced, out_pdf)
        if keep_docx:
            shutil.copy2(docx, out_pdf.with_suffix(".docx"))

    import fitz
    with fitz.open(str(out_pdf)) as doc:
        pages = doc.page_count
        page = doc[0]
        blocks = page.get_text("blocks")
        fill = max((b[3] for b in blocks), default=0) / page.rect.height * 100
    return pages, fill


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cv", help="CV riscritto in Markdown (dal template della skill)")
    ap.add_argument("--out", help="PDF di destinazione (default: accanto al .md)")
    ap.add_argument("--compact", action="store_true",
                    help="spaziatura piu' stretta, sempre sopra i minimi tipografici")
    ap.add_argument("--no-docx", action="store_true", help="non scrivere il DOCX accanto al PDF")
    a = ap.parse_args()

    src = Path(a.cv).resolve()
    if not src.exists():
        print(f"errore: {src} non esiste", file=sys.stderr)
        return 1
    out_pdf = Path(a.out).resolve() if a.out else src.with_suffix(".pdf")

    profile = "compact" if a.compact else "default"
    pages, fill = md_to_pdf(src, out_pdf, profile, keep_docx=not a.no_docx)

    print(f"ok  {out_pdf}")
    if not a.no_docx:
        print(f"ok  {out_pdf.with_suffix('.docx')}")
    print(f"pagine: {pages}; riempimento pagina 1: {fill:.0f}%; spaziatura: {profile}")

    if pages > 1:
        hint = ("togliere contenuto" if a.compact
                else "riprovare con --compact, oppure togliere contenuto")
        print(f"ATTENZIONE: il CV occupa {pages} pagine: {hint}.", file=sys.stderr)
        return 2
    if fill < 70:
        print(f"nota: la pagina e' piena al {fill:.0f}%. C'e' spazio per rimettere "
              f"contenuto tolto in fase di scaletta.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
