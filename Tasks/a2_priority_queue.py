"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any
from collections import deque

priority_queue = {"high_priority": deque([]), "medium_priority": deque([]), "low_priority": deque([])}


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    if priority == 0:
        priority_queue["high_priority"].appendleft(elem)
    elif priority == 5:
        priority_queue["medium_priority"].appendleft(elem)
    elif priority == 10:
        priority_queue["low_priority"].appendleft(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    if priority_queue["high_priority"]:
        a = priority_queue["high_priority"].pop()
        return a
    elif priority_queue["medium_priority"]:
        a = priority_queue["medium_priority"].pop()
        return a
    elif priority_queue["low_priority"]:
        a = priority_queue["low_priority"].pop()
        return a
    else:
        return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if priority == 0 and ind == 0:
        return priority_queue["high_priority"][-1]
    elif ind > len(priority_queue["high_priority"]):
        return None
    else:
        return priority_queue["high_priority"][ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    priority_queue["high_priority"].clear()
    priority_queue["medium_priority"].clear()
    priority_queue["low_priority"].clear()
    return None


if __name__ == '__main__':
    enqueue(1)
    enqueue(2)
    enqueue(3)
    enqueue(1, 5)
    enqueue(2, 5)
    enqueue(3, 5)
    print(priority_queue)
    clear()
    print(priority_queue)