from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from user_management.models import Student
from leaderboard.models import Score


@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)
        Score.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_student_profile(sender, instance, **kwargs):
    instance.profile.save()
    instance.score.save()


