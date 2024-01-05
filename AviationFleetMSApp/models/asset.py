from django.db import models
from .aircraft import Aircraft


STATUS_CHOICES = Aircraft.STATUS_CHOICES


class Asset(models.Model):
    TYPES = (
        ('Engine', 'Engine'),
        ('Avionics', 'Avionics'),
        # Add more types as needed
    )

    type = models.CharField(max_length=20, choices=TYPES)
    manufacturer = models.CharField(max_length=255)
    installation_date = models.DateField()
    last_maintenance_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    class Meta:
        permissions = [
            ('view_asset_avmfs', 'Can view asset'),
            ('edit_asset_avmfs', 'Can edit asset'),
            ('add_asset_avmfs', 'Can add asset'),
            ('delete_asset_avmfs', 'Can delete asset'),
            # Add more permissions as needed
        ]
