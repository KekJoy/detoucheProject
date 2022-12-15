from django.contrib.auth.models import AbstractUser
from django.db import models

class PersonalSecurity(models.Model):
    login = models.CharField(max_length=25, name='Логин')
    password = models.CharField(max_length=25, name='Пароль')
    password_repeat = models.CharField(max_length=25, name='Повторите пароль')

    def __str__(self):
        return self.login

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=25, name='Имя')
    last_name = models.CharField(max_length=25, name='Фамилия')
    patronymic_name = models.CharField(max_length=25, null=True, name='Отчество')
    phone = models.CharField(max_length=100, name='Телефон')
    education_institute = models.CharField(max_length=250, name='ВУЗ')
    education_department = models.CharField(max_length=250, name='Факультет')
    education_profession = models.CharField(max_length=100, name='Специальность')
    education_course = models.CharField(max_length=50, name='Курс')

    def __str__(self):
        return self.first_name

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class PersonalPrograms(models.Model):
    CHOICES = (
        ('Департамент системной интеграции', 'Департамент системной интеграции'),
        ('Безопасная разработка', 'Безопасная разработка'),
        ('Исследовательский центр', 'Исследовательский центр'),
        ('USSC-SOC', 'USSC-SOC'),
        ('ePlat4m разработка', 'ePlat4m разработка'),
        ('DATAPK разработка', 'DATAPK разработка'),
        ('FT-Soft. Серверная, клиентская и мобильная разрабокта', 'FT-Soft. Серверная, клиентская и мобильная разрабокта'),
        ('Технический департамент', 'Технический департамент'),
    )
    program = models.CharField(max_length=100, choices=CHOICES, name='Направление')

    def __str__(self):
        return self.program

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'