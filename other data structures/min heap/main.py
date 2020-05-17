class Pair:
    def __init__(self, x, y):
        self.first = x
        self.second = y


class stack:
    def __init__(self):
        self.s=[]

    def push(self,x):
        #CODE HERE
        if len(self.s) == 0:
            self.s.append(Pair(x, x))
            return
        minVal = self.getMin()
        if minVal > x:
            self.s.append(Pair(x, x))
        else:
            self.s.append(Pair(x, minVal))

    def pop(self):
        #CODE HERE
        if len(self.s) == 0:
            return -1
        return self.s.pop().first
        

    def getMin(self):
        #CODE HERE
        if len(self.s) == 0:
            return -1
        return self.s[-1].second
    
if __name__ == '__main__':
    s = stack()
    s.push(3)
    print(s.getMin())
    print(s.pop())
    print(s.pop())
    print(s.getMin())
    s.push(4)
    print(s.getMin())

