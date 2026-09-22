# Rubrica di valutazione CV

Tre blocchi indipendenti, sempre tutti e tre:

- **Blocco A – Aderenza al ruolo**: quanto il candidato corrisponde alla job description (JD). È l'unico blocco che decide.
- **Blocco B – Contenuto del CV**: quanto il documento è fatto bene, secondo la
  [Guida Galattica per il CV](https://github.com/GuidoPenta/galactic-CV-guide-for-developers) di Guido Penta (MIT).
- **Blocco C – Grafica e tipografia**: quanto il documento è leggibile a colpo d'occhio, secondo
  [Your CV looks like sh*t](https://github.com/SimonDiff/devs-cv-typography-guidelines) di Simon Di Fresco (CC0).

B e C misurano il documento, non la persona: un ottimo candidato con un CV brutto resta un ottimo candidato.

## Stato dell'evidenza

Ogni riga del blocco A porta uno stato e una citazione testuale del CV.

| Stato | Significato |
|-------|-------------|
| `Verificato` | Scritto esplicitamente nel CV, in un'esperienza, formazione o certificazione datata |
| `Dichiarato` | Affermato dal candidato in risposta a una domanda, ma non presente nel CV. Vale solo se la risposta è diretta e riferita a lui; va citata come le righe del CV |
| `Dedotto` | Plausibile da ciò che è scritto, ma non esplicito (es. skill elencata ma mai usata in un'esperienza; "piattaforma su Kubernetes" senza "in produzione") |
| `Non verificabile` | Il CV non dice nulla in merito e non c'è base per dedurlo |
| `Assente` | Il CV contraddice il requisito o mostra chiaramente che manca (es. richiesto inglese fluente, dichiarato "scolastico") |

Regola: in dubbio tra `Verificato` e `Dedotto`, scegli `Dedotto`.

`Dichiarato` non si usa nello screening ordinario, dove l'unica fonte è il documento: compare solo
quando il candidato ha risposto direttamente, cioè nella fase di riscrittura (`rewrite-guide.md`) o
dopo un colloquio di verifica. È più forte di `Dedotto`, perché non è un'inferenza di chi valuta ma
un'affermazione della persona, e più debole di `Verificato`, perché nessun documento datato la
sostiene. Nel report va sempre accompagnato dalla citazione della risposta e dalla data in cui è
stata data.

### Convenzioni per i casi ricorrenti

| Caso | Regola |
|------|--------|
| Livello di lingua richiesto "fluente" | Dichiarato madrelingua / C1 / C2 / fluente / professionale → `Verificato`; buono / B2 / intermedio → `Non verificabile`; scolastico / base / A1–B1 → `Assente`; non dichiarato → `Non verificabile`. Una certificazione (IELTS, TOEFL, Cambridge) con livello ≥ C1 → `Verificato` |
| Sede / modalità di lavoro nella JD | Entra nel gate solo se la JD la marca come requisito ("richiesta residenza", "obbligatoria presenza"). Altrimenti non è un requisito: se il CV non dichiara indirizzo o disponibilità, va in "Da chiarire" |
| Date con soli anni | Conta la differenza secca tra gli anni (2016–2019 = 3); "oggi" = anno corrente. Scrivi "±1 anno per esperienza" accanto al totale |
| Ruolo di lead / manager | Conta come esperienza tecnica se l'esperienza cita le tecnologie usate; se cita solo attività di gestione, conta per A4 ma non per A1/A2 |
| Skill richiesta presente solo come certificazione | `Dedotto` per A2; `Verificato` per A5 |
| Requisito coperto da una risposta del candidato | `Dichiarato`, con citazione della risposta; il criterio si ricalcola e il report dice quali righe sono cambiate |
| Risultati (A3) distribuiti in modo disomogeneo | Valuta l'insieme della carriera pesando di più le esperienze recenti: risultati misurati solo nell'ultima esperienza → livello 3 |

## Blocco A – Aderenza al ruolo

### A0. Gate sui requisiti obbligatori (non pesato)

Una riga per ogni requisito obbligatorio della JD, con stato e citazione.

| Esito gate | Condizione |
|------------|------------|
| `Passa` | tutti `Verificato`, `Dichiarato` o `Dedotto` |
| `Da verificare` | almeno un `Non verificabile`, nessun `Assente` |
| `Non passa` | almeno un `Assente` |

Un requisito coperto solo da `Dichiarato` fa passare il gate, ma resta una domanda da porre: va
sempre in "Da chiarire al colloquio", perché è l'unico stato che nessun documento sostiene.

Se la JD non distingue obbligatori e graditi, considera obbligatori quelli marcati "richiesto/required/must" o con soglia numerica ("5+ anni"); gli altri sono graditi. Scrivilo nel report.

### A1–A5. Criteri pesati (livelli 0–4)

| # | Criterio | Peso | 0 | 2 | 4 |
|---|----------|------|---|---|---|
| A1 | Esperienza pertinente (anni e contesto simile alla JD) | 30% | Nessuna esperienza nel dominio/stack | Metà degli anni richiesti, o anni pieni ma in dominio diverso | Anni ≥ richiesti in contesto affine, ruoli continuativi |
| A2 | Competenze tecniche richieste (obbligatorie + gradite) | 25% | Quasi nessuna delle skill richieste | Metà delle skill, per lo più `Dedotto` | Tutte le obbligatorie `Verificato`, la maggior parte delle gradite presenti |
| A3 | Risultati e impatto dimostrati | 15% | Solo mansioni ("sviluppo backend") | Qualche risultato senza misura | Risultati misurati e attribuibili ("−70% tempi di deploy", "team di 6") |
| A4 | Crescita e responsabilità | 15% | Stesso ruolo per tutta la carriera senza segnali di crescita | Crescita implicita (aziende/progetti più grandi) | Progressione esplicita di ruolo e responsabilità (dev → senior → lead) |
| A5 | Formazione e certificazioni pertinenti | 15% | Nessuna pertinente | Formazione generica, o certificazione datata/non pertinente | Titolo pertinente e certificazioni recenti allineate alla JD |

Livelli 1 e 3 sono intermedi. Se la JD ha priorità diverse (es. ruolo junior: A1 e A4 pesano meno, A5 di più) adatta i pesi e dichiaralo in testa al report; i pesi devono essere identici per tutti i CV dello stesso ranking.

**Punteggio A** = Σ (livello × peso) / 4, arrotondato all'intero (0–100).
Esempio: livelli 4,3,4,4,3 → (4·30 + 3·25 + 4·15 + 4·15 + 3·15) / 4 = (120+75+60+60+45)/4 = 90.

## Blocco B – Contenuto del CV (Guida Galattica)

Una riga per voce, esito `Sì` / `Parziale` / `No` / `N/A`, con nota breve.

| # | Voce | Cosa verificare |
|---|------|-----------------|
| B1 | Sintesi | Contenuto essenziale, senza ripetizioni; niente formato Europass |
| B2 | Lingua coerente con l'annuncio | JD in inglese → CV in inglese, e viceversa |
| B3 | Contatti | Email professionale, telefono, LinkedIn e GitHub/portfolio come link; in alto, non in fondo |
| B4 | About Me | Presente; contiene job title attuale, tecnologie principali, obiettivo professionale; niente frasi vuote ("orientato al risultato", "esperto di tutte le tecnologie") |
| B5 | Esperienze professionali | Ogni esperienza con date inizio/fine e azienda; bullet su progetti, tecnologie, risultati; struttura uniforme |
| B6 | Crescita leggibile | La progressione di ruoli emerge dalla sequenza delle esperienze |
| B7 | Formazione | Laurea/diploma con date; percorsi in corso (università, academy, bootcamp) dichiarati con data prevista di fine |
| B8 | Competenze tecniche | Elenco ordinato con le skill più forti per prime; coerenti con le esperienze; niente barre/stelline non leggibili dagli ATS; niente elenchi gonfiati |
| B9 | Soft skill | Presenti e specifiche; non il set standard "team player, problem solver, lavora sotto pressione" |
| B10 | Corsi e certificazioni | Sezione presente se pertinente, con ente e anno |
| B11 | Pubblicazioni | Se presenti: titolo, data, sede, DOI. `N/A` se il profilo non ne ha |
| B12 | Lingue | Livello dichiarato per ogni lingua, certificazioni se esistono |
| B13 | Hobby e interessi | Presenti (la Guida li considera spunti di conversazione, non criterio di merito) |
| B14 | Autorizzazione al trattamento dati | Frase presente (D.Lgs. 101/2018: non obbligatoria, ma evita un passaggio burocratico) |
| B15 | Foto | Se presente: `Sì` solo per "presente", nessun giudizio sull'aspetto. Se assente: `N/A` |

**Punteggio B** = (Sì × 1 + Parziale × 0,5) / voci non `N/A` × 100, arrotondato all'intero.

## Blocco C – Grafica e tipografia (Your CV looks like sh*t)

Richiede il **rendering delle pagine**: `python scripts/render_pages.py <cv.pdf|cv.docx>` produce un PNG per pagina; guardali tutti prima di compilare. Se il CV è solo testo (MD, TXT) o il rendering fallisce, tutto il blocco C è `N/A` con nota "nessun rendering disponibile": non dedurre l'impaginazione dal testo estratto.

Una riga per voce, esito `Sì` / `Parziale` / `No` / `N/A`, con nota breve che dica *dove* (es. "sezione Esperienze, seconda voce").

Se il rendering nasce da una conversione (DOCX → PDF), formato pagina (A4/Letter), font sostituiti e interruzioni di pagina possono essere scelte del convertitore: non giudicarli e scrivilo nella riga "Rendering" del report. Valuta solo ciò che dipende dal candidato: allineamenti, gerarchia, spaziature, grassetti, colori.

| # | Voce | Cosa verificare |
|---|------|-----------------|
| C1 | Allineamento a sinistra | Titoli, sezioni e paragrafi allineati a sinistra; centrati ammessi solo per nome e contatti |
| C2 | Niente giustificato, niente sillabazione | Spaziatura tra parole uniforme; nessuna parola spezzata a fine riga |
| C3 | Stessa gerarchia, stessa x | Elementi dello stesso livello (aziende, istituzioni, titoli sezione) alla stessa distanza dal margine sinistro |
| C4 | Date leggibili | Date di impiego allineate in modo coerente (tab a destra o riga dedicata), non distinte solo dallo stile |
| C5 | Margini | Testo non a filo dei bordi; margini simili ai default di un template (≈ 2 cm) |
| C6 | Separazione sezioni | Spaziatura sempre presente, più al massimo uno tra divisori e sfondi colorati; mai tutti e tre |
| C7 | Spaziatura gerarchica | Bullet < esperienze < sezioni, in modo coerente in tutto il documento |
| C8 | Niente orfani né vedove | Nessuna parola sola a fine paragrafo; nessuna riga sola a inizio pagina/colonna |
| C9 | Pagine e densità | Testo non compresso per stare in una pagina; se due pagine, la seconda non è quasi vuota |
| C10 | Typeface | Al massimo 2 famiglie di caratteri; 2–3 pesi; 3–4 stili in totale |
| C11 | Dimensioni e gerarchia | Corpo a dimensione standard (10–12 pt); titoli più grandi/pesanti senza salti drammatici; stessa gerarchia stesso stile in tutte le sezioni |
| C12 | Grassetto parco | Pochi grassetti per esperienza, come segnalibri per chi scorre; non il grassetto come stile di default |
| C13 | Colore | Al massimo un colore oltre al nero, con contrasto sufficiente, usato con parsimonia (nome, titoli); sfondo chiaro, non trasparente; niente color coding delle skill |
| C14 | Leggibilità complessiva | A colpo d'occhio si distinguono nome, ruolo attuale, esperienze e competenze in meno di 10 secondi |

**Punteggio C** = (Sì × 1 + Parziale × 0,5) / voci non `N/A` × 100, arrotondato all'intero. Se tutte le voci sono `N/A`, scrivi `N/A`.

I punteggi B e C **non entrano** nella decisione né nel ranking; compaiono nel report come informazione a sé e come feedback eventualmente da restituire al candidato.

## Regola di decisione

| Gate A0 | Punteggio A | Decisione |
|---------|-------------|-----------|
| `Non passa` | qualsiasi | **Non procedere** (indica quale obbligatorio manca) |
| `Da verificare` | ≥ 60 | **Chiamare per verificare** (prima domanda = il requisito non verificabile) |
| `Da verificare` | < 60 | **Non procedere**, salvo pochi candidati disponibili |
| `Passa` | ≥ 75 | **Chiamare** |
| `Passa` | 55–74 | **Chiamare se ci sono posti** nello screening |
| `Passa` | < 55 | **Non procedere** |

## Dati non considerati

Non usare mai, in nessun criterio: età o data di nascita, genere, foto (aspetto), stato civile e figli,
nazionalità, luogo di nascita, religione, salute, opinioni politiche o sindacali, anno di
diploma/laurea come proxy dell'età. Elencali nel report solo per dichiarare che sono stati ignorati.

Gap temporali e cambi frequenti di lavoro: non pesano su nessun criterio. Vanno nella sezione
"Da chiarire al colloquio" come domanda neutra ("Cosa ha fatto tra il 2019 e il 2021?").
