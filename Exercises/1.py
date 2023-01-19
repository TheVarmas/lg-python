# Write a program which will find all such numbers which are divisible by 7 but 
# are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained
# should be printed in a comma-separated sequence on a single line.

list_of_nummies = []

for i in range(2000,3201):
    if i%7 == 0:
        if i%5 != 0:
           list_of_nummies.append(str(i)) 

#print(list_of_nummies)       

print(", ".join(list_of_nummies))