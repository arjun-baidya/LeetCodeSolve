
def isValid(s):
    if len(s) % 2 != 0:
        return False
    stack = []
    for i in s:
        print(i)
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
            # print('stack',stack)
        elif i == ')' and stack[-1] == '(':
            stack.pop()
            print('stack',stack)
        elif i == '}' and stack[-1] == '{':
            stack.pop()
        elif i == ']' and stack[-1] == '[':
            stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False

a = isValid('()''[]')
print(a)


def isValid( s):
    if len(s) % 2 != 0:
        return False
    dict = {'(' : ')', '[' : ']', '{' : '}'}
    stack = []
    for i in s:
        if i in dict.keys():
            stack.append(i)
        else:
            if stack == []:
                return False
            a = stack.pop()
            if i!= dict[a]:
                return False
    return stack == []
a = isValid('()''}')
print(a)