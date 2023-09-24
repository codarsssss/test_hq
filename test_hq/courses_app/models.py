from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['owner']
        verbose_name_plural = "Продукт"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    video_link = models.URLField()
    duration = models.IntegerField()
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name


class View(models.Model):
    STATUS_CHOICES = [
        ('not viewed', 'Не просмотрено'),
        ('viewed', 'Просмотрено'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    view_time = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='not viewed')

    class Meta:
        ordering = ['-view_time']
        verbose_name_plural = "Просмотры"

    def __str__(self):
        return str(self.lesson)

    def status_view(self):
        if self.view_time >= self.lesson.duration * 0.8:
            return 'viewed'
        else:
            return 'not viewed'
