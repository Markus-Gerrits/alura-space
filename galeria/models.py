from django.db import models
from datetime import datetime

class Phothography(models.Model):
    
    CATEGORY_OPTIONS = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]
    
    name = models.CharField(max_length=100, null=False, blank=False)
    legend = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY_OPTIONS, default='')
    description = models.TextField(null=False, blank=False)
    photo = models.CharField(max_length=150, null=False, blank=False)
    published = models.BooleanField(default=False)
    phothography_date = models.DateTimeField(default=datetime.now, blank=False)
    
    def __str__(self):
        return f"Photography [name={self.name}]"