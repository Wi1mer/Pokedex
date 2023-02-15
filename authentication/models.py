from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

#  Hacemos que el email en la bd sea unico
class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    # pass
    # add additional fields in here

    def __str__(self):
        return self.username