from uuid import uuid4

from django.db import models


# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4)
    username = models.CharField(max_length=32, null=False, unique=True)
    password = models.TextField(null=False)

    @classmethod
    def create_user(cls, username, password):
        return cls.objects.create(
            username=username,
            password=password
        )


class Book(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=64)
    year = models.IntegerField(default=1)
