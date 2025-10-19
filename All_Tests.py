import Test_1
import Test_2
import Test_3

# Combine all question-answer pairs from each section
all_tests_questions = Test_1.questions | Test_2.questions | Test_3.questions

# Combine all responses for each answer from each section
all_tests_responses = Test_1.responses | Test_2.responses | Test_3.responses

# Combine all questions from each section in order to find certain answer-response pair using numerical index
all_quest_key_list = Test_1.quest_key_list + Test_2.quest_key_list + Test_3.quest_key_list

# Combine all response keys from each section in order to find answer-response pair using numerical index
all_resp_key_list = Test_1.resp_key_list + Test_2.resp_key_list + Test_3.resp_key_list
