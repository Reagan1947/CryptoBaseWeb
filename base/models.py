from django.db import models


# Create your models here.
class Authentic(models.Model):
    user_id = models.IntegerField(default=1)
    user_fake_id = models.IntegerField(default=1)
    pair_key = models.IntegerField(default=1)


class Authentic2(models.Model):
    user_id = models.IntegerField(default=1)
    user_fake_id = models.IntegerField(default=1)
    pair_key = models.IntegerField(default=1)

    class Meta:
        app_label = 'service_02'


class BaseInformation(models.Model):
    service_id = models.IntegerField(default=1)
    service_key = models.TextField(max_length=20000)
    tpk = models.TextField()
    mk = models.TextField()

    class Meta:
        app_label = 'service_01'


class BaseInformation2(models.Model):
    service_id = models.IntegerField(default=1)
    service_key = models.TextField(max_length=20000)
    tpk = models.TextField()
    mk = models.TextField()

    class Meta:
        app_label = 'service_02'
