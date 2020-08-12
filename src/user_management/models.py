from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import uuid

# Create your models here.


BRANCH_CHOICES = [
    "Biomedical Engineering (BME)",
    "Biotechnology (BT)",
    "Chemical Engineering (CHE)",
    "Civil Engineering (CIE)",
    "Computer Science and Business systems (COBS)",
    "Computer Engineering (COE)",
    "Computer Science & Engineering (Patiala Campus) (COPC)",
    "Computer Science & Engineering (Derabassi Campus) (COSE)",
    "Electronics & Communication Engineering (ECE)",
    "Electrical and Computer Engineering (ELC)",
    "Electronics (Instrumentation & Control) Engineering (EIC)",
    "Electrical Engineering (ELE)",
    "Electronics and Computer Engineering (ENC)",
    "Mechatronics (MEC)",
    "Mechanical Engineering (MEE)",
    "Mechanical Engineering (Production) (MPE)",
    "Dual-Degree BE-MBA (Electronics & Communication Engineering) (BEMBA-ECE)",
    "Dual-Degree BE-MBA (Mechanical Engineering) (BEMBA-MEE)",
    "Not Applicable",
]

BRANCH_CHOICES = [(x, x) for x in BRANCH_CHOICES]

GENDER = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Non Binary", "Non Binary"),
    ("NIL", "Prefer Not Say"),
]


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    rollNumber = models.CharField(max_length=100, default="")
    fullName = models.CharField(max_length=150, default="")
    branch = models.CharField(
        max_length=150, choices=BRANCH_CHOICES, default="Not Applicable"
    )
    gender = models.CharField(choices=GENDER, default="NIL", max_length=100)
    birthday = models.DateField(blank=True, null=True)
    points = models.IntegerField(default=0)

    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return self.user.username
