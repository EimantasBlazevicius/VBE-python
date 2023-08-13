def process_data(participants):
    """
    Resort the data based on grade
    :param participants: list of participants
    :return: a list of obejcts like this:
    [{'grade': participant grade,
     'amount': amount of participants in this grade,
     'kilometers': round(kilometers, 2)}]
    """

    result = [] # initialize the result list to store objects
    for participant in participants: # for each participant
        all_steps = 0 # At the start there are 0 steps
        for steps in participant[2:]: # then for each step record of the steps the participant took
            all_steps += int(steps) # we add the steps to the total of participant steps
        kilometers = all_steps * (int(participant[1]) / 100000) #convert steps into kilometers based on participant step length

        # if no records in the results list, we just add the object into this list
        if not len(result):
            result.append({'grade': participant[0], 'amount': 1, 'kilometers': round(kilometers, 2)})
        else: # if it is not the first record
            is_new = True # we assume that it is a new and fresh grade
            for index, record in enumerate(result): # iterating through results list to find if it is really new one
                if record['grade'] == participant[0]: # if grade from results matches the grade of the participant
                    is_new = False # we assume that the grade is not new
                    # we adjust the existing grade object to include current participant data
                    result[index] = {'grade': record['grade'], 'amount': record['amount']+1,
                                     'kilometers': record['kilometers'] + round(kilometers, 2)}
            # if the grade is new, we just add the object into the list
            if is_new:
                result.append({'grade': participant[0], 'amount': 1, 'kilometers': round(kilometers, 2)})

    return result

with open('u1.txt') as source: # Reading the source file
    amount_of_participants = int(source.readline()) # We read the first line and get amount of participants
    real_participants = [] # Initialize the empty list to append with actual participants later

    for _ in range(amount_of_participants): # iterating per amount of participants
        is_participating = True # by default we assume the people are good and they log progress every day
        participant = source.readline().strip().split() # Read and clean data of participant
        for steps in participant[2:]: # Since steps only start from col 3, we start from the index 2 to get all the steps values
            if steps == '0': # if user did not enter steps correctly that day it will be equal to 0
                is_participating = False # in that case this participant is not participating anymore :)

        # if participant is still good he will be added to the list of real participants
        if is_participating:
            real_participants.append(participant)

    # we send the participants list to process
    # function and expect to receive data to write to file
    preapared_data = process_data(real_participants)

    #writing data to the file
    with open('U1rez.txt', 'w') as output:
        for grade in preapared_data:
            output.write(f"{grade['grade']} {grade['amount']} {grade['kilometers']}\n")