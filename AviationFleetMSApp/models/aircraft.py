from django.db import models


class Aircraft(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('In Maintenance', 'In Maintenance'),
        ('Retired', 'Retired'),
    )

    model = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    purchase_date = models.DateField()
    last_maintenance_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
