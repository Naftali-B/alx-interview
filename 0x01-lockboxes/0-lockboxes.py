#!/usr/bin/python3

"""
    You have n number of locked boxes in front of you
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes
    
    method that determines if all the boxes can be opened
"""

def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    progress = set()
    checked = [0] # Start from 0

    while checked:
        current_box = checked.pop(0) # Pop the first box
        progress.add(current_box) # Mark the current box

        # Check each key in the current box
        for key in boxes[current_box]:
            if key not in progress and key < n:
                checked.append(key)

    # If all checked, return True, otherwise False
    return len(progress) == n
