from django.db import models


# Create your models here.
class Topic(models.Model):
    # 用户学习的主题
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # 返回模型的字符串表示
        return self.text


class Entry(models.Model):
    # 学到的有关某个主题的具体知识
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    # 在 Django 中，on_delete 参数可以填写以下选项来指定外键关联对象被删除时的处理方式：
    # models.CASCADE: 当关联的对象被删除时，与之相关联的对象也会被级联删除。
    # models.PROTECT: 如果还有对象和当前对象存在关联，就不允许删除当前对象。
    # models.SET_NULL: 当关联的对象被删除时，与之相关联的字段会被设置为 null（前提是该字段允许为 null）。
    # models.SET_DEFAULT: 当关联的对象被删除时，与之相关联的字段会被设置为默认值。
    # models.SET(): 当关联的对象被删除时，与之相关联的字段会被设置为指定的值。
    # models.DO_NOTHING: 什么也不做，数据库完全交给用户自己去处理。
    # 这些选项允许你根据具体情况来定义外键字段在关联对象被删除时的行为，以确保数据的完整性和一致性。
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        # 返回模型的字符串表示
        return self.text[:50] + '...'
