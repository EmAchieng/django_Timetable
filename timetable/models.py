from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
#many-to-many relationship




from django.db import models
from django.utils import timezone
from django.forms import ModelForm

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    credits = models.IntegerField(max_length=18)
    choice = models.CharField(max_length=7)
    coursecode =models.IntegerField(max_length=9)
    monday = models.CharField(max_length=1)
    tuesday = models.CharField(max_length=1)
    wednesday = models.CharField(max_length=2)
    thursday = models.CharField(max_length=2)
    friday = models.CharField(max_length=1)




    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



from django.contrib.auth.models import User


class UserProfile(models.Model):
        # This field is required.
        user = models.OneToOneField(User)
        # These fields are optional
        website = models.URLField(blank=True)
        picture = models.ImageField(upload_to='imgs', blank=True)

        def __unicode__(self):
                return self.user.username



from django.forms import ModelForm

class UserForm(forms.ModelForm):
        class Meta:
                model = User
                fields = ["username", "email", "password"]

class UserProfileForm(forms.ModelForm):
        class Meta:
                model = UserProfile

