from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    

        # is_staff = models.BooleanField('Is theatre staff', default=False)
        # is_customer = models.BooleanField('Is customer', default=False)
    # is_superuser = models.BooleanField('Is Superuser',default=False)
    # TH_STAFF = 1
    # USER = 0
    
    # ROLE_CHOICES = (
    #     (TH_STAFF, 'Theatre Staff'),
    #     (USER, 'Normal User'),
    # )
    email = models.EmailField("Email Address",unique=True,max_length=255, blank=True, null=True)
    # role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=USER)

# class User(AbstractUser):
#     is_admin= models.BooleanField('Is admin', default=False)
#     is_customer = models.BooleanField('Is customer', default=False)
#     is_employee = models.BooleanField('Is employee', default=False)