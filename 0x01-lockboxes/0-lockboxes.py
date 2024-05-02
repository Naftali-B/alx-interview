#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    progress = set()
    checked = [0] # Start from 0

    while checked:
        current_box = queue.pop(0)
        progress.add(current_box)

        for key in boxes[current_box]:
            if key not in progress and key < n:
                checked.append(key)

    return len(progress) == n

# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False

