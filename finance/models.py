from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()

TYPE = ((1, "income"), (2, "expense"))
STATUS = ((0, "Not Paid"), (1, "Paid"), (2, "Void"))

# Create your models here.


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="transaction")
    type = models.IntegerField(choices=TYPE)
    amount = models.FloatField()
    note = models.CharField(max_length=180)
    created_on = models.DateField(auto_now_add=True)
    property = models.ForeignKey('properties.Property', on_delete=models.CASCADE, related_name="transactions")
    status = models.IntegerField(choices=STATUS, default=0)
    overdue_fee = models.FloatField(default=0)
    transaction_month = models.DateField(null=True, blank=True, default=None)
    due_date = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return f"Invoice ID: {self.transaction_id} Status: {self.status} Name: {self.user.first_name} {self.user.last_name}"