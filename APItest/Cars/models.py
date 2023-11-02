from django.db import models

# Create your models here.

class Car(models.Model):
    id = models.BigAutoField(primary_key=True)
    brands = models.ForeignKey('Brand', on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brands} - {self.cat}"

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
    
class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)