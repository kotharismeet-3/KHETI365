import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    sqft = models.DecimalField(max_digits=6, decimal_places=2)
    acre = models.DecimalField(max_digits=4, decimal_places=2)

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)

    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    list_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("listing-detail", kwargs={"pk": self.pk})
