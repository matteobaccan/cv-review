# Note al CV riscritto – Mario Rossi

> **Questo è un esempio del repository.** Mario Rossi non esiste: il CV di partenza è fittizio e le
> risposte dell'intervista riportate qui sotto sono state scritte come parte dell'esempio, per
> mostrare come la fase 9 usa le risposte del candidato. In un uso reale ogni citazione
> "(intervista)" sarebbe una frase detta dalla persona.

**Questo file non fa parte del CV e non va inviato.** Serve a verificare che nel CV non sia
entrato nulla che non venga dal CV originale o da una risposta.

## Target

CV costruito per una posizione sola: **Senior Backend Engineer – Piattaforma pagamenti**
(`examples/jd_senior_backend.md`), lingua italiana come l'annuncio.

Cosa dipende da questo target: l'ordine delle competenze (Backend prima di tutto, "Dominio" con
PCI-DSS e PSD2 al terzo posto), il numero di bullet dati a FinSoft rispetto alle altre esperienze,
la riga sull'inglese nel profilo, la lingua del documento.

Su un altro annuncio **non si riusa questo CV**: si riparte dal CV originale
(`cv_mario_rossi.pdf`) e da una nuova valutazione. Le risposte dell'intervista, invece, restano
valide e si riusano.

## Mappa origine → riga

| Riga del CV riscritto | Origine |
|---|---|
| Nome, telefono, email | CV originale, testata |
| "Sesto San Giovanni" | Intervista: "Abito a Sesto San Giovanni, l'ibrido su Milano non è un problema" |
| "linkedin.com/in/mariorossi" | Intervista: profilo indicato dal candidato. GitHub non compare: "GitHub non ho niente di pubblico" |
| "Senior Backend Engineer · Tech Lead" | CV originale: ruolo attuale "Tech Lead – FinSoft S.r.l."; il titolo target viene dall'annuncio |
| Profilo, riga 1 (otto anni, core banking e pagamenti) | CV originale: date 2016–2019 e 2021–oggi, "core banking", "piattaforma di pagamenti" |
| Profilo, riga 2 (Tech Lead di sei, PCI-DSS, migrazione, in produzione dal 2022) | CV originale per team, migrazione e stack; intervista per "certificata PCI-DSS" e "in produzione da marzo 2022" |
| Profilo, riga 3 (inglese quotidiano, team distribuito) | Intervista: "Metà del team FinSoft è a Lisbona: riunioni di architettura e code review sono in inglese da quattro anni" |
| FinSoft, bullet 1 (team di 6) | CV originale: "Guida di un team di 6 sviluppatori su piattaforma di pagamenti" |
| FinSoft, bullet 2 (migrazione a microservizi) | CV originale: "Migrazione monolite Java a microservizi Spring Boot su Kubernetes" |
| FinSoft, bullet 3 (tre cluster EKS, ~400 req/s, reperibilità) | Intervista: "In produzione da marzo 2022: tre cluster EKS, il team gestisce deploy e reperibilità, il picco sta intorno alle 400 richieste al secondo" |
| FinSoft, bullet 4 (−70% deploy) | CV originale: "Riduzione tempi di deploy del 70%" |
| FinSoft, bullet 5 (audit PCI-DSS, SCA PSD2) | Intervista: "la piattaforma è certificata PCI-DSS, seguo io la parte applicativa dell'audit annuale dal 2023; su PSD2 abbiamo implementato la SCA sui pagamenti con carta" |
| FinSoft, bullet 6 (RabbitMQ) | Intervista: "Kafka non l'ho mai usato; su FinSoft usiamo RabbitMQ per gli eventi di pagamento" |
| FinSoft, bullet 7 (mentoring, code review a rotazione) | Intervista: "Due dei sei sviluppatori li ho seguiti dall'ingresso in azienda fino al ruolo senior; ho introdotto le code review a rotazione" |
| Banca XYZ, bullet 1 (Java/Oracle core banking) | CV originale |
| Banca XYZ, bullet 2 (test automatici da copertura nulla) | CV originale per JUnit/Mockito; "partendo da una copertura nulla" dall'intervista: "la copertura era partita da zero" |
| WebAgency Blu | CV originale, compresso in un bullet solo |
| Competenze, **Backend** | Tutte presenti in un'esperienza del CV originale, tranne RabbitMQ (intervista) |
| Competenze, **Infrastruttura e cloud** | Kubernetes e Docker dal CV originale; "EKS, RDS Aurora, S3" dall'intervista: "i cluster sono su EKS, usiamo RDS Aurora e S3" |
| Competenze, **Dominio** | CV originale per pagamenti e core banking; PCI-DSS, PSD2 e SCA dall'intervista |
| Competenze, **Altri linguaggi** | Intervista: "Go l'ho usato per due tool interni"; PHP dall'esperienza WebAgency Blu |
| Formazione, laurea e certificazione AWS | CV originale, invariate |
| Lingue | Italiano dal CV originale; la riga sull'inglese riscrive l'uso dichiarato in intervista invece del "buono" del CV |
| Autorizzazione al trattamento dati | Intervista: "L'autorizzazione al trattamento dati mettila" |

Nessuna riga del CV proviene da un'inferenza. Le righe che vengono **solo** dall'intervista, e che
quindi nessun documento sostiene, sono: profilo riga 3, FinSoft bullet 3, 5, 6 e 7, la riga
"Sesto San Giovanni", l'etichetta Dominio per la parte PCI-DSS/PSD2 e la riga sull'inglese.

## Cosa verificare prima di inviare

1. **L'indirizzo LinkedIn**: è stato scritto come dettato, ma va aperto per controllare che sia
   raggiungibile e che il profilo dica le stesse cose del CV.
2. **"Picchi intorno alle 400 richieste al secondo"**: il numero è approssimativo come è stato
   detto. Se esiste un dato preciso, va sostituito; se non esiste, si può togliere la cifra.
3. **"Parte applicativa dell'audit PCI-DSS annuale dal 2023"**: verificare che il perimetro sia
   descritto come lo descriverebbe l'azienda, e che non ci siano vincoli di riservatezza sul
   nominare la certificazione.
4. **Telefono ed email**: nel CV originale erano `333 1234567` e `mario.rossi@example.com`,
   riportati identici. Vanno confermati.
5. **Mesi di inizio e fine** delle esperienze: il CV riporta i soli anni, come l'originale. Se li
   ricorda, aggiungerli rende leggibile anche il periodo 2019–2021.

## Cosa resta scoperto

| Voce | Perché |
|---|---|
| Obiettivo professionale nel profilo (B4) | Non chiesto: il tetto di dieci domande è stato speso sui requisiti obbligatori e sulle competenze. Il profilo dice cosa fa, non dove vuole arrivare |
| Hobby e interessi (B13) | Dichiarati fuori dalle dieci domande prima dell'intervista. La sezione manca |
| Sedi e mesi delle esperienze (B5) | Non raccolti; il CV resta con i soli anni, come l'originale |
| Livello QCER dell'inglese e certificazione (B12) | Il candidato ha detto di non averne: "Non ho certificazioni". La riga descrive l'uso, non il livello, perché un livello non dichiarato non si assegna |
| Numeri sui risultati prima del 2021 (A3) | L'unica risposta è stata un intervallo, "intorno al 60-70%": o il numero esatto o nessuna cifra. Il bullet dice "partendo da una copertura nulla", che è l'unica parte certa |
| Il periodo fra il 2019 e il 2021 | Visibile nella sequenza delle date e non spiegato. Non è un difetto del CV: è una domanda da colloquio |

## Contenuti tagliati, recuperabili

- **Dati anagrafici**: data e luogo di nascita, stato civile, figli, segnaposto `[foto]`. Tolti su
  richiesta del candidato e perché sono dati protetti, esclusi dalla valutazione.
- **Profilo originale**: "Senior developer con forte passione per la tecnologia, team player,
  problem solver, orientato al risultato. Esperto di tutte le principali tecnologie moderne."
  Sostituito: nessuna delle due frasi era verificabile in una riga sotto.
- **Competenze rimosse**: Python, React, Angular, Node.js, Rust, Machine Learning, Blockchain,
  Scrum Master, DevOps, NoSQL. Motivo, dalle parole del candidato: "Rust e Blockchain mai in un
  progetto, Machine Learning solo un corso"; React e Angular risalgono a WebAgency Blu e sono
  frontend, fuori dal ruolo target. Su un annuncio full-stack, React e Angular tornano dentro.
- **Kafka**: mai inserito, perché mai usato. Il requisito gradito dell'annuncio ammette "altri
  sistemi di messaging", coperto da RabbitMQ.
- **WebAgency Blu**: sei anni compressi in un bullet. Su un annuncio PHP o full-stack quella
  esperienza si riapre.

## Verifica sul CV riscritto: voci B e C

Si ricompilano le **voci**, non i punteggi: un punteggio calcolato sul documento appena scritto
misura la stessa checklist usata per scriverlo e non è confrontabile con quello del CV originale.

Rendering verificato su `cv_mario_rossi-senior-backend-riscritto.pdf`: 1 pagina, riempimento 77%,
A4 con margini 20 mm, corpo 10 pt, interlinea di profilo predefinito — tutti sopra i minimi
tipografici (10 pt / 1.0 / 18 mm).

### Voci che hanno cambiato esito

| Voce | Da | A | Cosa è cambiato |
|---|---|---|---|
| B1 Sintesi | Parziale | Sì | La testata non porta più dati anagrafici: la riga più letta del CV dice ruolo e contatti |
| B3 Contatti | Parziale | Sì | Email, telefono, città e LinkedIn in alto, su una riga. GitHub resta assente perché non esiste |
| B4 About Me | No | Parziale | Job title attuale, tecnologie portanti e dominio al posto delle frasi vuote; manca ancora l'obiettivo professionale |
| B8 Competenze tecniche | No | Sì | Da 17 voci indistinte a 4 etichette ordinate per pertinenza, ogni voce presente in un'esperienza o in una risposta |
| B9 Soft skill | No | Parziale | Il set standard è sparito; mentoring e code review a rotazione compaiono come fatti dentro l'esperienza, non come aggettivi |
| B14 Autorizzazione dati | No | Sì | Frase presente in chiusura |
| C4 Date leggibili | No | Parziale | Le date stanno nella riga di intestazione di ogni esperienza, sempre nella stessa posizione; non su colonna a destra né riga dedicata |
| C7 Spaziatura gerarchica | Parziale | Sì | Bullet, esperienze e sezioni hanno tre stacchi distinti e coerenti |
| C8 Orfani e vedove | No | Sì | Nessuna parola sola a fine paragrafo (l'ultimo bullet di FinSoft è stato accorciato apposta) |
| C14 Leggibilità complessiva | Parziale | Sì | Nome, ruolo attuale, dominio e stack si leggono in meno di dieci secondi |

Invariate e già a `Sì`: B2, B6, B7, C1, C2, C3, C5, C6, C9, C10, C11, C12, C13. Invariate a `N/A`:
B11 (nessuna pubblicazione), B15 (nessuna foto — il segnaposto `[foto]` è stato tolto).

### Voci che restano No o Parziale, con il motivo

| Voce | Esito | Motivo |
|---|---|---|
| B4 About Me | Parziale | Obiettivo professionale non raccolto: nessun dato disponibile e nulla è stato inventato |
| B5 Esperienze professionali | Parziale | Date con i soli anni e nessuna sede: non chiesti in intervista |
| B9 Soft skill | Parziale | Nessuna sezione dedicata, per stare in una pagina; i due episodi disponibili sono dentro l'esperienza |
| B10 Corsi e certificazioni | Parziale | La certificazione AWS sta dentro "Formazione e lingue": una sezione a sé costerebbe tre righe per una sola voce |
| B12 Lingue | Parziale | Nessun livello QCER e nessuna certificazione: il candidato ha dichiarato di non averne |
| B13 Hobby e interessi | No | Fuori dal tetto di dieci domande, dichiarato prima dell'intervista |
| C4 Date leggibili | Parziale | Il modello a una pagina tiene le date nella riga di intestazione; una colonna a destra costerebbe spazio orizzontale ai titoli |

## Effetto sulla valutazione

La riscrittura **non ha cambiato il blocco A**: la persona è la stessa. A cambiarlo è stata
l'intervista, che ha fatto emergere evidenza assente dal documento. Il report aggiornato è
`cv_mario_rossi-senior-backend-valutazione.md`: gate da `Da verificare` a `Passa`, aderenza da 86 a
93, decisione da *Chiamare per verificare* a *Chiamare*.

Due dei requisiti che chiudono il gate — inglese fluente e Kubernetes in produzione — hanno stato
`Dichiarato`: sono affermazioni del candidato, non evidenze documentali, e restano domande per il
colloquio.
