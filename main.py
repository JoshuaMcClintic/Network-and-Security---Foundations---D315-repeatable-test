import sys

import Test_1
import Test_2
import Test_3
import All_Tests
import random

# used_list in order to not get the same question twice when using a random question order
used_list = []


def random_test(test_num: str):
    """
    test_num is type: str because it takes input from user at the end of this script. Input might not be type: int.
    Gathers questions, answers, and index numbers from Test_n modules, generates random number;
    Using random number and key_lists, print question and answers at that index;
    Check responses dictionary at that index and check index of the answer given by the user;
    Return response at previous index;
    Loop while not correct
    :param test_num: Section number, test number
    :return: None
    """
    # Define variable to determine if the answer given by user is correct
    correct = False
    # Gather questions, answers, key_lists from Test_n modules
    if test_num == '1':
        quest = Test_1.questions
        resp = Test_1.responses
        q_list = Test_1.quest_key_list
        r_list = Test_1.resp_key_list
        question = random.randrange(0, 20)
    elif test_num == '2':
        quest = Test_2.questions
        resp = Test_2.responses
        q_list = Test_2.quest_key_list
        r_list = Test_2.resp_key_list
        question = random.randrange(0, 20)
    elif test_num == '3':
        quest = Test_3.questions
        resp = Test_3.responses
        q_list = Test_3.quest_key_list
        r_list = Test_3.resp_key_list
        question = random.randrange(0, 20)
    # If test_num is not string: 1, 2, or 3; use All_Tests module
    else:
        quest = All_Tests.all_tests_questions
        resp = All_Tests.all_tests_responses
        q_list = All_Tests.all_quest_key_list
        r_list = All_Tests.all_resp_key_list
        question = random.randrange(0, 60)

    # Take value from questions dictionary (possible answers), create list of answers in random order
    answers = random.sample(quest[q_list[question]], 4)
    # Check list of used questions, add current question to list
    if q_list[question] not in used_list:
        used_list.append(q_list[question])
        # Print question and possible answers; find index of key in questions dictionary using key_list;
        # Using key_list[index_num] as the key for searching through dictionary, find original order of answers;
        # Check response dictionary using same method; response[key_list[index_num]] correlates to
        # questions[key_list[index_num]]
        # Search for index number of answer, return index number of response
        # Loop until the answer given is correct
        while not correct:
            print()
            print(q_list[question])
            print(f'A: {answers[0]}\n'
                  f'B: {answers[1]}\n'
                  f'C: {answers[2]}\n'
                  f'D: {answers[3]}')
            user_response = input('Type your answer (a, b, c, d): ').lower()
            print()

            if user_response == 'a':
                resp_index = quest[q_list[question]].index(answers[0])
                # print(resp[r_list[question]])
                for item in quest[q_list[question]]:
                    if item == answers[0]:
                        print(resp[r_list[question]][resp_index])
                        if resp[r_list[question]][resp_index][0:3] == 'Tha':
                            correct = True
                            print('-----------------------------------------------------------------------------------')

            elif user_response == 'b':
                resp_index = quest[q_list[question]].index(answers[1])
                # print(resp[r_list[question]])
                for item in quest[q_list[question]]:
                    if item == answers[1]:
                        print(resp[r_list[question]][resp_index])
                        if resp[r_list[question]][resp_index][0:3] == 'Tha':
                            correct = True
                            print('-----------------------------------------------------------------------------------')

            elif user_response == 'c':
                resp_index = quest[q_list[question]].index(answers[2])
                # print(resp[r_list[question]])
                for item in quest[q_list[question]]:
                    if item == answers[2]:
                        print(resp[r_list[question]][resp_index])
                        if resp[r_list[question]][resp_index][0:3] == 'Tha':
                            correct = True
                            print('-----------------------------------------------------------------------------------')

            elif user_response == 'd':
                resp_index = quest[q_list[question]].index(answers[3])
                # print(resp[r_list[question]])
                for item in quest[q_list[question]]:
                    if item == answers[3]:
                        print(resp[r_list[question]][resp_index])
                        if resp[r_list[question]][resp_index][0:3] == 'Tha':
                            correct = True
                            print('-----------------------------------------------------------------------------------')

            elif user_response == 'exit':
                sys.exit()

            else:
                print('Please make a selection.')


def set_test(test_num: str):
    """
    test_num is type: str because it takes input from user at the end of this script. Input might not be type: int.
    Gathers questions, answers, and index numbers from Test_n modules, creates question variable;
    Using question var and key_lists, print question and answers at that index;
    Check responses dictionary at that index and check index of the answer given by the user;
    Return response at previous index;
    Loop while not correct
    Once given response is correct, add 1 to question var
    :param test_num: Section number, test number
    :return: None
    """
    # Define variable to determine if the answer given by user is correct
    correct = False
    # Gather questions, answers, key_lists from Test_n modules
    if test_num == '1':
        quest = Test_1.questions
        resp = Test_1.responses
        q_list = Test_1.quest_key_list
        r_list = Test_1.resp_key_list
        question = 0
    elif test_num == '2':
        quest = Test_2.questions
        resp = Test_2.responses
        q_list = Test_2.quest_key_list
        r_list = Test_2.resp_key_list
        question = 0
    elif test_num == '3':
        quest = Test_3.questions
        resp = Test_3.responses
        q_list = Test_3.quest_key_list
        r_list = Test_3.resp_key_list
        question = 0
    # If test_num is not string: 1, 2, or 3; use All_Tests module
    else:
        quest = All_Tests.all_tests_questions
        resp = All_Tests.all_tests_responses
        q_list = All_Tests.all_quest_key_list
        r_list = All_Tests.all_resp_key_list
        question = 0

    # Take value from questions dictionary (possible answers), create list of answers in random order
    answers = random.sample(quest[q_list[question]], 4)
    # Print question and possible answers; find index of key in questions dictionary using key_list;
    # Using key_list[index_num] as the key for searching through dictionary, find original order of answers;
    # Check response dictionary using same method; response[key_list[index_num]] correlates to
    # questions[key_list[index_num]]
    # Search for index number of answer, return index number of response
    # Loop until the answer given is correct
    while not correct:
        print()
        print(q_list[question])
        print(f'A: {answers[0]}\n'
              f'B: {answers[1]}\n'
              f'C: {answers[2]}\n'
              f'D: {answers[3]}')
        user_response = input('Type your answer (a, b, c, d): ').lower()
        print()

        if user_response == 'a':
            resp_index = quest[q_list[question]].index(answers[0])
            # print(resp[r_list[question]])
            for item in quest[q_list[question]]:
                if item == answers[0]:
                    print(resp[r_list[question]][resp_index])
                    if resp[r_list[question]][resp_index][0:3] == 'Tha':
                        correct = True
                        question += 1
                        print('-----------------------------------------------------------------------------------')

        elif user_response == 'b':
            resp_index = quest[q_list[question]].index(answers[1])
            # print(resp[r_list[question]])
            for item in quest[q_list[question]]:
                if item == answers[1]:
                    print(resp[r_list[question]][resp_index])
                    if resp[r_list[question]][resp_index][0:3] == 'Tha':
                        correct = True
                        question += 1
                        print('-----------------------------------------------------------------------------------')

        elif user_response == 'c':
            resp_index = quest[q_list[question]].index(answers[2])
            # print(resp[r_list[question]])
            for item in quest[q_list[question]]:
                if item == answers[2]:
                    print(resp[r_list[question]][resp_index])
                    if resp[r_list[question]][resp_index][0:3] == 'Tha':
                        correct = True
                        question += 1
                        print('-----------------------------------------------------------------------------------')

        elif user_response == 'd':
            resp_index = quest[q_list[question]].index(answers[3])
            # print(resp[r_list[question]])
            for item in quest[q_list[question]]:
                if item == answers[3]:
                    print(resp[r_list[question]][resp_index])
                    if resp[r_list[question]][resp_index][0:3] == 'Tha':
                        correct = True
                        question += 1
                        print('-----------------------------------------------------------------------------------')

        elif user_response == 'exit':
            sys.exit()

        else:
            print('Please make a selection.')


which_test = input('Which section would you like to review? (1, 2, 3, all): ' or 'all')
question_order = input('Would you like the questions to be in a random order? (y/n): ' or 'y')

if which_test == '1' or which_test == '2' or which_test == '3':
    num_questions = 20
    cur_quest = 0
    # Random question order
    if question_order == 'y':
        while cur_quest < num_questions:
            print(f'Question {cur_quest + 1}')
            random_test(which_test)
            cur_quest += 1
    # Set question order
    elif question_order == 'n':
        while cur_quest < num_questions:
            print(f'Question {cur_quest + 1}')
            set_test(which_test)
            cur_quest += 1
    else:
        print('No selection made. Aborting')

else:
    num_questions = 60
    cur_quest = 0
    # Random question order
    if question_order == 'y':
        while cur_quest < num_questions:
            print(f'Question {cur_quest + 1}')
            random_test(which_test)
            cur_quest += 1
    # Set question order
    elif question_order == 'n':
        while cur_quest < num_questions:
            print(f'Question {cur_quest + 1}')
            set_test(which_test)
            cur_quest += 1
    else:
        print('No selection made. Aborting')
