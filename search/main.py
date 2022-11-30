class Search:
    def __init__(self):
        # To be removed if not needed
        pass

    @staticmethod
    def binary(lst, to_find):
        if not lst:
            return 'not found'

        low = 0
        high = len(lst) - 1
        mid = (low + high) // 2

        while to_find not in [lst[mid], lst[low], lst[high]]:
            if to_find > lst[mid]:
                low = mid
            else:
                high = mid

            mid = (low + high) // 2

        if lst[mid] == to_find:
            return mid
        elif lst[low] == to_find:
            return low
        elif lst[high] == to_find:
            return high

        return 'not found'


tests = [[[0, 1, 2, 3, 5, 6, 8, 9, 12, 15, 20], 5],
         [[5, 6, 7, 11, 12, 13], 5],
         [[1, 3, 4, 5, 6, 7, 21, 22, 23, 25], 25],
         [[], 1],
         [[1], 1],
         [[5, 5, 5, 5, 5, 5], 5]]

search = Search()

for data in tests:
    print('Original data: ', data[0], 'Searching for: ', data[1])
    print('Position of {0} is {1}'.format(data[1], search.binary(data[0], data[1])), end='\n\n')
