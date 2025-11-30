from django.db import models

# Create your models here.

class Hood(models.Model):
    name =models.CharField(max_length=2048)
    
    
    def __str__(self):
        return self.name

class Gym(models.Model):
    
    class RatingChoices(models.IntegerChoices):
        STAR1 = 1, "One Star"
        STAR2 = 2, "Two Stars"
        STAR3 = 3, "Three Stars"
        STAR4 = 4, "Four Stars"
        STAR5 = 5, "Five Stars"

    name =models.CharField(max_length=2048)
    image =models.ImageField(upload_to="images/")
    hood =models.ManyToManyField(Hood)
    has_coach=models.BooleanField(default=True)
    about =models.TextField()
    rating =models.SmallIntegerField(choices=RatingChoices.choices)

