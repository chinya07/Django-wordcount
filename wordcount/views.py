from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext1=request.GET['fulltext1']
    fulltext2=request.GET['fulltext2']
    wordlist1=fulltext1.split(' ')
    wordlist2=fulltext2.split(' ')
    from difflib import SequenceMatcher
    similarity_ratio = SequenceMatcher(None, wordlist1, wordlist2).ratio()
    # count=0
    # for word in wordlist1:
    #     if word in wordlist2:
    #         count+=1

    # worddic = {}
    #
    # for word in wordlist:
    #     if word in worddic:
    #         #increase
    #         worddic[word] += 1
    #     else:
    #         #  add to worddic
    #         worddic[word] = 1
        #sortedwords=sorted(worddic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext1':fulltext1, 'fulltext2':fulltext2, 'count':similarity_ratio})

def about(request):
    return render(request, 'about.html')
