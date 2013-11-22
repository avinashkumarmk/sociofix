from django.db import models

# Create your models here.
class Issues(models.Model):
	issue_name = models.CharField(max_length=200)
	location   = models.CharField(max_length=100)

	def __unicode__(self):
		return self.location


