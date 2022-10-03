
def any_base_to_decimal(number, base):
    # calling the builtin function
    # int(number, base) by passing
    # two arguments in it number in
    # string form and base and store
    # the output value in temp
    temp = int(number, base)

    # printing the corresponding decimal
    # number
    print(temp)


def any_base_hex(number):
    temp = hex(number)
    print(temp)


def any_base_octal(number):
    temp = oct(number)
    print(temp)


if __name__ == '__main__':
    # what do you have to put here to call any_base_to_decimal?? details need to be put here
    menuoption = int (input('enter option: \n1) Convert into decimal from any base \n2) Convert into hex from any base \n3) Convert into octal from any base'))
    if menuoption==1:
        any_base_to_decimal(input("Enter number "), int(input("Enter base:")))
    elif menuoption==2:
        any_base_hex(int(input("Enter number ")))
    elif menuoption==3:
        any_base_octal(int(input("Enter number ")))
    else:
        print("Wrong input")
        menuoption = int(input('enter option: \n1) Convert into decimal from any base \n2) Convert into hex from any base \n3) Convert into octal from any base'))

