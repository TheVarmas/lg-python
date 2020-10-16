# string is longer than 10 characters and starts with 'a' then print 'long sentence starting with a'
# string is longer than 10 characters and does not start with 'a' then print 'long sentence not starting with a'
# string is shorter than 10 characters and starts with 'a' then print 'short sentence starting with a'
# string is shorter than 10 characters and does not start with 'a' then print 'short sentence not starting with a'

# foo = ["sdfsfsf","goo"]
# a = "dfdfdf"

# if a in foo:
#   print(f'{a} is in the list')
# else:
#   print(f'{a} is not in the list')



str1 = "Apple"
alist = ['a', 'A']

print(str1)
if len(str1) >= 10:
  if str1[0] in alist:
    print("long sentence starting with a ")
  else:
    print("long sentence not starting with a")
else:
  if str1[0] in alist:
    print("short sentence starting with a")     
  else:
    print("short sentence not starting with a" )  

#=====================================================

str1 = str1.lower()
print(str1)

if len(str1) >= 10:
  if str1[0] == 'a':
    print("long sentence starting with a ")
  else:
    print("long sentence not starting with a")
else:
  if str1[0] == 'a':
    print("short sentence starting with a")     
  else:
    print("short sentence not starting with a" )  

#=====================================================

str1 = str1.upper()
print(str1)

if len(str1) >= 10:
  if str1[0] == 'a':
    print("long sentence starting with a ")
  else:
    print("long sentence not starting with a")
else:
  if str1[0] == 'a':
    print("short sentence starting with a")     
  else:
    print("short sentence not starting with a" )  
