"""
My little Queue
"""
from typing import Any
from collections import deque

queue = deque([])


def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    print(elem)
    queue.append(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    if queue:
        a = queue.popleft()
        return a
    else:
        return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    print(ind)
    if ind == 0:
        return queue[0]
    elif ind > len(queue):
        return None
    else:
        return queue[ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    queue.clear()
    return None


if __name__ == '__main__':
    print(queue)
    items = [i for i in range(10)]
    print(items)
    for i in items:
        enqueue(i)
    print(queue)