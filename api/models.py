from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='product', blank = True, null=True )
    date = models.DateField()
    
    def __str__(self):
        return f" {self.title}"