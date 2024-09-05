import datetime
import time
from time import sleep
import random
import TextEncryption
import sys
from plyer import notification
from rich.progress import *
import os

services    = ["text encryption", 
               "dates", 
               "random password generator", 
               "sorting", 
               "Convertion", 
               "typing test"]

servicesKey = ["1", "encryption", "encrypt", "text", "text encrypt", "text encryption", 
               "2", "datetime", "dates", "date countdown", "countdown", "now", 
               "3", "password", "pw", "generate", "password generation", "random password", 
               "4", "Sorting", "sorting", "reorder", "order", "sequence"
               "5", "Temperature", "temperature", "temp", "conversion", "convert"
               "6", "Typing test", "typing test", "Type", "type", "typing"
               ]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printServices(): # Print all available services
    for i in range(len(services)):
        print(str(i+1) + " " + services[i])

def findWords(target):
    for i in range(len(servicesKey)):
        if target in servicesKey[i]:
            if i <= 5:
                return 1
            elif i > 5 and i <= 10:
                return 2
            elif i > 10 and i <= 15:
                return 3
            elif i > 15 and i <= 20:
                return 4
            elif i > 20 and i <= 25:
                return 5
            elif i > 25 and i <= 30:
                return 6
    return False

def Func_textEncryption(): # Encryption
    userInput = input("Are you going to: " + 
                      "1: encrypt or 2: decrypt the text? ")
    if userInput == "1":
        print("Result: ", TextEncryption.Encrypt(input("Please input the message: ")))
    elif userInput == "2":
        print("Result: ", TextEncryption.Decrypt(input("Please input the encrypted message: ")))

def Func_datetime(): # Date time calculations
    print("\nAre you going to:\n\n", 
          "1: Retrive current time, or\n", 
          "2: Count how many days from a specific date, or\n", 
          "3: Count down timer, or\n", 
          "4: Count down to specific time? ")
    userInput = input("\nPlease enter: ")
    if userInput == "1":
        print(str(datetime.datetime.now())[:19])
    if userInput == "2":

        dateResult = ""
        
        flag = True
        while(flag):
            desiredDate = input("Please input a past date (mm/dd/yyyy): ")
            if len(desiredDate) != 10:
                print("Incorrect date format. ")
            else:
                
                start = datetime.datetime.strptime(desiredDate, '%m/%d/%Y')

                current = datetime.datetime.now()

                delta = current - start
                count = delta.days

                print("It's", count,"days")
                flag = False
    if userInput == "3":
        userTime = input("Please input the time you want (hh-mm-ss): ")
        print()
        
        hour = int(userTime[0:2])
        minute = int(userTime[3:5])
        second = int(userTime[6:8])
        
        count = (hour*60+minute)*60+second
        countSave = time.strftime('%H:%M:%S', time.gmtime(count))
        
        timeFlag = True
        while(timeFlag):
            sys.stdout.write('\r'+time.strftime('%H:%M:%S', time.gmtime(count)))
            # sys.stdout.write("\033[K")
            # sys.stdout.write("\033[F")
            sleep(1)
            count -= 1
            if count <= 0:
                timeFlag = False
                sys.stdout.write('\r'+time.strftime('%H:%M:%S', time.gmtime(count)))
            
        print("\nTimer Ended! ")
        notification.notify(
            title= "Timer Ended! ",
            message=("Timer for " + countSave),
            app_icon="./clock.ico",
            timeout=12
        )      
    if userInput == "4":
        
        flag = True
        while flag:
            
            userTime = input("\nPlease input the time you want (hh-mm-ss): ")
            # print(datetime.datetime.now())
            datetimeNow = str(datetime.datetime.now())
            
            if userTime == "no":
                flag = False
                break
            elif len(userTime) != 8:
                print("Incorrect time format. ")
                continue
            
            hour = int(userTime[0:2])
            minute = int(userTime[3:5])
            second = int(userTime[6:8])
            
            hourNow = int(datetimeNow[11:13])
            minuteNow = int(datetimeNow[14:16])
            secondNow = int(datetimeNow[17:19])
            
            count = (hour*60+minute)*60+second
            countNow = (hourNow*60+minuteNow)*60+secondNow
            
            if countNow > count:
                print("You've entered a time in the past. Please re-enter. ")
            else:
                
                print("You've set a timer counting to " + str(time.strftime('%H:%M:%S', time.gmtime(count))) + "\n")
                
                progressDot = [".","..","...","   "]
                progressSlash = ["|","/","-","\\","|","/","-","\\"]
                progressDotcount = 0
                counting = True
                while counting:
                    datetimeNow = str(datetime.datetime.now())
                    hourNow = int(datetimeNow[11:13])
                    minuteNow = int(datetimeNow[14:16])
                    secondNow = int(datetimeNow[17:19])
                    countNow = (hourNow*60+minuteNow)*60+secondNow
                    
                    if secondNow % 0.5 == 0:
                        # sys.stdout.write('\r'+"Current time: "+time.strftime('%H:%M:%S', time.gmtime(countNow)))
                        sys.stdout.write('\r'+"Time remaining: "+time.strftime('%H:%M:%S', time.gmtime(count-countNow))+"  "+progressSlash[progressDotcount])
                        progressDotcount += 1
                        if progressDotcount > 7:
                            progressDotcount = 0
                        sleep(0.5)
                        
                    if countNow >= count:
                        print("\nTimer Ended! ")
                        notification.notify(
                        title= "Timer Ended! ",
                        message=("Timer set for " + str(time.strftime('%H:%M:%S', time.gmtime(count)))),
                        app_icon="./clock.ico",
                        timeout=12
                        )
                        counting = False
                        break
            
            # time.strftime('%H:%M:%S', time.gmtime(count))
        
def Func_passwordGeneration(): # Generates random password
    userInput = input("How many characters are required? ")
    Result = ""
    Sequence = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    for i in range(int(userInput)):
        Result += Sequence[random.randint(0,61)]
    print("\nGenerated password: " + Result)

def Func_sorting(): # Sorts text input
    userInput = input("Please input the sequence: ")
    print("Result: "+''.join(sorted(userInput)))

def Func_conversion():
    print("\nThe current available conversions are: \n",
          "1 temperature conversion\n",
          "2 length conversion\n",
          "3 weight conversion\n",
          "4 currency conversion\n")
    userInput = input("Please specify what type of conversions: ")
    
    if userInput == "1":
        temp = int(input("\nPlease enter the temperature: "))
        degreeC = (temp - 32) * 5 / 9
        degreeF = temp * 9 / 5 + 32
        print()
        print(userInput + "°F =", str(int(degreeC)) + "°C")
        print(userInput + "°C =", str(int(degreeF)) + "°F")
    if userInput == "2":
        length = int(input("\nPlease enter the length: "))
        # inch & cm
        inch = length / 2.54
        cm = length * 2.54
        
        print()
        print(userInput + " cm =", str(int(inch)) + " inch")
        print(userInput + " inch =", str(int(cm)) + " cm")
    

def Func_typingTest():
    
    text = "This is a typing test that has a bug which it cannot go to the second line. "
    userInput = input("please specify the test taking time (mm-ss): ")
    minute = int(userInput[0:2])
    second = int(userInput[3:5])
    count = minute*60 + second
    
    datetimeNow = str(datetime.datetime.now())
    minuteNow = int(datetimeNow[14:16])
    secondNow = int(datetimeNow[17:19])
    countNow = minuteNow*60 + secondNow
    
    print("\n" + text)
    
    print("\nPlease start typing below...\n")
    
    typed = input()



# Main Program Starts

clear()
print("Welcome back, Will. Here lists the available functions: ")

flag = True
while(flag):
    print()
    printServices()
    user = input("\nWhat service do you want? ")
    response = findWords(user)
    if response == 1:
        Func_textEncryption()
    elif response == 2:
        Func_datetime()
    elif response == 3:
        Func_passwordGeneration()
    elif response == 4:
        Func_sorting()
    elif response == 5:
        Func_conversion()
    elif response == 6:
        Func_typingTest()
        
    if input("\nPress enter to clear console...") == "":
        clear()
    else:
        print("please re-enter your response: ")