from django.db import models
from django.contrib.auth.models import User # default model provided by django
from django.utils import timezone # used to consider timezone settings
from django.urls import reverse
class Path(models.Model):
    title = models.CharField(max_length=100) #attributes = models.datatype(Constraints)
    Author = models.ForeignKey(User,on_delete=models.CASCADE)
    Book = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    link = models.TextField(default="")
    #img = models.ImageField(default='default.jpg',upload_to='profile_pics')

    #def __str__(self):
     #   return self.title

    #def get_absolute_url(self):
     #   return reverse('post-detail', kwargs={'pk':self.pk})