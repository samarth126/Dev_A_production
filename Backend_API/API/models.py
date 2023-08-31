from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.


class CustomUsers(AbstractUser):
    username = None
    Phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    Country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    objects = UserManager()
    REQUIRED_FIELDS = []
# Create your models here.


class TherapistDetail(models.Model):
    user = models.OneToOneField(CustomUsers, on_delete=models.CASCADE)  # Assuming you're using Django's built-in User model
    age = models.PositiveIntegerField()
    work_experience = models.PositiveIntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email
    

class ClientDetail(models.Model):
    user = models.OneToOneField(CustomUsers, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    about_client = models.TextField()

    def __str__(self):
        return self.user.email 


class BusinessUnit(models.Model):
    name_business_unit = models.CharField(max_length=100)
    detail_business_unit = models.TextField()

    def __str__(self):
        return self.name_business_unit
    

class Services(models.Model):
    business_unit = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    name_service = models.CharField(max_length=100)
    is_program = models.BooleanField()
    isactive = models.BooleanField()


    def __str__(self):
        return self.name_service 



class BookingOrder(models.Model):
    therapist_user = models.ForeignKey(CustomUsers, on_delete=models.CASCADE, related_name='therapist_bookings')
    client_user = models.ForeignKey(CustomUsers, on_delete=models.CASCADE, related_name='client_bookings')
    created_at = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    total_sessions_bought = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_status = models.CharField(max_length=100)

    def __str__(self):
        return f"Booking Order #{self.id}" 
    


    
class ClientSubscription(models.Model):
    user = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)
    total_sessions_bought = models.PositiveIntegerField()
    sessions_left = models.PositiveIntegerField()
    isactive = models.BooleanField()
    schedule = models.CharField(max_length=200)
    bookin_id = models.ForeignKey(BookingOrder, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - Subscription"  
    
    

class Transaction(models.Model):
    bank_name = models.CharField(max_length=100)
    txn_amount = models.DecimalField(max_digits=10, decimal_places=2)
    txn_status = models.CharField(max_length=50)
    bank_txn_id = models.CharField(max_length=100)
    booking_order = models.ForeignKey(BookingOrder, on_delete=models.CASCADE)

    def __str__(self):
        return f"Transaction #{self.id}"  
    


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title