from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

from django.shortcuts import redirect

# class PreventAdminLoginMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.user.is_superuser and not request.path.startswith('/admin/'):
#             return redirect('/admin/')
#         response = self.get_response(request)
#         return response


class CustomSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            settings.SESSION_COOKIE_NAME = settings.ADMIN_SESSION_COOKIE_NAME
        else:
            settings.SESSION_COOKIE_NAME = 'main_sessionid'
        response = self.get_response(request)
        if request.path.startswith('/admin/'):
            settings.SESSION_COOKIE_NAME = settings.ADMIN_SESSION_COOKIE_NAME
        else:
            settings.SESSION_COOKIE_NAME = 'main_sessionid'
        return response

class DisableAdminLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path.startswith('/admin/login/') and request.user.is_superuser:
            return redirect('/admin/')  # توجيه المشرفين إلى صفحة رئيسية أو أي صفحة أخرى
        return response
    

class DisableAdminLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path.startswith('/admin/logout/') and request.user.is_superuser:
            return redirect('/admin/')  # توجيه المشرفين إلى صفحة رئيسية أو أي صفحة أخرى
        return response