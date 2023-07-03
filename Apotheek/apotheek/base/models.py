from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    city = models.CharField(max_length=50)
    bio = models.TextField()
    date_of_birth = models.DateField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Medicine(models.Model):
    name = models.CharField(max_length=50)
    manufacture = models.CharField(max_length=50)
    cures = models.CharField(max_length=50)
    side_effects = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Collection(models.Model):
    medicine = models.ForeignKey(
        Medicine, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(blank=False,)
    collected = models.BooleanField(default=False)
    collected_approved = models.BooleanField(default=False)
    collected_approved_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='approved_by', null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    

