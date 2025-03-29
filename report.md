### DBSCAN VS KMEANS, COMPARED TO OTHER...
### TSNE VS UMAP
TODO: other
Dbscan TODO: include picture
dbscan i wanted to preserve outliers

DBSCAN:

    Forms clusters based on local density.

    Does not force all points into clusters — allows noise and flexible shapes.

    So clusters can overlap in 2D because:

        UMAP preserves local structure, and density-based groupings may span continuous regions.

        UMAP might not "pull apart" similar dense areas because they’re connected.

🔵 KMeans:

    Assigns every point to a cluster (no noise).

    Enforces globular (spherical) clusters in feature space.

    UMAP receives these hard, often well-separated partitions and may emphasize their separation in 2D, especially since:

        KMeans uses global centroid distance — UMAP might exaggerate this.

        Clusters are clean and non-overlapping by design.

📌 So, to directly answer:

    Is the 2D visual difference just coincidental?

    Partially, yes. It's a result of:

        The clustering strategy (hard vs. density).

        The way UMAP distorts distances and structure in going from 25D → 2D.

    Clusters in DBSCAN may look overlapped due to UMAP preserving neighborhood continuity.

    Clusters in KMeans look more separate because UMAP gets input with hard partitions.

Cluster shape	Spherical (globular)	Arbitrary
Assignment	Hard (every point)	Core + border + noise
Separation in UMAP (2D)	Often well-separated	Can appear overlapping
Visual separation	Expected	Expected




TSNE was not clear enough, increasing preplexity just emphesizes these aggressiveness ... not the goal. TO SAY
TODO: include picture

Aspect	t-SNE Behavior	UMAP Behavior
Local Structure	✅ Excellent at preserving small-scale neighbor relationships	✅ Also very good
Global Structure	❌ Often distorts (e.g., distances between clusters not meaningful)	✅ Tends to preserve it better
Cluster Tightness	✅ Tight, well-separated clusters (sometimes artificially so)	✅ Preserves real density more faithfully
Continuum Representation	❌ Poor for continuous transitions (e.g. time series)	✅ Better at capturing gradual transitions
Overlapping Clusters	✅ Can show overlap if points are similar	⚠️ UMAP often pushes clusters apart
Noise and Outliers	❌ Can squash or scatter randomly	✅ Handles them more smoothly

Distances between clusters are not neccesarly preserved, which is good with umap (but umap also pushes them appart sometimes?)
When t-SNE Might Be Better:

    You care primarily about local similarity — i.e. who is next to whom.

    You're analyzing fine-grained local structure inside clusters.

    You don’t care about how far clusters are from each other globally.

    You're visualizing subtopics or subclasses within a large topic.

    You want tighter, more compact clusters visually (even if exaggerated).


Might be better for analysing inside clusters ... not interested ... i saw someone have success here

TODO: check final script with chatGPT

-------------
### DBSCAN VS KMEANS, COMPARED TO OTHER...
kmeans random inherently... but still best silhouettes and easier understanding

DBSCAN produced semantically similar clusters as kmeans, just that with dbscan i had to use knn to classify outliers (my choice). With kmeans, which is also much faster clustering was semantically similar and coherent, getting also the highest scores..., but the main choice was the ability to set number of clusters explicitly. DBSCAN identified 26 clusters, out of which most are easy to interpret, but some are really not easy and too similar. For that kmeans was used. The downside of kmeans is that it is naturally not deterministic, which means that some clusters will fall apart on some restarts and viceversa. However, with testing, all decompositions were semantically correct, so here maybe even some knowledge can be gained like, ... movies, music, literature ... sometimes generalizes into culture.
Speaking of determinism i would like to say that even umap i used is not necesarrily deterministic. svd or pca on the other hand for dimensionality reduction are deterministic, but did not produce better results than umap, since umap preserves nonlinear relationships.


Explained
/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/fromnumeric.py:3504: RuntimeWarning:

Mean of empty slice.

/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/_methods.py:129: RuntimeWarning:

invalid value encountered in scalar divide

tfidf:  ['izraelski', 'gaza', 'izrael', 'napad', 'človek', 'palestinski', 'hamas', 'vojska', 'država', 'izraelski vojska', 'libanon', 'ubit', 'pomoč', 'sila', 'območje', 'ameriški', 'vojna', 'leto', 'humanitaren', 'palestinec']
yake:  ['izraelski vojska napad', 'gaza izraelski napad', 'gaza izraelski vojska', 'napad izraelski vojska', 'izraelski napad gaza', 'izraelski vojska gaza', 'gaza ubit človek', 'izraelski sila gaza', 'izraelski vojska izraelski', 'palestinski gibanje hamas', 'izraelski napad ubit', 'gaza izraelski sila', 'človek izraelski vojska', 'napad hamas izrael', 'izrael izraelski vojska', 'prekinitev ogenj gaza', 'izraelski napad izraelski', 'izraelski zračen napad', 'izraelski sila napad', 'ubit človek izraelski']
keybert:  ['bombardiran', 'bombardiranje', 'protiizraelski', 'izraelski', 'bomben', 'bombnik', 'izraelskost', 'israel', 'genocid', 'palästina', 'proizraelski', 'palestinkam', 'zaradiizraelski', 'netanjahujev', 'priznanjepalestina', 'terorističen', 'propalestinec', 'izraelk', 'genocida', 'izraelv']
npmi:  ['izraelski', 'izrael', 'gaza', 'napad', 'palestinski', 'človek', 'država', 'vojska', 'hamas', 'drug', 'sila', 'vojna', 'območje', 'leto', 'ubit', 'pomoč', 'palestinec', 'ameriški', 'humanitaren', 'zda']
size of cluster: 1493
---- Izrael vse glasneje o selitvi Palestincev iz Gaze. Oblasti skrbi obtožba zaradi genocida.
---- Ameriška letalonosilka Gerald R. Ford zapušča Sredozemlje
---- V Libanonu ubit namestnik vodje Hamasa. Izrael bo na ICJ-ju izpodbijal obtožbe genocida.
---- Ugledne izraelske javne osebnosti obsodile "hujskanje h genocidu"
---- V eksploziji dveh bomb v Iranu ubitih več kot sto ljudi
---- Hutijevci napovedujejo odgovor in kaznovanje za ameriške napade
---- Atentat na drugega moža Hamasa v Bejrutu: vodja Hezbolaha zagrozil Izraelu
---- Članice VS-ja hutijevce pozivajo, naj prenehajo napadati ladje v Rdečem morju
---- ZDA: Tožba Južne Afrike zoper Izrael zaradi očitkov o genocidu kontraproduktivna
---- Odgovornost za napad v Iranu prevzela Islamska država
/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/fromnumeric.py:3504: RuntimeWarning:

Mean of empty slice.

/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/_methods.py:129: RuntimeWarning:

invalid value encountered in scalar divide

tfidf:  ['tekma', 'minuta', 'točka', 'leto', 'liga', 'slovenija', 'sezona', 'dober', 'olimpija', 'gol', 'ekipa', 'slovenski', 'prvenstvo', 'zadnji', 'zmaga', 'klub', 'igralec', 'reprezentanca', 'evropski', 'igra']
yake:  ['tekma liga prvak', 'tekma tekma tekma', 'tekma evropski prvenstvo', 'minuta konec tekma', 'finale liga prvak', 'tekma tekma minuta', 'tekma krog liga', 'evropski prvenstvo nemčija', 'sezona liga prvak', 'liga prvak tekma', 'minuta minuta konec', 'evropski prvenstvo tekma', 'slovenija evropski prvenstvo', 'tekma liga narod', 'konec tekma minuta', 'minuta konec točka', 'minuta tekma točka', 'igra tekma tekma', 'liga liga liga', 'tekma osmina finale']
keybert:  ['žeželj', 'feliciani', 'felicetti', 'slaviš', 'jakoslava', 'pellegri', 'srečko', 'onnela', 'presrečen', 'čestitek', 'veseljak', 'sinjemodrim', 'lykkegaard', 'podeželje', 'posrečen', 'čestitk', 'slavić', 'benfico', 'hoffenhe', 'srečka']
npmi:  ['tekma', 'minuta', 'prvi', 'drug', 'dober', 'točka', 'liga', 'ekipa', 'leto', 'sezona', 'zadnji', 'slovenija', 'zmaga', 'igra', 'slovenski', 'prvenstvo', 'konec', 'gol', 'igralec', 'olimpija']
size of cluster: 3768
---- "Vseh dobrih stvari je enkrat konec, a sanje o košarki bodo vselej z mano"
---- Liverpool se je po trilerju na Anfieldu utrdil na vrhu
---- Pianigiani zapustil Cedevito Olimpijo, na ljubljanski klopi znova Martić
---- Velika zmaga Olimpije na Madžarskem
---- Manchester United van de Beeka posodil v Frankfurt
---- Hapoel išče zamenjavo za Džikića, glavni kandidat Golemac
---- Decembra Luka Dončić v slogu MVP-ja lige
---- V ZDA in Kanadi zaživela nova profesionalna ženska liga
---- Rooney že po 83 dneh zapustil klop Birminghama
---- Z Zoranom Martićem se je v zmajevo gnezdo vrnil tudi Zoran Dragić

tfidf:  ['policija', 'leto', 'policist', 'sodišče', 'napad', 'dejanje', 'človek', 'moški', 'kazniv', 'preiskava', 'kazniv dejanje', 'policijski', 'kazen', 'otrok', 'država', 'leten', 'zapor', 'primer', 'evro', 'nov']
yake:  ['storitev kazniv dejanje', 'kazniv dejanje policija', 'policijski uprava ljubljana', 'preiskava kazniv dejanje', 'kazniv dejanje spolen', 'sum kazniv dejanje', 'policijski uprava nov', 'kazniv dejanje zloraba', 'dejanje kazniv dejanje', 'kazniv dejanje umor', 'policija kazniv dejanje', 'kazniv dejanje kazniv', 'uprava nov mesto', 'policija policijski uprava', 'žrtev kazniv dejanje', 'kraj kazniv dejanje', 'kazniv dejanje', 'osumljenec kazniv dejanje', 'generalen policijski uprava', 'sum storitev kazniv']
keybert:  ['polisario', 'vladislava', 'rusjana', 'sovrstnik', 'hudodelski', 'salisin', 'čakovac', 'melikov', 'jaroslav', 'nasilnež', 'rangsiman', 'vrtčevski', 'kriminologija', 'hudiči', 'karačajev', 'zamakajoč', 'njegošev', 'vladislav', 'zabojnik', 'russa']
npmi:  ['leto', 'policija', 'sodišče', 'policist', 'drug', 'dejanje', 'človek', 'napad', 'država', 'kazniv', 'primer', 'preiskava', 'otrok', 'kazen', 'policijski', 'nov', 'leten', 'zapor', 'velik', 'nasilje']
size of cluster: 1857
---- Giorgia Meloni na udaru, potem ko se je za silvestrovo sprožila pištola njenega poslanca
---- Vrhovno sodišče zavrnilo Janševo zahtevo za varstvo zakonitosti v primeru razžalitve novinark
---- Na Hrvaškem pridržali uslužbenca zunanjega ministrstva zaradi suma tihotapljenja ljudi 
---- Žrtev virtualne ugrabitve: kitajskega najstnika našli v gozdovih Utaha
---- Italijanska radiotelevizija RAI praznuje: 70 let televizijskega in 100 let radijskega oddajanja
---- Britanska policija preiskuje prvo virtualno posilstvo v metaprostoru
---- V streljanju na šoli v Iowi več ranjenih
---- Meloni zaradi incidenta s pištolo iz stranke Bratje Italije suspendirala poslanca Pozzola
---- Za dolgoletne spolne zlorabe treh hčerk 52-letnik obsojen na 23 let in pol zapora
---- Rop pošte v Gameljnah: neznanec zagrozil uslužbenki in iz blagajne vzel nekaj bankovcev
/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/fromnumeric.py:3504: RuntimeWarning:

Mean of empty slice.

/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/_methods.py:129: RuntimeWarning:

invalid value encountered in scalar divide

tfidf:  ['leto', 'razstava', 'slovenski', 'muzej', 'delo', 'nov', 'svet', 'mesto', 'umetnost', 'slovenija', 'velik', 'galerija', 'del', 'umetnik', 'dan', 'človek', 'prostor', 'projekt', 'kultura', 'čas']
yake:  ['evropski prestolnica kultura', 'muzej sodoben umetnost', 'naroden muzej slovenija', 'akademija likoven umetnost', 'kulturen dediščina slovenija', 'muzej nov sodoben', 'slovenski likoven umetnik', 'slovenski kulturen praznik', 'likoven umetnost oblikovanje', 'nov gorica gorica', 'slovenski kulturen prostor', 'kultura nov gorica', 'nov sodoben zgodovina', 'galerija likoven umetnost', 'prestolnica kultura nov', 'likoven umetnost ljubljana', 'razstava sodoben umetnost', 'sodoben zgodovina slovenija', 'nov stalen razstava', 'slovenski kulturen dediščina']
keybert:  ['miroslava', 'religiološki', 'religiologija', 'religijski', 'religioznost', 'religiozen', 'verovškov', 'religija', 'svečenica', 'verstvo', 'grškokatoliški', 'papeštvo', 'papeški', 'papeža', 'karikisa', 'papeževanje', 'duhovščina', 'pobožen', 'pobožnost', 'churchillov']
npmi:  ['leto', 'razstava', 'drug', 'delo', 'nov', 'slovenski', 'velik', 'del', 'svet', 'mesto', 'čas', 'slovenija', 'muzej', 'človek', 'prvi', 'prostor', 'dan', 'kulturen', 'kultura', 'projekt']
size of cluster: 2578
---- Papež pri novoletni maši poudaril pomen žensk za mir na svetu
---- Katoliška cerkev zaznamuje svetovni dan miru
---- Evropske prestolnice kulture 2024: Tartu v Estoniji, arktični Bodø in Bad Ischl v Avstriji
---- Zgornji dom britanskega parlamenta lani kupil za več kot sto tisočakov šampanjca
---- Novoletna preizkušnja s skokom v vodo pogumno premagana
---- V nemških zbirkah še zmeraj najmanj 17.000 človeških posmrtnih ostankov iz kolonialnega obdobja
---- Na razstavi v ZDA, ki razkriva drznost umetnikov vzhodnega bloka, tudi Vipotnik in Godina
---- Za vsakim muzejskim predmetom stoji restavrator z ogromno vedenja in iznajdljivosti
---- Narodna galerija v 2024: zbirka Kroples in secesijsko gibanje v Ukrajini
---- Italijanski državni svet: Muzej J. Paul Getty lahko obdrži sliko Jacopa Bassana
/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/fromnumeric.py:3504: RuntimeWarning:

Mean of empty slice.

/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/_methods.py:129: RuntimeWarning:

invalid value encountered in scalar divide

tfidf:  ['dirka', 'etapa', 'pogačar', 'mesto', 'leto', 'ekipa', 'zmaga', 'kolesar', 'dober', 'sezona', 'roglič', 'cilj', 'zadnji', 'sekunda', 'dan', 'svetoven', 'konec', 'čas', 'velik', 'vzpon']
yake:  ['dirka italija dirka', 'dirka francija dirka', 'etapa kolesarski dirka', 'etapa dirka francija', 'zmaga dirka francija', 'zmaga dirka dirka', 'dirka svetoven prvenstvo', 'dirka sezona dirka', 'skupen zmaga dirka', 'etapen zmaga dirka', 'etapa dirka italija', 'dirka svetoven serija', 'konec sezona dirka', 'etapa letošnji dirka', 'letošnji dirka francija', 'zmaga dirka italija', 'zmagovalec etapa dirka', 'dirka dirka francija', 'dirka francija etapa', 'dirka dirka dirka']
keybert:  ['bik', 'avstrijski', 'avstrijka', 'bikoborec', 'ekipen', 'germani', 'nemka', 'nemce', 'nemca', 'bika', 'valkenburg', 'equipe', 'nemčija', 'equipo', 'braslovče', 'ekipa', 'nemčev', 'hansgroh', 'benussi', 'nemški']
npmi:  ['dirka', 'etapa', 'drug', 'mesto', 'zmaga', 'prvi', 'ekipa', 'pogačar', 'leto', 'dober', 'zadnji', 'kolesar', 'cilj', 'sezona', 'konec', 'dan', 'velik', 'roglič', 'sekunda', 'svetoven']
size of cluster: 1034
---- Rdeči biki prevzemajo Rogličevo novo ekipo
---- Po puščavi in gorah tudi Simon Marčič in Toni Mulec
---- Prolog za uvod v reli Dakar: Marčič 76., Mulec 96.
---- Marčiča po težavah reševali s helikopterjem
---- Toni Mulec v tretji etapi drugi v razredu rally2
---- Tadej Pogačar
---- Philipsen v sprintu dvanajsterice do spomenika, Pogačar tretji!
---- Pogačar za las prekratek za zmago na uvodni etapi
---- Sproščeni Pogačar veliko testira, se šali in pili gorsko formo
---- Razočarani Pogačar analizira: Če Philipsen ne bi imel svetovnega prvaka, bi zmagal Mohorič
/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/fromnumeric.py:3504: RuntimeWarning:

Mean of empty slice.

/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/_methods.py:129: RuntimeWarning:

invalid value encountered in scalar divide

tfidf:  ['leto', 'zakon', 'odstotek', 'evro', 'predlog', 'vlada', 'ministrstvo', 'javen', 'delo', 'slovenija', 'sindikat', 'plača', 'nov', 'podjetje', 'deloven', 'delavec', 'milijon', 'šola', 'otrok', 'država']
yake:  ['predlog novela zakon', 'plača javen sektor', 'sindikat javen sektor', 'ministrstvo javen uprava', 'sistem plača javen', 'evro milijon evro', 'predlog nov zakon', 'plačen sistem javen', 'predlog sprememba zakon', 'vlada predlog zakon', 'vlada sindikat javen', 'milijon evro odstotek', 'delo družina socialen', 'sistem javen sektor', 'ministrstvo delo družina', 'nov plačen sistem', 'nov plačen zakon', 'milijon evro milijon', 'milijon evro ministrstvo', 'milijarda evro odstotek']
keybert:  ['deloven', 'izplačevanje', 'normativa', 'zaslužkarstvo', 'zakonodajen', 'zakonodaja', 'obdavčenost', 'subvencioniranje', 'laburističen', 'odplačevanje', 'neplačevanje', 'sobodajalstvo', 'davkoplačevalec', 'normativen', 'fiskalen', 'vlada', 'ekonomskoplosloven', 'delodajalski', 'subvencija', 'dohodek']
npmi:  ['leto', 'zakon', 'drug', 'javen', 'slovenija', 'vlada', 'delo', 'ministrstvo', 'odstotek', 'predlog', 'evro', 'nov', 'plača', 'deloven', 'država', 'sindikat', 'državen', 'velik', 'čas', 'sistem']
size of cluster: 1794
---- V veljavi podražitve napotitev delavcev
---- Na Hrvaškem sta se ponoči rodili dvojčici, prva v letu 2023, druga v 2024
---- Zakon o dolgotrajni oskrbi za zdaj prinaša nove pravice oskrbovalcem družinskih članov
---- Prvi deček se je rodil v Ljubljani, prva deklica v Mariboru
---- Slovenija med redkimi evropskimi državami, ki praznujejo tudi 2. januar
---- Po božično-novoletnih počitnicah spet v šolo
---- Inšpekcija pri nadzoru proizvajalčeve razširjene odgovornosti ugotovila več kršitev
---- V Angliji začetek šestdnevne stavke specializantov
---- Najpogostejši novoletni zaobljubi: bolj zdravo življenje in več druženja
---- Potrdila o darovanju krvi odslej elektronska
/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/fromnumeric.py:3504: RuntimeWarning:

Mean of empty slice.

/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/_methods.py:129: RuntimeWarning:

invalid value encountered in scalar divide

tfidf:  ['leto', 'slovenija', 'velik', 'nov', 'dan', 'država', 'evro', 'voda', 'človek', 'mesto', 'odstotek', 'žival', 'območje', 'temperatura', 'del', 'milijon', 'stopinja', 'občina', 'visok', 'promet']
yake:  ['temperatura stopinja celzij', 'evropski vesoljski agencija', 'evro milijon evro', 'milijon evro milijon', 'agencija okolje arso', 'vrednost milijon evro', 'uprava varen hrana', 'mednaroden vesoljski postaja', 'milijon evro nov', 'del milijon evro', 'stopinja celzij stopinja', 'agencija varnost promet', 'javen potniški promet', 'slovenija milijon evro', 'milijon evro slovenija', 'zakon zaščita žival', 'hitrost kilometer ura', 'projekt milijon evro', 'ministrstvo naraven vir', 'slovenija evropski vesoljski']
keybert:  ['turističnoinfoisforski', 'turističnoinformacijski', 'turizem', 'turističen', 'turistica', 'turističnoinfoinforski', 'turistk', 'turist', 'tourist', 'turistka', 'izletniški', 'počitnice', 'resoren', 'obiska', 'obiskovalec', 'obiskovalka', 'izletnik', 'slovenjgraški', 'slovenski', 'obisk']
npmi:  ['leto', 'velik', 'drug', 'slovenija', 'nov', 'država', 'dan', 'človek', 'odstotek', 'voda', 'del', 'evro', 'prvi', 'območje', 'mesto', 'čas', 'visok', 'milijon', 'temperatura', 'žival']
size of cluster: 2077
---- Turizem v letu 2023 – rekord turistov, boj za ležalnike in zvezdice za Slovenijo
---- Letalska družba ponujala dvakratno silvestrovanje, a je potnike pustila na cedilu
---- Iz Šanghaja izplula prva na Kitajskem izdelana križarka
---- Največ poletov v 2023 z Brnika opravil Turkish Airlines in prehitel Lufthanso
---- Na skrajnem severu Evrope v novo leto vstopili pri minus 40 stopinjah Celzija
---- Letos bomo lahko iz Slovenije opazovali komete, konjunkcijo planetov in severni sij
---- Na Hrvaškem tuji turisti poskrbeli za rekordne prihodke
---- Neurje Henk povzroča težave v delih Evrope
---- Smučišča, kolesarske poti, kampi – ugotovljenih več nedovoljenih posegov na zavarovanih območjih
---- Ministrstvo pozvalo k spoštovanju gozdnega bontona
/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/fromnumeric.py:3504: RuntimeWarning:

Mean of empty slice.

/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/_methods.py:129: RuntimeWarning:

invalid value encountered in scalar divide

tfidf:  ['igra', 'skok', 'točka', 'tekma', 'dončić', 'minuta', 'sezona', 'dallas', 'podaj', 'dober', 'zmaga', 'liga', 'zadnji', 'met', 'leto', 'ekipa', 'četrtina', 'gol', 'igra skok', 'končnica']
yake:  ['igra skok podaj', 'igra podaj skok', 'točka skok podaj', 'igra prost met', 'točka podaj skok', 'dončić igra skok', 'prost met skok', 'met skok podaj', 'igra dončić igra', 'skok podaj minuta', 'točka met igra', 'met igra točka', 'jokić igra skok', 'tekma točka skok', 'dvojček točka skok', 'dončić igra prost', 'davis igra skok', 'tatum igra skok', 'igra točka skok', 'met podaj skok']
keybert:  ['hokejisti', 'rangers', 'rangerse', 'hokejski', 'hokejist', 'ekip', 'hokej', 'rangersov', 'hockey', 'rangersi', 'gol', 'golov', 'canucks', 'športnica', 'ekipen', 'ekipa', 'tima', 'sportradar', 'prvenstvo', 'šampionski']
npmi:  ['igra', 'točka', 'tekma', 'skok', 'prvi', 'minuta', 'dončić', 'dallas', 'dober', 'zadnji', 'podaj', 'sezona', 'zmaga', 'drug', 'met', 'četrtina', 'liga', 'ekipa', 'konec', 'leto']
size of cluster: 911
---- Boston za vodilnimi Rangersi zaostaja samo še točko
---- Pelikani pokvarili LeBronovo rojstnodnevno slavje
---- Utah se je z izjemno predstavo oddolžil Dallasu za visok poraz
---- Daccord prvi, ki je na zimski klasiki ohranil mrežo nedotaknjeno
---- Oklahoma City porazil še najboljšo ekipo Vzhoda
---- Najlažje dihajo pri Baltimoru in San Franciscu, na voljo še pet prostih mest
---- Kingsi prvič letos streljali s praznimi naboji, zmaga Toronta
---- Dončić in Irving že do odmora potopila odpisani Portland
---- Dončič po prvih dveh tednih glasovanja četrti na Zahodu in prvi med branilci
---- Četrti zaporedni poraz Kraljev, Rdeča krila slavila po loteriji
/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/fromnumeric.py:3504: RuntimeWarning:

Mean of empty slice.

/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/_methods.py:129: RuntimeWarning:

invalid value encountered in scalar divide

tfidf:  ['stranka', 'vlada', 'volitev', 'leto', 'slovenija', 'predsednik', 'država', 'evropski', 'nov', 'sodišče', 'odstotek', 'zakon', 'kandidat', 'svet', 'komisija', 'minister', 'poslanec', 'predsednica', 'parlament', 'političen']
yake:  ['predsednica evropski komisija', 'predsednik vlada robert', 'volitev evropski parlament', 'stranka evropski volitev', 'predsednik ustaven sodišče', 'vlada predsednik vlada', 'predsednik vlada predsednik', 'državen volilen komisija', 'odločba ustaven sodišče', 'predsednik evropski svet', 'kabinet predsednik vlada', 'zakon ustaven sodišče', 'volitev odstotek glas', 'vodja poslanski skupina', 'odločitev ustaven sodišče', 'vlada robert golob', 'predsednik vlada stranka', 'nov predsednik vlada', 'stranka odstotek glas', 'poslanec evropski parlament']
keybert:  ['slovenija', 'slovenia', 'slovenijazvezdan', 'slovenica', 'slovenje', 'slovenj', 'slovenščina', 'slovenski', 'hrvatsk', 'slovensko', 'češko', 'češki', 'češka', 'češek', 'litva', 'slovak', 'slovenec', 'slovaška', 'slovaško', 'bratislava']
npmi:  ['stranka', 'vlada', 'leto', 'predsednik', 'drug', 'slovenija', 'država', 'volitev', 'evropski', 'nov', 'sodišče', 'zakon', 'poslanec', 'odstotek', 'velik', 'komisija', 'svet', 'državen', 'političen', 'minister']
size of cluster: 2689
---- Slovenija dve leti na stolčku nestalne članice Varnostnega sveta. Fajon: Želimo pustiti svoj pečat.
---- Izraelsko vrhovno sodišče razveljavilo ključni del pravosodne reforme
---- Predsednica novoletni obisk namenila starostnikom v Domžalah
---- Katere protokolarne obveznosti opravlja predsedničin soprog Aleš Musar?
---- Glasovanje ponavljajo še na osmih voliščih v Srbiji
---- Claudine Gay po obtožbah antisemitizma in plagiatorstva odstopila kot predsednica Harvarda
---- V New Yorku pred dvorano Varnostnega sveta ZN-a od zdaj tudi slovenska zastava
---- Po zamenjavi oblasti na Poljskem tudi zamenjava predstavnika na beneškem bienalu
---- V Srbiji po ponovljenem glasovanju na nekaterih voliščih potrdili zmago vladajočega SNS-ja
---- Golob v DZ še ni poslal predloga za kmetijskega ministra. Vojko Adamič naj ne bi bil edini kandidat.
/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/fromnumeric.py:3504: RuntimeWarning:

Mean of empty slice.

/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/_methods.py:129: RuntimeWarning:

invalid value encountered in scalar divide

tfidf:  ['ruski', 'ukrajina', 'ukrajinski', 'napad', 'rusija', 'država', 'predsednik', 'zda', 'vojna', 'zelenski', 'vojaški', 'sila', 'oblast', 'leto', 'trump', 'ameriški', 'vojska', 'evropski', 'raketa', 'človek']
yake:  ['ruski napad ukrajina', 'ukrajinski predsednik volodimir', 'ruski predsednik vladimir', 'ruski obramben ministrstvo', 'ruski napad ukrajinski', 'vojaški pomoč ukrajina', 'ukrajinski sila ruski', 'ruski sila ukrajinski', 'predsednik volodimir zelenski', 'ruski sila ukrajina', 'ruski invazija ukrajina', 'ukrajinski vojska ruski', 'ukrajina ukrajinski predsednik', 'ruski vojna ukrajina', 'ukrajina ruski sila', 'vojna ukrajina ruski', 'ukrajinski napad ruski', 'ukrajina ruski predsednik', 'napad ruski ozemlje', 'ruski agresija ukrajina']
keybert:  ['frakcija', 'grupacija', 'članica', 'skupina', 'članski', 'organizacija', 'zunajkoalicijski', 'konzorcij', 'koalicijski', 'skupinski', 'mednarodnopolitičen', 'član', 'koalicija', 'group', 'kolektiv', 'nadvlad', 'kolektiven', 'organizacijski', 'poslanca', 'združenje']
npmi:  ['ukrajina', 'ruski', 'ukrajinski', 'rusija', 'država', 'napad', 'predsednik', 'leto', 'vojna', 'vojaški', 'zda', 'sila', 'drug', 'zelenski', 'ameriški', 'oblast', 'vojska', 'evropski', 'velik', 'človek']
size of cluster: 1382
---- Skupina BRICS odslej z novimi polnopravnimi članicami
---- Prenehala je obstajati separatistična republika Gorski Karabah
---- Zelenski obljublja pospešeno izdelavo ukrajinskega orožja, Putin pa napoveduje krepitev napadov
---- Moški južnokorejskega opozicijskega voditelja z nožem zabodel v vrat
---- Kijev po novih obsežnih zračnih napadih zaveznike poziva k hitrejši dobavi orožja
---- Poljska se zavzema za dobavo raket dolgega dosega Ukrajini
---- Samuel Žbogar: Naša naloga je odpravljanje polarizacije
---- Največja izmenjava vojnih ujetnikov med Rusijo in Ukrajino od začetka vojne
---- Konflikt v Mjanmaru se čuti čez mejo na Kitajsko
---- Srbska vojska predlaga odpravo ukinitve obveznega služenja vojaškega roka
/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/fromnumeric.py:3504: RuntimeWarning:

Mean of empty slice.

/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/_methods.py:129: RuntimeWarning:

invalid value encountered in scalar divide

tfidf:  ['trump', 'predsednik', 'zda', 'leto', 'ameriški', 'harris', 'biden', 'volitev', 'država', 'trumpov', 'zvezen', 'predsedniški', 'kandidat', 'nekdanji', 'sodišče', 'donald', 'demokratski', 'demokrat', 'donald trump', 'soočenje']
yake:  ['predsednik donald trump', 'zda donald trump', 'predsednik zda donald', 'ameriški predsednik donald', 'nekdanji predsednik zda', 'kandidat donald trump', 'predsednik joe biden', 'nekdanji predsednik trump', 'ameriški predsednik joe', 'nekdanji ameriški predsednik', 'trump predsednik zda', 'ameriški predsedniški volitev', 'volitev donald trump', 'trump predsedniški volitev', 'ameriški zvezen država', 'donald trump predsednik', 'republikanec donald trump', 'predsedniški volitev zda', 'trump ameriški predsednik', 'donald trump trump']
keybert:  ['sokrivec', 'obtoženec', 'osumljenec', 'demonizacija', 'pedofilo', 'pedofilski', 'obdolženec', 'goljufija', 'namigovanjakgresnreknik', 'obtožnica', 'obtoženčev', 'izdajanjenekater', 'ponarejanje', 'šarlatanski', 'govorica', 'dvomljivec', 'priimek', 'zločinec', 'zavajajoč', 'obtoženca']
npmi:  ['trump', 'predsednik', 'zda', 'ameriški', 'leto', 'država', 'volitev', 'trumpov', 'drug', 'biden', 'predsedniški', 'harris', 'donald', 'kandidat', 'zvezen', 'prvi', 'nekdanji', 'velik', 'demokrat', 'demokratski']
size of cluster: 580
---- Vplivni in bogati v strahu pred objavo 180 imen, povezanih z Epsteinom
---- Trump se je pritožil na odločitev o izključitvi iz glasovanja v Mainu
---- Trump s pritožbo na vrhovno sodišče tudi glede prepovedi kandidature v Koloradu
---- Ameriško sodišče razkrilo imena posameznikov v povezavi z Epsteinom
---- Biden ob tretji obletnici vdora v Kapitol ostro nad Trumpa: Odloča se o demokraciji
---- Ameriško vrhovno sodišče bo odločalo o primernosti Trumpa za predsedniško kandidaturo
---- Sodelavci Taylor Swift jezno nad neokusno kolumno: "Etično poročanje je drugotnega pomena"
---- Biden kljub neprijavljeni hospitalizaciji zaupa obrambnemu ministru
---- Ameriški kongres nad TikTok: Odrecite se kitajskemu lastniku ali pa bo TikTok v ZDA prepovedan
---- Začetek sojenja Trumpu v New Yorku preložili za en mesec
/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/fromnumeric.py:3504: RuntimeWarning:

Mean of empty slice.

/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/_methods.py:129: RuntimeWarning:

invalid value encountered in scalar divide

tfidf:  ['požar', 'nesreča', 'človek', 'letalo', 'območje', 'gasilec', 'policist', 'leten', 'leto', 'voznik', 'policija', 'vozilo', 'poškodovan', 'kraj', 'ura', 'helikopter', 'mesto', 'policijski', 'država', 'reševalec']
yake:  ['francoski tiskoven agencija', 'policijski uprava nov', 'uprava zaščita reševanje', 'tiskoven agencija afp', 'nesreča leten voznik', 'hud prometen nesreča', 'prometen nesreča leten', 'poškodba kraj nesreča', 'policijski uprava ljubljana', 'vzrok požar znan', 'kraj nesreča policist', 'nujen medicinski pomoč', 'število smrten žrtev', 'človek poškodovan človek', 'nesreča policijski uprava', 'kraj prometen nesreča', 'območje policijski uprava', 'nemški tiskoven agencija', 'hud poškodba kraj', 'gorski reševalen služba']
keybert:  ['cunamij', 'cunami', 'seizmičen', 'japan', 'prefektura', 'fukušima', 'japonsko', 'japonska', 'tokijski', 'japonec', 'tokijčan', 'japonski', 'nevihten', 'katastrofa', 'peloponeza', 'nippon', 'meteorogog', 'pretresenost', 'tornadi', 'okinava']
npmi:  ['požar', 'nesreča', 'človek', 'območje', 'leto', 'letalo', 'gasilec', 'ura', 'drug', 'pomoč', 'poškodovan', 'policija', 'helikopter', 'velik', 'policist', 'mesto', 'država', 'kraj', 'reševalec', 'leten']
size of cluster: 1263
---- Iz Japonske po potresu poročila o žrtvah pod zrušenimi stavbami
---- Pri Benetkah se je prevrnil avtobus z 79 turisti iz BiH-a
---- Vseh 379 ljudi na potniškem letalu ubežalo ognju, pet članov posadke letala obalne straže umrlo
---- Število smrtnih žrtev letalskih nesreč lani med najmanjšimi v zadnjih desetletjih
---- V občini Bohinj plaz odnesel tri alpiniste, med njimi sta dva lažje poškodovana
---- Potres na Japonskem zahteval 57 življenj, reševalcem delo otežujejo uničene ceste
---- Preiskava letalske nesreče v Tokiu: dovoljenje za pristanek ali vzlet?
---- 26-letnik pod vplivom prepovedanih mamil zbil kolesarko in bežal pred policisti
---- Požar v podjetju na Ljubnem ob Savinji pogašen, poziv občanom preklican
---- Število smrtnih žrtev potresa na Japonskem naraslo na 73
/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/fromnumeric.py:3504: RuntimeWarning:

Mean of empty slice.

/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/_methods.py:129: RuntimeWarning:

invalid value encountered in scalar divide

tfidf:  ['mesto', 'tekma', 'olimpijski', 'dober', 'leto', 'svetoven', 'igra', 'finale', 'sezona', 'slovenski', 'točka', 'pokal', 'turnir', 'velik', 'niz', 'sekunda', 'svetoven pokal', 'zmaga', 'medalja', 'čas']
yake:  ['tekma svetoven pokal', 'olimpijski igra pariz', 'sezona svetoven pokal', 'zmaga svetoven pokal', 'točka svetoven pokal', 'seštevek svetoven pokal', 'svetoven pokal tekma', 'finale finale finale', 'nastop olimpijski igra', 'svetoven pokal mesto', 'olimpijski igra svetoven', 'medalja svetoven prvenstvo', 'tekma svetoven prvenstvo', 'svetoven pokal', 'zlat olimpijski medalja', 'medalja olimpijski igra', 'mesto tekma svetoven', 'svetoven pokal točka', 'finale svetoven pokal', 'mesto svetoven pokal']
keybert:  ['veleslalomski', 'slovenjgradčanka', 'nordisski', 'nordijski', 'nordhagen', 'veleslalomistko', 'zimskošporten', 'izslovenski', 'ukrajinec', 'veleslalomistka', 'slovenecza', 'lisovska', 'svojomoški', 'slovenec', 'norges', 'amundsenov', 'slalomski', 'slovenci', 'latvija', 'silvestrov']
npmi:  ['mesto', 'prvi', 'dober', 'tekma', 'drug', 'leto', 'svetoven', 'igra', 'olimpijski', 'finale', 'velik', 'slovenski', 'sezona', 'tretji', 'točka', 'zadnji', 'zmaga', 'pokal', 'konec', 'čas']
size of cluster: 2608
---- Po odstopih Urevc in Ličefa edina slovenska predstavnica ostaja Mandeljc 
---- Chebet v Barceloni postavila nov svetovni rekord, Botolin pa državnega
---- Kvitova na porodniški dopust, Osaka se je z njega vrnila
---- Rafael Nadal
---- Hrgota: Finalni skok eden najboljših v Laniškovi karieri
---- Nika Prevc s petim mestom v Oberstdorfu zmagovalka turneje dveh večerov
---- Popoln skok Anžeta Laniška v leto 2024
---- Barbara Jolič: Motivacija sledi akciji
---- Nadal zanesljivo ugnal Thiema po 350 dneh premora
---- Lanišek najboljši tudi v kvalifikacijah na Bergislu
/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/fromnumeric.py:3504: RuntimeWarning:

Mean of empty slice.

/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/_methods.py:129: RuntimeWarning:

invalid value encountered in scalar divide

tfidf:  ['odstotek', 'leto', 'evro', 'električen', 'nov', 'vozilo', 'avtomobil', 'energija', 'cena', 'podjetje', 'velik', 'slovenija', 'rast', 'milijon', 'delnica', 'model', 'visok', 'država', 'družba', 'milijon evro']
yake:  ['odstotek milijon evro', 'milijon evro odstotek', 'cena električen energija', 'odstotek milijarda evro', 'evro milijon evro', 'milijarda evro odstotek', 'evro evro evro', 'milijon evro milijon', 'odstotek odstotek odstotek', 'proizvodnja električen energija', 'milijon evro čist', 'vrednost milijon evro', 'milijon evro evro', 'obnovljiv vir energija', 'dobiček milijon evro', 'cena evro evro', 'odstotek odstoten točka', 'okolje podnebje energija', 'odstoten točka odstotek', 'nov jedrski elektrarna']
keybert:  ['šanghaj', 'china', 'kitajska', 'avtoindustrija', 'kitajsko', 'šendžen', 'kitajski', 'multinacionalk', 'multinacionalen', 'multinacionalka', 'tokijski', 'japonsko', 'automobili', 'cars', 'japonska', 'japonec', 'hongkonški', 'multinacionalkam', 'automobiles', 'azijski']
npmi:  ['leto', 'odstotek', 'evro', 'nov', 'velik', 'energija', 'električen', 'cena', 'slovenija', 'drug', 'visok', 'podjetje', 'rast', 'država', 'vozilo', 'milijon', 'trg', 'avtomobil', 'odstoten', 'prvi']
size of cluster: 1397
---- Kitajska na dobri poti do največjega izvoznika avtomobilov
---- Podražila se je cestnina za predor Karavanke
---- Kateri ukrepi za blaženje energetske draginje ostajajo v letu 2024?
---- Na Hrvaškem nič več označevanja cen v kunah, le še v evrih
---- Gospodarska aktivnost v območju evra decembra upadla
---- Popravek na delniških trgih, bitcoin prvič po aprilu 2022 nad mejo 45 tisoč
---- Maserati se s posebnimi izvedenkami poslavlja od osemvaljnikov
---- Država se bo zadolžila za 1,5 milijarde evrov
---- NSi napoveduje referendum o noveli energetskega zakona, če je vlada ne bo spremenila
---- S četrtkom dražji bencin, dizel in kurilno olje
/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/fromnumeric.py:3504: RuntimeWarning:

Mean of empty slice.

/opt/homebrew/anaconda3/envs/IS/lib/python3.12/site-packages/numpy/core/_methods.py:129: RuntimeWarning:

invalid value encountered in scalar divide

tfidf:  ['film', 'leto', 'festival', 'slovenski', 'nagrada', 'pesem', 'nov', 'album', 'glasba', 'predstava', 'glasben', 'filmski', 'koncert', 'človek', 'zgodba', 'svet', 'življenje', 'dober', 'velik', 'čas']
yake:  ['festival slovenski film', 'slovenski filmski center', 'film slovenski filmski', 'mednaroden filmski festival', 'slovenski film film', 'nagrada življenjski delo', 'film slovenski film', 'festival dokumentaren film', 'radijski igra otrok', 'film festival slovenski', 'slovenski film festival', 'slovenski film', 'film nov film', 'nov slovenski film', 'film', 'film film', 'glaven vloga film', 'evropski filmski nagrada', 'slovenski film slovenski', 'filmski festival film']
keybert:  ['filharmonijaletos', 'skladateljski', 'ciaffoni', 'kakofonija', 'češčina', 'melodijski', 'soundczech', 'ssimfonik', 'skladateljica', 'fiharmonija', 'skladateljev', 'basistko', 'folkglasbenica', 'melodičen', 'štokavščina', 'slovenščinen', 'simfoničen', 'glasbenoteorsetski', 'muzikološki', 'ukrajinščina']
npmi:  ['leto', 'film', 'drug', 'slovenski', 'prvi', 'nov', 'festival', 'nagrada', 'velik', 'čas', 'človek', 'dober', 'svet', 'zgodba', 'pesem', 'delo', 'glasba', 'življenje', 'filmski', 'dan']
size of cluster: 4062
---- "Zasanjane melodije iz čeških gajev, ognjeviti ritmi ruske glasbe in vedre pesmi naše dežele"
---- Bogat program, bogat odziv: oddaja Srečno 2024! poskrbela za nepozaben glasbeni vstop v novo leto
---- Novoletni koncert Dunajskih filharmonikov je tudi letos minil s slovensko udeležbo
---- Duh iztekajočih se novoletnih praznikov
---- Vesolje med nami, slovenski mladinski film – ponedeljek, 1. 1., ob 20.05 na TV SLO 1 
---- Antonio Gramsci
---- Od "žurerskega princa" do novega danskega kralja
---- Skoraj stoletje kasneje Mišek Miki in druga pomembna dela prehajajo v javno last
---- Pregled leta: s kakšnimi glasbenimi poslasticami je postreglo leto 2023?
---- Javier Milei na odru strastno poljubil svojo izbranko