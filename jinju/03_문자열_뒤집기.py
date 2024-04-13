input_str = input()
# "010011" -> " 1  11" -> ["1", "11"]
# "0 00  " -> ["0", "00"]

result = min(len(input_str.replace("0", " ").split()), len(input_str.replace("1", " ").split()))

print(result)