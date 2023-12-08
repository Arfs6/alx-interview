#!/usr/bin/python3
"""
Question: You have n number of locked boxes in front of you.
Each box is numbered sequentially
from 0 to n - 1 and each box may contain keys to the other boxes.
"""

from collections import deque


def canUnlockAll(boxes):
    """Checks if you can unlock all the boxes.
    parameters:
    - boxes: List of list containing keys to ther boxes.
    Returns:
    - True: You can open all boxes.
    - False: You cannot open all boxes.
    """
    if not boxes:
        return False
    elif not boxes[0] and len(boxes) == 1:  # All boxes opened!
        return True
    knownKeys = set()
    openedBoxes = [False for i in boxes]
    firstBox = openBox(0, knownKeys, openedBoxes, boxes)
    stack = deque()
    stack.append(firstBox)
    while True:
        if not stack:
            break
        try:
            key = next(stack[-1])
        except StopIteration:
            stack.pop()
        else:
            box = openBox(key, knownKeys, openedBoxes, boxes)
            stack.append(box)
    return all(openedBoxes)


def openBox(num, knownKeys, openedBoxes, boxes):
    """Open a box and use the keys in it to open the boxes the keys can open.
    Parameters:
    - num: The number of box to open.
    - knownKeys: A set containing all the keys we have.
    - openedBoxes: A list of all opened boxes represented by bools.
    - boxes: All boxes.
    """
    if num + 1 > len(boxes):
        return
    elif openedBoxes[num]:
        return
    openedBoxes[num] = True
    keys = boxes[num]
    knownKeys.update(keys)
    for key in keys:
        yield key
