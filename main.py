char = input('>>enter a char:')
num = int(input('>>enter a possitive number (>5)'

for i in range(1,5):
  for col in range(1,8):
    if row==4 or row+col==5 or col-row==3:
       print("*", end="")
   else:
       print(end=" ")
print()


char = input('>>enter a char:')
num = int(input('>>enter a positive number (>5):'))

for i in range(1, num + 1):
  text = ''
  for j in range(i):
    text += char
    print(text)
  