from django.db import models
from .user import CustomUser


class Communication(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')
    message_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('Read', 'Read'),
        ('Unread', 'Unread'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    class Meta:
        permissions = [
            ('view_communication_avmfs', 'Can view communication'),
            ('add_communication_avmfs', 'Can add communication'),
            ('edit_communication_avmfs', 'Can edit communication'),
            ('delete_communication_avmfs', 'Can delete communication'),
            # Add more permissions as needed
        ]
