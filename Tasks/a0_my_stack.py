"""
My little Stack
"""
from typing import Any


stack = []


def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    stack.append(elem)
    print(elem)
    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """
    if stack:
        a = stack.pop(-1)
        return a
    else:
        return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    print(ind)
    if ind == 0:
        return stack[-1]
    elif ind > len(stack):
        return None
    else:
        return stack[ind]


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    stack.clear()
    return None


if __name__ == '__main__':
    push(7)
    push(3)
    push(5)

    print(stack)
    print(peek(-1))
    print(stack)
    clear()
    print(stack)
