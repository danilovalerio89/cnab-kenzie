import uuid

from django.core.validators import MaxValueValidator
from django.db import models


class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    type = models.CharField(max_length=1)
    date = models.DateField()
    value = models.CharField(validators=[MaxValueValidator(9999999999)])
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField()
    store_owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)
