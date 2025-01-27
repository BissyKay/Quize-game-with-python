from questions import questions
def run_quize():
    score = 0
    print("welcome to the quize game")
    print("answer the following questions from a to d \n")

    for i, q in enumerate(questions):
        print(f"Question {i + 1}): {q['question']}")

        for option in q["options"]:
            print(option)
        user_answer = input("Your answer is ").strip().upper()

        if user_answer == q['answer']:
            print("Correct! \n")
            score += 1
        else:
            print(f"Wrong! The correct anwer is {q['answer']}. \n")
    print(f"Your score is {score} out of {len(questions)}!")
    if score == len(questions):
        print("Excellent!")
    elif score >= len(questions):
        print("Good job! Keep going")
    else:
        print("Better Luck Next time")


if __name__ == "__main__":
    run_quize()