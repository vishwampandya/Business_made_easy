from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
    #return HttpResponse("This is the home page")

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")