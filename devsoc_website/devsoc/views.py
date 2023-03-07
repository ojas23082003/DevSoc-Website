from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import *
from .forms import *
from django.conf import settings

# Create your views here.

def home(request):
    # a = model.objects.all()
    team = Team.objects.all()
    form = ContactForm()
    # print(team)
    # exec = []
    # foh = []
    # oh = []
    # dh = []
    # for each in team:
    #     if(each.title.name == "Executive Head"):
    #         exec.append(each)
    #     elif(each.title == "Finance & Operations Head"):
    #         foh.append(each)
    #     elif(each.title == "Outreach Head"):
    #         oh.append(each)
    #     elif(each.title == "Development Head"):
    #         dh.append(each)
    # faq = FAQ.objects.all()
    # print(exec)
    return render(request, 'index.html', { 'team':team, 'form':form})

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def forum(request):
    return render(request, 'forum.html')

def noticeboard(request):
    notices = Notice.objects.filter(display=True)
    images = NoticeImage.objects.all()
    # for notice in notices:
    #     image = NoticeImage.objects.filter(topic=notice.topic)
    #     img = [image]
    #     images.append(img)
    # print(len(images))
    return render(request, 'noticeboard.html', {'notices':notices, 'images':images})

def resources(request):
    return render(request, 'resources.html')

def contact(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        form.save()
        # subject = str(form.cleaned_data.get('subject'))
        # message = str(form.cleaned_data.get('message'))
        # send_mail(subject, message, settings.EMAIL_HOST_USER, ['ojas.modak23@kgpian.iitkgp.ac.in'],fail_silently=False)
        # subject = request.POST.get('subject')
        # message = request.POST.get('message')
        # from_email = request.POST.get('email')
        # send_mail(subject, message, from_email, ['ojas.modak23@gmail.com'])
    return redirect("/")