print('{a} is in the list')# If the last character is 'r' and longer than 5 print: Long sentence ending with "r"
# If the last character is not 'r' print: Short sentence 

string = 'ebsfsdfsdfsdfsdfsr'
alist = ['r','R']
if string [-1] in alist :
  if len(string) > 5:
    print('long sentence ending with "r"')
else:
  print("short sentence")   

#============================================

if len(string) > 5:
  if string [-1] in alist:
    print('long sentence ending with "r"')

if string [-1] in alist:
  pass
else:
  print("short sentence")   

#============================================

if len(string) > 5:
  if string [-1] in alist:
    print('long sentence ending with "r"')

if string [-1] not in alist:
  print("short sentence")   

#============================================

if string [-1] in alist and len(string) > 5:
  print('long sentence ending with "r"')
elif string[-1] not in alist:
  print("short sentence")   
