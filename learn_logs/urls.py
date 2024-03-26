from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import IndexTopicLearnLogsView, ListTopicLearnLogsView, DetailsTopicLearnLogsView, NewTopicLearnLogsView, \
    NewEntryLearnLogsView, DetailsEntryLearnLogsView

urlpatterns = [
    # path('bc', csrf_exempt(ExportBCOrderView.as_view())),
    path('index', csrf_exempt(IndexTopicLearnLogsView.as_view()), name='learn_logs_index'),
    path('topics', csrf_exempt(ListTopicLearnLogsView.as_view()), name='learn_logs_topics'),
    path('topics/<int:topic_id>', csrf_exempt(DetailsTopicLearnLogsView.as_view()), name='learn_logs_topic_details'),
    path('topics/new', csrf_exempt(NewTopicLearnLogsView.as_view()), name='learn_logs_topic_new'),
    path('entries/new/<int:topic_id>', csrf_exempt(NewEntryLearnLogsView.as_view()), name='learn_logs_entry_new'),
    path('entries/<int:entry_id>', csrf_exempt(DetailsEntryLearnLogsView.as_view()), name='learn_logs_entry_details'),
]
