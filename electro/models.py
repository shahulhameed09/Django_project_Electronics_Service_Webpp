from django.db import models
from django.contrib.auth.models import User
# Create your models here.

request_type=(
    ("--PLEASE CHOOSE A SERVICE--","--Please choose a service--"),
    ("laptop","LAPTOP"),
    ("tv","TV"),
    ("smart phone","SMART PHONE"),
    ("wifi","WIFI"),
    ("ac","AC"),
)

class customer_request(models.Model):
    customer_name=models.CharField(max_length=25)
    email_ID=models.EmailField()
    phone_number=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    pin_code=models.CharField(max_length=12)
    request_Type=models.CharField(max_length=50, choices=request_type, default=" ")
    description=models.TextField()
    date=models.DateField()
    connect=models.ForeignKey(User,default=None, on_delete=models.CASCADE, null=True)
    cdate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name

class customer_message(models.Model):
    name=models.CharField(max_length=25)
    email_ID=models.EmailField()
    phone_number=models.CharField(max_length=10)
    subject=models.CharField(max_length=30)
    message=models.TextField()
    author=models.ForeignKey(User,default=None, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default="profile_pics/default.png", upload_to="profile_pics")
                          
    def __str__(self):
        return f'{self.user.username} Profile'

class subscriber(models.Model):
    email_ID = models.EmailField()

    def __str__(self):
        return self.email_ID

class technician(models.Model):
    name=models.CharField(max_length=20)
    Date_Of_Birth=models.CharField(max_length=10,default="")
    phone_number=models.CharField(max_length=10)
    email_ID=models.EmailField()
    address=models.TextField()

    def __str__(self):
        return self.name

class review(models.Model):
    review_message=models.TextField()
    boss=models.ForeignKey(User,default=None, on_delete=models.CASCADE, null=True)

    # def __str__(self):
    #     return self.boss.first_name

