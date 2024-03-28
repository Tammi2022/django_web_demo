from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View


# Create your views here.
class UserLoginView(View):
    def get(self, request):
        form = AuthenticationForm(request.POST)
        context = {'form': form}
        return render(request, 'users_login.html', context)

    def post(self, request):
        form = AuthenticationForm(request.POST)
        print(form)
        if form.is_valid():
            username = form.username
            password = form.password
            print(username, password)
            try:
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect(reverse('learn_logs_index'))  # 重定向到登录成功后的页面
            except Exception as e:
                print(e)
                return HttpResponseRedirect(reverse('learn_logs_index'))  # 重定向到登录成功后的页面
        return HttpResponseRedirect(reverse('learn_logs_index'))  # 重定向到登录成功后的页面


class UserLogoutView(View):
    def get(self, request):
        logout(request)  # 注销用户
        return HttpResponseRedirect(reverse('users_login'))


class UserRegisterView(View):
    def get(self, request):
        # 显示空的注册表单
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'users_register.html', context)

    def post(self, request):
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重定向到主页
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
        return HttpResponseRedirect(reverse('learn_logs_index'))
