from django.shortcuts import render
from basic_app import views

def index(request):
    context_dict = {'text':'Hello World','number':1000}
    return render(request,'basic_app/index.html',context_dict)


def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
