def getDigit(array):
    for i in range(5):
        array[i] = "".join(array[i])
    if array[0] == "***" and array[1] == "* *" and array[2] == "* *" and array[3] == "* *" and array[4] == "***":
        return "0"
    if array[0] == "  *" and array[1] == "  *" and array[2] == "  *" and array[3] == "  *" and array[4] == "  *":
        return "1"
    if array[0] == "***" and array[1] == "  *" and array[2] == "***" and array[3] == "*  " and array[4] == "***":
        return "2"
    if array[0] == "***" and array[1] == "  *" and array[2] == "***" and array[3] == "  *" and array[4] == "***":
        return "3"
    if array[0] == "* *" and array[1] == "* *" and array[2] == "***" and array[3] == "  *" and array[4] == "  *":
        return "4"
    if array[0] == "***" and array[1] == "*  " and array[2] == "***" and array[3] == "  *" and array[4] == "***":
        return "5"
    if array[0] == "***" and array[1] == "*  " and array[2] == "***" and array[3] == "* *" and array[4] == "***":
        return "6"
    if array[0] == "***" and array[1] == "  *" and array[2] == "  *" and array[3] == "  *" and array[4] == "  *":
        return "7"
    if array[0] == "***" and array[1] == "* *" and array[2] == "***" and array[3] == "* *" and array[4] == "***":
        return "8"
    if array[0] == "***" and array[1] == "* *" and array[2] == "***" and array[3] == "  *" and array[4] == "***":
        return "9"
    return "x"

inp = []

for i in range(5):
    inp.append([char for char in input()])

numbers = []
i = 0
for digit in range(len(inp[0]) // 4 + 1):
    number = []
    for row in range(5):
        number.append(inp[row][i:i+3])
    numbers.append(number)
    i += 4

result = ""
for number in numbers:
    result += getDigit(number)

try:
    result = int(result)
    if result % 6 == 0:
        print("BEER!!")
    else:
        print("BOOM!!")
except Exception as e:
    print("BOOM!!")


