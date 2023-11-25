# questions.py

questions = [
    {
        'question': 'What is the correct order of execution for the following code?',
        'code': [
            'def foo():',
            '    print("Hello")',
            'foo()',
        ],
        'correct_order': [0, 1, 2]
    },
    {
        'question': 'What will be the output of the following code?',
        'code': [
            'x = 5',
            'y = 3',
            'print(x + y)',
        ],
        'correct_order': [0, 1, 2]
    },
    {
        'question': 'How do you comment multiple lines in Python?',
        'code': [
            '# This is a comment',
            '# This is another comment',
            '# And one more comment',
        ],
        'correct_order': [0, 1, 2]
    },
    # Add more questions here
    {
        'question': 'What does the "self" keyword refer to in Python?',
        'code': [
            'class MyClass:',
            '    def __init__(self, x):',
            '        self.x = x',
        ],
        'correct_order': [0, 1, 2]
    },
    {
        'question': 'How do you open a file in Python?',
        'code': [
            'with open("example.txt", "r") as file:',
            '    content = file.read()',
        ],
        'correct_order': [0, 1]
    },
    {
        'question': 'What is the purpose of the "__init__" method in a Python class?',
        'code': [
            'class MyClass:',
            '    def __init__(self):',
            '        # Constructor code here',
        ],
        'correct_order': [0, 1, 2]
    },
    {
        'question': 'How do you check if a key is in a dictionary?',
        'code': [
            'my_dict = {"key": "value"}',
            'if "key" in my_dict:',
            '    print("Key found!")',
        ],
        'correct_order': [0, 1, 2]
    },
    {
        'question': 'What is the purpose of the "break" statement in a loop?',
        'code': [
            'for i in range(5):',
            '    if i == 3:',
            '        break',
        ],
        'correct_order': [0, 1, 2]
    },
    {
        'question': 'How do you define a function in Python?',
        'code': [
            'def my_function():',
            '    # Function code here',
        ],
        'correct_order': [0, 1]
    },
    {
        'question': 'What is the output of the following code?',
        'code': [
            'nums = [1, 2, 3, 4, 5]',
            'squared_nums = [x**2 for x in nums]',
            'print(squared_nums)',
        ],
        'correct_order': [0, 1, 2]
    },
]
