from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name ="Название")
    class Meta:
        verbose_name = "Приложение"
        verbose_name_plural ="Приложения"

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=50, verbose_name="название")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description = models.CharField(max_length=200, verbose_name="Описание")
    image = models.ImageField(upload_to = "images", verbose_name="Картинка")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    active = models.BooleanField(default=True, verbose_name="Активна")
    count = models.IntegerField(verbose_name="Количество")

    class Meta:
        verbose_name = "товар"
        verbose_name_plural ="товары"

    def __str__(self):
        return self.name