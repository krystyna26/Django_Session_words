from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    print strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return render(request, 'add_word/index.html')

def processing(request):
    if request.method == "POST":
        if not 'inputs' in request.session:
            request.session['inputs'] = []
        else:
            request.session['inputs'] = request.session['inputs']
        temp = {
            'word':request.POST['word'],
            'color':request.POST['color'],
            'font':request.POST['font'], 
            'time':strftime("%H:%M:%S, %B %d, %Y", gmtime())
            }
        request.session['inputs'].append(temp)
    	return redirect("/")
    else:
    	return redirect("/")

def clear(request):
    request.session['inputs'] = []
    return redirect("/")