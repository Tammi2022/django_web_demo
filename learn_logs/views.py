from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from learn_logs.models import Topic
from utils.auth import auth
from utils.obj_response import ObjectResp

# Create your views here.
'''
class ExportLearnLogsView(View):
    # @auth.http_command
    def get(self, request):
        # store_hash = request.META['user_information'].get('store_hash', None)
        # if not store_hash:
        #     return JsonResponse(ObjectResp.value_of(code=400, message='Authentication failed'))
        return JsonResponse(ObjectResp.value_of())'''


class IndexLearnLogsView(View):
    def get(self, request):
        return render(request, 'learn_logs_index.html')


# def index(request):
#     """学习笔记的主页"""
#     # return render(request, 'learning_logs/index.html')
#     return render(request, 'learn_logs_index.html')

class ListLearnLogsView(View):
    def get(self, request):
        # 显示所有的主题
        # topics = Topic.objects.all()
        topics = Topic.objects.order_by('date_added')
        context = {'topics': topics}
        return render(request, 'learn_logs_topics.html', context)