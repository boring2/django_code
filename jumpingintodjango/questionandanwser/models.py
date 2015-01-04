from django.db import models
from django.utils import timezone

# Create your models here
class Question(models.Model):
	subject = models.CharField(max_length=100)
	description = models.TextField()
	#pub_date = models.DateTimeField()
	pub_date = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.subject
	
	def was_published_today(self):
		return self.pub_date.date() == timezone.now().date()
class Anwser(models.Model):
	question = models.ForeignKey(Question)
	content = models.TextField()
	best_anwser = models.BooleanField('is best answer?',default=False)

	def __unicode__(self):
		return self.content

