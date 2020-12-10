class Integer:

    def __init__(self, value: int):
        self.value = value

    @staticmethod
    def from_float(value):
        if not isinstance(value, float):
            return "value is not a float"
        return Integer(int(value))

    @staticmethod
    def from_roman(value):
        roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
                      'XC': 90, 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        while i < len(value):
            if i + 1 < len(value) and value[i:i + 2] in roman_nums:
                num += roman_nums[value[i:i + 2]]
                i += 2
            else:
                # print(i)
                num += roman_nums[value[i]]
                i += 1
        return Integer(num)
        # number = 0
        # previous_element = 'Z'
        # if isinstance(value, str):
        #     for each in value:
        #         #number += roman_nums[each]
        #         if previous_element + each in roman_nums:
        #
        #         previous_element = each
        #     return Integer(number)

    @staticmethod
    def from_string(value):
        if isinstance(value, str):
            for digit in value:
                if not 48 <= ord(digit) <= 57:
                    return "wrong type"
                return Integer(int(value))
        return "wrong type"

    def add(self, integer):
        if not isinstance(integer, Integer):
            return "number should be an Integer instance"
        return self.value + integer.value


first_num = Integer(10)
second_num = Integer.from_roman("IV")
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))
