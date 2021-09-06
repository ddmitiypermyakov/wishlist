from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=120, verbose_name='Наименование')
    link=models.URLField()
    price=models.IntegerField(verbose_name='Цена')
    create_at=models.DateTimeField(auto_created=True)


    def __str__(self):
        return self.title
