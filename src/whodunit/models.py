from django.db import models

# Create your models here.

CONTENT_TYPES = [
    ('Video', 'Video'),
    ('Image', 'Image'),
    ('dynamicJS', 'dynamicJS'),
]

class Question(models.Model):
    question_text = models.TextField(default="")
    level = models.IntegerField(default=0)
    content_link = models.CharField(max_length=300, blank=True, null=True, default="")
    content_type = models.CharField(max_length=100, choices=CONTENT_TYPES, blank=True, null=True, default="")

    answer_field = models.TextField(default="")

    current_points = models.IntegerField(default=100)
    
    point_decrement = models.IntegerField(default=5)
    minimum_points = models.IntegerField(default=60)

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.question_text

    def reduce_points(self, value=5):
        if self.current_points > self.minimum_points:
            self.current_points -= self.point_decrement

    def switch_state(self):
        self.active = not self.active

