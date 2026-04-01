## Numero di leptoni nello stato finale
Quando le particelle vengono prodotte in un collisionatore di particelle, spesso decadono immediatamente in altre particelle. Questi prodotti di decadimento sono ciò che rileviamo e analizziamo. Studiando le particelle nello stato finale (quelle visibili dopo tutti i decadimenti), possiamo dedurre quali particelle sono state originariamente create nella collisione.

Per capirlo meglio, diamo un’occhiata ai [diagrammi di Feynman](https://cds.cern.ch/record/2759490/files/Feynman%20Diagrams%20-%20ATLAS%20Cheat%20Sheet.pdf). Questi diagrammi aiutano a visualizzare le interazioni tra particelle. Negli esempi qui sotto, leggiamo i diagrammi **da sinistra a destra**: le particelle a sinistra vengono prodotte nella collisione, e le particelle a destra sono i prodotti finali del decadimento che rileviamo.

Ecco un diagramma che mostra un bosone Z che decade in due leptoni (elettroni o muoni):

![Decadimento del bosone Z in due leptoni](images/Z_decay_{theme}.png)

Nel diagramma precedente, la linea ondulata a sinistra rappresenta il bosone Z, prodotto nella collisione. Man mano che ci spostiamo verso destra, il bosone Z raggiunge un vertice, dove decade in due leptoni. Questi leptoni sono mostrati come linee rette, etichettate con ℓ, che possono essere elettroni o muoni. Le frecce sulle linee indicano se ciascun leptone è una particella o un’antiparticella: le frecce che puntano verso destra indicano particelle, mentre quelle che puntano verso sinistra indicano antiparticelle. Questo diagramma illustra come un bosone Z decada in una coppia di leptoni con cariche opposte, che rileviamo nel nostro esperimento.

Processi più complessi, come i decadimenti del bosone di Higgs, possono produrre più leptoni nello stato finale. Per esempio, ecco un bosone di Higgs che decade in due bosoni Z, ciascuno dei quali decade ulteriormente in due leptoni:

![Decadimento del bosone di Higgs in bosoni Z e leptoni](images/higgs4l_decay_{theme}.png)

Una linea tratteggiata a sinistra rappresenta il bosone di Higgs (H). Il bosone di Higgs decade in un vertice in due bosoni Z, mostrati come linee ondulate etichettate con Z. Ciascun bosone Z poi decade ulteriormente in due leptoni, proprio come nel primo diagramma. Ancora una volta, le linee rette con frecce rappresentano i leptoni, con la direzione della freccia che indica se si tratta di particelle o antiparticelle. In totale, questo processo produce quattro leptoni, che sono le particelle finali che rileviamo. Questo diagramma mostra come il decadimento di un bosone di Higgs possa portare a più particelle attraverso una cascata di interazioni.

In molti processi tra particelle, le particelle vengono spesso prodotte in coppie. Per esempio, il bosone Z decade in due leptoni — una particella e la sua antiparticella — perché interagisce allo stesso modo sia con la materia sia con l’antimateria. Allo stesso modo, il bosone di Higgs produce più leptoni quando il suo decadimento coinvolge particelle intermedie come i bosoni Z, che a loro volta decadono in coppie di leptoni.

Il dataset che stai analizzando contiene eventi con numeri variabili di leptoni. Qui sotto c’è un grafico che mostra la distribuzione del numero di leptoni nell’intero dataset. Gli eventi con meno leptoni sono più comuni perché i processi più semplici, come quelli che coinvolgono bosoni W o Z, avvengono più frequentemente rispetto a quelli più rari e complessi, come i decadimenti del bosone di Higgs.

![Distribuzione del numero di leptoni rilevati per evento nel dataset](images/lepton_plot_{theme}_{lumi}.png)

Studia i diagrammi di Feynman e i dati sopra. A seconda che tu voglia trovare il bosone Z o il bosone di Higgs, seleziona il numero di leptoni che ti aspetti di osservare nello stato finale.

> [!CAUTION] 
Quando selezioni il numero di leptoni, vengono applicati criteri aggiuntivi per garantire la qualità dei dati. I leptoni devono essere ben separati dalle altre particelle (**isolati**) e **identificati accuratamente** come elettroni o muoni. Poiché le particelle possono talvolta essere identificate in modo errato, utilizziamo livelli di identificazione per misurare quanto siamo sicuri del loro tipo. Inoltre, vengono inclusi solo gli eventi con segnali sufficientemente forti da attivare il sistema di selezione del rivelatore (chiamato trigger), in particolare per l’identificazione di elettroni o muoni.
> [!END]