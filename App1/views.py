from django.shortcuts import render

# Create your views here.
def First(request):
    return render(request,'First.html')

def Papu(request):
    return render(request,'S2nd.html')