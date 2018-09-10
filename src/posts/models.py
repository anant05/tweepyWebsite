# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
#MVC MODEL VIEW CONTROLLER

class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField() # by default bigger than charfield
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True) # when post updated, database would be updated.
	updated = models.DateTimeField(auto_now=True, auto_now_add=False) # when post is added in the database timestamp would be saved

	def __unicode__(self):
		return self.title

	# In Python 3, we only define __str__
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={'id': self.id})
		# return "/posts/{}/".format(self.id)