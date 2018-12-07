from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __repr__(self):
        return "<Blog object: {} {} {} {}>".format(self.first_name, self.last_name, self.email,self.age)
