def run_quiz(questions):
    score = 0
    for question in questions:
        print("\n" + question["question"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        if answer == question["answer"]:
            print(" Correct!")
            score += 1
        else:
            print(f" Wrong! The correct answer was {question['answer']}")
    print(f"\nYour final score is {score} out of {len(questions)}")

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. Java", "C. PHP", "D. All of the above"],
        "answer": "D"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A. 10", "B. 12", "C. 13", "D. 14"],
        "answer": "B"
    }
]

run_quiz(questions)
