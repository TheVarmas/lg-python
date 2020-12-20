question_bag = [
    {
        "question":"Where does the sun rise?",
        "options":["East","West", "North", "South"],
        "answer": 0
    }, 
    {
        "question":"Where does the sun set?",
        "options":["North","East", "West", "South"], 
        "answer": 2
    },
    {
        "question":"When is Canada day?",
        "options":["June 2nd","August 20th", "July 1st", "November 3rd"], 
        "answer": 2
    }
]
valid_options = ['a', 'b', 'C', 'd']
option_separator = '.'
score = 0
qno = 0
print("Welcome to the Quiz!")
invalid_questions = 0
while qno < len(question_bag):
    if len(question_bag[qno]["options"]) != len(valid_options):
        print("Something is wrong with this questsion or the options so I will skip it.")
        qno += 1
        invalid_questions += 1
        continue

    print(question_bag[qno]["question"])
    print()

    answer = valid_options[question_bag[qno]["answer"]]
    index = 0
    for i in question_bag[qno]["options"]:
        print(f'{valid_options[index]}{option_separator} {i}')
        index += 1

    input_answer = input('Enter your answer: ')

    if input_answer.upper() not in valid_options and input_answer.lower() not in valid_options:
        print('You entered an invalid answer')
        continue
    elif input_answer.upper() == answer.upper():
        score += 1

    qno += 1

print(f'Your score is {score} / {len(question_bag) - invalid_questions}')

