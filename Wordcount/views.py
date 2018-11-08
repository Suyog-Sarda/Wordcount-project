from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    s = {'`','~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','[','}',']','|','\\',':',';','"','\'','<',
        ',','>','.','?','/',' ','0','1','2','3','4','5','6','7','8','9'}
    t = ''
    wordlist = []
    for el in fulltext:
        if el in s:
            if len(t) > 0:
                wordlist.append(t)
                t = ''
        else:
            t += el
    if len(t) > 0:
        wordlist.append(t)
    n = len(wordlist)
    wordCount = dict()
    for word in wordlist:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    sortedWordCount = sorted(wordCount.items(), key = lambda x:x[1], reverse=True)
    return render(request, 'count.html',{'fulltext':fulltext,'count':n, 'sortedwordcount':sortedWordCount})

def about(request):
    return render(request, 'about.html')
