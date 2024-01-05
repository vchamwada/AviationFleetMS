from django.db import models
from .aircraft import Aircraft


class CarbonEmissions(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    emission_date = models.DateField()
    emission_value = models.FloatField()
    emission_source = models.CharField(max_length=255)

    class Meta:
        permissions = [
            ('view_carbonemissions_avmfs', 'Can view carbon emissions'),
            ('add_carbonemissions_avmfs', 'Can add carbon emissions'),
            ('edit_carbonemissions_avmfs', 'Can edit carbon emissions'),
            ('delete_carbonemissions_avmfs', 'Can delete carbon emissions'),
            # Add more permissions as needed
        ]
