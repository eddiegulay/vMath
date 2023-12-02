from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    voice_prompt = models.FileField(upload_to='voice_prompts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    explanation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

"""
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Vote(models.Model):
    VOTE_TYPES = [
        ('Upvote', 'Upvote'),
        ('Downvote', 'Downvote'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=10, choices=VOTE_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
"""