from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.template.loader import render_to_string
from .models import User
from django.contrib import messages
import os
from django.core.mail import send_mail, BadHeaderError
from personalSite import settings


# Create your views here.
def CarRentalIndexView(request):
    return render(request, 'carRental/CarRental_index.html', {})


def CreateNewUser(*args):
    new_user = User(first_name=args[0], last_name=args[1],
                    email=args[2], password=args[3], SSN=args[4],
                    Car_License_Number=args[5], Picture_For_Car_License_Number=args[6])
    new_user.save()


def signupView(request):
    if request.method == 'POST':
        sign_up_form = request.POST
        first_name = sign_up_form['fname']
        last_name = sign_up_form['lname']
        email = sign_up_form['email']
        password = sign_up_form['pwd']
        SSN = sign_up_form['SSN']
        Car_License_Number = sign_up_form['carNumber']
        # check if the user is customer not driver..
        if Car_License_Number != '':
            Picture_For_Car_License_Number = request.FILES['picCarNumber']
            pathForLicImg = default_storage.save('CarRental/static/carRental/img/licImg/'+str(
                Picture_For_Car_License_Number.name), ContentFile(Picture_For_Car_License_Number.read()))
        else:
            pathForLicImg = ''
        try:  # check if the SSN/email is duplicate..
            CreateNewUser(first_name, last_name, email, password,
                          SSN, Car_License_Number, pathForLicImg)
            return render(request, 'carRental/welcome_page.html', {
                'User_name': first_name + ' ' + last_name,
            })
        except Exception:
            # delete any saved image if any problem occurred..
            if pathForLicImg != '':
                os.remove(r'CarRental/static/carRental/img/licImg/'+str(
                    Picture_For_Car_License_Number.name))
            messages.add_message(request, messages.ERROR,
                                 'Check Your Inputs Again!!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def checkUserInfo(email, password):
    try:
        usr = User.objects.get(email=email, password=password)
        return [usr.first_name, usr.last_name]
    except Exception:
        return None


def logInView(request):
    if request.method == 'POST':
        login_form = request.POST
        email = login_form['email']
        password = login_form['pwd']
        if checkUserInfo(email, password) != None:
            first_name, last_name = checkUserInfo(email, password)
            return render(request, 'carRental/welcome_page.html', {
                'User_name': first_name + ' ' + last_name,
            })
        else:
            messages.add_message(request, messages.ERROR,
                                 'Check Your Inputs Again!!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def check_if_email_exist(email):
    try:
        usr = User.objects.get(email=email)
        return [usr.first_name, usr.email]
    except Exception:
        return None


def send_email_to_reset(email):
    subject = "Password Reset Requested"
    email_template_name = "carRental/password/password_reset_email.txt"
    tags_in_mail = {
        'domain': '127.0.0.1:8000',
        'protocol': 'http',
    }
    sent_email_content = render_to_string(email_template_name, tags_in_mail)
    try:
        send_mail(subject, sent_email_content, settings.EMAIL_HOST_USER,
                  [email], fail_silently=False)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')


def password_reset_request(request):
    if request.method == "POST":
        reset_email_form = request.POST
        email = reset_email_form['email']
        if check_if_email_exist(email) != None:
            first_name, request.session['email'] = check_if_email_exist(email)
            send_email_to_reset(request.session['email'])
            return render(request, 'carRental/password/password_reset_done.html', {
                'user_first_name': first_name,
            })
        else:
            messages.add_message(request, messages.ERROR,
                                 'Email not found!!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return render(request, 'carRental/password/password_reset.html')


def password_reset_confirm(request):
    if request.method == 'POST':
        new_password = request.POST['confrmnewpwd']
        try:
            usr = User.objects.get(email=request.session['email'])
            usr.password = new_password
            usr.save()
            del request.session['email'] # to make the reset email link one-time available 
            request.session.modified = True
            return render(request, 'carRental/password/password_reset_complete.html')
        except Exception:
            return HttpResponse('Invalid URL..!')
    else:
        return render(request, 'carRental/password/password_reset_confirm.html')
