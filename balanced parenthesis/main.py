

def isBalanced(s):
    stack = []
    for x in s:
        if x == '(':
            stack.append(x)
        elif x == '[':
            stack.append(x)
        elif x == '{':
            stack.append(x)
        elif x == ')':
            if len(stack) == 0:
                return False
            if stack.pop() != '(':
                return False
        elif x == ']':
            if len(stack) == 0:
                return False
            if stack.pop() != '[':
                return False
        elif x == '}':
            if len(stack) == 0:
                return False
            if stack.pop() != '{':
                return False
    if len(stack) == 0:
        return True
    else:
        return False
        


def main():
    t = int(input())
    for i in range(0, t):
        s = input()
        sol = isBalanced(s)
        if sol == True:
            print('balanced')
        else:
            print('not balanced')

main()