#!/usr/bin/env python
"""Verifica di cv_to_pdf.py. Uso: python test_cv_to_pdf.py

Due casi, che sono i due modi in cui l'impaginazione puo' fallire:
un CV corto deve stare in una pagina, un CV troppo lungo deve essere respinto
invece di produrre in silenzio un PDF di due pagine.

Controlla anche che il documento prodotto usi una sola famiglia di caratteri:
i bullet di pandoc escono in Symbol e farebbero fallire la voce C10 della
rubrica sul CV prodotto dalla skill stessa.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "cv_to_pdf.py"

HEAD = """---
title: "Mario Rossi"
subtitle: "Senior Backend Engineer"
author: "Milano · mario.rossi@example.com"
lang: it
---

# Profilo

Dieci anni di sviluppo backend su Java e PostgreSQL, con responsabilita' di architettura.

# Esperienza

**Acme S.p.A.** — Senior Backend Engineer · 2018 – oggi · Milano

- Architettura dei servizi di pagamento, 2.000 richieste al secondo.
- Riduzione dei tempi di deploy del 70%.
"""

FILLER = """
**Azienda {n}** — Backend Engineer · 20{a} – 20{b} · Milano

- Sviluppo di servizi REST in Java con persistenza su PostgreSQL e cache Redis.
- Integrazione con sistemi esterni tramite code di messaggi e webhook firmati.
- Automazione del rilascio con pipeline di integrazione continua.
"""


def run(md_text: str, extra: list[str]) -> tuple[int, str]:
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "cv.md"
        src.write_text(md_text, encoding="utf-8")
        r = subprocess.run(
            [sys.executable, str(SCRIPT), str(src), "--no-docx", *extra],
            capture_output=True, text=True,
        )
        return r.returncode, r.stdout + r.stderr


def fonts_of(md_text: str) -> set[str]:
    import fitz
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "cv.md"
        src.write_text(md_text, encoding="utf-8")
        out = Path(tmp) / "cv.pdf"
        subprocess.run([sys.executable, str(SCRIPT), str(src), "--out", str(out), "--no-docx"],
                       capture_output=True, text=True)
        with fitz.open(str(out)) as doc:
            return {f[3].split("+")[-1].split("-")[0] for f in doc[0].get_fonts(full=True)}


def main() -> int:
    failures = []

    code, out = run(HEAD, [])
    if code != 0 or "pagine: 1" not in out:
        failures.append(f"CV corto: atteso codice 0 e una pagina, ottenuto {code}\n{out}")

    lungo = HEAD + "".join(FILLER.format(n=i, a=10 + i, b=11 + i) for i in range(12))
    code, out = run(lungo, ["--compact"])
    if code != 2:
        failures.append(f"CV lungo: atteso codice 2, ottenuto {code}\n{out}")

    famiglie = fonts_of(HEAD)
    if len(famiglie) > 1:
        failures.append(f"attesa una sola famiglia di caratteri, trovate: {sorted(famiglie)}")

    for f in failures:
        print("FALLITO:", f)
    if failures:
        return 1
    print("ok  3 verifiche superate")
    return 0


if __name__ == "__main__":
    sys.exit(main())
