from django.conf import settings
from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail

# Create your views here.
def contact(request):
     myinfo=Info.objects.first()  
     myinfo2=Info.objects.last()

     if request.method=='POST':
          subject= request.POST['subject']
          email=request.POST['email']
          message=request.POST['message']

          send_mail(
               subject,
               message,
               settings.EMAIL_HOST_USER, #from
               [email],#to
               fail_silently=False,
        )

     return render(request,'contact.html',{'myinfo':myinfo,'myinfo2':myinfo2})