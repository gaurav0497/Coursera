# I had created that file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):

    removepunc= request.POST.get('removepunc','off')
    charcount = request.POST.get('charcount','off')
    text= request.POST.get('text','default')
    analyzed = ""
    purpose=""
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        purpose = "Removed punctuations"
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char

    if charcount == "on":
        analyzed=str(len(text))
        purpose="Length of string"  
    params={'purpose':purpose,'analyzed_text':analyzed}
    return render(request,'analyze.html',params)

def capfirst(request):
    return HttpResponse("<button>Capitalise First</button>")

def newline(request):
    return HttpResponse("<button>New Line</button>")

def charcount(request):
    return HttpResponse("<button>character count</button>")

#python manage.py runserver