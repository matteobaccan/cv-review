# Template report

## Report singolo CV

Sezioni fisse, in quest'ordine, nessuna in più. Compilare ogni riga; niente sezioni vuote (scrivere `Nessuno` o `N/A`). Il file inizia con il blocco YAML (titolo e sottotitolo: `title` e `subtitle` finiscono nella **copertina** del PDF) e usa titoli di primo livello `#` per le sezioni: è ciò che `scripts/report_to_pdf.py` si aspetta. Mantieni le righe separatrici delle tabelle come nel template: nel PDF le larghezze delle colonne seguono il numero di trattini.

**Nome del file:** `<nome-cv>-<posizione>-valutazione.md` (`<posizione>` abbreviata, minuscola, con trattini), oppure `<nome-cv>-valutazione.md` se non c'è una posizione di riferimento. Lo stesso candidato si valuta su più annunci: senza la posizione nel nome, il secondo report sovrascrive il primo.

**Due regole che valgono per ogni report:**

- **Requisiti dedotti.** Se i requisiti non vengono da una JD reale, dichiaralo in "Requisiti usati". Se poi è proprio un requisito dedotto a far fallire il gate, scrivi accanto alla decisione quale sarebbe l'esito trattandolo come gradito: un candidato non si scarta su un requisito scritto da chi valuta.
- **Pagine esaminate.** Nella riga "Rendering" del blocco C elenca le pagine che hai davvero guardato e perché sono sufficienti (di norma quelle indicate da `render_pages.py`). Un blocco C compilato su pagine non viste non è tracciabile.

```markdown
---
title: "Valutazione CV – <Nome Cognome>"
subtitle: "<Titolo posizione | Analisi del documento (senza posizione di riferimento)> – <data>"
lang: it
---

**Decisione:** <Chiamare | Chiamare se ci sono posti | Chiamare per verificare | Non procedere>
**Gate obbligatori:** <Passa | Da verificare | Non passa>  ·  **Aderenza (A):** <0–100>/100  ·  **Contenuto CV (B):** <0–100>/100  ·  **Grafica CV (C):** <0–100 | N/A>/100
**In una riga:** <profilo in ≤ 30 parole: ruolo attuale, anni pertinenti, punti forti, rischio principale>

# Requisiti usati
Fonte: <JD `file` | JD da URL: <indirizzo>, recuperata il <data> | requisiti dedotti dalla richiesta>. Pesi: <standard | modificati: ...>.
- Obbligatori: <elenco>
- Graditi: <elenco>

# Dati non considerati
<elenco di ciò che il CV riporta tra i dati protetti, es. "data di nascita, stato civile, foto">, oppure `Nessuno`.

# A0. Gate requisiti obbligatori
| Requisito | Stato | Evidenza (citazione dal CV) |
|----------------|----------|-----------------------------------|
| ... | Verificato / Dichiarato / Dedotto / Non verificabile / Assente | "..." |

# A. Aderenza al ruolo
| # | Criterio | Livello 0–4 | Peso | Evidenza (citazione dal CV) |
|------|------------------|---------|--------|------------------------------------------|
| A1 | Esperienza pertinente | | 30% | anni: <conto esplicito, es. 2016–2019 + 2021–2026 = 3 + 5 = 8> |
| A2 | Competenze tecniche | | 25% | obbligatorie: ...; gradite: ... |
| A3 | Risultati e impatto | | 15% | |
| A4 | Crescita e responsabilità | | 15% | |
| A5 | Formazione e certificazioni | | 15% | |
**Punteggio A:** <calcolo: (l1·30 + l2·25 + l3·15 + l4·15 + l5·15) / 4 = N>

# B. Contenuto del CV (Guida Galattica)
| # | Voce | Esito | Nota |
|------|-------------------|-----------|-----------------------------------------------|
| B1 | Sintesi | Sì / Parziale / No / N/A | |
| ... | ... (tutte le 15 voci) | | |
**Punteggio B:** <calcolo>

# C. Grafica e tipografia
Rendering: <N pagine; esaminate le pagine <elenco> (indicate da `render_pages.py`: una per gruppo strutturale, più prima e ultima) | nessuno: blocco N/A>
| # | Voce | Esito | Nota (dove) |
|------|-------------------|-----------|-----------------------------------------------|
| C1 | Allineamento a sinistra | Sì / Parziale / No / N/A | |
| ... | ... (tutte le 14 voci) | | |
**Punteggio C:** <calcolo | N/A>

# Punti di forza
- <max 5, ciascuno con riferimento a una riga A/B/C>

# Rischi e lacune
- <max 5, solo elementi con stato Dedotto / Non verificabile / Assente>

# Da chiarire al colloquio
1. <max 5 domande, in ordine di priorità; la prima copre il gate se "Da verificare"; ognuna riferita a una riga del report>

# Spunti di conversazione
- <hobby, tesi, pubblicazioni, certificazioni "aspirazionali" (es. PM/Scrum) citati nel CV>, oppure `Nessuno`

# Feedback sul documento (per il candidato)
- <max 5 correzioni concrete tratte dalle righe B/C con esito No/Parziale, in ordine di impatto>, oppure `Nessuno`
```

## Report aggiornato dopo l'intervista (fase 9)

Se la fase di riscrittura raccoglie risposte che coprono righe del blocco A, il report **non si
riscrive da capo**: si aggiorna quello esistente, sempre con le stesse sezioni. Tre sole aggiunte,
tutte dentro sezioni già previste:

1. Sotto il blocco in testa, una riga in corsivo con la data dell'intervista e quante righe hanno
   cambiato stato:
   `*Aggiornato il <data> dopo l'intervista di riscrittura (fase 9): <N> righe hanno cambiato stato. Le righe marcate `Dichiarato` sono affermazioni dirette del candidato, non evidenze documentali.*`
2. Nelle righe cambiate, lo stato `Dichiarato` con l'evidenza nella forma
   `Era <stato precedente>. <citazione della risposta> (intervista, <data>)`.
3. Nel calcolo del punteggio A, il valore precedente fra parentesi e il motivo del cambio.

Una risposta può **peggiorare** il quadro: un requisito `Non verificabile` che il candidato
dichiara di non possedere diventa `Assente` e fa fallire il gate. L'esito va scritto come viene,
mai ammorbidito.

## Ranking di più CV

Prima tutti i report singoli, poi questa tabella in `ranking.md`. Ordina per gate (`Passa` > `Da verificare` > `Non passa`), poi per punteggio A decrescente. Stessi pesi per tutti. B e C sono solo informativi.

```markdown
# Ranking – <Titolo posizione> – <N> CV valutati il <data>

Pesi: <standard | modificati: ...>. Requisiti obbligatori: <elenco>.

| Pos. | Candidato | Gate | A /100 | B /100 | C /100 | Decisione | Rischio principale | Report |
|------|-----------|------|--------|--------|--------|-----------|--------------------|--------|
| 1 | ... | Passa | 82 | 60 | 71 | Chiamare | ... | `<file>.md` |

Esclusi al gate: <nomi e requisito mancante>, oppure `Nessuno`.
```
