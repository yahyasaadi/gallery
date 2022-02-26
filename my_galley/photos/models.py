from django.db import models

# Create your models here.
class Location(models.Model):
    img_location = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.img_location}'


class Category(models.Model):
    img_category = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.img_category}'


class Photo(models.Model):
    img = models.ImageField(upload_to='images')
    img_name = models.CharField(max_length=50)
    img_description = models.CharField(max_length=150)
    img_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    img_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.img_name}, {self.img_category}, {self.img_location}'
