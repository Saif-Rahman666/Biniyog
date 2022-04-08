from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Member_fee(models.Model):
    fee = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.fee
        
class Auction_User(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=10,null=True)
    image = models.FileField(null=True)
    membership = models.ForeignKey(Member_fee,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.user.username


class Bidder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=10,null=True)
    image = models.FileField(null=True)
    membership = models.ForeignKey(Member_fee,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.user.username