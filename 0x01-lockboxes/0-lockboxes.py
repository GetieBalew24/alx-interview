#!/usr/bin/python3
""" Display  locked boxes in front of you"""


def canUnlockAll(boxes):
    """Define unlock array of boxes"""
    unlocked = set([0]
    key = set(boxes[0]
    while True:
        next_box = None
        for i in range(len(boxes)):
            if i not in unlocked and set(boxes[i]).intersection(key):
                next_box = i
                break
        if next_box is None:
            break
        else:
            unlocked.add(next_box)
            key.update(boxes[next_box])

    if len(unlocked) == len(boxes)
        return true
    else:
    return false
