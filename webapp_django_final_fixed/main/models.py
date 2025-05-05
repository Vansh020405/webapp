from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class SearchData(models.Model):
    location = models.CharField(max_length=100)
    checkin_date = models.CharField(max_length=50)
    checkout_date = models.CharField(max_length=50)
    guests = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.location}"

class Hostel(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField(max_length=500)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    reviews_count = models.IntegerField(default=0)
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    discount_percentage = models.IntegerField(default=0)
    amenities = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s review for {self.hostel.name}"

class Booking(models.Model):
    STATUS_CHOICES = (
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guests = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    special_requests = models.TextField(blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Booking for {self.hostel.name} by {self.user.username}"
        
    def save(self, *args, **kwargs):
        # Calculate total price if not provided
        if not self.total_price and self.hostel and self.check_in_date and self.check_out_date:
            nights = (self.check_out_date - self.check_in_date).days
            self.total_price = float(self.hostel.price_per_night) * nights
        super().save(*args, **kwargs)
