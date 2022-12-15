# from django.db import models
#
# class Task_text(models.Model):
#     title = models.CharField('Задание', max_length=50)
#     task = models.TextField('Описание')
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Задача'
#         verbose_name_plural = 'Задачи'
#
# class Task_check(models.Model):
#     title = models.CharField('Задание', max_length= 250)
#     topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Задача'
#         verbose_name_plural = 'Задачи'
#
# class Topic(models.Model):
#     title = models.CharField('Название', max_length= 50)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Направление'
#         verbose_name_plural = 'Направления'