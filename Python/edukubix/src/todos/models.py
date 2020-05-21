from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model() 

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.CharField(max_length=500, null=False,blank=False,
                            help_text="This field is required")
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)