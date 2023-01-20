#Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320

nummies = input("Enter a  comma seperated sequence of numbers: ")
list_of_nummies = nummies.split(",")

for i in list_of_nummies:
    facty = 1

    for j in range(2,int(i)+1):
        facty=facty*j

    print(facty)
