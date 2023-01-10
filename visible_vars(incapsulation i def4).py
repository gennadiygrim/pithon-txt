
def message(number):
    def print_message():
       return 'Число '+ str(number)
    return print_message()

print(message(4))
#print(print_message()) impossible error!!!

def message1(x):
    def print_message1(y):
       return x,y
    return print_message1

b=message1(5)
print(b)
print(b(5))
print(b(8))