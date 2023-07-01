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



with open('U1.txt') as failas:
    uzduociu_kiekis = int(failas.readline())
    uzduociu_laikai = failas.readline().strip().split(' ')
    uzduociu_taskai = failas.readline().strip().split(' ')
    dalyviai = []

    for zmogus in failas.readlines():
        dalyvis = zmogus.strip().split(' ')
        if not dalyvis[1].isnumeric():
            dalyvis[0] += f" {dalyvis[1]}"
            dalyvis.pop(1)
        dalyviai.append({'vardas': dalyvis[0], 'laikai': [laikas for laikas in dalyvis[1:]]})

    daugiausia_tasku = 0
    final_dalyviai = []
    for dalyvis in dalyviai:
        final_dalyviai.append(dalyvio_rezultatai(dalyvis))
        if daugiausia_tasku < dalyvio_rezultatai(dalyvis)['taskai']:
            daugiausia_tasku = dalyvio_rezultatai(dalyvis)['taskai']


    with open('U1rez.txt', 'w') as output:
        output.write(f"{daugiausia_tasku}\n")
        for dalyvis in sorted(final_dalyviai, key=lambda x: x['laikas'], reverse=True):
            if dalyvis['taskai'] == daugiausia_tasku:
                output.write(f"{dalyvis['vardas']} {dalyvis['teisingi']} {dalyvis['laikas']}\n")