from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(req):
    content= '<html><body><h1><i>Hello World</i></h1></body></html>'
    
    return HttpResponse(content)

def home(request):
    return render(request,
                  'index.html',
                  {'user':'Naveen Gupta'})    