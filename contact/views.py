from django.conf import settings
from django.shortcuts import render, redirect
from .models import Info
from django.core.mail import send_mail
from django.contrib.auth.views import redirect_to_login

# Create your views here.
def contact(request):
    myinfo = Info.objects.first()
    myinfo2 = Info.objects.last()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path())

        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,  # from
            [email],  # to
            fail_silently=False,
        )

    return render(request, 'contact.html', {'myinfo': myinfo, 'myinfo2': myinfo2})
