from django.contrib import admin

from .models import User, Loan_taken, Loan_paid

# Register your models here.
# admin.site.register(Client)
# admin.site.register(Loan_taken)
# admin.site.register(Loan_paid)

@admin.register(Loan_taken)
class LoanTakenAdmin(admin.ModelAdmin):
    list_display = ('client','loan_amt', 'interest_rate', 'loan_date')

@admin.register(Loan_paid)
class LoanPaidAdmin(admin.ModelAdmin):
    list_display = ('client', 'payment', 'payment_date')
