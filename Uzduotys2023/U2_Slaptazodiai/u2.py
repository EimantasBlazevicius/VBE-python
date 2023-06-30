def kodu_panasumo_reiksme(kodas1, kodas2):
    """
    :param kodas1:
    :param kodas2:
    :return: Atemus reiksmes ir paemus ju absoliuciu reiksmiu suma gaunam panasumo indeksa
    """
    ilgis = kodas1['ilgis'] - kodas2['ilgis']
    didziosios = kodas1['didziosios'] - kodas2['didziosios']
    mazosios = kodas1['mazosios'] - kodas2['mazosios']
    skaiciai = kodas1['skaiciai'] - kodas2['skaiciai']
    spec = kodas1['spec'] - kodas2['spec']

    return abs(ilgis) + abs(didziosios) + abs(mazosios) + abs(skaiciai) + abs(spec)


def maziausio_radimas(kodas, listas):
    """
    :param kodas:
    :param listas:
    :return: Naudodami kodu_panasumo_reiksme() funkcija
    randam maziausia panasumo indeksa duotam kodui, duodam liste
    Su idėja kad pagal nutylėjimą nepanasumas neperlips 99
    """
    maziausias = 99
    for paruostas_kodas in listas:
        if kodu_panasumo_reiksme(kodas, paruostas_kodas) < maziausias:
            maziausias = kodu_panasumo_reiksme(kodas, paruostas_kodas)

    return maziausias


# Programos pradzia
# nuskaitom U2.txt i duomenys kontekstą
with open('U2.txt') as duomenys:
    # nusiskaitom pirmą eilutę ir ją padalinam į du kintamuosius
    vartotojo_pass_kiekis, paruostu_pass_kiekis = duomenys.readline().split(' ')
    # inicijuoju tuščius listus į kuriuos paskui pridėsiu reikšmių
    vartotojo_passwords = []
    paruosti_passwords = []

    # Du daug maž vienodi ciklai kad nuskaityt po žinomą kiekį eilučių iš failo
    # ir jas sudėliojus į dictionary pridėt į atitinkamus sąrašus
    for _ in range(int(vartotojo_pass_kiekis)):
        kodas = duomenys.readline().strip().split(' ')
        vartotojo_passwords.append({'kodas': kodas[0], 'ilgis': int(kodas[1]), 'didziosios': int(kodas[2]),
                               'mazosios': int(kodas[3]), 'skaiciai': int(kodas[4]), 'spec': int(kodas[5])})

    for _ in range(int(paruostu_pass_kiekis)):
        kodas = duomenys.readline().strip().split(' ')
        paruosti_passwords.append({'kodas': kodas[0], 'ilgis': int(kodas[1]), 'didziosios': int(kodas[2]),
                               'mazosios': int(kodas[3]), 'skaiciai': int(kodas[4]), 'spec': int(kodas[5]), 'lygis': kodas[6]})

    # inicijuojam tuščia rezultatu sąrašą
    rezultatai = []
    # kiekvienam kodui
    for vart_kodas in vartotojo_passwords:
        # prisikiriam pavadinimą ir tuščią panašių kodų listą
        vartotojas = {'kodas': vart_kodas['kodas'], 'panasus': []}
        # pagal nutylėjimą saugumo lygio nėra
        lygis = ''
        # susirandu mažiausią šio kodo panašumą su listu
        maziausias_panasumas = maziausio_radimas(vart_kodas, paruosti_passwords)
        # iteruoju per kodus kurie atitinka mano mažiausio panasumo reikalavimą ir prisiskiriu reiksmes
        for paruostas_kodas in paruosti_passwords:
            if kodu_panasumo_reiksme(vart_kodas, paruostas_kodas) <= maziausias_panasumas:
                lygis = paruostas_kodas['lygis']
                vartotojas['panasus'].append(paruostas_kodas['kodas'])
        # pridedu reikamas reiksmes į dictionary
        vartotojas['maziausias_panasumas'] = maziausias_panasumas
        vartotojas['lygis'] = lygis
        # prided dictionary į rezultatų sąrašą
        rezultatai.append(vartotojas)

    # Rašom į failą
    with open('U2rez.txt', 'w') as output:
        for irasas in rezultatai:
            output.write(f"{irasas['kodas']} {irasas['maziausias_panasumas']} {irasas['lygis']}\n")
            # išrykiuoju panašius kodus pagal ilgy nuo ilgiausio iki trumpiausio ir nieko nedarau kai kodai vienodo ilgio,
            # [agal nutylėjimą sort funkcija nieko nekeis jeigu pagal kriterijų, negali
            irasas['panasus'].sort(key=len, reverse=True)
            for kodas in irasas['panasus']:
                output.write(f"{kodas}\n")
