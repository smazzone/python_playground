with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.strip())


with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    #print(line.strip())
    sum = float(line)
    sum += sum
print(sum)


