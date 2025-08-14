class NonIntArgumentException(Exception):
    pass

def handleNonIntArguments(func):
    def wrapper(*args):
        for item in args:
            if type(item) is not int:
                raise NonIntArgumentException()
        return func(*args)
    return wrapper
@handleNonIntArguments
def sum(a,b,c):
    return a+b+c
try :
    result=sum(1,2,3)
    print (result)
    print('This should not print out')
    result = sum(1, '2', 3)
    print('This should not praint out')
except NonIntArgumentException: print('Hooray')
