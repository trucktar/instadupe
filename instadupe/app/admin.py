from django.contrib import admin

from instadupe.app.models import Comment, Image, Like, Profile

admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Like)
admin.site.register(Comment)
