#!/usr/bin/env python
"""Converte un report di valutazione (Markdown) nel PDF ufficiale di cv-review.

Uso:
    python report_to_pdf.py <report.md> --out "<cartella>/<nome-cv>-valutazione.pdf" [--cv "Nome file CV"]

Catena: Markdown -> DOCX (pandoc, con stili generati qui) -> PDF (LibreOffice) ->
copertina (pymupdf) + intestazione, pie' di pagina, contatore "Pagina X di Y" e link alla skill (pymupdf).

Dipendenze: pandoc, LibreOffice (soffice), pymupdf, python-docx.
Il logo e' in ../assets/logo.png (relativo a questo script).
"""
import argparse
import datetime as dt
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SKILL_URL = "https://github.com/matteobaccan/cv-review"
SKILL_URL_SHORT = "github.com/matteobaccan/cv-review"
GUIDO_PENTA_SHORT = "github.com/GuidoPenta/galactic-CV-guide-for-developers"
LICENSE_TEXT = "Licenza MIT \u2013 software libero"
MONTHS_IT = [
    "gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno",
    "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre",
]
HERE = Path(__file__).resolve().parent
LOGO = HERE.parent / "assets" / "logo.png"

# Palette (coerente con il logo)
INK = (0x15 / 255, 0x3E / 255, 0x4C / 255)      # #153E4C
MUTED = (0x4A / 255, 0x6C / 255, 0x78 / 255)    # #4A6C78
RULE = (0xB8 / 255, 0xCC / 255, 0xD3 / 255)     # #B8CCD3

BODY_FONT = "Calibri"       # LibreOffice sostituisce con Carlito se assente
FONT_FILES = [              # per intestazione e pie' di pagina
    Path(r"C:\Windows\Fonts\calibri.ttf"),
    Path("/usr/share/fonts/truetype/crosextra/Carlito-Regular.ttf"),
    Path("/Library/Fonts/Calibri.ttf"),
]

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


def _get_font():
    """Ritorna (fontname, fontfile, fitz.Font) per copertina, intestazione e pie' di pagina."""
    import fitz

    fontfile = next((str(f) for f in FONT_FILES if f.exists()), None)
    fname = "cvr" if fontfile else "helv"
    font = fitz.Font(fontfile=fontfile) if fontfile else fitz.Font("helv")
    return fname, fontfile, font


def data_italiana(d: dt.date) -> str:
    """Data in formato italiano (es. 21 settembre 2026)."""
    return f"{d.day} {MONTHS_IT[d.month - 1]} {d.year}"


def parse_yaml_frontmatter(md_text: str) -> dict:
    """Estrae i campi del front matter YAML (title, subtitle, ...) dal report Markdown."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", md_text, re.DOTALL)
    if not m:
        return {}
    result = {}
    for line in m.group(1).split("\n"):
        line = line.strip()
        if not line or ":" not in line:
            continue
        key, val = line.split(":", 1)
        val = val.strip()
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]
        result[key.strip()] = val
    return result


# --------------------------------------------------------------------------- #
# 0. copertina
# --------------------------------------------------------------------------- #
def create_cover_page(title: str, subtitle: str, out_path: Path) -> None:
    """Crea la pagina di copertina (PDF) con logo e informazioni sul report.

    Riporta la data di valutazione e la posizione, il logo del progetto, la nota
    sull'analisi realizzata tramite IA (suggerimenti da verificare), lo scopo
    (migliorare il CV seguendo la Guida Galattica per il CV di Guido Penta) e
    il riferimento al progetto open source con licenza MIT.
    """
    import fitz

    fname, fontfile, font_obj = _get_font()

    doc = fitz.open()
    page = doc.new_page(width=595, height=842)  # A4 in punti
    w, h = page.rect.width, page.rect.height
    cx = w / 2
    lm = 2.0 * 28.35
    rm = w - 2.0 * 28.35

    def tw(text, size):
        return font_obj.text_length(text, fontsize=size)

    def centered_text(y, s, size, color=INK):
        page.insert_text(
            (cx - tw(s, size) / 2, y), s, fontsize=size,
            fontname=fname, fontfile=fontfile, color=color,
        )

    def wrapped_lines(y, lines, size, color=INK, spacing=None):
        if spacing is None:
            spacing = size * 1.5
        for line in lines:
            centered_text(y, line, size, color)
            y += spacing
        return y

    # --- Logo ---
    y = 7 * 28.35
    if LOGO.exists():
        logo_px = fitz.Pixmap(str(LOGO))
        logo_h = 1.8 * 28.35
        logo_w = logo_h * logo_px.width / logo_px.height
        logo_x = (w - logo_w) / 2
        page.insert_image(fitz.Rect(logo_x, y, logo_x + logo_w, y + logo_h), pixmap=logo_px)
        y += logo_h + 30
    else:
        y += 20

    # --- Titolo ---
    y += 10
    centered_text(y, "VALUTAZIONE CURRICULUM VITAE", 24, INK)
    y += 45

    # --- Nome candidato ---
    name = title
    for prefix in ("Valutazione CV \u2013", "Valutazione CV -"):
        if name.startswith(prefix):
            name = name[len(prefix):].strip()
            break
    centered_text(y, name, 18, INK)
    y += 35

    # --- Posizione e data (subtitle) ---
    centered_text(y, subtitle, 13, MUTED)
    y += 35

    # --- Divisore ---
    page.draw_line((lm, y), (rm, y), color=RULE, width=1)
    y += 25

    # --- Nota sull'analisi AI ---
    y += 10
    y = wrapped_lines(y, ["NOTA SULL'ANALISI"], 12, INK, 22)
    y += 5
    y = wrapped_lines(y, [
        "Questo report \u00e8 stato generato tramite Intelligenza Artificiale.",
        "Le indicazioni contenute sono da intendersi come suggerimenti",
        "e devono essere valutate e verificate prima di essere applicate.",
    ], 10.5, MUTED, 16)
    y += 20

    # --- Scopo dell'analisi ---
    y = wrapped_lines(y, [
        "Scopo dell'analisi \u00e8 migliorare il curriculum vitae",
        "seguendo le indicazioni della Guida Galattica per il CV",
        "di Guido Penta.",
    ], 10.5, INK, 16)
    centered_text(y, GUIDO_PENTA_SHORT, 9.5, (0x1F / 255, 0x5F / 255, 0x73 / 255))
    y += 16
    centered_text(y, "distribuita con licenza MIT.", 10.5, INK)
    y += 30

    # --- Sezione finale: riferimenti ---
    y_bdiv = h - 4.5 * 28.35
    page.draw_line((lm, y_bdiv), (rm, y_bdiv), color=RULE, width=0.6)
    y_foot = y_bdiv + 18
    centered_text(y_foot, "Per informazioni: progetto open source, licenza MIT.", 10, MUTED)
    y_foot += 16
    centered_text(y_foot, SKILL_URL_SHORT, 10, INK)

    link_w = tw(SKILL_URL_SHORT, 10)
    page.insert_link({
        "kind": fitz.LINK_URI,
        "from": fitz.Rect(cx - link_w / 2, y_foot - 10, cx + link_w / 2, y_foot + 3),
        "uri": SKILL_URL,
    })
    y_foot += 18
    centered_text(y_foot, LICENSE_TEXT, 9, MUTED)

    doc.save(str(out_path))
    doc.close()


# --------------------------------------------------------------------------- #
# 1. reference.docx con gli stili del report
# --------------------------------------------------------------------------- #
def build_reference_docx(target: Path) -> None:
    from docx import Document
    from docx.enum.section import WD_ORIENT  # noqa: F401
    from docx.oxml import parse_xml
    from docx.oxml.ns import nsdecls
    from docx.shared import Cm, Pt, RGBColor

    default = subprocess.run(
        ["pandoc", "-o", str(target), "--print-default-data-file", "reference.docx"],
        capture_output=True,
    )
    if default.returncode != 0 or not target.exists():
        raise RuntimeError("pandoc non disponibile o reference.docx non generato")

    doc = Document(str(target))
    st = doc.styles

    def font(style_name, size, bold=None, color=None, name=BODY_FONT):
        s = st[style_name]
        s.font.name = name
        s.font.size = Pt(size)
        if bold is not None:
            s.font.bold = bold
        if color is not None:
            s.font.color.rgb = RGBColor.from_string(color)
        # font anche per i set east-asian / complex script, altrimenti Word ignora
        rpr = s.element.get_or_add_rPr()
        rfonts = rpr.find("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rFonts")
        if rfonts is None:
            rfonts = parse_xml(f'<w:rFonts {nsdecls("w")}/>')
            rpr.append(rfonts)
        for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
            rfonts.set(f"{{http://schemas.openxmlformats.org/wordprocessingml/2006/main}}{attr.split(':')[1]}", name)
        return s

    def spacing(style_name, before=None, after=None, line=None):
        pf = st[style_name].paragraph_format
        if before is not None:
            pf.space_before = Pt(before)
        if after is not None:
            pf.space_after = Pt(after)
        if line is not None:
            pf.line_spacing = line

    font("Normal", 10.5, color="222222")
    spacing("Normal", before=0, after=5, line=1.15)
    font("Body Text", 10.5, color="222222")
    spacing("Body Text", before=0, after=5, line=1.15)
    font("First Paragraph", 10.5, color="222222")
    font("Compact", 9.5, color="222222")           # celle delle tabelle
    spacing("Compact", before=1, after=1, line=1.1)
    from docx.enum.text import WD_ALIGN_PARAGRAPH

    font("Title", 24, bold=True, color="153E4C")
    spacing("Title", before=0, after=2)
    st["Title"].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    font("Subtitle", 11.5, bold=False, color="4A6C78")
    spacing("Subtitle", before=0, after=14)
    st["Subtitle"].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    font("Heading 1", 15, bold=True, color="153E4C")
    spacing("Heading 1", before=16, after=5)
    font("Heading 2", 12.5, bold=True, color="1F5F73")
    spacing("Heading 2", before=12, after=4)
    font("Heading 3", 11, bold=True, color="1F5F73")

    # Bordo inferiore sottile sotto Heading 1
    h1 = st["Heading 1"].element.get_or_add_pPr()
    h1.append(parse_xml(
        f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="6" w:space="2" w:color="B8CCD3"/></w:pBdr>'
    ))

    # Tabelle: righe orizzontali leggere, intestazione con sfondo e grassetto
    tbl = st["Table"].element
    for old in tbl.findall("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tblPr"):
        tbl.remove(old)
    tbl.append(parse_xml(
        f'<w:tblPr {nsdecls("w")}>'
        '<w:tblBorders>'
        '<w:top w:val="single" w:sz="8" w:space="0" w:color="153E4C"/>'
        '<w:bottom w:val="single" w:sz="8" w:space="0" w:color="153E4C"/>'
        '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="D9E4E8"/>'
        '<w:left w:val="nil"/><w:right w:val="nil"/><w:insideV w:val="nil"/>'
        '</w:tblBorders>'
        '<w:tblCellMar><w:top w:w="50" w:type="dxa"/><w:bottom w:w="50" w:type="dxa"/>'
        '<w:left w:w="80" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tblCellMar>'
        '</w:tblPr>'
    ))
    tbl.append(parse_xml(
        f'<w:tblStylePr {nsdecls("w")} w:type="firstRow">'
        '<w:rPr><w:b/><w:color w:val="153E4C"/></w:rPr>'
        '<w:tcPr><w:shd w:val="clear" w:color="auto" w:fill="EAF1F4"/>'
        '<w:tcBorders><w:bottom w:val="single" w:sz="8" w:space="0" w:color="153E4C"/></w:tcBorders></w:tcPr>'
        '</w:tblStylePr>'
    ))

    # Pagina A4 con spazio per intestazione e pie' di pagina
    for sec in doc.sections:
        sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
        sec.top_margin, sec.bottom_margin = Cm(3.2), Cm(2.6)
        sec.left_margin, sec.right_margin = Cm(2.0), Cm(2.0)
        sec.header_distance, sec.footer_distance = Cm(1.0), Cm(1.0)

    doc.save(str(target))


# --------------------------------------------------------------------------- #
# 2. intestazione, pie' di pagina, contatore, link
# --------------------------------------------------------------------------- #
def decorate_pdf(pdf_in: Path, pdf_out: Path, cv_label: str) -> None:
    import fitz

    fname, fontfile, measure = _get_font()

    def width(text, size):
        return measure.text_length(text, fontsize=size)

    def text(page, x, y, s, size, color, align="left"):
        if align == "right":
            x -= width(s, size)
        elif align == "center":
            x -= width(s, size) / 2
        page.insert_text((x, y), s, fontsize=size, fontname=fname, fontfile=fontfile, color=color)

    doc = fitz.open(pdf_in)
    total = doc.page_count
    today = dt.date.today().strftime("%d/%m/%Y")
    logo_px = fitz.Pixmap(str(LOGO)) if LOGO.exists() else None

    for i, page in enumerate(doc, 1):
        w, h = page.rect.width, page.rect.height
        lm, rm = 2.0 * 28.35, w - 2.0 * 28.35   # margini 2 cm in punti

        # --- intestazione ---
        top = 1.0 * 28.35
        logo_h = 0.95 * 28.35
        if logo_px:
            logo_w = logo_h * logo_px.width / logo_px.height
            page.insert_image(fitz.Rect(lm, top, lm + logo_w, top + logo_h), pixmap=logo_px)
        text(page, rm, top + logo_h * 0.45, "Valutazione CV", 9.5, INK, align="right")
        text(page, rm, top + logo_h * 0.45 + 12, cv_label, 8.5, MUTED, align="right")
        y_rule = top + logo_h + 6
        page.draw_line((lm, y_rule), (rm, y_rule), color=RULE, width=0.6)

        # --- pie' di pagina ---
        y_frule = h - 1.55 * 28.35
        page.draw_line((lm, y_frule), (rm, y_frule), color=RULE, width=0.6)
        y = y_frule + 12
        text(page, lm, y, SKILL_URL_SHORT, 8.5, INK)
        link_rect = fitz.Rect(lm, y - 9, lm + width(SKILL_URL_SHORT, 8.5), y + 3)
        page.insert_link({"kind": fitz.LINK_URI, "from": link_rect, "uri": SKILL_URL})
        text(page, (lm + rm) / 2, y, f"Report generato il {today} con la skill cv-review", 8, MUTED, align="center")
        text(page, rm, y, f"Pagina {i} di {total}", 8.5, INK, align="right")

    doc.set_metadata({
        "title": f"Valutazione CV – {cv_label}",
        "author": "cv-review",
        "subject": "Report di valutazione CV",
        "keywords": "cv, valutazione, cv-review, claude code",
        "creator": SKILL_URL,
    })
    doc.save(str(pdf_out), garbage=3, deflate=True)
    doc.close()


# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("report", help="report in Markdown (dal template della skill)")
    ap.add_argument("--out", help="PDF di destinazione (default: <report>.pdf)")
    ap.add_argument("--cv", help="etichetta del CV nell'intestazione (default: nome del PDF senza -valutazione)")
    args = ap.parse_args()

    src = Path(args.report)
    if not src.exists():
        print(f"[errore] non trovato: {src}", file=sys.stderr)
        return 1
    out = Path(args.out) if args.out else src.with_suffix(".pdf")
    out.parent.mkdir(parents=True, exist_ok=True)
    cv_label = args.cv or out.stem.replace("-valutazione", "")

    # Metadati per la copertina (dal front matter del report)
    yml = parse_yaml_frontmatter(src.read_text(encoding="utf-8"))
    if yml.get("title"):
        title = yml["title"]
        subtitle = yml.get("subtitle") or f"Analisi del documento \u2013 {data_italiana(dt.date.today())}"
    else:
        # Report senza front matter (es. ranking.md): l'etichetta e' la posizione.
        title = cv_label
        subtitle = f"Report generato il {data_italiana(dt.date.today())}"

    with tempfile.TemporaryDirectory() as tmp:
        tmpd = Path(tmp)
        try:
            ref = tmpd / "reference.docx"
            build_reference_docx(ref)

            docx = tmpd / "report.docx"
            r = subprocess.run(
                ["pandoc", str(src), "--reference-doc", str(ref), "-o", str(docx)],
                capture_output=True, text=True,
            )
            if r.returncode != 0:
                raise RuntimeError(f"pandoc: {r.stderr.strip()}")

            r = subprocess.run(
                [find_soffice(), "--headless", "--convert-to", "pdf", "--outdir", str(tmpd), str(docx)],
                capture_output=True, text=True, timeout=240,
            )
            raw_pdf = tmpd / "report.pdf"
            if r.returncode != 0 or not raw_pdf.exists():
                raise RuntimeError(f"LibreOffice: {r.stderr.strip() or r.stdout.strip()}")

            # Pagine del report decorate con intestazione e pie' di pagina
            decorated_pdf = tmpd / "decorated.pdf"
            decorate_pdf(raw_pdf, decorated_pdf, cv_label)

            # Copertina + report unificati nel PDF finale
            cover_pdf = tmpd / "cover.pdf"
            create_cover_page(title, subtitle, cover_pdf)

            import fitz
            final = fitz.open()
            with fitz.open(cover_pdf) as cover_doc:
                final.insert_pdf(cover_doc)
            with fitz.open(decorated_pdf) as report_doc:
                final.insert_pdf(report_doc)
            final.set_metadata({
                "title": f"Valutazione CV \u2013 {cv_label}",
                "author": "cv-review",
                "subject": "Report di valutazione CV",
                "keywords": "cv, valutazione, cv-review, claude code",
                "creator": SKILL_URL,
            })
            final.save(str(out), garbage=3, deflate=True)
            final.close()
        except Exception as e:  # noqa: BLE001
            print(f"[errore] {e}", file=sys.stderr)
            return 2

    print(f"ok  {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
