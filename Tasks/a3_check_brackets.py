import re


def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    a = "".join([i for i in brackets_row if i == "(" or i == ")"])
    if a == "":
        return True
    for i in range(len(a)):
        if not a:
            return True
        a = re.sub(r"\(\)", "", a)
    return False
