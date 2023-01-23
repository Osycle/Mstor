from distutils.command.upload import upload
from wsgiref.validate import validator
from django.db import models
from django.core.validators import FileExtensionValidator
from base.services import *

class AuthUser(models.Model):
  """ Модель пользователя на платформе
  """
  email = models.EmailField(max_length=150, unique=True)
  join_date = models.DateTimeField(auto_now_add=True)
  country = models.CharField(max_length=30, blank=True, null=True)
  city = models.CharField(max_length=30, blank=True, null=True)
  bio = models.TextField(max_length=2000, blank=True, null=True)
  display_name = models.CharField(max_length=30, blank=True, null=True)
  avatar = models.ImageField(
    upload_to=get_path_upload_avatar,
    blank=True,
    null=True,
    validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_image]
  )

  def is_authenticated(self):
    """ Всегда возвращает True. Это способ узнать, был ли пользователь аутентифицирован
    """
    return True

  def __str__(self):
    return self.email