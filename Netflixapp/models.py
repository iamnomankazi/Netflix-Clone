from django.db import models

# Create your models here.
class netflix_titles(models.Model):
    Type = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    Release_year = models.IntegerField()
    Category = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='product_img', blank=True)
    
    def __str__(self):
        return self.Title
    

class Signup(models.Model):
    CustomerUsername = models.CharField(max_length=100)
    CustomerPassword = models.CharField(max_length=32)
    CustomerEmail = models.EmailField(blank=True)
    MembershipChoice = (
            ('Silver', 'Silver'),
            ('Gold', 'Gold'),
            ('Diamond', 'Diamond')
            )   
    MembershipType = models.CharField(max_length=20, choices=MembershipChoice)
    Member = models.BooleanField(blank=True)
    
    def __str__(self):
        return self.CustomerUsername
    

class MembershipEmail(models.Model):
    clientemail = models.EmailField()
    
    def __str__(self):
        self.clientemail