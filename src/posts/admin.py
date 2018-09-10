# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
# Register your models here.
from .models import Post #relative import from post's model

#documentation : model Admin

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "timestamp", "updated"]
	list_display_links = ["updated"]
	list_editable = ["title"]
	list_filter = ["timestamp", "updated"]
	search_fields = ["title", "content"]
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)


