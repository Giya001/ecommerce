from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,related_name='subcategories',blank=True,null=True)

    def __str__(self):
        if self.parent:
            return f'{self.name}:{self.parent}'
        else:
            return f'{self.name}'
