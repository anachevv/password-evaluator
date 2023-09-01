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
        return "<h1>Password is strong!</h1>"

    issues = password_evaluator(pwd)
    new_line = '\n'

    return f"<h1>Password is weak! It is highly recommended to strengthen your password.</h1>\n<h2>Issues:</h2>\n" \
           f"<h3>{new_line.join(str(issues.index(x) + 1) + '.' + x for x in issues)}</h3>".replace("\n", "<br>")
