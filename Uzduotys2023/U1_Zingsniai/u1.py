# funkcija priima dalyvių sąrašą
def viena_funkcija(dalyviai):
    # Pasiruošiam tušią rezultatų listą kad jį būtų galima papildyti
    rezultatas = []

    # Su kiekvienu dalyviu
    for dalyvis in dalyviai:
        # inicijuoju zingsniu sumos kintamaji
        visi_zingsniai = 0
        # sudedu dalyvio zingsnius
        for zingsniai in dalyvis[2:]:
            visi_zingsniai += int(zingsniai)
        # ir padauginu bendrą nueitu zingsniu kiekį is zingsnio ilgio padalindamas iš 100000,
        # nes galop reiks reikšmės kilometrais
        kilometrai = int(visi_zingsniai) * (int(dalyvis[1]) / 100000)

        # Jeigu rezultatų sąrašas tuščias
        if not len(rezultatas):
            # Įrašom pirmą eilutę be jokių patikrinimu
            rezultatas.append({'klase': dalyvis[0], 'kiekis': 1,
                               'kilometrai': round(kilometrai, 2)})
        # Kitu atveju
        else:
            # pagal nutylėjimą manysiu kad klasė yra nauja ir prieš tai nebuvo
            # paminėta rezultatų sąraše
            nauja = True
            # patikrinimui ar dalyvio klasė jau įtraukta į rezultatų sąrašą iteruoju rezultatų listą
            # pasiimdamas ir index reikšmę, kad galėčiau pakeisti įrašą jeigu klasė jau yra sąraše
            for index, irasas in enumerate(rezultatas):
                # Jeigu rezultatų faile randu atitikmenį dabartinio dalyvio klasei
                if irasas['klase'] == dalyvis[0]:
                    # pasižymiu kad šio dalyvio klasė nebus nauja
                    nauja = False
                    # atnaujinu šio rezultatų failo įrašą pridedamas reikšmes iš šio dalyvio
                    rezultatas[index] = {'klase': irasas['klase'], 'kiekis': irasas['kiekis'] + 1,
                                         'kilometrai': irasas['kilometrai'] + round(kilometrai, 2)}
            # jeigu dalyvio klasė dar nebuvo paminėra rezultatų faile
            if nauja:
                # Pridedu šio dalyvio informaciją į rezultatus
                rezultatas.append({'klase': dalyvis[0], 'kiekis': 1,
                                   'kilometrai': round(kilometrai, 2)})
    # funkcija gražina rezultatų listą.
    return rezultatas


# Programos pradžia
# persikeliam duomenų failą į 'duomenys' kontekstą
with open('u1.txt') as duomenys:
    # perskaitom pirmą eilutę kad turėtumėm bendrą dalyvių kiekį
    dalyviu_kiekis = int(duomenys.readline())
    # pasiruošiam tuščią list kad galėtumėm jį papildyt dalyviais kurie kiekvieną dieną įvedė reikšmes
    tikri_dalyviai = []
    # sukam ciklą tiek kartų kiek bendrai yra dalyvių, _ yra naudojamas kaip nereikalingas kimtamasis kurio nenaudosim
    for _ in range(dalyviu_kiekis):
        # Jeigu nebus pasakyta kitaip, pagal nutylėjimą dalyvis viską padarė gerai, ir jis dalyvauja konkurse
        dalyvauja = True
        # Pasiruošiam dalyvio duomenis:
        # readline() - nuskaito eilutę
        # strip() - panaikina '\n' elementus nuo kiekvienos eilutės pabaigos
        # split(' ') - suskirsto kiekvieną tarpu atskirtą reikšmę kaip atskirą listo reikšmę
        dalyvis = duomenys.readline().strip().split(' ')

        # pasukam ciklą per žingsnių reikšmes šiam dalyviui,
        # dalyvis[2:] pradeda iteruoti praleisdamas
        # klasę ir žingsnio ilgį
        for zingsniai in dalyvis[2:]:
            # Jeigu liste randamas bent vienas žingsnis paminėtas kaip 0
            if zingsniai == '0':
                # mokinys konkurse nebendalyvauja
                dalyvauja = False
        # Jeigu dalyvavimas nebuvo atšauktas dėl neįvestų žingsnių
        if dalyvauja:
            # pridedam dalyvį į tikrų dalyvių listą
            tikri_dalyviai.append(dalyvis)
    # paruošiam duomenis rašyti į failą
    duomenys_failui = viena_funkcija(tikri_dalyviai)

    # priskirsiu rezultatu_failas kontekstui rezultatų failą su galimybe į jį rašyt
    with open('U1rez.txt', 'w') as rezultatu_failas:
        # kiekviena rezultatų eilutė
        for rez in duomenys_failui:
            # surašomą į failą kaip suformatuotas string elementas su \n jos gale,
            # kad pradėtų sekantį įrašą naujoj eilutėj
            rezultatu_failas.write(f"{rez['klase']} {rez['kiekis']} {rez['kilometrai']}\n")
