from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', 
                                on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)


class PlanType(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    display_name = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name
   # type = models.CharField(max_length=20, null=True, blank=True)

class Plan(models.Model):
    type = models.ForeignKey(PlanType, related_name='plantype', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True, blank=True)
    price = models.FloatField(max_length=10, null=True, blank=True)

    
    def __str__(self):
        return self.name
