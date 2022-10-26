def encryptReverse(lst):
    x = lst[::-1]
    y = "".join([chr(c) for c in x])
    return "Your decrypted message is: \n" + y #<-- new message
    #return "Your decrypted message is: \n " <-- original input
    
def encryptShift(string, firstShift, secShift, direction):
    # converts each letter to ascii value(number) and shifts
    a = []
    if direction == "+": # if direction is +, shifted to the right
        i = 0
        while i < len(string):
            for char in string:
                if i%2 == 0: # if even, shifted right by firstShift amount
                    q = ord(char) + firstShift
                    if q == 126:
                        a.append(q)
                        i+=1
                    elif q > 126:
                        qNew = q - 126 + 31
                        a.append(qNew)
                        i += 1
                    else:
                        a.append(q)
                        i += 1
                else: # if odd, shifted right by secShift amount
                    shifted = ord(char) + secShift
                    if shifted > 126:
                        shifted = shifted - 95
                        a.append(shifted)
                        i += 1
                    else:
                        a.append(shifted)
                        i += 1 
    else:
       i = 0
       # if direction is -, shifted to the left 
       while i < len(string):
            for char in string:
                if i%2 == 0: # if even, shifted left by firstShift amount
                    shifted = ord(char) - firstShift
                    if shifted < 32:
                        shifted = shifted + 95
                        a.append(shifted)
                        i += 1
                    else:
                        a.append(shifted)
                        i += 1
                else: # if odd, shifted left by secShift amount
                    otherShift = ord(char) - secShift
                    if otherShift < 32:
                        otherShift = otherShift + 95
                        a.append(otherShift)
                        i +=1
                    else:
                        a.append(otherShift)
                        i += 1
    return encryptReverse(a)

def encrypt(string, integer, direction):
    # validates whether user input of first/second shift is in range
    string = raw_input("Please type your message: ")
    #integer = int(input("Please input a number between 1 and 94 to be used as a first shift>> "))
    while True: #infinite loop
        firstShift = integer
        integer = raw_input("Please input a number between 1 and 94 to be used as a first shift >>> ") #asks for number in range
        try: #tries to int the input to see user put correct value           
            a = int(integer)
            if a < 1 or a > 95: #checking number in range
                print "Invalid input. Your input is not in the range." 
            else:
                break #ends loop if the number is in range
        except ValueError: #accepts value error and says tries again
            print "Invalid input. Your input is not an integer." + "\n"
    while True: #infinite loop
        secShift = integer
        integer = raw_input("Please input a number between 1 and 94 to be used as a second shift >>> ") #asks for number in range
        try: #tries to int the input to see user put correct value
            b = int(integer)
            if b < 1 or b > 95: #checking number in range
                print "Invalid input. Your input is not in the range." 
            else:
                break #ends loop if the number is in range
        except ValueError: #accepts value error and says tries again
            print "Invalid input. Your input is not an integer." + "\n"
    direction = raw_input("Please input encryption direction. Type + or - >> ")
    while direction != "+" and direction != "-":
        print "Invalid input." + "\n"
        direction = raw_input("Please input encryption direction. Type + or - >> ")
    else:
        print "Your encrypted message is: " + "\n" + str(string)
        return encryptShift(string, firstShift, secShift, direction)



def decryptShift(string, firstShift, secShift, direction):
    # converts each letter to ascii value(number) and shifts
    a = []
    b = ""
    if direction == "+": # if direction is +, shifted to the left
        i = 0
        while i < len(string):
            for char in string:
                if i%2 == 0: # if even, shifted left by firstShift amount
                    shifted = ord(char) - firstShift
                    if shifted < 32:
                        shifted = shifted + 95
                        a.append(chr(shifted))
                        i += 1
                    else:
                        a.append(chr(shifted))
                        i += 1
                else: # if odd, shifted left by secShift amount
                    otherShift = ord(char) - secShift
                    if otherShift < 32:
                        otherShift = otherShift + 95
                        a.append(chr(otherShift))
                        i +=1
                    else:
                        a.append(chr(otherShift))
                        i += 1
    else:
       i = 0
       # if direction is -, shifted to the right
       while i < len(string):
            for char in string:
                if i%2 == 0: # if even, shifted right by firstShift amount
                    q = ord(char) + firstShift
                    if q == 126:
                        a.append(chr(q))
                        i += 1
                    elif q > 126:
                        qNew = q - 126 + 31
                        a.append(chr(qNew))
                        i += 1
                    else:
                        a.append(chr(q))
                        i += 1
                else: # if odd, shifted right by secShift amount
                    shifted = ord(char) + secShift
                    if shifted > 126:
                        shifted = shifted - 95
                        a.append(chr(shifted))
                        i += 1
                    else:
                        a.append(chr(shifted))
                        i += 1 
    z = ''.join(a)
    print "Your decrypted message is: \n" + z, "\n",  "Your encrypted message is:   \n"+ string
    return "\n"

def decryptReverse(s): # returns string
    i = len(s) - 1
    sNew = ""
    while i >= 0:
        sNew = sNew + str(s[i])
        i -= 1
    return sNew

def decrypt(string, integer, direction):
    # validates whether user input of first/second shift is in range
    string = raw_input("Please type your message: ")
    integer = int(input("Please input a number between 1 and 94 to be used as a first shift>> "))
    firstShift = integer
    while type(firstShift) != int:
        print "Invalid input.",
        integer = input("Please input a number between 1 and 94 to be used as a first shift>> ")
    while not 0 < firstShift < 94:
        # if not in range, error message + asked again for first shift
        print "Invalid input.",
        integer = input("Please input a number between 1 and 94 to be used as a first shift>> ")
    else:
        # if in range, user asked for second shift number
        integer = input("Please input a number between 1 and 94 to be used as a second shift>> ")
        secShift = integer
        while not 0 < secShift < 94:
            # if not in range, error message + asked again for second shift            
            print "Invalid input.",
            integer = input("Please input a number between 1 and 94 to be used as a first shift>> ")
            secShift = integer
        else:
            # if in range, user asked for direction for shifts
            direction= raw_input("Please input encryption direction. Type + or - >> ")
            while direction != "+" and direction != "-":
                # if + or - not inputted, error message shown and asked again for direction
                print "Invalid input.",
                direction = input("Please input encryption direction. Type + or - >> ")
            else:
                # if in shifts in range and direction is inputted
                # performs next function: the actual shifting of letters
                return decryptShift(str(decryptReverse(string)), firstShift, secShift, direction)

def inputAndValidation(x):
    # validates the user input in main
    # a, b, c are actually the parameters string, integer, and direction
    a = ""
    b = ""
    c = ""
    # if user input is other than any form of the letters e or d
    # error message is shown and user is asked question again
    while x != "E" and x != "e" and x != "D" and x != "d":
        print "Invalid input.",
        x = raw_input("Would you like to encrypt or decrypt your message? Type E or D >> ")
    if x == "E" or x == "e":
        # if user input is e, encrypt is performed
        return encrypt(a, b, c)
    else:
        # if user input is d, decrypt is performed
        return decrypt(a, b, c)
    

def main():
    # asks user for input of e or d
    # goes to next function
    x = raw_input("Would you like to encrypt or decrypt your message? Type E or D >> ")
    print inputAndValidation(x)
main()

