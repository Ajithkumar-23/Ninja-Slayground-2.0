def getSecondOrderElements(n: int, a: [int]) -> [int]:
    if n < 2:
        return []
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')
    for num in a:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return [second_largest, second_smallest]
