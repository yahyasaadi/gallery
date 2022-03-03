from django.test import TestCase
from .models import Photo, Location, Category

# Create your tests here.
class TestPhotoModel(TestCase):
    
    def setUp(self):
        self.img_1 = Photo(img='', img_name='Test Image', img_description='Tesing the Photo Model')
        

    def test_instance(self):
        self.assertTrue(isinstance(self.img_1))


    def test_save_image(self):
        self.img_1.save_image()
        imgs = Photo.objects.all()
        self.assertTrue(len(imgs)>0)


class TestLocationModel(TestCase):
    pass

class TestCategoryModel(TestCase):
    pass