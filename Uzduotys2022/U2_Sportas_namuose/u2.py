def suformuoti(treniruotes):
    rezultatas = []
    for treniruote in treniruotes:
        if not len(rezultatas):
            irasas = {'tipas': treniruote['tipas'], 'kartai': [treniruote['diena']], 'pratimai': treniruote['pratimai'],
                      'laikai': [{'laikas': treniruote['laikas'], 'kartai': 1}]}
            rezultatas.append(irasas)
        else:
            naujas_tipas = True
            for index, irasas in enumerate(rezultatas):
                dienos = irasas['kartai']
                if treniruote['tipas'] == irasas['tipas']:
                    naujas_tipas = False
                    laikai = irasas['laikai']
                    naujas_laikas = True
                    for ind, laikas in enumerate(laikai):
                        if laikas['laikas'] == treniruote['laikas']:
                            naujas_laikas = False

                            laikai[ind] = {'laikas': laikas['laikas'], 'kartai': int(laikas['kartai']) + 1}

                    if naujas_laikas:
                        irasas['laikai'].append({'laikas': treniruote['laikas'], 'kartai': 1})
                    if treniruote['diena'] not in dienos:
                        dienos.append(treniruote['diena'])
                    rezultatas[index] = {'tipas': irasas['tipas'], 'kartai': dienos,
                                         'pratimai': int(irasas['pratimai']) + int(treniruote['pratimai']),
                                         'laikai': laikai}
            if naujas_tipas:
                rezultatas.append({'tipas': treniruote['tipas'], 'kartai': [treniruote['diena']], 'pratimai': treniruote['pratimai'],
                 'laikai': [{'laikas': treniruote['laikas'], 'kartai': 1}]})

    for value in rezultatas:
        value['kartai'] = len(value['kartai'])

    return rezultatas

def split_list(listas):
    start = 0
    end = len(listas)
    step = 3
    rezultatas = []
    for i in range(start, end, step):
        x = i
        rezultatas.append(listas[x:x + step])

    return rezultatas

with open('U2.txt') as failas:
    kiekis = int(failas.readline())
    treniruotes = []
    for dienos_index in range(kiekis):
        diena = failas.readline().strip().split(' ')
        treniruociu_per_diena = diena.pop(0)
        if int(treniruociu_per_diena) > 1:
            for pratimas in split_list(diena):
                treniruote = {'tipas': pratimas[0], 'laikas': pratimas[1], 'pratimai': pratimas[2], 'diena': int(dienos_index)}
                treniruotes.append(treniruote)
        else:
            treniruote = {'tipas': diena[0], 'laikas': diena[1], 'pratimai': diena[2], 'diena': int(dienos_index)}
            treniruotes.append(treniruote)

    paruosta_isvedimui = suformuoti(treniruotes)

    with open('U2rez.txt', 'w') as output:
        for treniruote in sorted(paruosta_isvedimui, key=lambda x: x['tipas']):
            output.write(f"{treniruote['tipas']} {treniruote['kartai']} {treniruote['pratimai']}\n")
            for laikas in treniruote['laikai']:
                output.write(f"{laikas['laikas']} {laikas['kartai']}\n")
