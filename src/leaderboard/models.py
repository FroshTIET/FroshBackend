from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Score(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="score")
    wh_score_space = models.IntegerField(default=0)
    wh_score_murder = models.IntegerField(default=0)
    wh_score_vexed = models.IntegerField(default=0)

    game_of_wits_score = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)

    wh_level = models.IntegerField(default=1000000)

    def __str__(self):
        return self.user.username + "'s score"

    def get_wh_level(self, story):
        if story == 1:
            return self.wh_level % 100
        elif story == 2:
            return int((self.wh_level % 10000 - self.wh_level % 100) / 100)
        elif story == 3:
            return int((self.wh_level % 1000000 - self.wh_level % 10000) / 10000)

    def inc_wh_level(self, story):
        if story == 1:
            self.wh_level += 1
        elif story == 2:
            self.wh_level += 100
        elif story == 3:
            self.wh_level += 10000
        
        self.save()

    def save(self, *args, **kwargs):
        self.total_score = (
            self.wh_score_space
            + self.wh_score_murder
            + self.wh_score_vexed
            + self.game_of_wits_score
        )
        super(Score, self).save(*args, **kwargs)
