import random

class Quiz:
    def __init__(self, max_diff, operator, number_of_items):
        self.max_diff = max_diff
        self.operator = operator
        self.number_of_items = number_of_items
        self.score = 0
        self.correct = 0
        self.wrong = 0

    def get_question(self):
        a = any.randint(1, 100)
        b = any.randint(1, 100)

        if self.operator == "Addition":
            question = a + b
        elif self.operator == "Subtraction":
            question = a - b
        elif self.operator == "Multiplication":
            question = a * b

        choices = [question]
        for i in range(self.number_of_items - 1):
            while True:
                temp = any.randint(1, 100)
                if abs(temp - question) <= self.max_diff:
                    break
            choices.append(temp)

        any.shuffle(choices)
        return a, b, question, choices

    def check_answer(self, user_answer, a, b, correct_answer):
        if self.operator == "Addition":
            correct_answer = a + b
        elif self.operator == "Subtraction":
            correct_answer = a - b
        elif self.operator == "Multiplication":
            correct_answer = a * b

        if user_answer == correct_answer:
            self.score += 1
            self.correct += 1
            return True
        else:
            self.wrong += 1
            return False

def print_results(quiz):
    print("\n\nScore: ", quiz.score)
    print("Correct: ", quiz.correct)
    print("Wrong: ", quiz.wrong)

def quiz_settings ():
    max_diff = int(input("Max difference of choices from the correct answer: "))
    operator = input("Operator: ").strip().capitalize()
    number_of_items = int(input("Number of items: "))
    return max_diff, operator, number_of_items

def start_quiz ():
    max_diff, operator, number_of_items = quiz_settings()
    quiz = Quiz(max_diff, operator, number_of_items)

    for i in range(5):
        a, b, correct_answer, choices = quiz.get_question()
        print("\nQuestion: ", i + 1)
        print("Operand 1: ", a)
        print("Operand 2: ", b)
        for j in range(number_of_items):
            print(j + 1, ". ", choices[j])
        user_answer = int(input("Your answer: "))
        result = quiz.check_answer(user_answer, a, b, correct_answer)
        if result:
            print("Correct!")
        else:
            print("Wrong! The correct answer is ", correct_answer)

    print_results(quiz)

    







