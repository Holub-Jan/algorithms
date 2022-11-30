class Search:
    def __init__(self):
        # To be removed if not needed
        pass

    def binary(self, lst, to_find):
        if not lst:
            return 'not found'

        low = 0
        high = len(lst) - 1
        mid = (low + high) // 2

        while to_find not in [lst[mid], lst[low], lst[high]]:
            if to_find > mid:
                low = mid + 1
            else:
                high = mid - 1

            mid = lst[(low + high) // 2]

        if mid == to_find:
            return mid
        elif low == to_find:
            return low
        elif high == to_find:
            return high

        return 'not found'


tests = [[[3, 6, 2, 9, 12, 8, 0, 5, 1, 15, 20], 5],
         [[12, 11, 13, 5, 6, 7], 12],
         [[21, 1, 22, 23, 3, 4, 7, 6, 5, 25], 25],
         [[], 1],
         [[1], 1],
         [[5, 5, 5, 5, 5, 5], 5]]

search = Search()

for data in tests:
    print('Original data: ', data[0], 'Searching for: ', data[1])
    print('Position of {0} is {1}'.format(data[1], search.binary(data[0], data[1])), end='\n\n')