# Reverse the string :
# enter the string
# tumhe mujhe pagalpan hai
# iahna plaga pehjumeh mut

actual_str1 = []
reverse_str1=[]
print("enter the string")
actual_str1=input()

# for i in range(0,len(actual_str1)):
#     if actual_str1[i].isalpha():
#         reverse_str1.append(actual_str1[])

count = len(actual_str1)
i = 0
while count >= 0 and i < len(actual_str1):
    #aif actual_str1[i].isalpha() and actual_str1[count-1].isspace() :
    if actual_str1[i].isalpha() and actual_str1[count-1].isspace() == False:
        # print(actual_str1[count-1])
        reverse_str1.append(actual_str1[count - 1])
        count = count - 1
        i = i + 1
    elif actual_str1[i].isalpha() and actual_str1[count-1].isspace() :
        # reverse_str1.append(actual_str1[count - 2])
        count = count - 1
        i = i
    elif actual_str1[i].isalpha() == False:
        reverse_str1.append(" ")
        i = i + 1

    # count = count - 1
    # i = i + 1

# for element in actual_str1:
#     if element.isalpha():
#

print(''.join(reverse_str1))