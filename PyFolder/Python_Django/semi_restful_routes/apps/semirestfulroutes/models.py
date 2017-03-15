from __future__ import unicode_literals
from django.db import models

class ProductManager(models.Manager):
    def newprod(self, info):
        Product.objects.create(name=info['name'], description=info['description'], price=info['price'])
        return {'msg':'You have created a product!'}

    def updateprod(self, info, id):
        update = Product.objects.get(id=id)
        update.name = info['name']
        print update.name
        update.description = info['description']
        update.price = info['price']
        update.save()
        return {'msg' : 'Your product has been updated!'}

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = ProductManager()
