from django.db import models
import datetime

class Users(models.Model):
	username = models.CharField(max_length=25)
	password = models.CharField(max_length=100)
	email = models.CharField(max_length=150)
	registered = models.DateTimeField('date registered')
	def __unicode__(self):
		return u"%s, %s" % (self.username, self.email)
