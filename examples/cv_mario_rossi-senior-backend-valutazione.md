---
title: "Valutazione CV – Mario Rossi"
subtitle: "Senior Backend Engineer – Piattaforma pagamenti – 22 settembre 2026"
lang: it
---

**Decisione:** Chiamare (era: Chiamare per verificare)
**Gate obbligatori:** Passa (era: Da verificare)  ·  **Aderenza (A):** 93/100 (era 86)  ·  **Contenuto CV (B):** 42/100  ·  **Grafica CV (C):** 79/100
**In una riga:** Tech Lead su piattaforma di pagamenti PCI-DSS, 8 anni di backend Java in ambito finanziario, crescita esplicita fino alla guida di un team di 6; rischio: i due requisiti che chiudono il gate sono affermazioni del candidato, non evidenze documentali.

*Aggiornato il 22 settembre 2026 dopo l'intervista di riscrittura (fase 9): 3 righe hanno cambiato stato. Le righe marcate `Dichiarato` sono affermazioni dirette del candidato, non evidenze documentali.*

# Requisiti usati
Fonte: JD `examples/jd_senior_backend.md`. Pesi: standard.
- Obbligatori: 5+ anni di esperienza backend Java/Kotlin; Spring Boot e architetture a microservizi; Kubernetes in produzione; sistemi di pagamento o contesti regolamentati (PSD2, PCI-DSS); inglese fluente.
- Graditi: esperienza AWS; Kafka o altri sistemi di messaging; esperienza come tech lead / mentoring.

La sede (Milano, ibrido 2 giorni) non è marcata come requisito nella JD: non entra nel gate e va in "Da chiarire al colloquio".

# Dati non considerati
Data di nascita (12/03/1981), luogo di nascita, stato civile e figli ("Coniugato, 2 figli"), segnaposto fotografia ("[foto]"). Elencati solo per dichiarare che non sono stati usati in nessun criterio. Non pesa su nessun criterio nemmeno l'interruzione fra il 2019 e il 2021, che diventa una domanda neutra.

# A0. Gate requisiti obbligatori
| Requisito | Stato | Evidenza (citazione dal CV) |
|----------------|----------|-----------------------------------|
| 5+ anni backend Java/Kotlin | Verificato | "Sviluppo backend Java/Oracle per sistemi di core banking" (2016–2019) e "Migrazione monolite Java a microservizi Spring Boot" (2021 – oggi): 3 + 5 = 8 anni, ±1 anno per esperienza |
| Spring Boot e microservizi | Verificato | "Migrazione monolite Java a microservizi Spring Boot su Kubernetes" |
| Kubernetes in produzione | Dichiarato | Era `Dedotto`. "In produzione da marzo 2022: tre cluster EKS, il team gestisce deploy e reperibilità, il picco sta intorno alle 400 richieste al secondo" (intervista, 22 settembre 2026) |
| Sistemi di pagamento o contesti regolamentati | Verificato | "Guida di un team di 6 sviluppatori su piattaforma di pagamenti"; "sistemi di core banking". In intervista il candidato ha aggiunto: "la piattaforma è certificata PCI-DSS, seguo io la parte applicativa dell'audit annuale dal 2023; su PSD2 abbiamo implementato la SCA sui pagamenti con carta" (22 settembre 2026). La riga era già `Verificato` dal documento e resta tale |
| Inglese fluente | Dichiarato | Era `Non verificabile`. "Metà del team FinSoft è a Lisbona: riunioni di architettura e code review sono in inglese da quattro anni. Non ho certificazioni" (intervista, 22 settembre 2026) |

**Esito gate:** Passa (era `Da verificare`): due requisiti sono passati a `Dichiarato`, nessun `Assente`. Entrambi restano domande per il colloquio: nessun documento li sostiene.

# A. Aderenza al ruolo
| # | Criterio | Livello 0–4 | Peso | Evidenza (citazione dal CV) |
|------|------------------|---------|--------|------------------------------------------|
| A1 | Esperienza pertinente | 4 | 30% | anni: 2016–2019 + 2021–2026 = 3 + 5 = 8 (±1 anno per esperienza), tutti backend Java in ambito finanziario: "core banking" e "piattaforma di pagamenti". Sopra i 5 richiesti, in contesto affine. Gli anni 2010–2016 su "Siti web PHP/MySQL, WordPress" non sono conteggiati |
| A2 | Competenze tecniche | 4 (era 3) | 25% | obbligatorie: Java `Verificato`, Spring Boot e microservizi `Verificato`, dominio pagamenti `Verificato`, Kubernetes `Dichiarato`, inglese `Dichiarato` — tutte coperte, due però solo da affermazioni del candidato. gradite: tech lead `Verificato` ("Guida di un team di 6 sviluppatori"), AWS `Dichiarato` ("i cluster sono su EKS, usiamo RDS Aurora e S3; la certificazione l'ho presa dopo, nel 2023" — intervista, 22 settembre 2026), messaging `Dichiarato` ("Kafka non l'ho mai usato; su FinSoft usiamo RabbitMQ per gli eventi di pagamento"), quindi Kafka in senso stretto `Assente` ma il requisito gradito cita "o altri sistemi di messaging". L'elenco di 17 voci del CV è stato ridimensionato dal candidato stesso: "Go l'ho usato per due tool interni, Rust e Blockchain mai in un progetto, Machine Learning solo un corso" |
| A3 | Risultati e impatto | 3 | 15% | "Riduzione tempi di deploy del 70%" e "team di 6 sviluppatori" sono misurati e attribuibili, ma solo nell'esperienza in corso; Banca XYZ e WebAgency Blu riportano mansioni ("Sviluppo backend Java/Oracle", "Gestione clienti") senza misura. L'intervista non ha chiuso la lacuna: sulla copertura dei test in Banca XYZ la risposta è un intervallo ("stava intorno al 60-70% quando sono uscito"), quindi nessuna cifra utilizzabile. Livello invariato |
| A4 | Crescita e responsabilità | 4 | 15% | progressione esplicita: "Developer – WebAgency Blu" (2010–2016) → "Senior Developer – Banca XYZ" (2016–2019) → "Tech Lead – FinSoft S.r.l." (2021 – oggi), con portata dichiarata ("team di 6 sviluppatori") |
| A5 | Formazione e certificazioni | 3 | 15% | "Laurea triennale in Informatica, Università di Milano (2005)" pertinente; "Certificazione AWS Solutions Architect Associate (2023)" recente ma allineata a un requisito gradito, non al nucleo della JD (Java, Spring, Kubernetes, pagamenti) |
**Punteggio A:** (4·30 + 4·25 + 3·15 + 4·15 + 3·15) / 4 = (120 + 100 + 45 + 60 + 45) / 4 = 370 / 4 = **93** (era **86**: A2 sale da 3 a 4 perché l'intervista ha coperto Kubernetes, inglese, AWS e messaging; gli altri quattro criteri sono invariati, compreso A3, che l'intervista non ha migliorato).

Regola di decisione: gate `Passa` con punteggio A ≥ 75 → **Chiamare** (era **Chiamare per verificare**). Il cambio viene dall'intervista, non dalla riscrittura: il documento non è ancora cambiato. Due dei requisiti che chiudono il gate sono `Dichiarato` e vanno riverificati al colloquio.

# B. Contenuto del CV (Guida Galattica)
| # | Voce | Esito | Nota |
|------|-------------------|-----------|-----------------------------------------------|
| B1 | Sintesi | Parziale | Una pagina, nessuna ripetizione, nessun formato Europass; però la riga di testata è occupata da data e luogo di nascita, stato civile e figli, che non servono alla selezione |
| B2 | Lingua coerente con l'annuncio | Sì | Annuncio in italiano, CV in italiano |
| B3 | Contatti | Parziale | Email professionale e telefono in alto, ma mescolati ai dati anagrafici; nessun LinkedIn, nessun GitHub o portfolio |
| B4 | About Me | No | "Senior developer con forte passione per la tecnologia, team player, problem solver, orientato al risultato. Esperto di tutte le principali tecnologie moderne": frasi vuote, nessun job title attuale (è Tech Lead), nessun obiettivo professionale |
| B5 | Esperienze professionali | Parziale | Tutte con azienda, ruolo, date e bullet su tecnologie e risultati, struttura uniforme; ma date con soli anni (il conteggio resta ±1 anno per esperienza) e nessuna sede |
| B6 | Crescita leggibile | Sì | Developer → Senior Developer → Tech Lead emerge dalla sola sequenza, in ordine di data decrescente |
| B7 | Formazione | Sì | "Laurea triennale in Informatica, Università di Milano (2005)", con istituto e anno; nessun percorso in corso da dichiarare |
| B8 | Competenze tecniche | No | 17 voci in un blocco indistinto: Go, Rust, Machine Learning, Blockchain e Scrum Master non compaiono in nessuna esperienza, "DevOps" e "Scrum Master" non sono tecnologie. L'elenco gonfiato toglie credibilità anche alle voci vere |
| B9 | Soft skill | No | "team player, problem solver, orientato al risultato": esattamente il set standard che la Guida indica di non usare, e senza un episodio che lo sostenga |
| B10 | Corsi e certificazioni | Parziale | "Certificazione AWS Solutions Architect Associate (2023)" ha l'anno e l'ente implicito nel nome, ma sta dentro Formazione senza una sezione propria |
| B11 | Pubblicazioni | N/A | Il profilo non ne riporta |
| B12 | Lingue | Parziale | Entrambe con livello ("madrelingua", "buono"), ma in scala informale: nessun riferimento QCER e nessuna certificazione. È il punto su cui resta aperto il gate |
| B13 | Hobby e interessi | No | Sezione assente |
| B14 | Autorizzazione al trattamento dati | No | Frase assente |
| B15 | Foto | N/A | Nessuna immagine nel documento: al suo posto il segnaposto testuale "[foto]", rimasto visibile nel PDF |
**Punteggio B:** (3 Sì · 1 + 5 Parziale · 0,5) / 13 voci non N/A · 100 = 5,5 / 13 · 100 = **42**

# C. Grafica e tipografia
Rendering: 1 pagina; esaminata la pagina 1 (unica pagina e unico gruppo strutturale indicato da `render_pages.py`). Il PDF nasce da una conversione del sorgente Markdown: formato pagina (216×279 mm, Letter) e sostituzione dei font (LiberationSerif) sono scelte del convertitore e non vengono giudicate.
| # | Voce | Esito | Nota (dove) |
|------|-------------------|-----------|-----------------------------------------------|
| C1 | Allineamento a sinistra | Sì | Nome, titoli di sezione e corpo tutti allineati a sinistra; nessun blocco centrato |
| C2 | Niente giustificato, niente sillabazione | Sì | Spaziatura fra parole uniforme su tutta la pagina, nessuna parola spezzata a fine riga |
| C3 | Stessa gerarchia, stessa x | Sì | I tre titoli di esperienza e i cinque titoli di sezione partono dalla stessa distanza dal margine sinistro; i punti elenco di Formazione sono rientrati come livello inferiore |
| C4 | Date leggibili | No | Sezione Esperienze: le date stanno fra parentesi dentro la riga di intestazione, subito dopo il nome dell'azienda, senza colonna a destra né riga dedicata; nel paragrafo compatto si perdono fra i trattini dei bullet |
| C5 | Margini | Sì | Margini del testo 25 mm a sinistra, 28 mm a destra, 32 mm in alto: nulla a filo dei bordi |
| C6 | Separazione sezioni | Sì | Solo spaziatura verticale, nessun divisore e nessuno sfondo colorato |
| C7 | Spaziatura gerarchica | Parziale | Sezione Esperienze: lo stacco fra due esperienze è quasi uguale a quello fra un titolo di sezione e il suo corpo, quindi il livello non si distingue dalla spaziatura |
| C8 | Niente orfani né vedove | No | Terza esperienza (WebAgency Blu): "clienti" resta da solo sull'ultima riga; anche la riga dei contatti chiude con "1234567 [foto]" |
| C9 | Pagine e densità | Sì | Una pagina, corpo a 12 pt, nessuna compressione; l'ultimo terzo della pagina (89 mm) resta bianco, ma il testo non è stato schiacciato |
| C10 | Typeface | Sì | Una sola famiglia di testo (LiberationSerif, regular e bold); SymbolMT compare solo nei due punti elenco di Formazione |
| C11 | Dimensioni e gerarchia | Sì | Corpo 12 pt, titoli di sezione 16 pt, nome 20 pt: gerarchia in tre passi senza salti drammatici, uguale in tutte le sezioni |
| C12 | Grassetto parco | Sì | Grassetto solo su ruolo e azienda in apertura di ogni esperienza, mai dentro il testo |
| C13 | Colore | Sì | Un solo colore oltre al nero (blu) su nome e titoli di sezione, sfondo bianco, nessun color coding delle competenze |
| C14 | Leggibilità complessiva | Parziale | Nome e sezioni si trovano subito, il ruolo attuale no: il profilo dice "Senior developer" mentre l'esperienza in corso è Tech Lead, e le tre esperienze sono blocchi di testo continuo in cui le responsabilità non si scorrono |
**Punteggio C:** (10 Sì · 1 + 2 Parziale · 0,5) / 14 voci non N/A · 100 = 11 / 14 · 100 = **79**

I punteggi B e C non entrano nella decisione né in un eventuale ranking: misurano il documento, non il candidato.

# Punti di forza
- Otto anni di backend Java tutti in ambito finanziario, contro i cinque richiesti, senza deviazioni di dominio nell'ultimo decennio (A1).
- Il dominio della posizione è coperto da due esperienze distinte: "piattaforma di pagamenti" in FinSoft e "core banking" in Banca XYZ (A0, quarto requisito).
- L'architettura chiesta dall'annuncio è quella del lavoro in corso: "Migrazione monolite Java a microservizi Spring Boot su Kubernetes" (A0, secondo requisito; A2).
- Progressione di ruolo esplicita e leggibile dalla sola sequenza delle esperienze, fino alla guida di sei persone (A4, B6).
- Un risultato misurato e attribuibile, "Riduzione tempi di deploy del 70%", coerente con la migrazione descritta sopra (A3).

# Rischi e lacune
- I due requisiti che chiudono il gate, inglese e Kubernetes in produzione, sono coperti solo da affermazioni del candidato: nessun documento li sostiene (A0, `Dichiarato`). Il CV originale continua a dire "Inglese (buono)".
- Kafka in senso stretto non c'è: "Kafka non l'ho mai usato" (A2). Il requisito gradito è salvo solo perché la JD ammette "altri sistemi di messaging" e il candidato dichiara RabbitMQ.
- Nessun risultato misurato prima del 2021: sui test automatici in Banca XYZ l'unica risposta è un intervallo, inutilizzabile (A3).
- L'esperienza AWS è reale ma emerge solo in intervista: il CV la mostra unicamente come certificazione del 2023, ottenuta dopo l'uso (A2, A5).
- L'elenco competenze del CV porta cinque voci che nessuna esperienza sostiene e che il candidato stesso ha ridimensionato: finché resta così, abbassa l'affidabilità anche delle voci vere (A2, B8).

# Da chiarire al colloquio
1. Inglese: la fluenza è affermata in intervista ("riunioni di architettura e code review in inglese da quattro anni") ma non documentata e senza certificazione. Va verificata conducendo parte del colloquio in inglese. (A0, riga "Inglese fluente", stato `Dichiarato`.)
2. Kubernetes: l'esercizio in produzione è affermato in intervista (tre cluster EKS, ~400 richieste al secondo di picco, reperibilità sul team). Chiedere incidenti gestiti, strategia di rollout e chi possiede i cluster. (A0, riga "Kubernetes in produzione", stato `Dichiarato`.)
3. Pagamenti: qual è stato il suo ruolo preciso nell'audit PCI-DSS e nell'implementazione della SCA, e che cosa ha deciso in prima persona? (A0 quarto requisito; A2.)
4. Risultati prima del 2021: c'è un numero recuperabile sull'introduzione dei test automatici in Banca XYZ, o su qualunque altro effetto misurabile di quel periodo? (A3, livello 3.)
5. Cosa ha fatto fra il 2019 e il 2021? Domanda neutra, non pesa su nessun criterio.

# Spunti di conversazione
- Il passaggio da siti web PHP e WordPress al core banking, nel 2016, è un cambio di dominio netto: come è avvenuto.
- La certificazione AWS del 2023 arriva dopo anni di uso dichiarato della piattaforma: interessante capire perché l'ha presa allora.
- Due dei sei sviluppatori del team sono stati portati dall'ingresso in azienda al ruolo senior: un percorso di mentoring da farsi raccontare.
- Il CV non riporta hobby o interessi e l'intervista non li ha toccati: nessun altro spunto disponibile.

# Feedback sul documento (per il candidato)
- Togliere dalla testata data e luogo di nascita, stato civile, figli e il segnaposto "[foto]", rimasto nel PDF come testo: occupano la riga più letta del CV e non servono alla selezione (B1, B15).
- Riscrivere il profilo. Oggi dice "team player, problem solver, orientato al risultato" ed "esperto di tutte le principali tecnologie moderne": nessuna delle due frasi è verificabile in una riga sotto. Al loro posto ruolo attuale, anni, stack portante e dominio (B4, B9).
- Ridurre le competenze alle voci che compaiono in un'esperienza, in ordine di forza e raggruppate per etichetta: un elenco di 17 tecnologie fa dubitare anche di Java e Kubernetes (B8).
- Aggiungere LinkedIn e un eventuale GitHub come link, e l'autorizzazione al trattamento dei dati (B3, B14).
- Nel PDF le esperienze perdono i punti elenco e si appiattiscono in un paragrafo unico, con le date incastonate fra parentesi: mettere le date su una colonna o una riga dedicata e verificare che i bullet sopravvivano alla conversione (C4, C7, C14).
