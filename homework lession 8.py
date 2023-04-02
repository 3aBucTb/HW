def get_common_elements(set1, set2):
    return set1.intersection(set2)


def get_unique_elements(set1, set2):
    return set1.symmetric_difference(set2)


fruits_list = ['apple', 'melon', 'peach']
upper_string_list = list(map(str.upper, fruits_list))
print(upper_string_list)


number_list = [1, 'two', 2, 'three', 3]
filtered_list = list(filter(lambda x: type(x) == int, number_list))
print(filtered_list)