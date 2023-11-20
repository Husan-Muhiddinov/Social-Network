from django.contrib import admin
from .models import Post, Notification, Action
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['body']


admin.site.register([Action, Notification])