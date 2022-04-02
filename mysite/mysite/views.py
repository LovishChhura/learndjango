#I have created this file: Lovish
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcounter = request.POST.get('charcounter','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps=="on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Full Caps', 'analyzed_text': analyzed}
        djtext=analyzed


    if(extraspaceremover=="on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed extraspace', 'analyzed_text': analyzed}
        djtext=analyzed

    if(newlineremover=="on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
        params = {'purpose': 'Removed extraspace', 'analyzed_text': analyzed}
        djtext=analyzed

    if charcounter == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        length=0
        for char in djtext:
            if char not in punctuations:
                length=length+1
                analyzed = analyzed + char
        params = {'purpose': 'Char Counter', 'analyzed_text': length}
        djtext=analyzed

    if (removepunc!='on' and charcounter!='on' and fullcaps!='on' and extraspaceremover!='on' and newlineremover!='on'):
        return HttpResponse('''Error''')

    return render(request, 'analyze.html', params)