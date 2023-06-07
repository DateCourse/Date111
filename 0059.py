stack = []
sentence = input()
for i in range(len(sentence)):
    if sentence[i] == '+' or sentence[i] == '-':
        a = stack.pop()
        b = stack.pop()
        c = '(' + b + sentence[i] + a + ')'
        stack.append(c)
    else:
        stack.append(sentence[i])
print(stack[-1])
