def mult_tables():
  num = int(input("Enter a number to get the multiplication table: "))
  upto = int(input("Upto? ")) + 1

  for i in range(1, upto):
    print(f"{num} X {i} = {i*num}")