from django.utils.text import slugify
from enum import unique
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Banner(models.Model):
    image_one = models.ImageField(upload_to='banner_port')
    def __str__(self):
        return f"Banner {self.id}"
    
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Portfolio(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    short_discription=models.CharField(max_length=250)
    slug=models.SlugField(unique=True,blank=True)
    image_one=models.ImageField(upload_to='portfolio')
    image_two=models.ImageField(upload_to='portfolio/detail')
    image_three=models.ImageField(upload_to='portfolio/detail')
    image_four=models.ImageField(upload_to='portfolio/detail')
    image_five=models.ImageField(upload_to='portfolio/detail')
    client_name=models.CharField(max_length=25)
    start_date=models.DateField(blank=True,null=True)
    asign_to=models.CharField(max_length=30)
    challenge_title=RichTextField()
    story=RichTextField()
    approach=RichTextField()
    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
    