from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    ROLES = (
        ('Administrator', 'Administrator'),
        ('Fleet Manager', 'Fleet Manager'),
        ('Maintenance Personnel', 'Maintenance Personnel'),
        ('Communication Officer', 'Communication Officer'),
    )

    role = models.CharField(max_length=30, choices=ROLES)

    class Meta:
        permissions = [
            ('view_aircraft_avmfs', 'Can view aircraft'),
            ('edit_aircraft_avmfs', 'Can edit aircraft'),
            ('add_aircraft_avmfs', 'Can add aircraft'),
            ('delete_aircraft_avmfs', 'Can delete aircraft'),
            # Add more permissions as needed
        ]


# resolve the clashes in reverse accessor names between the CustomUser model and the Group and Permission models
CustomUser.groups.field.remote_field.related_name = 'custom_user_groups'
CustomUser.user_permissions.field.remote_field.related_name = 'custom_user_permissions'
