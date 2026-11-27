from typing import List


def shuffleArray(arr: List[int], n: int) -> List[int]:
    res = []

    for i in range(n):
        res.append(arr[i])
        res.append(arr[i + n])

    return res