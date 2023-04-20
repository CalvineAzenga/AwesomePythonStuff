import itertools
file=open('./wordlist_en_US.dic','r')
data=str(file.read()).lower().split('\n')
file.close()
def jumbleSolve(entry,text,length):
    wordslist=[]
    wordd=entry.get().strip()
    letters=[letter for letter in wordd]
    a=0
    b=0
    try:
        for s in itertools.permutations(letters,r=int(length)):
            value=""
            for k in s:
                value+=k
            if(str(value).lower() in data):
                if(str(value).lower().capitalize() in wordslist):
                    pass
                else:
                    wordslist.append(str(value.lower()).capitalize())
                    text.delete("0.0","end")
                    text.insert("0.0",'\t'.join([word for word in wordslist]))
                    b+=1
            a+=1
        txt=f"{b} words found after {a} iterations"
        return wordslist,txt
    except:
        pass