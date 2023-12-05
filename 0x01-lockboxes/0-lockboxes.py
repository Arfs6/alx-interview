#!/usr/bin/python3
"""
Question: You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""

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
    keys = set(boxes[0])
    keys.add(0)  # First box is already opened
    for num, box in enumerate(boxes):
        if num not in keys:
            return False
        keys.update(box)

    return True
