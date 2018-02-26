from django.db import models

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=22)
    description = models.CharField(max_length=2500)



class Question(models.Model):
    story = models.ForeignKey(Story, related_name='questions', on_delete=models.CASCADE) #Story
    prompt = models.CharField(max_length=500)  # Scenario


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=2500)
    nextQuestion = models.IntegerField(blank=True)  # This is just questionID
    anim = models.CharField(max_length=4)
    damage = models.IntegerField()
