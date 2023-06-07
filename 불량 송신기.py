num = input()
str1Num,str2Num,str3Num = num.split(' ')
str1Num = eval(str1Num)
str2Num = eval(str2Num)
str3Num = eval(str3Num)

str1 = input()
str2 = input()
str3 = input()

stack=[]

for c in str3:
    if not stack or c != stack[-1]: #stack이 비어있거나 현재 문자와 스택의 마지막 문자가 다르면 추가한다.
        stack.append(c)

stack = ''.join(x for x in stack)

if str1 in stack:
    print("YES")
else:
    print("NO")

if str2 in stack:
    print("YES")
else:
    print("NO")