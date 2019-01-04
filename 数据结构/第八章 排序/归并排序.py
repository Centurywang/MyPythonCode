# Recursively implementation of Merge Sort
def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result


def merge_sort(L):
    if len(L) <= 1:
        # When D&C to 1 element, just return it
        return L
    mid = len(L) // 2
    left = L[:mid]
    right = L[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    # conquer sub-problem recursively
    return merge(left, right)
    # return the answer of sub-problem


if __name__ == "__main__":
    test = [25,84,21,47,15,27,68,35,20]
    print("original:", test)
    print("Sorted:", merge_sort(test))