from django.shortcuts import render

# Create your views here.
def page2(request):
    return render(request,'page2.html')
def page1(request):
    return render(request,'page1.html')
def page4(request):
    return render(request,'page4.html')