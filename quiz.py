score = 0

print("Welcome to the Python Quiz!")
print()

answer = input("1. What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("2. What does RAM stand for? ").lower()

if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("3. What does HTML stand for? ").lower()

if answer == "hypertext markup language":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("4. What does CSS stand for? ").lower()

if answer == "cascading style sheets":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("5. Which language is commonly used for AI and Data Science? ").lower()

if answer == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nQuiz Finished!")
print(f"Your score: {score}/5")

percentage = (score / 5) * 100
print(f"Percentage: {percentage}%")