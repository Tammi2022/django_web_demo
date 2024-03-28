from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View


# Create your views here.
class UserLoginView(View):
    def get(self, request):
        return render(request, 'users_login.html')

    def post(self, request):
        return render(request, 'users_login.html')


class UserLogoutView(View):
    def get(self, request):
        logout(request) # 注销用户
        return HttpResponseRedirect(reverse('users_login'))
