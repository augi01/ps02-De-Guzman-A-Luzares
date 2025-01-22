import copy

nested_list = [[1, 2], [3, 4]]
alias_nested = nested_list
alias_nested[0][1] = 99

deep_copied_list = copy.deepcopy(nested_list)
deep_copied_list[0][1] = 2 

print("Original nested list:", nested_list)
print("Aliased nested list:", alias_nested)
print("Deep copied list:", deep_copied_list)
