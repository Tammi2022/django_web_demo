from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views
from .views import IndexLearnLogsView,ListLearnLogsView,DetailsLearnLogsView

urlpatterns = [
    # path('bc', csrf_exempt(ExportBCOrderView.as_view())),
    path('index', csrf_exempt(IndexLearnLogsView.as_view())),
    path('topics', csrf_exempt(ListLearnLogsView.as_view())),
    path('topics/<int:id>', csrf_exempt(DetailsLearnLogsView.as_view())),
]