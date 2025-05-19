cube_dict = {}
# normal way
for x in range(1, 11, 2):
    cube_dict[x] = x ** 3
print("Dictionary of cubes of odd integers from 1 - 10 :- ")
for x, y in cube_dict.items():
    print(f"{x} = {y}")

# using comprehension
cube_dict = {x: x ** 3 for x in range(1, 11) if x % 2 != 0}
print("Dictionary of cubes of odd integers from 1 - 10 using comprehension:- ")
print(cube_dict)