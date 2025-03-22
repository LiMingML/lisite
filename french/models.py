from django.db import models

# Create your models here.
class Vocabulary(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    review_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.name