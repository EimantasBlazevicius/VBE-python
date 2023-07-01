from operator import itemgetter

def dalyvio_rezultatai(dalyvis):
    surinkti_taskai = 0
    teisingi_sprendimai = 0
    sprendimo_laikas = 0
    for index, dalyvio_laikas in enumerate(dalyvis['laikai']):
        if int(dalyvio_laikas) <= int(uzduociu_laikai[index]) and dalyvio_laikas != '0':
            surinkti_taskai += int(uzduociu_taskai[index])
            teisingi_sprendimai += 1
            sprendimo_laikas += int(dalyvio_laikas)
        elif int(dalyvio_laikas) > int(uzduociu_laikai[index]):
            surinkti_taskai += int(uzduociu_taskai[index]) // 2
            teisingi_sprendimai += 1
            sprendimo_laikas += int(dalyvio_laikas)

    return {'vardas':dalyvis['vardas'], 'taskai': surinkti_taskai,
            'teisingi': teisingi_sprendimai, 'laikas': sprendimo_laikas}


# Programos pradzia
# Nuskaitom failą
with open('U1.txt') as failas:
    # Prisiskiriam reikšmes
    uzduociu_kiekis = int(failas.readline())
    uzduociu_laikai = failas.readline().strip().split(' ')
    uzduociu_taskai = failas.readline().strip().split(' ')
    # nuskaitom dalyvius
    dalyviai = []
    for zmogus in failas.readlines():
        dalyvis = zmogus.strip().split(' ')
        # issprendziam tą nesamonę kur gali būt du vardai
        if not dalyvis[1].isnumeric():
            dalyvis[0] += f" {dalyvis[1]}"
            dalyvis.pop(1)
        # supildom dalyvius mum patogiu formatu
        dalyviai.append({'vardas': dalyvis[0], 'laikai': [laikas for laikas in dalyvis[1:]]})

    # pasiruosiam kintamuosius rezultatam
    daugiausia_tasku = 0
    final_dalyviai = []
    # performatuojam dalyvius i nauja listą
    for dalyvis in dalyviai:
        final_dalyviai.append(dalyvio_rezultatai(dalyvis))
        # randam daugiausia taškų rezultata
        if daugiausia_tasku < dalyvio_rezultatai(dalyvis)['taskai']:
            daugiausia_tasku = dalyvio_rezultatai(dalyvis)['taskai']


    # rašom i failą
    with open('U1rez.txt', 'w') as output:
        output.write(f"{daugiausia_tasku}\n")
        # surikiuojam rezultatu faila pagal laiką nuo daugiausia uztrukusio iki trumpiausia
        for dalyvis in sorted(final_dalyviai, key=lambda x: x['laikas'], reverse=True):
            if dalyvis['taskai'] == daugiausia_tasku:
                output.write(f"{dalyvis['vardas']} {dalyvis['teisingi']} {dalyvis['laikas']}\n")