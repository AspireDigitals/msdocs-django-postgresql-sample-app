from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.
User = get_user_model()



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    password = models.CharField(max_length=100)
    profileimg = models.ImageField(upload_to='profile_images', default='user.png')
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
   

    def __str__(self):
        return self.user.username



class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.UUIDField()
    password = models.CharField(max_length=100)
    profileimg = models.ImageField(upload_to='profile_images', default='user.png')
    companyname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
   

    def __str__(self):
        return self.user.username




class AboutU(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='about_images')

    def __str__(self):
        return self.title



class Privacy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title




class Term(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title




class Team(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='team_images')

    def __str__(self):
        return self.name




class Slider(models.Model):
    title = models.CharField(max_length=100)
    maintitle = models.CharField(max_length=100)
    image = models.ImageField(upload_to="slider_images")


    def __str__(self):
        return self.title



class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="service_images")

    def __str__(self):
        return self.title



class Processe(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="process_images")

    def __str__(self):
        return self.title



class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to="posts_images")
    date_posted = models.DateTimeField(default=timezone.now)
    posted_by = models.CharField(max_length=100, default="Admin")

    def __str__(self):
        return self.title




class Package(models.Model):
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    benefit1 = models.CharField(max_length=300)
    benefit2 = models.CharField(max_length=300)
    benefit3 = models.CharField(max_length=300, blank=True, null=True)
    benefit4 = models.CharField(max_length=300, blank=True, null=True)
    benefit5 = models.CharField(max_length=300, blank=True, null=True)
    benefit6 = models.CharField(max_length=300, blank=True, null=True)


    def __str__(self):
        return self.title




class PackageApplication(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    package = models.CharField(max_length=100)
    service = models.CharField(max_length=100)


    def __str__(self):
        return f"Package Application from {self.name}"



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=300)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"Enquiry from {self.name}"




class Progres(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()
    image = models.ImageField(upload_to="progress_images")


    def __str__(self):
        return self.title




class Project(models.Model):
    title = models.CharField(max_length=100)
    overview = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to="posts_images")

    def __str__(self):
        return self.title



class ServiceArea(models.Model):
    errandfrom = models.CharField(max_length=100)
    errandto = models.CharField(max_length=100)

    def __str__(self):
        return f"Service from {self.errandfrom} to {self.errandto}"



class Job(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    overview = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to="posts_images")
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title




class Gender(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class Personnel(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    Gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    statement = models.CharField(max_length=300)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    servicearea = models.ForeignKey(ServiceArea, on_delete=models.CASCADE)
    description = models.TextField()
    onerrandsto = models.CharField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to="personnel_images")
    availability = models.BooleanField(default=True, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name



class Errand(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    errandfrom = models.CharField(max_length=300)
    errandto = models.CharField(max_length=300)
    service = models.CharField(max_length=300)
    payment = models.CharField(max_length=300)
    description = models.TextField()
    date_requested = models.DateTimeField(default=timezone.now)
    accepted = models.BooleanField(default=False)
    waiting = models.BooleanField(default=False)
    onride = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    errandby = models.ForeignKey(Personnel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Errand Request from {self.name} to {self.location}"



class Employer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to="employer_images")
    
   

    def __str__(self):
        return self.name




class Testimony(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=300)
    company = models.CharField(max_length=100)
    testimony = models.TextField()
    image = models.ImageField(upload_to="testimony_images")
    date_posted = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return f"Testimony from {self.name} of {self.company}"