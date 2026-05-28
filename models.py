from django.db import models
from django.contrib.auth.models import User


class Report(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='reports/')
    description = models.TextField()

    latitude = models.CharField(max_length=100, blank=True)
    longitude = models.CharField(max_length=100, blank=True)

    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('In Progress', 'In Progress'),
            ('Resolved', 'Resolved')
        ],
        default='Pending'
    )

    severity = models.CharField(
        max_length=20,
        choices=[
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('High', 'High'),
            ('Critical', 'Critical')
        ],
        default='Low'
    )

    created_at = models.DateTimeField(auto_now_add=True)


class OTP(models.Model):

    email = models.EmailField()

    otp = models.CharField(max_length=6)

    created_at = models.DateTimeField(auto_now_add=True)