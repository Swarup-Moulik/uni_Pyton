question = ('Hi, How are you ?',
            'Where are you from?',
            'How is your day going?')
answer = ('Hello, I am good. Thank you ! ',
          'I am from India.',
          'My day is going super.')
qna = zip(question, answer)
print("Question answer series :- ")
for question, answer in qna:
    print(f"Q: {question}")
    print(f"A: {answer}")