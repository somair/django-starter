from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    accountNum = models.CharField(max_length=50, blank = True, default='')

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

#profile created automatically when referenced
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)
