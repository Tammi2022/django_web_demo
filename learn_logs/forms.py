from django import forms

from learn_logs.models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        label = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        label = {'text': ''}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80}),
        }  # 定制字段'text'的输入小部件，将文本区域的宽度设置为80列
