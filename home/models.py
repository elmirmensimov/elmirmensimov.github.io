from django.contrib.auth.models import User
from django.db import models

ORDERSTATUS = ((1, "Beklemede"), (2, "Gönderildi"), (3, "Yolda"), (4, "Teslim Edildi"))

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.TextField(default='{"objects": []}', null=True, blank=True)
    total = models.CharField(max_length=100, null=True, blank=True)
    status = models.IntegerField(choices=ORDERSTATUS, default=1)
    created = models.DateTimeField(auto_now_add=True)
