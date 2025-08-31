rows=int(input("enter number of rows: "))
for i in range(rows):
  for j in range(i+1):
   print("*",end="")
  print("\n")

#rows = int(input("Enter number of rows: "))
#cols = int(input("Enter number of columns: "))

#for j in range(1, cols + 1):     # increasing stars in columns
    #for i in range(rows):        # printing for each row
        #print("*" * j)           # print j stars
cols = int(input("Enter number of columns: "))

for row in range(1, cols + 1):        # row loop
    for col in range(1, cols + 1):    # column loop
        if row <= col:
            print("*", end="")
        else:
            print(" ", end="")
        print(" ", end="")  # space between columns
    print()
