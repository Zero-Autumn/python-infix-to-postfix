
infix = input('Exp with spaces:   ').split()
postfix = ''
operators = ['^','*','/','+','-']
parenthesis = ['(',')']
priorityDict = {'^':5,'*':4,'/':3,'+':2,'-':1}

class Stack:
    def __init__(self,si):
        self.size = si
        self.top = -1
        self.stack = ['']*self.size
    
    def push(self,data):
        if self.top >= self.size-1:
            raise Exception('Stack Full')
        else:
            self.top += 1
            self.stack[self.top] = data
            # print('one push',st.stack)

    def pop(self):
        if self.top <0:
            raise Exception('Stack Empty')
        else:
            self.stack[self.top] = ''
            self.top -= 1
    
    
    def empty(self,one):
        isEmpty = False
        if self.top == -1 or st.stack[0] == '(':
            isEmpty = True
        
        return isEmpty
        

st = Stack(len(infix))


for one in infix:
    if one.isalpha():
        print(1)
        postfix += one
        print('1 Done')
        
    
    elif one == '(':
        print(2)
        st.push(one)
        
    
    elif one in operators and (st.empty(one) == True or priorityDict[st.stack[st.top]] < priorityDict[one]):
        print(3)
        st.push(one)
        

    elif one in operators and priorityDict[st.stack[st.top]] > priorityDict[one]:
        print(4)
        while st.top != -1:
            if st.stack[st.top] >= one:
                postfix += st.stack[st.top]
                st.pop()
            else:
                break
        st.push(one)

    elif one == ')':
        print(5)
        while st.stack[st.top] != '(':
            postfix += st.stack[st.top]
            st.pop()
        if st.stack[st.top] == '(':
            st.pop()
print(6)
if st.top != -1:
    print(f"top {st.top}")
    print(7)
    while st.top != -1:
        # print('whats popping')
        postfix += st.stack[st.top]
        st.pop()
    print('7 Done')
print(8)
print(postfix)
print(st.stack)