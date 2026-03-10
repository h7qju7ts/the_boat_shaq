from decimal import Decimal

from django.db import models
from profiles.models import UserProfile
from boats.models import Boat

# Create your models here.

class Order(models.Model):
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders"
    )
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    street_address1 = models.CharField(max_length=255)
    street_address2 = models.CharField(max_length=255, blank=True)
    town_or_city = models.CharField(max_length=100)
    county = models.CharField(max_length=100, blank=True)
    postcode = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))

    def __str__(self):
        return f"Order {self.id}"
    
    def update_total(self):
        self.order_total = sum(item.lineitem_total for item in self.lineitems.all())
        self.save()


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="lineitems"
    )      
    boat = models.ForeignKey(
        Boat,
        on_delete=models.CASCADE
    )  
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.boat.name} on order {self.order.id}"
    
    @property
    def lineitem_total(self):
        if self.boat.price:
            return self.boat.price * self.quantity
        return Decimal("0.00")