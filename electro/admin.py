from django.contrib import admin
from electro.models import customer_request,customer_message,subscriber,technician,Profile,review
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User,Group

# Register your models here.

admin.site.unregister(Group)
admin.site.register(customer_request)
admin.site.register(customer_message)
admin.site.register(technician)
admin.site.register(subscriber)
admin.site.register(Profile)
admin.site.register(review)


# class AccountInline(admin.StackedInline):
#     model=Profile
#     can_delete=False
#     verbose_name_plural='Profiles'

# class CustomizedUserAdmin(UserAdmin):
#     inlines=(AccountInline, )

# admin.site.unregister(User)
# admin.site.register(User, CustomizedUserAdmin)

