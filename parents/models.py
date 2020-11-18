from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.conf import settings
from django.utils import timezone
import random



class Parent(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/ParentProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=True)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" "+self.user.last_name
# Create your models here.



def generate_pk():
    number = random.randint(10, 99)
    return 'CID{}{}'.format(timezone.now().strftime('%d'), number)


class Child(models.Model):
    date_of_birth=models.DateField( auto_now=False, auto_now_add=False, blank=False)
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    age=models.CharField(max_length=40)
    parent=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    child_id=models.CharField(default=generate_pk, primary_key=True, max_length=255, unique=True)

    class Meta:
        verbose_name_plural="Children"

    def __str__(self):
        return self.parent.username
