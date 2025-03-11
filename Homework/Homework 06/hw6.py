from functools import reduce
check_even_odd = lambda x: "even" if x % 2 == 0 else "odd"
print(check_even_odd(5))

sum_list = lambda lst: sum(lst)
print(sum_list([1, 2, 3, 4]))

names = ["alice", "bob", "kobe"]
sorted_names = sorted(names, key=lambda name: len(name))
print(sorted_names)

numbers = [1, 2, 3, 4, 5]
filtered_numbers = list(filter(lambda x: x > 2, numbers))
print(filtered_numbers)

mapped_numbers = list(map(lambda x: x ** 2, numbers))
print(mapped_numbers)

product = reduce(lambda x, y: x * y, numbers)
print(product)

for index, value in enumerate(numbers):
    print(f"Index: {index}, Value: {value}")

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
zipped_list = list(zipped)
print(zipped_list)
