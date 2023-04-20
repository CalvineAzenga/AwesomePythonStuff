# NLTK is a natural Language ToolKit library in python

from nltk.chat.util import Chat,reflections

pairs=[
    ['my name is (.*)',['Hello ! % 1']],
    ['(hi|hello|hey|holla|hola)' ,['Hey there !','Hi there !','Hey !']],
    ['(.*) your name ?',['My name is Geeky']],
    ['(.*) do you do ?',['We provide a platform for tech enthusiasts, a wide range of options !']],
    ['(.*) created you ?',['Geeksforgeeks created me using python and NLTK']]
]

chat=Chat(pairs,reflections)
# chat.converse()
while True:
    tetx=input(">> ")
    answer=chat.respond(tetx)
    if answer==None:
        print("Type help...")
    else:
        print(answer)