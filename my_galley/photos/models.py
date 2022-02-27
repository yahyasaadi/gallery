from django.db import models

# Create your models here.
class Location(models.Model):
    img_location = models.CharField(max_length=50)


    def save_location(self):
        return self.save()


    def delete_location(self):
        return self.delete()


    def update_location(self, img_location):
        self.img_location = img_location
        return self.save()

    def __str__(self):
        return f'{self.img_location}'


class Category(models.Model):
    img_category = models.CharField(max_length=50)


    def save_category(self):
        return self.save()


    def delete_category(self):
        return self.delete()


    def update_category(self, img_category):
        self.img_category = img_category
        return self.save()

    def __str__(self):
        return f'{self.img_category}'


class Photo(models.Model):
    img = models.ImageField(upload_to='images')
    img_name = models.CharField(max_length=50)
    img_description = models.CharField(max_length=150)
    img_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    img_category = models.ForeignKey(Category, on_delete=models.CASCADE)


    # Methods for the Photo Models
    def save_image(self):
        return self.save()


    def delete_image(self):
        return self.delete()


    def update_image(self, img, img_name, img_description, img_location, img_category):
        self.img = img
        self.img_name = img_name
        self.img_description = img_description
        self.img_location = img_location
        self.img_category = img_category

        return self.save()
    
    @classmethod
    def get_image_by_id(cls, img_id):
        img_objs = cls.objects.get(id = img_id)
        return img_objs


    @classmethod
    def search_image(cls, category):
        by_category = cls.objects.filter(img_category__name = category)
        return by_category

    
    @classmethod
    def filter_by_location(cls, location):
        by_location = cls.objects.filter(img_location__name = location)
        return by_location

    def __str__(self):
        return f'{self.img_name}, {self.img_category}, {self.img_location}'


    # Make migrations for the Db to work
