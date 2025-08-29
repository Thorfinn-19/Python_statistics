Három dobókocka eloszlásának vizsgálata
Leírás

Ez a program a három dobókockával végzett dobások eloszlását vizsgálja két különböző megközelítésben:

Teljes elméleti eloszlás (szabályos eloszlás, a programban x_normal):
Itt minden lehetséges dobáskombinációt (6³ = 216 eset) generálunk, majd kiszámítjuk az összegeket. Ez egy teljes populáció, amely pontosan mutatja, milyen gyakorisággal fordulhatnak elő az egyes összegek.

Véletlenszerű minta (sztochasztikus eloszlás, a programban x_random):
Ezután véletlenszerűen is dobunk 216-szor a három kockával, és a kapott összegeket egy másik listába mentjük. Ez egy minta, amely a valóságban történő dobásokat szimulálja.

A kétféle adatforrást összehasonlítjuk a következők szerint:

Átlag (mean)

Medián (median)

Szórás (standard deviation)

Végül hisztogramokon ábrázoljuk mindkét eloszlást, így vizuálisan is megfigyelhetjük a különbségeket.

Tudományos háttér

A három kocka összegének eloszlása nem egyenletes, hanem haranggörbére emlékeztető alakot követ.
Ennek oka a kombinatorika: például a 10-es összeg sokféleképpen előállítható (pl. 4+3+3, 6+2+2, 5+4+1 stb.), míg a 3 vagy 18 csak egyetlen módon (1+1+1 illetve 6+6+6).

Az elméleti eloszlás a pontos szabályosságot mutatja, ahol minden kombináció számításba van véve.

A véletlen minta viszont a tényleges dobások során tapasztalható fluktuációkat és mintavételi zajt mutatja.

Ezzel a kísérlettel szemléltethető, hogy egy véges számú kísérlet (pl. 216 dobás) hogyan közelíti a teljes populáció valódi eloszlását, és hogyan jelennek meg a véletlen hatásai.
