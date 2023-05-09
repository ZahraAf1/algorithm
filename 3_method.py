def my_func(char, name):
    
    c = name.find(char)
    return c

char = input("enter character : ")
name = input("enter name : ")

c = my_func(char, name)

print(c)