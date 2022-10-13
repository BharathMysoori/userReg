from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
products = (
	("Electronics", "Electronics"),
	("Clothing", "Clothing"),
	("Furniture", "Furniture"),
	("Books", "Books"),
	
)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20,choices=products,default='Others')
    contactNo = models.CharField(max_length=18)
    
    firstName = models.CharField(max_length=15,null=True,blank=True)
    surname = models.CharField(max_length=15,null=True,blank=True)
    userpic = models.ImageField(upload_to='profile_image/',null=True,blank=True,default='profile_image/default.png')

    def __str__(self):
    	return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance,created, **kwargs):
    if created==False:
        instance.customer.save()
        print('save-user_profile')