from django.db import models
import uuid
# Create your models here.

def generate_unique_code():
    code = str(uuid.uuid4())[:8]  # Generate UUID and take first 8 characters
    return code


class Url(models.Model):
    code = models.CharField(max_length=8, unique=True, default=generate_unique_code)
    url = models.TextField(max_length=200 , blank=False)
    num_visits = models.DecimalField(decimal_places=0  ,max_digits=4, default=0)
    createdAT = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.url}"