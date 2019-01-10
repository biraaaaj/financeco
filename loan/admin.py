from django.contrib import admin

from .models import User, LoanTaken, LoanPaid

# Register your models here.
# admin.site.register(Client)
# admin.site.register(Loan_taken)
# admin.site.register(Loan_paid)

@admin.register(LoanTaken)
class LoanTakenAdmin(admin.ModelAdmin):
    list_display = ('client','loan_amt', 'interest_rate', 'loan_date')

@admin.register(LoanPaid)
class LoanPaidAdmin(admin.ModelAdmin):
    list_display = ('client', 'payment', 'payment_date')
