"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any
from collections import deque

queue = deque([])


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    if priority == 0:
        queue.appendleft(elem)
    elif priority == 5:
        queue.append(elem)
    elif priority == 10:
        queue.append(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    if queue:
        a = queue.popleft()
        return a
    else:
        return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    return None


if __name__ == '__main__':
    pass
