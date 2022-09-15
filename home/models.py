from django.db import models

# Create your models here.

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    city = models.CharField(max_length=70, default="")
    zip = models.CharField(max_length=70, default="")
    state = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    ven = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
