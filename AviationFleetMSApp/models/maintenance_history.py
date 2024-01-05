from django.db import models
from .aircraft import Aircraft
from .asset import Asset


class MaintenanceHistory(models.Model):
    maintenance_types = (
        ('Routine', 'Routine'),
        ('Major', 'Major'),
        # Add more types as needed
    )

    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    maintenance_type = models.CharField(max_length=20, choices=maintenance_types)
    maintenance_date = models.DateField()
    description = models.TextField()

    permissions = [
        ('view_maintenancehistory_avmfs', 'Can view maintenance history'),
        ('add_maintenancehistory_avmfs', 'Can add maintenance history'),
        ('edit_maintenancehistory_avmfs', 'Can edit maintenance history'),
        ('delete_maintenancehistory_avmfs', 'Can delete maintenance history'),
        # Add more permissions as needed
    ]


# add cost field to MaintenanceHistory model
