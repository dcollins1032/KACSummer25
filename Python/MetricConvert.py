'''
Metric Converter
Dave Collins
'''


def main():
    print("Hello, what can I help you with?")
    print("================================")
    print("               Menu             ")
    print("1. Convert Inches to Centimeters")
    print("2. Convert Feet  to Meters      ")
    print("3. Hours to Minutes             ")
    choice = int(input())

    if choice == 1:
        inches_to_cm()
    elif choice == 2:
        feet_to_meters()
    elif choice == 3():
        hours_to_minutes()


def inches_to_cm():
    inches = float(input("How many inches?"))
    centimeter = inches * 2.54
    print("You measured something that is",centimeter,"Centimeters Long!")

def feet_to_meters():
    feet = float(input("How many feet?"))
    meters = feet * 0.304
    print("You measured something that is",meters,"meters long!")

def hours_to_minutes():
    hours = float(input("how many hours?"))
    minutes = hours * 60
    print("You measured",minutes,"minutes!")



main()