from django.contrib import admin

from learn_logs.models import Topic, Entry

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)