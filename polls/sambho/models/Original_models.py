from django.contrib.auth.models import User
import uuid
from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Quize(models.Model):
    question_area = models.CharField( max_length=200)
    published_date = models.DateTimeField('date published')
    def __str__(self):  # this function  will return the question
        return self.question_area
    def publisher_recently(self):
        return self.published_date>=timezone.now() - datetime.timedelta(days=1)
        
        
    

class Option(models.Model):
    quize = models.ForeignKey(Quize, on_delete=models.CASCADE) # we used foreign key to use calss quize values
    # ForeignKey. That tells Django each Choice is related to a single Question. 
    option_text = models.CharField( max_length=200)
    vote_count = models.IntegerField(default=0)
    def __str__(self): #__str__ is required
        return self.option_text
    
class baseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class meta:
        abstract = True
        
        
class Colors(baseModel):
    color_code = models.CharField(max_length=100)
    def __str__(self):
        return self.color_code
    

class People(baseModel):
    name = models.CharField(max_length=100)
    about = models.TextField()
    age = models.IntegerField()
    email = models.EmailField()
    colors = models.ManyToManyField(Colors)
    def __str__(self):
        return self.name
    
    
class PeopleAddress(baseModel):
    peoples = models.ForeignKey(People, on_delete=models.CASCADE,  related_name= "address")
    address = models.TextField()
    def __str__(self):
        return self.address
    
