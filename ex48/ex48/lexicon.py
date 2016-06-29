directions = ['north','south','east','west','down','up','left','right','back']
verbs = ['go','stop','kill','eat']
stop = ['the','in','of','from','at','it']
nouns = ['door','bear','princess','cabinet']

def Split_words(stuff):
    words = stuff.split()
    lis = []
    for word in words:
        if word in directions:
            stmt = ('direction',str(word))
            lis.append(stmt)
        elif word in verbs:
            stmt = ('verb',str(word))
            lis.append(stmt)
        elif word in stop:
            stmt = ('stop',str(word))
            lis.append(stmt)
        elif word in nouns:
            stmt = ('noun',str(word))
            lis.append(stmt)
        elif word.isdigit():
            stmt = ('number',str(word))
            lis.append(stmt)
        else:
            stmt = (str(word),'Token Error')
            lis.append(stmt)
    return lis
