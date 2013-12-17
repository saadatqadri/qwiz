from django.db import models

# Create your models here.


class Qwiz(models.Model):
	pass

class Question(models.Model):
	text = models.TextField()
	qwiz = models.ForeignKey(Qwiz)

