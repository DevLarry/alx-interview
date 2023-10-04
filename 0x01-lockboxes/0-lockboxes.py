#!/usr/bin/python3
"""This is an interview challenge"""

def canUnlockAll(boxes=[]):
    """canUnlockAll"""
    keys = {0}
    opened = list(map(lambda a: False, boxes))
    newKey = True
    while newKey:
        newKey = False
        for index in range(len(boxes)):
            box = boxes[index]
            opens = False
            if index in keys:
                opens = True
            opened[index] = opens
            if opens:
                for key in box:
                    if key not in keys:
                        newKey = True
                        keys.add(key)
    return all(opened)
