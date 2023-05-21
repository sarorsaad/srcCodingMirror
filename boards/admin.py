from django.contrib import admin
from .models import Board, Topic, Post

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('subject', 'board', 'created_by', 'created_dt')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('message', 'topic', 'created_by', 'created_dt')
