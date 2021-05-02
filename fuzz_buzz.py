
print('Enter the number')
integer_list = list(map(int, input().split()))

# print(integer_list)
# print(type(integer_list))

for i in integer_list:
    for j in range( 1,i+1):
        if j % 3==0 and j % 5 == 0:
            print('buzzfuzz')
        elif j % 3 == 0:
            print('buzz')
        elif j % 5 ==0:
            print('fuzz')
        else:
            print(j)