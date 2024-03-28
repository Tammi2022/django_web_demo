from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from users.views import UserLoginView, UserLogoutView

urlpatterns = [
    # path('bc', csrf_exempt(ExportBCOrderView.as_view())),
    path('login', csrf_exempt(UserLoginView.as_view()), name='users_login'),
    path('logout', csrf_exempt(UserLogoutView.as_view()), name='users_logout'),
    ]
