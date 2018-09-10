# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
# CRUD methods, done via http calls through views
# Create --POST -- make New
# Retrieve -- GET -- List/Search
# Update -- PUT/PATCH -- Edit
# Delete -- Delete -- Delete


def post_create(request):
	return HttpResponse("<h1>Create!! </h1>")

def post_detail(request):
	context = {
		"title": "Detail"
	}
	return render(request, "index.html", context)

def post_list(request):
	queryset = Post.objects.all()
	context = {
		"object_list" : queryset,
		"title" : "List"
	}
	# if request.user.is_authenticated():
	# 	context = {
	# 		"title": "My user list"
	# 	}
	# else:
	# 	context = {
	# 		"title": "List"
	# 	}
	return render(request, "index.html", context)
	#return HttpResponse("<h1>List!!</h1>")

def post_update(request):
	return HttpResponse("<h1>Update!!</h1>")

def post_delete(request):
	return HttpResponse("<h1>Delete!!</h1>")