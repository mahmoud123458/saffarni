from django.shortcuts import render

# Create your views here.
def blog(request):
     image_url = "static/images/land-3.jpg"
     return render(request,'blog.html',{'image_url': image_url})

