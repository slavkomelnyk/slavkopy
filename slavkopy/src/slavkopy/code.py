def hello(name):
    a = "hello " + name
    return a

def test():
    a = int(input("1 + 1 = "))
    if a == 2 :
        a = "1 + 1 = %s " % a
        return a
    return "?"