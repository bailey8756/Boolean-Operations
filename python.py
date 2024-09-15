#Convert binary to integer
def main():
    global binaryString
    binaryString = input("Please input the binary number you would like to convert to decimal: ")

nums = ["0","1"]

def check(nums, binaryString):
        results = []
        for i in binaryString:
            if i in nums:
                results.append("True")
            else:
                results.append("False")
        if "False" in results:
            print("You entered an invalid binary number. Please try again.")
            main()

def binToDec():
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

main()
check(nums, binaryString)
binToDec()