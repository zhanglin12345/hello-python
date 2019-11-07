def fib(n):
    a = 0
    b = 1
    l = list()
    while a <= n:
        l.append(a)
        a, b = b, a + b
    return l

class TestClass():
    a=[]
    b=[]
    def TestMethod(self):
        self.a = ["1","2","3"]
        self.b = ["4","5","6"]
        return zip(self.a,self.b)
        
    def __str__(self):
        list = self.TestMethod()
        result = ""
        for l in list:
            result += l + ","
        return result
    
t = TestClass()
print(t)

# print(fib(1).__eq__([0, 1, 1]))
# print(fib(2).__eq__([0, 1, 1, 2]))
# print(fib(3).__eq__([0, 1, 1, 2, 3]))
# print(fib(4).__eq__([0, 1, 1, 2, 3]))
# print(fib(5).__eq__([0, 1, 1, 2, 3, 5]))