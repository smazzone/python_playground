squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

#list comprehension - same result as above
squares = [value**2 for value in range(1, 11)]
print(squares)