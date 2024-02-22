#Method for the logic implementation
def is_valid_method(number):
    number_string = str(number)
    the_sum = 0

    #Multiplies every other digit starting from the second-to-last digit by 2
    for i in range(len(number_string) - 2, -1, -2):
        multiply = int(number_string[i]) * 2

        #add all of the digits together
        the_sum += the_sum(int(digit) for digit in str(multiply))

    #adds the previous sum to the digits that werent multiplied by 2
    for i in range(len(number_string) - 1, -1, -2):
        the_sum += int(number_string[i])

    #if the sum modulo 10 is 0, runs the full program
    return the_sum % 10 == 0

#Method for the card types      
def card_type(number):
    if len(number) == 15 and number.startswith(("34", "37")):
        return "AMERICAN EXPRESS"
    elif len(number) == 16 and number.startswith(("51", "52", "53", "54", "55")):
        return "MASTERCARD"
    elif (len(number) == 16 or len(number) == 13) and number.startswith("4"):
        return "VISA"
    else:
        return "UNKNOWN"

#prints out the card type if card is valid, if not then u retry
def user_input():
    while True:
        number = input("Number: ")
        if number.isdigit() and (len(number) == 16 or len(number) == 15 or len(number) == 13):
            print(card_type(number))
            break
user_input()   

'''
OUTPUT

Number: 4003-6000-0000-0014
Number: Test
Number: 1
Number: 4003600000000014
VISA

Number: abc
Number: 5555555555554444
MASTERCARD

Number: 378282246310005
AMERICAN EXPRESS

Number: 6011000000000004
UNKNOWN

'''

