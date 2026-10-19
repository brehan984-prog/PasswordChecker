import re

def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add a number.")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add a special character.")

    levels = {5: "Strong", 4: "Good", 3: "Medium"}
    return levels.get(score, "Weak"), feedback

if __name__ == "__main__":
    pwd = input("Enter a password: ")
    level, tips = check_strength(pwd)
    print(f"Strength: {level}")
    for tip in tips:
        print(" -", tip)