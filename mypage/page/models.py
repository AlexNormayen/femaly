from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 30, unique = True)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Good(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    description  = models.TextField()
    in_stock = models.BooleanField(default = True, db_index = True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    price = models.PositiveIntegerField()
    
    class Meta:
        ordering = ["-price", "name"]
        unique_together = ("category", "name", "price")
        verbose_name = "товар"
        verbose_name_plural = "товары"
    
    
    
    def __str__(self):
        s = self.name
        if not self.in_stock:
            s = s + " (нет в наличии) "
        return s
    
        
