from django.contrib import admin
from .models import *

# Register your models here.

class DetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'payment_receiver', 'payment_amount', 'mode_of_payment', 'transaction_id']
admin.site.register(Detail, DetailAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['fname', 'email', 'phone', 'massage']
admin.site.register(Contact, ContactAdmin)