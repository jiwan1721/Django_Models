from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
        ('S','Small'),
        ('M', 'Medium'),
        ('L','Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size= models.CharField(max_length=1,choices=SHIRT_SIZES)
    def __str__(self):
        return self.name
class Runner(models.Model):
    Medal_Type = models.TextChoices('MedalTytpe','Gold Solver Bronze')
    name_runner = models.CharField(max_length=600)
    medal_choice = models.CharField(blank=True,choices=Medal_Type.choices,max_length=10)
    def __str__(self):
        return self.name_runner,self.medal_choice

class Fruit(models.Model):
    name = models.CharField(max_length=25, primary_key=True)
    def __str__(self):
        return self.name
class VerbosExample(models.Model):
    first_name = models.CharField("person's first name", max_length=50) # here verbos name is Persns first name
    first_name_again = models.CharField(max_length=30) #here vaerbos name is first_name_again
    fruit = models.ForeignKey(Fruit, on_delete= models.CASCADE, verbose_name= "the related name")
    runner = models.OneToOneField(Runner, on_delete= models.CASCADE, verbose_name="runner ups")
    def __str__(self):
        return self.first_name,self.fruit,self.runner
class ManyToManyField_Test(models.Model):
    verbosexamples = models.ManyToManyField(VerbosExample)
    def __str__(self):
        return self.verbosexamples
    