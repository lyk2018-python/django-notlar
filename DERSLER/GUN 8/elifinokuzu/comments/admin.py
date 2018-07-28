from django.contrib import admin
from .models import Comment_To_Node, Comment_To_Edge


admin.site.register(Comment_To_Node)
admin.site.register(Comment_To_Edge)