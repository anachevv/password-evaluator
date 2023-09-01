from re import findall


def password_evaluator(pwd):
    recommended_length = len(pwd) >= 12  # 12 or more characters in password
    alternating_caps = len([letter for letter in pwd if letter.isupper()]) >= 1  # 1 or more uppercase letters
    include_numbers = len([num for num in pwd if num.isdigit()]) >= 2  # 2 or more digits in password
    include_special_chars = len(findall(r"[^A-Za-z\d]", pwd)) >= 1  # 1 or more special symbols
    conditions = [recommended_length, alternating_caps, include_numbers, include_special_chars]

    if all(conditions):  # Checks that all conditions are True
        return []

    issues = []
    if not recommended_length:
        message = "Password must contain 12 or more characters."
        issues.append(message)
    if not alternating_caps:
        message = "Password must contain 1 or more uppercase letters."
        issues.append(message)
    if not include_numbers:
        message = "Password must contain 2 or more digits."
        issues.append(message)
    if not include_special_chars:
        message = "Password must contain 1 or more special symbols."
        issues.append(message)

    return issues


def password_advisor(pwd):
    if not password_evaluator(pwd):
        return "Password is strong!", ""

    issues = password_evaluator(pwd)
    new_line = '\n'
    password_condition = "Password is weak! It is highly recommended to strengthen your password."
    issues = f"{new_line.join(x for x in issues)}"

    return password_condition, issues