from django.shortcuts import render

# Create your views here.
def blog(request):
     image_url = "static/images/land-3.jpg"
     return render(request,'blog.html',{'image_url': image_url})


def readMore1(request):
     return render(request,"cultural-tourism.html")


def readMore2(request):
     return render(request,"eco-tourism.html")

def readMore3(request):
     return render(request,"leisure-tourism.html")

def readMore4(request):
     return render(request,"religious-tourism.html")