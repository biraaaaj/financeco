from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.

# class LoanTakenQuerySet(model.QuerySet):
#     def getLoanTaken(client_id):
#         return self.filter(
#             models.Q(published=True) & models.Q(showcase=True)
#         )
#
# class LoanPaidQuerySet(model.QuerySet):
#     def getLoanPaid(client_id):
#         return self.filter(
#             models.Q(published=True) & models.Q(showcase=True)
#         )

class LoanTaken(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_amt = models.IntegerField()
    interest_rate = models.IntegerField()
    loan_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.client.first_name} {self.client.last_name} {self.loan_amt}"


class LoanPaid(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.IntegerField()
    payment_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.payment} {self.payment_date}"
