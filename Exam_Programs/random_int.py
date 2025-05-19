import random

random_list = [random.randint(1, 100) for _ in range(10)]
print("Random 10 integer :- ", *random_list)
odd = list(filter(lambda n: n % 2 != 0, random_list))
even = list(filter(lambda n: n % 2 == 0, random_list))
print("Odd values from it :- ", *odd)
print("Even values from it :- ", *even)


