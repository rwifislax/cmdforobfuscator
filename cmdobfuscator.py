# CMD command obfuscator

import random

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

    #build cmd one liner
    cmd = 'cmd /V /C "set test=' + shuffled_string + '&&for %A in (' + numbers_list + ') do set word=!word!!test:~%A,1!&&if %A==' + str(random_number) + ' call %word:~-' + str(string_length) + '%"'
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
