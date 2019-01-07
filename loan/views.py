from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Loan_taken, Loan_paid


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "loan/login.html", {"message": None})
    user = request.user
    try:
        borrow = Loan_taken.objects.get(client=user.id)
        payment = Loan_paid.objects.get(client=user.id)
    except User.DoesNotExist:
        raise Http404("Client does not exist")
    except Loan_taken.DoesNotExist:
        raise Http404("Client hasn't borrowed any sum of money")
    except Loan_paid.DoesNotExist:
        raise Http404("Client hasn't paid any sum of money")
    context = {
        "user": user,
        "loan_amt": borrow.loan_amt,
        "loan_date": borrow.loan_date,
        "interest_rate": borrow.interest_rate,
        "payment": payment.payment,
        "payment_date": payment.payment_date,
        "remaining": borrow.loan_amt - payment.payment
    }
    # print(context['user'].id)
    return render(request, "loan/user.html", context)


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "loan/login.html", {"message": "Invalid credentials"})


def logout_view(request):
    logout(request)
    return render(request, "loan/login.html", {"message": "Logged out."})


def user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        borrow = Loan_taken.objects.get(client=user_id)
        payment = Loan_paid.objects.get(client=user_id)
    except User.DoesNotExist:
        raise Http404("Client does not exist")
    except Loan_taken.DoesNotExist:
        raise Http404("Client hasn't borrowed any sum of money")
    except Loan_paid.DoesNotExist:
        raise Http404("Client hasn't paid any sum of money")
    context = {
        "user": user,
        "loan_amt": borrow.loan_amt,
        "loan_date": borrow.loan_date,
        "interest_rate": borrow.interest_rate,
        "payment": payment.payment,
        "payment_date": payment.payment_date,
        "remaining": borrow.loan_amt - payment.payment
    }
    print(context)
    return render(request, "loan/user.html", context)
