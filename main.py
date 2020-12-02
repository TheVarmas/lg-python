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
        "question":"Where does the sun set?",
        "options":["North","East", "West", "South"], 
        "answer": 2
    }
]
valid_options = ['a', 'b', 'C', 'd']
option_separator = ':'
score = 0
qno = 0
print("Welcome to the Quiz!")

while qno < len(question_bag):
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
    elif input_answer.upper() == answer.upper():
        score += 1

    qno += 1

print(f'Your score is {score} / {len(question_bag)}')

