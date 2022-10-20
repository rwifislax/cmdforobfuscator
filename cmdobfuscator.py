# CMD command obfuscator

import random
import string

def random_words():
    alphanumeric = string.ascii_lowercase + string.digits
    random_word = ""
    n = random.randint(5,10)
    for i in range(n):
        random_number = random.randint(0,35)
        random_word = random_word + alphanumeric[random_number]

    return random_word

def builder(string):
    #shuffle string and get numbers
    shuffled_string = ''.join(random.sample(string, len(string)))
    
    random_number = random.randint(0,2000)
    string_length = len(string)

    numbers_list = ""
    for a in string:
        counter = 0
        for b in shuffled_string:
            if a == b:
                numbers_list = numbers_list + str(counter) + " " 
                break
            counter = counter + 1

    numbers_list = numbers_list + str(random_number)

    #get random words for the variables
    var1 = random_words()
    var2 = random_words()
    
    #build cmd one liner
    cmd = 'cmd /V /C \'set ' + var1 + '=' + shuffled_string + '&&for %A in (' + numbers_list + ') do set ' + var2 + '=!' + var2 + '!!' + var1 + ':~%A,1!&&if %A==' + str(random_number) + ' call %' + var2 + ':~-' + str(string_length) + '%\''
    return cmd

def main():
    
    print("******** CMD Command obfuscator ********\nEnter CMD command to obfuscate.\nPress Enter when done.")
    while True:
        string = input("Command: ")
        if string == "":
            break
            
        result = builder(string)
        print(result)

if __name__ == '__main__':
    main()
