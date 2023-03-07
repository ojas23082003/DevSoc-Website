from django.db import models

# Create your models here.

class model(models.Model):
    topic = models.CharField(max_length=250)

    def __str__(self):
        return (self.topic)

class Status(models.Model):
    status = models.CharField(max_length=250)

    def __str__(self):
        return (self.status)
    
class Portfolio(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return (self.name)

class Team(models.Model):
    name = models.CharField(max_length=250)
    title = models.ForeignKey(Portfolio, on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    fbLink = models.URLField(null=True, blank=True)
    emailLink = models.URLField(null=True, blank=True)
    linkedinLink = models.URLField(null=True, blank=True)

    def __str__(self):
        return (self.name)

class ContactUs(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    subject = models.TextField(null=True, blank=True)
    message = models.TextField()
    viewed = models.BooleanField(default=False, null=True, blank=True)
    status = models.ForeignKey(Status,on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return (self.name)

class NoticeTopic(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return (self.name)

class Notice(models.Model):
    topic = models.ForeignKey(NoticeTopic, on_delete=models.CASCADE, null=True, blank=True)
    desc = models.TextField()
    display = models.BooleanField(default=False)

    def __str__(self):
        return (str(self.topic))

class NoticeImage(models.Model):
    topic = models.ForeignKey(NoticeTopic, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="image/")
    banner = models.BooleanField(default=False)

    def __str__(self):
        return (str(self.topic))