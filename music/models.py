from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Mz_Post(models.Model):
	mz_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	mz_title = models.CharField(max_length=200)
	mz_text = models.TextField()
	mz_created_date = models.DateTimeField(default=timezone.now)
	mz_published_date = models.DateTimeField(blank=True, null=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.mz_title