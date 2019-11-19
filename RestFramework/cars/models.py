from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

CAR_TYPES = (
    (1, 'Седан'),
    (2, 'Хэчбек'),
    (3, 'Универсал'),
    (4, 'Купе'),
)

class Car(models.Model):
    vin = models.CharField(verbose_name="Vin", db_index=True, max_length=64)
    color = models.CharField(verbose_name="Color", max_length=64)
    brand = models.CharField(verbose_name="Brand", max_length=64)
    car_type = models.IntegerField(verbose_name='Car_Type', choices=CAR_TYPES)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)