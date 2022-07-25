from django.contrib import admin
from .models import ATMLogin, Customer_details,linkedAccounts,transactionHistory
# Register your models here.

admin.site.register(Customer_details)
admin.site.register(ATMLogin)
admin.site.register(linkedAccounts)
admin.site.register(transactionHistory)

