# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Post
from .forms import PostForm

# Create your views here.
# CRUD methods, done via http calls through views
# Create --POST -- make New
# Retrieve -- GET -- List/Search
# Update -- PUT/PATCH -- Edit
# Delete -- Delete -- Delete


def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None) # Ensures the validation for mandatory fields 
	# request.FILE calls in file/image data if its there.
	if form.is_valid():
		instance = form.save(commit=False)
		# print form.cleaned_data.get("title")
		instance.save()
		messages.success(request, "Successfully Created!")
		return HttpResponseRedirect(instance.get_absolute_url())
	# if request.method == "POST":
	# 	print request.POST.get("content")

	context = {
		"form" : form

	}
	return render(request, "post_form.html", context)

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": "Detail",
		"instance" : instance
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	queryset_list = Post.objects.all() #.order_by("-timestamp")
	paginator = Paginator(queryset_list, 4) # Show 4 posts per page
	page_request_var = 'page'
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    contacts = paginator.page(paginator.num_pages)
	context = {
		"object_list" : queryset,
		"title" : "List",
		"page_request_var" : page_request_var
	}
	# if request.user.is_authenticated():
	# 	context = {
	# 		"title": "My user list"
	# 	}
	# else:
	# 	context = {
	# 		"title": "List"
	# 	}
	return render(request, "post_list.html", context)
	#return HttpResponse("<h1>List!!</h1>")


def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance) 
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#''>Item </a> Saved!", extra_tags="html_safe") #added extra tag, could be seen while inspect element
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title": instance.title,
		"instance" : instance,
		"form": form
	}
	return render(request, "post_form.html", context)

def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Item Deleted!")

	return redirect("posts:list")
