from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import IndexLearnLogsView

urlpatterns = [
    # path('bc', csrf_exempt(ExportBCOrderView.as_view())),
    path('index', csrf_exempt(IndexLearnLogsView.as_view())),
]