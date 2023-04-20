from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.validators import FileExtensionValidator

from .helpers import ImageHashPath, ALLOWED_IMAGE_EXTENSIONS


# Create your models here.

class User(AbstractUser):
    class Meta:
        db_table = 'user'
        ordering = ['username']

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    id = models.AutoField(primary_key=True)
    username_validator = ASCIIUsernameValidator()
    profile_pic = models.ImageField(upload_to=ImageHashPath, blank=True, null=True,
                                    validators=[FileExtensionValidator(allowed_extensions=ALLOWED_IMAGE_EXTENSIONS)])
    username = models.CharField(max_length=150, unique=True, validators=[username_validator])
    email = models.EmailField(max_length=255, unique=True)
    groups = models.ManyToManyField('auth.Group', related_name="user_groups", blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name="user_perms", blank=True)







