from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import customer_request, customer_message, Profile, review
from django.forms import ModelForm

class register(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class update_profile(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class profile_pic_update(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        
class bookForm(ModelForm):
    class Meta:
        model = customer_request
        fields = ['customer_name','email_ID','phone_number','address','city','state','pin_code','request_Type','description','date']

class message(ModelForm):
    class Meta:
        model = customer_message
        fields = ['name','email_ID','phone_number','subject','message']

class c_reviews(ModelForm):
    class Meta:
        model = review
        fields = ['review_message']
