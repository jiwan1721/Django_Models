from django.db import models
class Person_many(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Group(models.Model):
    name = models.CharField(max_length=60)
    members = models.ManyToManyField(Person_many, through= 'Membership')
    def __str__(self):
        return self.name
class Membership(models.Model):
    person= models.ForeignKey(Person_many, on_delete=models.CASCADE)
    group= models.ForeignKey(Group, on_delete= models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=79)
    def __str__(self):
        return self.invite_reason
class ox(models.Model):
    horn_length = models.IntegerField()
    class meta:
        ordering = ["horn_length"]
        verbos_name_plural = "oxen"
        
class Baby(models.Model):
    first_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    def baby_bommer_status(self):
        "returns the persons baby bomer status"
        import datetime
        print("--------------------------------------------------------------------")
        print(type(self.birth_date))
        if self.birth_date < datetime.date(1990, 1, 1):
            return "pre-boomer"
        elif self.birth_date < datetime.date(2000, 1, 1):
            return "baby bommer"
        else:
            return "post-bommer"
    @property
    def full_name(self):
        "return persons full name"
        return '%s %s' %(self.first_name,self.Last_name)
    
#overriding pre-defined model methods
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    def save(self,*args,**kwargs):
        if self.name == "its jiwans blog":
            return
        else:
            super().save(*args,**kwargs)
# class Base(models.Model):
#     m2m = models.ManyToManyField(
#         OtherModel,
#         related_name="%(app_label)s_%(class)s_related",
#         related_query_name="%(app_label)s_%(class)ss",
#     )
#     class Meta:
#         abstract= True
# class ChildA(Base):
#     pass

# class ChildB(Base):
#   pass
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class unmanaged(models.Model):
    class Meta:
        abstract = True
        managed = False
        

class Student(CommonInfo,unmanaged):
    home_group = models.CharField(max_length=5)
    class Meta(CommonInfo.Meta,unmanaged.Meta):
        #db_table= 'student_info'
        pass
        
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    def __str__(self):
        return self.name


class Resturant(Place):
    serves_hotdogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
    def __str__(self):
        return self.address

class Person_OnceMore(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
class NewManager(models.Manager):
    # ...
    pass

class MyPerson_again(Person_OnceMore):
    objects = NewManager()

    class Meta:
        proxy = True
class MyPerson(Person_OnceMore):
    class Meta:
        proxy = True

    def do_something(self):
        # ...
        pass

class OrderedPerson(Person_OnceMore):
    class Meta:
        ordering = ["last_name"]
        proxy = True
