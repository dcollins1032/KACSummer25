'''
Hello World
Dave Collins
'''

def main():
    print("Hello World")
    print("My name is Python 3!")
    name = input("What is your name???")
    if name == "Alex":
        print("Wow...  That's terrible")
    elif name == "Leland":
        print("I guess that's ok...")
    elif name == "Ethan":
        print("Oof, that's unfortunate")
    else:
        print("Hello", name ,". That's a good name!")
    return

main()