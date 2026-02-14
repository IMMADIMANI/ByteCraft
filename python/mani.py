#  1 Use map() with a lambda to add 5 to every element of the following nested
#  list [[1, 2], [3, 4], [5, 6]]
#  nested_list = [[1, 2], [3, 4], [5, 6]]
#
#  result = list(map(lambda sublist: list(map(lambda x: x + 5, sublist)), nested_list))
#
#  print(result)
#
#  2 Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . Use
#  filter() to keep only the keys whose values are greater than 50.
#  d = {"apple": 100, "banana": 40, "cherry": 150}
#
#  filtered_dict = dict(filter(lambda item: item[1] > 50, d.items()))
#
#  print(filtered_dict)
#
#  3 Use functools.reduce() with a lambda to find the largest number from a given
#  list Dynamically.
# k = input()
# print(k.split())
# print(type(k))
#
# 4 What happens if the lambda passed to reduce() accepts only one parameter or
# three parameters? Explain the output or error.
# k = list(map(int, input().split()))
# m = -10**6
# for i in k:
#     if m<i:
#         m=1
# from functools import reduce
# print(reduce(lamda x,y: if x>y else y,k))
#
# print(m)
#
# 5 Use map() on a string to convert each character into its ASCII value
#  (using ord()). Print the result list.
#
# 6 Use filter() to remove all vowels from a string and print the final string.
#
# 7 Use reduce() to concatenate a list of characters into a single string.
# Example input: ['P', 'y', 't', 'h', 'o', 'n'].
#
# l = ['P','Y','T','H','O','N']
#
# st = reduce(lambda x,y: x+y, l)
# print(st)

# 8 Given a list of integers, use map() with id() to print the memory address
# of each element.
# Example: [10, 350, 10, 350, 20] — explain why some addresses repeat.

# l = [10,350,10,20,350]
# k = list(map(lambda x: id(x), l))
# print(k)

# 2 Given two lists:
# a = [1, 2, 3, 4] b = [10, 20, 30, 40]
# Use map() with a lambda to create a new list containing the sum of corresponding
# elements.
# What happens if the lists are of unequal length?

# a = [1,2,3,4]
# b = [10,20,30,40]
# k = list(map(lambda x,y:x+y,a,b))
# print(k)

# 3  Given a list:
# nums = [12, 15, 7, 18, 20, 21, 25]
# Use filter() and lambda to keep numbers that are divisible by 3 OR divisible by
# 5 but NOT divisible by both.
# Explain how the logical condition works.

# nums = [12,15,7,18,20,21,25]
# l = list(filter(lambda x: (x%3==0) ^ (x%5==0), nums))
# print(l)

# 4 Given a list:
# nums = [1, 2, 3, 4]
# Use reduce() with a lambda to compute the sum, but start with an initial value
# of 10.
# Explain how the initial value affects the reduction process.

# 5 Consider the code below:
# nums = [[1, 2], [3, 4], [5, 6]] result = list(map(lambda x: x.append(10), nums))
# print("Result:", result) print("Nums:", nums)
# Questions
# • What will be the output of result?
# • What will be the output of nums?
# • Why does map() behave this way with list.append()?
# • How can you modify the lambda so that nums is not changed?

nums = [[1,2],[3,4],[5,6]]
result = list(map(lambda x:x.append(10), nums))
print(result, nums, sep='/n')