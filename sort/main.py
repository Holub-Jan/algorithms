class Sort:
    def __init__(self):
        # To be added if needed
        pass

    def merge(self, lst):

        if len(lst) <= 1:
            return lst

        left, right = self.divide_lst(lst)
        result = []
        left = self.merge(left)
        right = self.merge(right)
        pos_l = 0
        pos_r = 0

        while pos_l != len(left) and pos_r != len(right):
            if left[pos_l] > right[pos_r]:
                result.append(right[pos_r])
                pos_r += 1
            else:
                result.append(left[pos_l])
                pos_l += 1

        if pos_l == len(left):
            result += right[pos_r:]
        else:
            result += left[pos_l:]

        return result

    def quick(self, lst):

        if len(lst) <= 1:
            return lst

        comp = lst[0]
        # less = [value for value in lst[1:] if value < comp]
        less = list()

        # more = [value for value in lst[1:] if value >= comp]
        more = list()

        for value in lst[1:]:
            if value < comp:
                less.append(value)
            else:
                more.append(value)

        return self.quick(less) + [comp] + self.quick(more)

    @staticmethod
    def divide_lst(to_divide):
        first_half = to_divide[:len(to_divide) // 2]
        sec_half = to_divide[len(to_divide) // 2:]

        return first_half, sec_half


tests = [[3, 6, 2, 9, 12, 8, 0, 5, 1, 15, 20],
         [12, 11, 13, 5, 6, 7],
         [21, 1, 22, 23, 3, 4, 7, 6, 5, 25],
         [],
         [1],
         [5, 5, 5, 5, 5, 5]]

sort = Sort()

for data in tests:
    print('Original data: ', data)
    print('Sorted data: ', sort.quick(data), end='\n\n')
