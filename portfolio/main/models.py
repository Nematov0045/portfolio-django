from django.db import models

# Create your models here.

class SendMessage(models.Model):
    email = models.CharField(max_length=255)
    phone_number= models.CharField(max_length=255)
    message = models.TextField()
    send_at = models.DateTimeField(auto_now_add=True)


    