from django.db import models
from customers.models import Customer



class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PRODUCTION', 'In Prouction'),
        ('COMPLETE', 'Complete'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
        ('NO_PAPERWORK', 'No Paper Work'),
        ('CONFIRMATION', 'Confirmation'),
    ]
    kitchen_or_bedroom = [
        ('KITCHEN', 'Kitchen'),
        ('BEDROOM', 'Bedroom'),
    ]
    
    job_name = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    kitchen_or_bedroom = models.CharField(max_length=50, choices=kitchen_or_bedroom, default='KITCHEN')
    cabs = models.IntegerField(default=0)
    robes = models.IntegerField(default=0)
    panels = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.job_name} ({self.status})"

    
class OrderAttachment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='order_attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
