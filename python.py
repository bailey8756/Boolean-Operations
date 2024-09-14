#Convert binary to integer
binaryString = input("Please enter your binary number: ")
size = len(binaryString)

container = []

for i in range(size):
    if binaryString[i] == "1":
        container.append((size - i)-1)
    else:
        continue

value = 0

for i in container:
    value = value + (2 ** i)

print(f"Your decimal value is {value}.")
