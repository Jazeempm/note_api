from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()
# Create your models here.
class Note(models.Model):
    user=models.ForeignKey(UserModel,on_delete=models.CASCADE)
    title= models.CharField(max_length=120)
    content = models.CharField(max_length=120)
    created = models.DateField(auto_now_add=True)

class NotesImage(models.Model):
    note=models.ForeignKey(Note,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='NotesImages')

