from django.db import models
from django.contrib.auth import get_user_model

User= get_user_model()
options =(('published','Published'),('draft','Draft'),)
class Posts(models.Model):
    
    author =models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content =models.CharField(max_length=240)
    status = models.CharField(max_length=10,choices=options,default='Published')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    

    def __str__(self) -> str:
        return self.title
