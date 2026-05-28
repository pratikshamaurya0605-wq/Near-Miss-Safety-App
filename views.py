from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# -----------------------
# LOGIN VIEW
# -----------------------
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import OTP
import random
from django.core.mail import send_mail
from django.conf import settings


def login_view(request):

    form = AuthenticationForm()
    error = None

    if request.method == "POST":

        # SEND OTP
        if "send_otp" in request.POST:

            email = request.POST.get("email")

            if email:

                otp = str(random.randint(100000, 999999))

                OTP.objects.create(email=email, otp=otp)

                send_mail(
                    "Login OTP - Safety Reporting System",
                    f"Your OTP is {otp}",
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )

                request.session["otp_email"] = email

            else:
                error = "Please enter your email"


        # VERIFY OTP
        elif "verify_otp" in request.POST:

            email = request.session.get("otp_email")
            entered_otp = request.POST.get("otp")

            otp_obj = OTP.objects.filter(email=email).last()

            if otp_obj and entered_otp == otp_obj.otp:

                user, created = User.objects.get_or_create(
                    username=email,
                    email=email
                )

                login(request, user)

                return redirect("report_list")

            else:
                error = "Invalid OTP"

    return render(request, "login.html", {
        "form": form,
        "error": error
    })


# -----------------------
# REPORT LIST
# -----------------------
@login_required
def report_list(request):
    return HttpResponse("Report list working")


# -----------------------
# CREATE REPORT
# -----------------------
@login_required
def create_report(request):
    return HttpResponse("Create report working")