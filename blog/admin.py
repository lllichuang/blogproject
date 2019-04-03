from django.contrib import admin
from .models import Post, Category, Tag
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category']


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)  # 给博客正文添加富文本输入框
        


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
