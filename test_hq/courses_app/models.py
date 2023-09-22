from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)

    class Meta:
        ordering = ['owner']
        verbose_name_plural = "Продукт"

    def str(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    video_link = models.URLField()
    duration = models.IntegerField()
    products = models.ManyToManyField(Product)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Уроки"

    def str(self):
        return self.name


class View(models.Model):
    def status_view(self):
        if self.view_time > self.lesson.duration * 1.8:
            return 'Да', 'Просмотрено'
        else:
            return 'Нет', 'Не просмотрено'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    view_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, default=status_view)

    class Meta:
        ordering = ['-view_time']
        verbose_name_plural = "Просмотры"

    def str(self):
        return self.lesson
