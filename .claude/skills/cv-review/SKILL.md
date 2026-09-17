---
name: cv-review
description: Use when asked to evaluate, screen, score, rank or compare one or more CVs/resumes (PDF, DOCX, MD, TXT) against a job description, role profile or list of requirements, or to judge a CV's content, layout and typography; also when a recruiter asks "chiamo questo candidato?", "chi convoco?", "shortlist", "valuta questo CV", "confronta questi curriculum", "com'è fatto questo CV".
---

# Valutare un CV

## Panoramica

Una valutazione utile è **confrontabile** (stessa rubrica per tutti i CV), **tracciabile** (ogni giudizio cita il CV o una pagina renderizzata) e **non discriminatoria** (ignora i dati protetti). Il giudizio lo dà l'output del contratto sotto, non un voto a sensazione.

Tre blocchi, sempre tutti: **A** aderenza al ruolo (decide), **B** contenuto del CV secondo la [Guida Galattica per il CV](https://github.com/GuidoPenta/galactic-CV-guide-for-developers), **C** grafica e tipografia secondo [Your CV looks like sh*t](https://github.com/SimonDiff/devs-cv-typography-guidelines).

## Quando usare

- Screening di uno o più CV contro una job description (JD) o un elenco di requisiti
- Shortlist / ranking di più candidati per la stessa posizione
- "Vale la pena chiamarlo?" con poco tempo a disposizione
- Feedback su come è fatto un CV (contenuto e impaginazione)

Non usare per: scrivere o riscrivere un CV al posto del candidato, preparare il candidato a un colloquio.

## Procedura

1. **Testo del CV.** Per file non testuali esegui `python scripts/extract_text.py <file|cartella>` (cartella → un `.txt` per CV). Se l'output è vuoto il PDF è una scansione: segnalalo e fermati, non inventare.
2. **Rendering.** Per PDF/DOCX esegui `python scripts/render_pages.py <file>` e guarda ogni PNG prodotto con il tool di lettura immagini. Lo script stampa anche font, dimensioni e margini rilevati: usali come evidenza per il blocco C. Se il rendering non è possibile, il blocco C è `N/A`.
3. **Requisiti.** Se manca la JD, chiedila o ricavala dalla richiesta e scrivi in testa al report i requisiti che stai usando. Separa **obbligatori** da **graditi**. Se la richiesta è solo "com'è fatto questo CV", compila B e C e scrivi `N/A` nel blocco A.
4. **Dati da ignorare.** Prima di giudicare, elenca nella sezione "Dati non considerati" tutto ciò che il CV riporta tra: età/data di nascita, genere, foto, stato civile/figli, nazionalità/luogo di nascita, religione, salute, opinioni. Non usarli mai, neanche per dedurre la sede o l'anzianità.
5. **Rubrica.** Compila `rubric.md` per intero. Blocco A: ogni riga ha stato dell'evidenza (`Verificato` / `Dedotto` / `Non verificabile` / `Assente`) e citazione testuale; mai `Verificato` per ciò che è solo plausibile. Blocchi B e C: esito `Sì` / `Parziale` / `No` / `N/A` con nota su dove.
6. **Punteggio e decisione.** Applica il calcolo e la regola di decisione della rubrica. Il gate sugli obbligatori viene prima del punteggio; B e C non entrano mai nella decisione né nel ranking.
7. **Report.** Produci il report con `report-template.md`, sezioni nell'ordine indicato, nessuna sezione in più o in meno. Un solo CV → report nella risposta, salvato come `<nome-cv>.md` solo se l'utente indica una cartella. Più CV → cartella `valutazioni/` (o quella indicata): un `<nome-cv>.md` per CV più `ranking.md`.

## Regole fisse

- **Gap e cambi frequenti** vanno in "Da chiarire al colloquio", mai come penalità o red flag.
- **Sede/disponibilità**: usa solo ciò che il CV dichiara esplicitamente (indirizzo, "disponibile a trasferimento"). Altrimenti `Non verificabile`.
- **Anni di esperienza**: calcolali dalle date, sull'anno corrente, e mostra il conto (es. 2016–2019 + 2021–oggi = 3 + 5 = 8).
- **Competenze elencate ma mai usate** nelle esperienze contano `Dedotto` al massimo, mai `Verificato`.
- **Blocco C solo da immagini**: nessuna voce grafica si compila dal testo estratto.
- Le **domande di verifica** sono al massimo 5, ognuna legata a un'evidenza `Dedotto`/`Non verificabile`/`Assente` del report.
- Ranking di più CV: solo dopo aver compilato tutte le rubriche con gli stessi pesi; ordina per gate, poi per punteggio A.

## Riferimenti

| File | Contenuto |
|------|-----------|
| `rubric.md` | Blocco A (criteri, pesi, livelli 0–4, gate, decisione), blocco B (15 voci di contenuto), blocco C (14 voci grafiche) |
| `report-template.md` | Template report singolo e tabella ranking |
| `scripts/extract_text.py` | Estrazione testo da PDF/DOCX/HTML/MD (vedi `--help`) |
| `scripts/render_pages.py` | PDF/DOCX → PNG per pagina + font, dimensioni, margini rilevati (vedi `--help`) |

## Errori comuni

| Errore | Correzione |
|--------|------------|
| Voto globale "8/10" senza criteri | Compila la rubrica: il voto è calcolato, non stimato |
| "OK (probabile)" su un requisito obbligatorio | Stato `Dedotto` o `Non verificabile`; il gate resta aperto |
| Dedurre sede o età da luogo/data di nascita o anno di laurea | Sono dati non considerati; usa solo dichiarazioni esplicite |
| Gap come red flag | Va in "Da chiarire", non pesa sul punteggio |
| Lista competenze presa per buona | Verifica ogni skill nelle esperienze; altrimenti `Dedotto` |
| Giudicare l'impaginazione dal testo estratto | Solo dai PNG renderizzati; altrimenti C è `N/A` |
| CV brutto → candidato scartato | B e C misurano il documento; la decisione dipende solo da gate e punteggio A |
| Ranking fatto CV per CV mentre si legge | Prima tutte le rubriche, poi la tabella |
| Report in formato libero diverso da CV a CV | Stesso template, stesse sezioni, stesso ordine |
