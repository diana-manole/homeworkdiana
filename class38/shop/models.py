from django.db import models

# Create your models here.

class Category(models.Model):
    name =models.CharField(max_length=200,db_index=True)
    slug =models.CharField(max_length=200,db_index=True,unique=True)
    
    class Meta:
        ordering =('name',)
        verbose_name='categorii'
        verbose_name_plural ='categorii'
    
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category=name =models.ForeignKey(Category,related_name='products',on_delete=models.DO_NOTHING)
    name =models.CharField(max_length=200,db_index=True)
    slug =models.CharField(max_length=200,db_index=True,unique=True)
    image=models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    available=models.BooleanField()
    created=models.DateTimeField(auto_now_add=True)
    updared=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering =('name',)
        index_together=(('id','slug'),)

    
    def __str__(self) -> str:
        return self.name