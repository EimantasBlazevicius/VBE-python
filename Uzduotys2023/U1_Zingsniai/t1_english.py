def process_data(participants):
    result = []
    for participant in participants:
        all_steps = 0
        for steps in participant[2:]:
            all_steps += int(steps)

        kilometers = all_steps * (int(participant[1]) / 100000)

        if not len(result):
            result.append({'grade': participant[0], 'amount': 1, 'kilometers': round(kilometers, 2)})
        else:
            is_new = True
            for index, record in enumerate(result):
                if record['grade'] == participant[0]:
                    is_new = False
                    result[index] = {'grade': record['grade'], 'amount': record['amount']+1,
                                     'kilometers': record['kilometers'] + round(kilometers, 2)}

            if is_new:
                result.append({'grade': participant[0], 'amount': 1, 'kilometers': round(kilometers, 2)})

    return result

with open('u1.txt') as source:
    amount_of_participants = int(source.readline())
    real_participants = []

    for _ in range(amount_of_participants):
        is_participating = True
        participant = source.readline().strip().split()
        for steps in participant[2:]:
            if steps == '0':
                is_participating = False

        if is_participating:
            real_participants.append(participant)

    preapared_data = process_data(real_participants)

    with open('U1rez.txt', 'w') as output:
        for grade in preapared_data:
            output.write(f"{grade['grade']} {grade['amount']} {grade['kilometers']}\n")