import math
import num2words
import os
from datetime import datetime
import threading
import json
import difflib
from tkinter import ttk,Listbox
def solveMath(quiz):
    text=f"Could not solve \n{quiz}"
    try:
        text=eval(quiz)
        text="The answer is "+str(text)
        pass
    except Exception as msg:
        text=f"Could not solve \n{quiz}\nError: {msg}"
        pass
    return text

def wikiSummary():
    pass

def imageSearch():
    pass























# Dictionary Section

data = json.load(open('data2.json'))
mylist=[]
for word in data:
    mylist.append(str(word))

def load_word(dict_word):
    key=dict_word

    key=str(key).lower()
    if key in data:
        key[0].upper()+key[1:]
        return data[key]
    elif key.title() in data:
        return data[key.title()]
    elif len(difflib.get_close_matches(key, data.keys())) > 0:

        close_key = difflib.get_close_matches(key, data.keys(),n=20)
        listOfCloseWords=[]
        
        for i in range(len(close_key)):
            listOfCloseWords.append(close_key[i])
        listOfCloseWords.append("CLOSEMATCHESONLY")
        return listOfCloseWords
    else:
        return "Was Not found"

def dictSearch(dict_word):
    HTMLTEXT=''
    # result = list(load_word().split(";"))
    result = load_word(dict_word)
    if type(result) == list:
        if result[-1]!="CLOSEMATCHESONLY":
            num = list(range(1, len(result)+1))
            for item, number in zip(result, num):
                HTMLTEXT+=f"\n{number}.) {item}"
                pass
            return "Definition of "+dict_word+"\n"+HTMLTEXT
        else:
            return "Definition of \""+dict_word+"\""+" was not found,\nclose matches were found though, "+", ".join(result[0:-1])
    else:
        return "Definition of "+dict_word+" Was Not found"
    pass

def newsFeed():
    pass

def launchApps():
    pass

def playMusic():
    pass

def machineStats():
    pass

def whoIs():
    pass

def personalQuestions(quiz,entry_field,GLOBALHEIGHT,CANVAS):
    quiz=str(quiz).lower()
    text="I didn't get that. Please rephrase"
    if(quiz=='date' or quiz=='time') or (('what is' in quiz) and ('date' in quiz or 'time' in quiz)):
        text=f"The current time and date {str(datetime.now()).split('.')[0]}"
    if('launch notepad' in quiz or 'open notepad' in quiz):
        text='Opening notepad'
        threading.Thread(target=lambda: os.system('notepad')).start()
    if('launch calculator' in quiz or 'open calculator' in quiz):
        text='Opening Calculator'
        threading.Thread(target=lambda: os.system('calc')).start()
    if(quiz.startswith('calculate') or quiz.startswith('math') or quiz.startswith('solve')):
        quiz=quiz.replace('calculate','').replace('math','').replace('solve','').strip()
        text=f"Trying to solve\n{quiz}"
        text+="\n"+str(solveMath(quiz))
    if('what is' in quiz and 'in words' in quiz or quiz[0].isdigit() and ('to words' in quiz or 'in words' in quiz)):
        try:
            num=int(quiz.replace('what is','').replace('in words','').replace('to words',''))
            text=num2words.num2words(number=num,lang='en-US')
            text=f"{num} converted to words makes:-\n\n"+text
        except:
            text="Error converting to words.\nPlease reformat the question."
    if('i thought you were smart' in quiz or 'are you this stupid' in quiz or 'you are so dumb' in quiz):
        text="What's with the attitude man! cut me some slack, I'm a robot, I learn with experience"
    if('who are you' in quiz or 'what is your name' in quiz or 'who created you' in quiz or 'why made you' in quiz):
        text="I'm your personal assistant, I was created by My Dad Calvine M. Azenga, a Software Engineer based in Kenya. He named me Soberano-after his crush Lizzy Soberano.\nPS: Thanks dad... \n muscalazems@gmail.com\n\t+254700666848"
        pass
    if('fuck you' in quiz or 'go fuck yourself' in quiz or 'my ass' in quiz or 'my foot' in quiz):
        text="Call me a bitch one more time! Motherfucker I'm gonna woop your snooty ass!"
    
    # Dictionary words
    
    if(quiz.startswith('define ')):
        dict_word=quiz.replace("define ",'').strip()
        meaning=dictSearch(dict_word)
        text=meaning
    if(quiz.startswith('definition of ')):
        dict_word=quiz.replace("definition of ",'').strip()
        meaning=dictSearch(dict_word)
        text=meaning
    if(quiz.startswith('translate') or quiz.startswith('translation')):
        text='Wait while we translate'

    if(quiz.startswith('pronunciation of')):
        text=f"The phrase is pronounced as, {quiz.replace('pronunciation of','')}"
    
    return text
