# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# CRUD methods, done via http calls through views
# Create --POST -- make New
# Retrieve -- GET -- List/Search
# Update -- PUT/PATCH -- Edit
# Delete -- Delete -- Delete


def post_create(request):
	return HttpResponse("<h1>Create!! </h1>")

def post_detail(request):
	return HttpResponse("<h1>Detail!!</h1>")

def post_list(request):
	return render(request, "index.html", {})
	#return HttpResponse("<h1>List!!</h1>")

def post_update(request):
	return HttpResponse("<h1>Update!!</h1>")

def post_delete(request):
	return HttpResponse("<h1>Delete!!</h1>")