
# fix division by 0 in 4th choice
#    version = 5.0
from decimal import * 
getcontext()


def main():
    import os
    import time
    import sys
    from math import sqrt
    os.system("title Flow's calculator!")
    from colorama import init, Fore, Style
    init(convert=True, autoreset=True)
    #Variables stored here that are defined not by the user.
    #--------------------------------------------DO NOT CHANGE----------------------------------------------------------

    no_choice = "INVALID CHOICE!"
    Status_of_calculator = True
    Avogadronumber = 6.0221409 * 10 ** 23
    nolist = ['no', 'n', 'nope', 'nop']
    yeslist = ['yes', 'y', 'yea', 'yeah']
    exitlist = ['q', 'quit', 'exit', 'die', 'exit()', 'leave', ' ']
    add = ['add', 'addition']
    multiply = ['multiply', 'time', 'x']
    go_back_list = ["go","back","plzback","plzgoback","backnow","goingback","gb"]
    logo_avagadro_number = f"""

                     █████╗ ██╗   ██╗ ██████╗  ██████╗  █████╗ ██████╗ ██████╗  ██████╗    ▄█   ███████╗      
                    ██╔══██╗██║   ██║██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔═══██╗   ██   ██╔════╝     
                    ███████║██║   ██║██║   ██║██║  ███╗███████║██║  ██║██████╔╝██║   ██║   ▀▀   ███████╗     
                    ██╔══██║╚██╗ ██╔╝██║   ██║██║   ██║██╔══██║██║  ██║██╔══██╗██║   ██║        ╚════██║     
                    ██║  ██║ ╚████╔╝ ╚██████╔╝╚██████╔╝██║  ██║██████╔╝██║  ██║╚██████╔╝        ███████║      
                    ╚═╝  ╚═╝  ╚═══╝   ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝         ╚══════╝      
                        
                        
                    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗   
                    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗   
                    ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝   
                    ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗   
                    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║    
                    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝    
                        """
    status_on = f"""{Fore.GREEN}
                                ███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗     ██████╗ ███╗   ██╗    
                                ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝    ██╔═══██╗████╗  ██║    
                                ███████╗   ██║   ███████║   ██║   ██║   ██║███████╗    ██║   ██║██╔██╗ ██║    
                                ╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║    ██║   ██║██║╚██╗██║    
                                ███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║    ╚██████╔╝██║ ╚████║    
                                ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝     ╚═════╝ ╚═╝  ╚═══╝    
        """
    status_off = f"""{Fore.RED}
                                    ███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗
                                    ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║
                                    ███████╗   ██║   ███████║   ██║   ██║   ██║███████╗    ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║
                                    ╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║    ██║  ██║██║   ██║██║███╗██║██║╚██╗██║
                                    ███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║    ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║
                                    ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝

        
        """
    #---------------------------------------FUNCTIONS STORED HERE------------------------------------------------------
    def quit_progam_any_time(check_input):
        if check_input in exitlist: 
            return True
        return False

    def is_digit(check_input):
        '''
        function checking if your string is a pure digit, int
        return : bool
        '''
        if check_input.isdigit():
            return True
        return False

    def is_string_only(check_input):
        '''
        function checking if your string is all letters
        return : bool
        '''    
        if check_input.isalpha():
            return True
        return False

    def is_string_with_space(check_input):
        '''
        function checking if your string is all letters, but including space(s)
        return : bool
        '''   
        valid = False
        if ' ' in check_input:
            for char in check_input:
                if char.isdigit():
                    valid = False
                elif char.isalpha() or char.isspace():
                    valid = True
        return valid

    def is_string_or_num(check_input):
        '''
        function checking if your string is all letters or numbers
        return : bool
        '''       
        if check_input.isalnum():
            return True
        return False

    def is_float(check_input):
        '''
        function checking if your string is a floating point
        return : bool
        '''   
        if '.' in check_input:
            split_number = check_input.split('.')
            if len(split_number) == 2 and split_number[0].isdigit() and split_number[1].isdigit():
                    return True
        return False
    def Status():
        
        Status_of_calculator = False
        return Status_of_calculator
    def first_num_check():
        global firstnum
        firstnum = input(f"{Fore.MAGENTA}\nPlease type your first desired number:  {Style.RESET_ALL}{Fore.BLUE}")
        while firstnum not in exitlist and not is_float(firstnum) and not is_digit(firstnum): #Loops if user inputs a letter and special characters, or actually anything else rather than a decimal or an integer
            print(f"{Fore.RED}\nInvalid entry. Only decimals and integers are accepted.")

            firstnum = input(f"{Fore.MAGENTA}\nPlease retype your first desired number:  {Style.RESET_ALL}{Fore.BLUE}")
        
        if quit_progam_any_time(firstnum) == True: #We add this part incase the user wants to exit while inputting
            print(f"{Style.BRIGHT}{Fore.YELLOW}Goodbye!")
            time.sleep(2)
            exit()
    def second_num_check():
        global secondnum
        secondnum = input(f"{Fore.MAGENTA}\nPlease type your second desired number:  {Style.RESET_ALL}{Fore.BLUE}")
        while secondnum not in exitlist and not is_float(secondnum) and not is_digit(secondnum):
            print(f"{Fore.RED}\nInvalid entry. Only decimals and integers are accepted.")
            secondnum = input(f"{Fore.MAGENTA}\nPlease retype your second desired number:  {Style.RESET_ALL}{Fore.BLUE}")
        if quit_progam_any_time(secondnum) == True: #We add this part incase the user wants to exit while inputting
            print(f"{Style.BRIGHT}{Fore.YELLOW}Goodbye!")
            time.sleep(2)
            exit()
    def base_num_check():
        global base_number
        base_number = input(f"{Fore.MAGENTA}\nPlease type your base number:  {Style.RESET_ALL}{Fore.BLUE}")
        if quit_progam_any_time(base_number) == True: #We add this part incase the user wants to exit while inputting
            print(f"{Style.BRIGHT}{Fore.YELLOW}Goodbye!")
            time.sleep(2)
            exit()  
        while base_number not in exitlist and not is_digit(base_number) and not is_float(base_number): #If user passes the while loop, then he is checked 1 more time and then converted to a float(decimal) as it has been set to as a string(letter)
            print(f"{Fore.RED}\nInvalid entry. Only decimals and integers are accepted.")
            base_number = input(f"{Fore.MAGENTA}\nPlease retype your desired base number:  {Style.RESET_ALL}{Fore.BLUE}")
    def exponent_num_check():
        global exponent
        exponent = input(f"{Fore.MAGENTA}\nPlease type your exponent number:  {Style.RESET_ALL}{Fore.BLUE}")

        if quit_progam_any_time(exponent) == True:
            print(f"{Style.BRIGHT}{Fore.YELLOW}Goodbye!")
            time.sleep(2)
            exit()
        while exponent not in exitlist and not is_digit(exponent) and not is_float(exponent): #If user passes the while loop, then he is checked 1 more time and then converted to a float(decimal) as it has been set to as a string(letter)
            print(f"{Fore.RED}\nInvalid entry. Only decimals and integers are accepted.")
            exponent = input(f"{Fore.MAGENTA}\nPlease retype your desired exponent number:  {Style.RESET_ALL}{Fore.BLUE}")
    def choice_check():
            global choice
            choice = input(f"{Fore.MAGENTA}\nPlease type your second desired number:  {Style.RESET_ALL}{Fore.BLUE}")
            while choice not in exitlist and not is_float(choice) and not is_digit(choice):
                print(f"{Fore.RED}\nInvalid entry. Only decimals and integers are accepted.")
                choice = input(f"{Fore.MAGENTA}\nPlease retype your second desired number:  {Style.RESET_ALL}{Fore.BLUE}")
            if quit_progam_any_time(choice) == True: #We add this part incase the user wants to exit while inputting
                print(f"{Style.BRIGHT}{Fore.YELLOW}Goodbye!")
                time.sleep(2)
                exit()
            choice = int(choice)
    #-GLOBAL VARIABLES STORED DOWN BELOW. DO NOT MODIFY AS THIS WILL BREAK PROGRAM-
    global firstnum
    global secondnum
    global base_number
    global exponent
    #------------------------------------------------------------------------------
    if Status_of_calculator == False:
        os.system("title :(")
        print(f"""{Fore.RED}
                                    ███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗
                                    ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║
                                    ███████╗   ██║   ███████║   ██║   ██║   ██║███████╗    ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║
                                    ╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║    ██║  ██║██║   ██║██║███╗██║██║╚██╗██║
                                    ███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║    ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║
                                    ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝

        
        """)
    elif Status_of_calculator == True:

        os.system("title Loading calculator. Please wait..")
                                                        # Title down below that will get deleted after 3 seconds.
        print(status_on)
        time.sleep(3)
        
        os.system("cls")
        os.system("title Flow's calculator -Running...")
      
        print(f""" {Fore.LIGHTMAGENTA_EX}
                                     ______           __                   __            __                       
                                    /      \         |  \                 |  \          |  \                      
                                   |  ▓▓▓▓▓▓\ ______ | ▓▓ _______ __    __| ▓▓ ______  _| ▓▓_    ______   ______  
                                   | ▓▓   \▓▓|      \| ▓▓/       \  \  |  \ ▓▓|      \|   ▓▓ \  /      \ /      \ 
                                   | ▓▓       \▓▓▓▓▓▓\ ▓▓  ▓▓▓▓▓▓▓ ▓▓  | ▓▓ ▓▓ \▓▓▓▓▓▓ \▓▓▓▓▓▓ |  ▓▓▓▓▓▓\  ▓▓▓▓▓▓
                                   | ▓▓   __ /      ▓▓ ▓▓ ▓▓     | ▓▓  | ▓▓ ▓▓/      ▓▓ | ▓▓ __| ▓▓  | ▓▓ ▓▓   \▓▓
                                   | ▓▓__/  \  ▓▓▓▓▓▓▓ ▓▓ ▓▓_____| ▓▓__/ ▓▓ ▓▓  ▓▓▓▓▓▓▓ | ▓▓|  \ ▓▓__/ ▓▓ ▓▓      
                                    \▓▓    ▓▓\▓▓    ▓▓ ▓▓\▓▓     \ ▓▓    ▓▓ ▓▓\▓▓    ▓▓  \▓▓  ▓▓\▓▓    ▓▓ ▓▓      
                                     \▓▓▓▓▓▓  \▓▓▓▓▓▓▓\▓▓ \▓▓▓▓▓▓▓ \▓▓▓▓▓▓ \▓▓ \▓▓▓▓▓▓▓   \▓▓▓▓  \▓▓▓▓▓▓ \▓▓      
                                                                                
                                                                                
                                                                                

        """)   
        
        
        print(f"{Fore.GREEN}You have opened up a calculator.\n")
        print(f"{Fore.RED}1 to 4 is basic math, 5 to 8 has more options to choose.{Fore.RESET}\n\n1 = add, 2 = subtract, 3 = multiply, 4 = divide\n\n5 = square root, 6 = power, 7 = Avogadro's selection")
        A = input(f"{Fore.MAGENTA}\nPlease type your choice:  {Style.RESET_ALL}{Fore.BLUE}")
        A = A.lower()            #We do this incase user inputs something of a capital letter for the exitlist keywords.

        while A not in exitlist and not is_digit(A):
            print(f"{Style.RESET_ALL}{Fore.RED}\nInvalid Input, Integers are the only values accepted.")
            A = input(f"{Fore.MAGENTA}\nPlease repick your choise from the list above:{Style.RESET_ALL}{Fore.RED}   ")

        if quit_progam_any_time(A) == True: #We add this part incase the user wants to exit while inputting a choice
            print(f"{Style.BRIGHT}{Fore.YELLOW}\nGoodbye!")
            time.sleep(2)
            exit() 

        if A != is_digit(A):
            A = int(A)

                                                # Calculation down below
        if A == 1:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}addition!{Style.RESET_ALL} \n \nWhat is the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
            first_num_check()
            second_num_check()

            # if firstnum or secondnum not in exitlist and is_digit(secondnum, firstnum) or is_float(secondnum, firstnum): #If user passes the while loop, then he is checked 1 more time and then converted to a float(decimal) as it has been set to as a string(letter)
            firstnum = Decimal(firstnum)
            secondnum = Decimal(secondnum)    
            total = firstnum + secondnum


                                    #Will add when I understand it

            print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} +{Style.RESET_ALL} {Fore.MAGENTA}{secondnum}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
            print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")        
            """
            print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} +{Style.RESET_ALL} {Fore.MAGENTA}{secondnum}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")

            print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}, and the {Fore.LIGHTGREEN_EX}rounded{Style.RESET_ALL}anwser is {rounded}{Style.BRIGHT}.")
            """
        elif A == 2:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX} subtraction!{Style.RESET_ALL} \n \nThis will subtract the first number by the second number.")
            print(f"\nWhat is the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
            
            first_num_check()
            second_num_check()

            if firstnum or secondnum not in exitlist and is_digit(secondnum, firstnum) or is_float(secondnum, firstnum): #If user passes the while loop, then he is checked 1 more time and then converted to a float(decimal) as it has been set to as a string(letter)
                firstnum = Decimal(firstnum)
                secondnum = Decimal(secondnum)
                total = firstnum - secondnum
                print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} -{Style.RESET_ALL} {Fore.MAGENTA}{secondnum}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")       
        elif A == 3:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}multiplication!{Style.RESET_ALL} \n \nWhat is the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
            first_num_check()
            second_num_check()


            if firstnum or secondnum not in exitlist and is_digit(secondnum, firstnum) or is_float(secondnum, firstnum): #If user passes the while loop, then he is checked 1 more time and then converted to a float(decimal) as it has been set to as a string(letter)
                firstnum = Decimal(firstnum)
                secondnum = Decimal(secondnum)
                total = firstnum * secondnum
                print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} * {Style.RESET_ALL}{Fore.MAGENTA}{secondnum}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
        elif A == 4:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}division!{Style.RESET_ALL} \n{Fore.YELLOW}Please note:{Style.RESET_ALL} This will divide the first number over the second number.\n \nWhat is the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
            
            first_num_check()
            second_num_check()
            if secondnum == 0:
                del secondnum
            try:
                secondnum
            except NameError:
                print(f" \n \n{Fore.RED}Division{Style.RESET_ALL} by {Style.BRIGHT}0{Style.RESET_ALL} is {Style.BRIGHT}impossible.\n\n")
                Repeat = input(f"\n\n{Fore.CYAN}Do you wish to restart the program?{Style.RESET_ALL}   {Fore.LIGHTBLUE_EX}").lower()
                if Repeat in yeslist:
                    os.system("cls")
                    main()
                elif Repeat in nolist:
                    exit()
                else:
                    exit()    
            if firstnum or secondnum not in exitlist and is_digit(secondnum, firstnum) or is_float(secondnum, firstnum): #If user passes the while loop, then he is checked 1 more time and then converted to a float(decimal) as it has been set to as a string(letter)
            
                firstnum = Decimal(firstnum)
                secondnum = Decimal(secondnum)
           
            if secondnum == 0:
                del secondnum
            try:
                secondnum
            except NameError:
                print(f" \n \n{Fore.RED}Division{Style.RESET_ALL} by {Style.BRIGHT}0{Style.RESET_ALL} is {Style.BRIGHT}impossible.\n\n")
                Repeat = input(f"\n\n{Fore.CYAN}Do you wish to restart the program?{Style.RESET_ALL}   {Fore.LIGHTBLUE_EX}").lower()
                if Repeat in yeslist:
                    os.system("cls")
                    main()
                elif Repeat in nolist:
                    exit()
                else:
                    exit()
                total = firstnum / secondnum

            print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} / {Style.RESET_ALL}{Fore.MAGENTA}{secondnum}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
            print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
        elif A == 5:
            
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}square root!{Style.RESET_ALL}")
            first_num_check()
            if firstnum not in exitlist and is_digit(firstnum) or is_float(firstnum):
                firstnum = Decimal(firstnum)
                result = sqrt(firstnum)
            print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} √ {Style.RESET_ALL}{Fore.YELLOW}{firstnum}{Style.RESET_ALL} = {Fore.RED}{result}{Style.RESET_ALL}{Style.BRIGHT}.")            
            print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{result}{Style.RESET_ALL}{Style.BRIGHT}.")

        elif A == 6:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}power!{Style.RESET_ALL}\n \nWhat is the {Fore.LIGHTMAGENTA_EX}base {Style.RESET_ALL}number?")
            base_num_check()
            print(f"\n{Fore.RESET}What is the {Fore.LIGHTMAGENTA_EX} exponent {Style.RESET_ALL}number? ")
            exponent_num_check()
            if base_number or exponent not in exitlist and is_digit(base_number, exponent) or is_float(base_number, exponent): #If user passes the while loop, then he is checked 1 more time and then converted to a float(decimal) as it has been set to as a string(letter)
                base_number = Decimal(base_number)
                exponent = Decimal(exponent)
                total = base_number ** exponent
            print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {base_number}{Style.RESET_ALL}{Style.BRIGHT} ^ {Style.RESET_ALL}{Fore.MAGENTA}{exponent}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
            print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")               
        elif A == 7:
            os.system("cls")
            print(logo_avagadro_number)
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}Avagadro's selection!{Style.RESET_ALL}")
            print(f"{Fore.RED}\n\n1 = addition + Avogadro's number, 2 = subtraction - Avogadro's number\n\n3 = multiplication * Avogadro's number, 4 = division /  Avogadro's number")
            avogadro_choice = input(f"{Fore.MAGENTA}\nPlease type your choice:  {Style.RESET_ALL}{Fore.BLUE}")
            while avogadro_choice not in exitlist and not is_digit(avogadro_choice):
                print(f"{Style.RESET_ALL}{Fore.RED}\nInvalid Input, Integers are the only values accepted.")
                avogadro_choice = input(f"{Fore.MAGENTA}\nPlease repick your choise from the list above:{Style.RESET_ALL}{Fore.RED}   ")

            if quit_progam_any_time(avogadro_choice) == True: #We add this part incase the user wants to exit while inputting a choice
                print(f"{Style.BRIGHT}{Fore.YELLOW}\nGoodbye!")
                time.sleep(2)
                exit() 

            if avogadro_choice != is_digit(avogadro_choice):
                avogadro_choice = int(avogadro_choice)
            if avogadro_choice == 1:
                print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}addition!{Style.RESET_ALL} \n \nWhat's the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
                first_num_check()
                print(f"\n{Fore.RESET}Do you want a second number? 1 = no, 2 = yes")
                choice_check()
                if choice == 1:
                    firstnum  = Decimal(firstnum)
                    total = float(firstnum) + Avogadronumber # we do this because we can't add Decimal class to float.
                    print(f"{Fore.RESET}\nThe {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} + {Style.RESET_ALL}{Fore.MAGENTA}{Avogadronumber}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                    print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                elif choice == 2:
                    print(f"\n{Fore.RESET}What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number then?")
                    second_num_check()
                    firstnum = Decimal(firstnum)
                    secondnum = Decimal(secondnum)
                    total = float(firstnum) + float(secondnum) + Avogadronumber
                    print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} + {Style.RESET_ALL}{Fore.MAGENTA}{secondnum}{Style.RESET_ALL}{Style.BRIGHT} +{Style.RESET_ALL} {Fore.MAGENTA}{Avogadronumber}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                    print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                else:
                    print(f"\n\n{Fore.RED}{no_choice}{Style.BRIGHT}")
                    time.sleep(5)
                    Repeat = input(f"\n\n{Fore.CYAN}Do you wish to restart the program?{Style.RESET_ALL}   {Fore.LIGHTBLUE_EX}").lower()
                    if Repeat in yeslist:
                        os.system("cls")
                        main()
                    else:
                        exit()
            elif avogadro_choice == 2:
                print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}subtraction!{Style.RESET_ALL} \n{Fore.YELLOW}Please note:{Style.RESET_ALL}This will subtract the first number to the second number (if you choose one) to Avogadro's number.")
                print(f"\nWhat's the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
                first_num_check()
                print(f"\n{Fore.RESET}{Style.BRIGHT}Do you want a second number? 1 = no, 2 = yes")
                choice_check()
                if choice == 1:
                    firstnum = Decimal(firstnum)
                    total = float(firstnum) - Avogadronumber
                    print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} - {Style.RESET_ALL}{Fore.MAGENTA}{Avogadronumber}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                    print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                elif choice == 2:
                    print(f"\n{Fore.RESET}What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number then?")
                    second_num_check()
                    secondnum = Decimal(secondnum)
                    firstnum = Decimal(firstnum)
                    total = (float(firstnum) - float(secondnum)) - Avogadronumber
                    print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Style.BRIGHT}({Style.RESET_ALL}{Fore.MAGENTA}{firstnum}{Style.RESET_ALL}{Style.BRIGHT} - {Style.RESET_ALL}{Fore.MAGENTA}{secondnum}{Style.RESET_ALL}{Style.BRIGHT}) - {Fore.MAGENTA}{Avogadronumber}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                    print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                else:
                    print(f"\n\n{Fore.RED}{no_choice}{Style.BRIGHT}")
                    time.sleep(5)
                    Repeat = input(f"\n\n{Fore.CYAN}Do you wish to restart the program?{Style.RESET_ALL}   {Fore.LIGHTBLUE_EX}").lower()
                    if Repeat in yeslist:
                        os.system("cls")
                        main()
                    else:
                        exit()
            elif avogadro_choice == 3:
                print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}multiplication!{Style.RESET_ALL} \n \nWhat's the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
                first_num_check()
                print(f"\n{Fore.RESET}Do you want a second number? 1 = no, 2 = yes")
                choice_check()
                
                if choice == 1:
                    firstnum = Decimal(firstnum)
                    total = float(firstnum) * Avogadronumber
                    print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} * {Style.RESET_ALL}{Fore.MAGENTA}{Avogadronumber}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                    print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                elif choice == 2:
                    print(f"\n{Fore.RESET}What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number then?")
                    second_num_check()
                    firstnum = Decimal(firstnum)
                    secondnum = Decimal(secondnum)
                    total = float(firstnum) * float(secondnum) * Avogadronumber
                    print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} * {Style.RESET_ALL}{Fore.MAGENTA}{secondnum}{Style.RESET_ALL}{Style.BRIGHT} * {Style.RESET_ALL}{Fore.MAGENTA}{Avogadronumber}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                    print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                else:
                    print(f"\n\n{Fore.RED}{no_choice}{Style.BRIGHT}")
                    time.sleep(5)
                    Repeat = input(f"\n\n{Fore.CYAN}Do you wish to restart the program?{Style.RESET_ALL}   {Fore.LIGHTBLUE_EX}").lower()
                    if Repeat in yeslist:
                        os.system("cls")
                        main()
                    else:
                        exit()            
            elif avogadro_choice == 4:
                print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}division!{Style.RESET_ALL} \n{Fore.YELLOW}Please note:{Style.RESET_ALL} This will divide the first number over the second number (If you choose a second number) over Avogadro's number.\n \nWhat's the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
                first_num_check()
                print(f"\n{Fore.RESET}{Style.BRIGHT}Do you want a second number? 1 = no, 2 = yes")
                choice_check()
                if choice == 1:
                    firstnum = Decimal(firstnum)
                    total = float(firstnum) / Avogadronumber 
                    print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} / {Style.RESET_ALL}{Fore.MAGENTA}{Avogadronumber}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                elif choice == 2:
                    print(f"\n{Fore.RESET}What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number then?")
                    second_num_check()
                    firstnum = Decimal(firstnum)
                    secondnum = Decimal(secondnum)

                    if secondnum == 0:
                        del secondnum
                    try:
                        secondnum
                    except NameError:
                        print(f" \n \n{Fore.RED}Division{Style.RESET_ALL} by {Style.BRIGHT}0{Style.RESET_ALL} is {Style.BRIGHT}impossible.\n\n")
                    else:
                        total = (float(firstnum) / float(secondnum)) / Avogadronumber
                        print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Style.BRIGHT}({Style.RESET_ALL}{Fore.MAGENTA}{firstnum}{Style.RESET_ALL}{Style.BRIGHT} / {Style.RESET_ALL}{Fore.MAGENTA}{secondnum}{Style.RESET_ALL}{Style.BRIGHT} / {Style.RESET_ALL}{Fore.MAGENTA}{Avogadronumber}{Style.RESET_ALL}{Style.BRIGHT}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                        print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.\n\n")
                else:
                    print(f"\n\n{Fore.RED}{no_choice}{Style.BRIGHT}")
                    time.sleep(5)
                    Repeat = input(f"\n\n{Fore.CYAN}Do you wish to restart the program?{Style.RESET_ALL}   {Fore.LIGHTBLUE_EX}").lower()
                    if Repeat in yeslist:
                        os.system("cls")
                        main()
                    else:
                        exit()            
            else:
                print(f"\n\n{Fore.RED}{no_choice}{Style.BRIGHT}")
        else:
            print(f"\n\n{Fore.RED}{no_choice}{Style.BRIGHT}")







        # print(f"{Fore.LIGHTCYAN_EX}\n\n\nIf you have any questions please contact me on my github(https://github.com/Flowgonnarap/calculator){Style.RESET_ALL}{Style.BRIGHT}.\n\n")
        Repeat = input(f"\n\n{Fore.CYAN}Do you wish to restart the program?{Style.RESET_ALL}   {Fore.LIGHTBLUE_EX}").lower()
        if Repeat in yeslist:
            os.system("cls")
            main()
        elif Repeat in nolist:
            exit()
        else:
            exit()
            #Where the code starts
main()
