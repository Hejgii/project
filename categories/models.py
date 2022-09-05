from django.db import models


class Category(models.Model):
    
    name = models.CharField(max_length=255, null=False, unique=True)
    #slug = models.SlugField(max_length=255)
    # is_active = models.BooleanField(default=True)
    class Meta:
        
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
        return '/%s/' % (self.slug)    

