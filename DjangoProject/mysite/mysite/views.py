from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def removepunc(request):
    text = request.POST.get('text', "default")
    rem = request.POST.get('opt', 'off')
    #print(rem)
    prams = {
        'analyzed_text':text,
        'rem_val':rem
    }
    return render(request, 'rempunc.html', prams)

def capfirst(request):
    return HttpResponse("cap first <a href='/'>home</a>")

def custom_404(request, exceptions):
    return render(request, 'error404.html', status=404)