# models.py
from django.db import models

class Payment(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_description = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=50, default='Pending')
    mpesa_receipt_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount}"

class UserPhoneNumber(models.Model):
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.phone_number
