from os import system
import sys
from colorama import Fore,Back,Style,init
from termcolor import colored
import pyttsx3
pyttsx3.init()
init()
system('cls')
system('title Find Prime numbers')

def prime_number_finder(number,amount):
    i=0
    primes=[]
    primes1=[]
    num=int(number)
    am=int(amount)
    if number>amount:
        amount=num
        number=am
        num=number
    number1=2
    system(f'title Find Prime numbers between {number} and {amount}')
    while number1<amount:
        for x in primes:
            if number1%x==0:
                break
        else:
            primes.append(number1)
        number1+=1
    for nums in primes:
        if nums>num:
            i+=1
            primes1.append(nums)
    del primes
    if i>1:
        text='are'
        text2='numbers'
    elif i==1:
        text='is'
        text2='number'
    else:
        text='is'
        text2='numbers'
    pyttsx3.speak(f"There {text} {i} prime {text2} between {num} and {amount}. I will be listing shortly.")

    return primes1

def main():
    try:
        numbers=input(Fore.GREEN+"Enter the range of values to find their prime numbers"+colored("(Comma separated(,)): ","yellow")).split(',')
        if str(numbers[0]).lower()=='q':
            print(str(numbers[0]).lower())
            pyttsx3.speak("System shutdown initiated.")
            sys.exit()
        system('cls')
        print("\n\t\t\t"+Fore.GREEN+Back.LIGHTWHITE_EX+"PRIME NUMBERS FINDER")
        print(Fore.WHITE+Back.BLACK+"\n\n")
        number=int(numbers[0])
        amount=int(numbers[1])
        print(Fore.CYAN+str(prime_number_finder(number,amount)))
        main()
    except ValueError:
        print(Fore.RED+"+ ERROR:- Ensure you have entered 2 NUMBERS separated by a comma")
        main()
    except Exception:
        print(Back.RED+"+ ERROR:- Some error occurred")
        main()
main()
