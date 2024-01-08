from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    payment_receiver = models.CharField(max_length=100)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    mode_of_payment = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=100)
    Payment_img = models.ImageField(upload_to='Payment_img/')
    

    def __str__(self):
        return self.payment_receiver

 
class Contact(models.Model):
    fname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    massage = models.TextField()


    def __str__(self):
        return self.fname