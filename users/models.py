from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    birth_day = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    current_password = models.CharField(blank=True, null=True, verbose_name='Текущий пароль')
    new_password = models.CharField(blank=True, null=True, verbose_name='Новый пароль')
    
    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
    
    def __str__(self):
        return self.username
    
