from django.db import models

# Create your models here.

class Client(model.Models):
    cl_id = models.CharField(max_length = 3)
    name = models.CharField(max_length = 64)

class Loan_taken(model.Models):
    loan_amt = models.IntegerField()
    interest_rate = models.IntegerField(max_length = 2)
    loan_date = models
