from django.contrib.auth import login, get_user_model, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import ToDoForm, UserRegisterForm, UserLoginForm
from .models import *
from .token import account_activation_token


def home(request):
    if request.user.is_authenticated:
        todo_items = ToDo.objects.filter(user=request.user)
        if request.method == 'POST':
            form = ToDoForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                todo = form.save(commit=False)
                todo.user = request.user
                todo.title = title
                todo.save()
        else:
            form = ToDoForm()
        return render(request, 'core/index.html', {'form': form, 'todo_items': todo_items})
    else:
        return redirect('signup')


def update_user_todo(request, todo_id):
    todo = get_object_or_404(ToDo, pk=todo_id, user=request.user)

    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ToDoForm(instance=todo)

    return render(request, 'core/todo_update.html', {'form': form, 'todo': todo})


def delete_user_todo(request, todo_id):
    todo = get_object_or_404(ToDo, pk=todo_id, user=request.user)

    if request.method == 'POST':
        todo.delete()
        return redirect('home')

    return render(request, 'core/todo_delete.html', {'todo': todo})


def confirm(request):
    return render(request, 'core/confirm.html')


def success(request):
    return render(request, 'core/success.html')


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('success')
    else:
        return HttpResponse('Activation link is invalid!')


def signup(request):
    form = UserRegisterForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(request)
        mail_subject = 'Activation link has been sent to your email id'
        message = render_to_string('core/acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return redirect('confirm')
    else:
        form = UserRegisterForm()
    return render(request, 'core/signup.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('home')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'core/signin.html', {'form': form})


class CustomPasswordResetView(PasswordResetView):
    template_name = 'core/custom_reset_password.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'core/custom_password_reset_confirm.html'


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'core/confirm.html'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'core/custom_password_reset_complete.html'

