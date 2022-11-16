from xml.etree.ElementInclude import include
from electro import views
from django.urls import path, include
from django.contrib import admin
from .views import PasswordsChangeView

admin.site.site_header = "Electro Administrator"
admin.site.site_title = "Welcome to Electro admin"
admin.site.index_title = "Electro Administrator"

urlpatterns = [
path('',views.index,name='home'),
path('reg',views.reg,name='reg'), 
path('logins',views.logins,name='logins'),
path('logoutuser',views.logoutuser,name='logoutuser'),
path('bookings',views.booking,name='bookings'),
path('profile_update',views.profile_update,name='profile_update'),
path('show/<request_ID>',views.show,name='show'),
path('delete_items/<request_ID>',views.delete_items,name='delete_items'),
path('delete_reviews/<id>',views.delete_reviews,name='delete_reviews'),
path('appointment',views.appointment,name='appointment'),
path('subscrib',views.subscrib,name='subscrib'),
path('reviews',views.reviews,name='reviews'),
path('change_password',PasswordsChangeView.as_view(template_name='change_password.html')),
path('myprofile',views.myprofile,name='myprofile'),
path('social-auth/', include('social_django.urls', namespace='socials')),
]