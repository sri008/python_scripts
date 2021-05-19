# Reverse the sequesnce of number
# 12345
# 54321
# 34512
number=[]
#input_number = map(int, input())
number=input()
count = len(number)

rev_number = []
while count >0:
    # print(number[count-1])
    rev_number.append(number[count-1])
    count = count -1

rev_number1 = []
print(''.join(rev_number))
for i in range( 2,-1,-1):
    rev_number1.append(rev_number[i])

for i in range(4,2, -1):
    rev_number1.append(rev_number[i])

print(''.join(rev_number1))