# Template CV monopagina

Struttura del CV riscritto, pensata per stare in una pagina e per soddisfare i blocchi B e C
della rubrica. Il file si converte con `scripts/cv_to_pdf.py`.

## Regole di scrittura del file

- **Blocco YAML in testa**: `title` è il nome, `subtitle` il titolo professionale, `author` la
  riga dei contatti. Sono i tre elementi della testata; `cv_to_pdf.py` li impagina come tali.
- **Titoli di sezione** con `#`. Niente `##` se non per raggruppamenti interni.
- **Niente interruzioni di riga con `\`**: non sopravvivono alla conversione in DOCX e le righe
  si attaccano. Per andare a capo si usa un paragrafo nuovo, cioè una riga vuota.
- **Niente tabelle, immagini, barre di livello, stelline**: gli ATS non le leggono (voce B8).
- **Grassetto** solo su nome dell'azienda ed etichette delle competenze: sono i segnalibri per
  chi scorre (voce C12). Mai grassetto dentro i bullet.
- Ogni esperienza ha una riga di intestazione `**Azienda** — Ruolo · date · sede` seguita dai
  bullet. Stessa forma per tutte: è la voce B5.
- Esperienze in ordine di data di fine decrescente, senza eccezioni: è ciò che rende leggibile
  la crescita (voce B6).

## Sezioni

L'ordine è fisso. Le sezioni senza contenuto si tolgono, non si lasciano vuote.

| # | Sezione | Contenuto |
|---|---------|-----------|
| 1 | Testata | Nome, titolo professionale, contatti su una riga |
| 2 | Profilo | 4–6 righe: anni, ruolo attuale, responsabilità più alta ricoperta, tecnologie portanti |
| 3 | Esperienza | 3–5 voci con bullet, più una riga di sintesi per tutto il resto |
| 4 | Competenze | 3–5 righe etichettate, la più pertinente al ruolo per prima |
| 5 | Formazione e lingue | Titoli con anno, lingue con livello |
| 6 | Altre sezioni | Divulgazione, pubblicazioni, certificazioni: solo se pertinenti al ruolo |
| 7 | Autorizzazione dati | Una riga, se il candidato la vuole |

## Scheletro

```markdown
---
title: "<Nome Cognome>"
subtitle: "<Titolo professionale>"
author: "<Città> · <telefono> · <email> · <link>"
lang: it
---

# Profilo

<4-6 righe. Anni di esperienza con il conto implicito, ruolo attuale, responsabilità più alta
ricoperta, tecnologie portanti. Niente frasi vuote: ogni affermazione deve essere verificabile
in una riga sotto.>

# Esperienza

**<Azienda>** — <Ruolo> · <mese anno> – <mese anno | oggi> · <Sede>

- <Responsabilità principale, con le tecnologie che contano per il ruolo target.>
- <Risultato con un numero, se il numero esiste.>
- <Altra responsabilità o risultato.>

**<Azienda>** — <Ruolo> · <anno> – <anno> · <Sede>

- <...>

**Altre esperienze** — <una riga per le esperienze che non meritano un blocco, e una riga di
sintesi per tutto ciò che precede la finestra di rilevanza.>

# Competenze

**<Etichetta più pertinente al ruolo>** — <voci, dalla più forte>

**<Etichetta>** — <voci>

# Formazione e lingue

<Titolo, istituto (anno)> · <Titolo, istituto (anno)> · <Lingua livello, lingua livello>

# <Sezione facoltativa: Divulgazione / Pubblicazioni / Certificazioni>

<2-3 righe.>

Autorizzo il trattamento dei miei dati personali ai sensi del D.Lgs. 101/2018.
```

## Quanto ci sta in una pagina

Con il profilo di spaziatura predefinito, una A4 con margini di 20 mm e corpo a 10 pt contiene
circa **48 righe** di testo, spaziature fra sezioni comprese; con `--compact` circa 54. Una riga
piena è di circa 100 caratteri.

Budget indicativo: testata 3, profilo 6, esperienze 24–28, competenze 5, formazione 2,
sezione facoltativa 3, autorizzazione 1.

Il conteggio è una stima: la verifica è sempre l'esecuzione di `cv_to_pdf.py`, che stampa il
numero di pagine e il riempimento della prima.
