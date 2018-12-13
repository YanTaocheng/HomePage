from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from home import forms
 
def index(request):
    if request.method == 'POST':# 当提交表单时
     
        form = forms.AddForm(request.POST) # form 包含提交的数据
         
        if form.is_valid():# 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
     
    else:# 当正常访问时
        form = forms.AddForm()
        name = "ytc"
    return render(request, 'home.html', {'form': form, 'name':name})

def next(request):
    count = 0
    if request.method == 'POST':
        count += 1
        
        if count == 1:
            welcome = "welcome to next!--1"
            return render(request, 'next.html', {'welcome':welcome})
        elif count == 2:
            welcome = "welcome to next!--2"
            return render(request, 'next.html', {'welcome':welcome})
        else:
            welcome = "welcome to next!--x"
            return render(request, 'next.html', {'welcome':welcome})
        
    return render(request, 'next.html')