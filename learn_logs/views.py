from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from learn_logs.forms import TopicForm, EntryForm
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


class IndexTopicLearnLogsView(View):
    def get(self, request):
        return render(request, 'learn_logs_index.html')


# def index(request):
#     """学习笔记的主页"""
#     # return render(request, 'learning_logs/index.html')
#     return render(request, 'learn_logs_index.html')

class ListTopicLearnLogsView(View):
    def get(self, request):
        # 显示所有的主题
        # topics = Topic.objects.all()
        topics = Topic.objects.order_by('date_added')
        context = {'topics': topics}
        return render(request, 'learn_logs_topics.html', context)


class DetailsTopicLearnLogsView(View):
    def get(self, request, topic_id):
        topic = Topic.objects.get(id=topic_id)
        entries = topic.entry_set.order_by('-date_added')
        context = {'topic': topic, 'entries': entries}
        return render(request, 'learn_logs_topic_details.html', context)


class NewTopicLearnLogsView(View):
    def get(self, request):
        form = TopicForm()  # 未提交数据：创建一个新表单
        context = {'form': form}
        return render(request, 'learn_logs_topic_new.html', context)

    def post(self, request):
        form = TopicForm(request.POST)  # POST提交的数据，对数据进行处理
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learn_logs_topics'))


class NewEntryLearnLogsView(View):
    def get(self, request, topic_id):
        topic = Topic.objects.get(id=topic_id)
        # 在特定的主题中添加新条目
        form = EntryForm()
        context = {'topic': topic, 'form': form}
        return render(request, 'learn_logs_entry_new.html', context)

    def post(self, request, topic_id):
        topic = Topic.objects.get(id=topic_id)
        form = EntryForm(request.POST)  # POST提交的数据，对数据进行处理
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
        return HttpResponseRedirect(reverse('learn_logs_topic_details', args=[topic_id]))
