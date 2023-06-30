def kodu_panasumo_reiksme(kodas1, kodas2):
    ilgis = kodas1['ilgis'] - kodas2['ilgis']
    didziosios = kodas1['didziosios'] - kodas2['didziosios']
    mazosios = kodas1['mazosios'] - kodas2['mazosios']
    skaiciai = kodas1['skaiciai'] - kodas2['skaiciai']
    spec = kodas1['spec'] - kodas2['spec']

    return abs(ilgis) + abs(didziosios) + abs(mazosios) + abs(skaiciai) + abs(spec)


def maziausio_radimas(kodas, listas):
    maziausias = 99
    for paruostas_kodas in listas:
        if kodu_panasumo_reiksme(kodas, paruostas_kodas) < maziausias:
            maziausias = kodu_panasumo_reiksme(kodas, paruostas_kodas)

    return maziausias


with open('U2.txt') as duomenys:
    slaptazodziu_kiekiai = duomenys.readline().split(' ')
    vartotojo_pass_kiekis, paruostu_pass_kiekis = slaptazodziu_kiekiai
    vartotojo_passwords = []
    paruosti_passwords = []

    for _ in range(int(vartotojo_pass_kiekis)):
        kodas = duomenys.readline().strip().split(' ')
        vartotojo_passwords.append({'kodas': kodas[0], 'ilgis': int(kodas[1]), 'didziosios': int(kodas[2]),
                               'mazosios': int(kodas[3]), 'skaiciai': int(kodas[4]), 'spec': int(kodas[5])})

    for _ in range(int(paruostu_pass_kiekis)):
        kodas = duomenys.readline().strip().split(' ')
        paruosti_passwords.append({'kodas': kodas[0], 'ilgis': int(kodas[1]), 'didziosios': int(kodas[2]),
                               'mazosios': int(kodas[3]), 'skaiciai': int(kodas[4]), 'spec': int(kodas[5]), 'lygis': kodas[6]})

    rezultatai = []
    for vart_kodas in vartotojo_passwords:
        vartotojas = {'kodas': vart_kodas['kodas'], 'panasus': []}
        lygis = ''
        maziausias_panasumas = maziausio_radimas(vart_kodas, paruosti_passwords)
        for paruostas_kodas in paruosti_passwords:
            if kodu_panasumo_reiksme(vart_kodas, paruostas_kodas) <= maziausias_panasumas:
                lygis = paruostas_kodas['lygis']
                vartotojas['panasus'].append(paruostas_kodas['kodas'])
        vartotojas['maziausias_panasumas'] = maziausias_panasumas
        vartotojas['lygis'] = lygis
        rezultatai.append(vartotojas)

    with open('U2rez.txt', 'w') as output:
        for irasas in rezultatai:
            output.write(f"{irasas['kodas']} {irasas['maziausias_panasumas']} {irasas['lygis']}\n")
            irasas['panasus'].sort(key=len, reverse=True)
            for kodas in irasas['panasus']:
                output.write(f"{kodas}\n")
