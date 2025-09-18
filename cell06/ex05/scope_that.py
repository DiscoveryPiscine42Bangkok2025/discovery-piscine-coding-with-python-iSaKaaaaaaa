def add_one(x):
    x += 1
    print(f"Inside add_one: {x}")


num = int(input())
print(f"Before add_one: {num}")


add_one(num)


print(f"After add_one: {num}")