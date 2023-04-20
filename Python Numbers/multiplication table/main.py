from os import system
from colorama import Fore,Back,Style,init
from termcolor import colored
import tabulate
system('cls')
def generate_multiplication_table(rows=4,columns=15):
    print("\n\t\t"+Fore.CYAN+Back.BLACK+"MULTIPLICATION TABLE IN PYTHON"+Back.BLACK)
    print(Back.BLACK+"")
    for row in range(1,rows+1):
        for column  in range(1,columns+1):
            answer=row*column
            
            if column==1 or row==1:
                print(Fore.YELLOW+str(answer),end='\t')
            else:
                print(Fore.GREEN+str(answer),end='\t')
            if column%columns==0:
                print("\n")
    print("\t\t\t\t\t"+Fore.CYAN+Back.BLACK+"Developed by Calvine Museywa Azenga\n"+colored("\t\t\t\t\tmuscalazems@gmail.com\n",'blue')+colored("\t\t\t\t\t+254700666848\n",'magenta'),end='\n\n\n')

    
    print(Fore.WHITE+"")
generate_multiplication_table()