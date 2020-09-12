from django.db import models

# Create your models here.

class Category(models.Model):
    title =  models.CharField(max_length = 50)
    description =  models.TextField()

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    insert_date = models.DateTimeField(auto_now_add=True, blank=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/upload/')

    def __str__(self):
        return self.title

