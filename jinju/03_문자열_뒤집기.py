input_str = input()
result = min(len(input_str.replace("0", " ").split()), len(input_str.replace("1", " ").split()))

print(result)