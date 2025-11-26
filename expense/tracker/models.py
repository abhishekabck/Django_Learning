from django.db import models
import uuid
# Create your models here.
class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Transactions(BaseModel):
    description = models.CharField(max_length=100)
    amount = models.FloatField()

    class Meta:
        ordering = ['description']

