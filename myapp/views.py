from django.shortcuts import render

# Create your views here.


def indepage(request):
    return render(request,"index.html")

def aboutpage(request):
    return  render(request,"aboutus.html")