n = input()
length_half = len(n)//2

first_number = sum(map(int,list(n[:length_half])))
second_number = sum(map(int,list(n[length_half:])))

if first_number == second_number:
  print("LUCKY")
else:
  print("READY")
