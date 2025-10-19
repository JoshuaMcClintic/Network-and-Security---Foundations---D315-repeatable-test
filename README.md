## README

If you would like to use this script to test yourself, simply download the .zip file in the Releases section and 
run the main.py file. No external libraries are needed to run, so it should be good to go, assuming you have python 
on your device.

This program was designed to review questions given in the Network and Security - Foundations D315 class at WGU 
course material -> Section _n_: Summary -> Section _n_: Test. Those questions do not reset after reloading the 
page, and always come in a set order. This script simply jumbles the questions and does not save progress, so you 
can redo as many times as you want. It also jumbles the answers for any given question, but does not include 
answers that the original question did not include in its multiple choice section. Also, all questions will be 
multiple choice. I will not be adding open answer. If you want that, either add it yourself or find a different 
script.
---
Included in the files is a Test_Template.py file that you can use to create your own test questions, if you want. 
Just keep in mind that, for each set of answers, the response _has to_ be in the same order (i.e. answers: a, b, c, d
are set to question 1, so responses: a, b, c, d should be set to response 1, in the same order). If you do not have 
20 separate questions to use, simply remove some of the key-value pairs in both the <questions> dictionary and the 
<responses> dictionary. You will also need to change the <num_questions> variable in lines 235 and 253 of the main.py
file to match the number of questions your test and in the total number of tests, respectively.

It's probable best to duplicate the Test_Template.py file and use the new file to create your test, so that you can 
still have a template file. Also, in the methods 'random_test' and 'set_test', the actual .py files for the test 
being used is hard-coded, so you will have to change that as well. It's not a difficult change, though, as you'll 
just have to change Test_n._attribute_ to your_test_name._attribute_.
---
## Inputs

On running the main.py file, you will be asked two questions to set up the quiz: 
'Which section would you like to review? (1, 2, 3, all): ' and 
'Would you like the questions to be in a random order? (y/n): '. The first determines which section you will be 
quizzed on, and the second determines whether they will be in a random order or the order given in the original test
section in the course material. Answers to individual questions will always be jumbled, since I've already wasted 
enough time on this. You can always type 'exit' to exit the test.
---
## Outputs

Output is the question and set of answers. After the user gives a response, the program will output a reply, saying 
whether it was correct, as well as an explanation of why it was or was not correct. The explanation was pulled 
straight from the course material test sections, so if you feel that it is not satisfactory, blame whoever made it, 
not me. If correct, you will see a separation between the new question you're being asked and the previous 
question you just got correct, as well as the new question number, like you see below.

    ------------------------------------------------------
    Question n

If the question is incorrect, you will be asked the same question, and the same answer order.

---
## Bugs and glitches

If you encounter something that prevents the script from running, please let me know in the issues section of GitHub, 
and I will see what I can do. If you want me to add something specific, type 'Request' or some other signifier that 
it is not an internal bug, but something you want to see added. Note that bugs will take priority, and not all 
requests will be added.
---


#### Python version 3.11
