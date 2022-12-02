from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from . models import *
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@login_required(login_url='/login')
def index(request):
    user_object = get_object_or_404(User, username=request.user.username)
    user_profile = get_object_or_404(Profile, user=user_object)


    slider = Slider.objects.all()
    service = Service.objects.all()
    process = Processe.objects.all()
    post = Post.objects.all()
    progress = Progres.objects.all()
    project = Project.objects.all()
    servicearea = ServiceArea.objects.all()
    job = Job.objects.all()
    testimony = Testimony.objects.all()
    context = {
        'sliders':slider,
        'services':service[:5],
        'processes':process,
        'posts':post[:2],
        'progresses':progress,
        'projects':project,
        'serviceareas':servicearea,
        'jobs':job,
        'testimonies':testimony,
        'user_object': user_object,
        'user_profile': user_profile,
    }
    return render(request, 'main/index.html', context)



@login_required(login_url='/login')
def about(request):
    about = AboutU.objects.all()
    progress = Progres.objects.all()
    process = Processe.objects.all()
    testimony = Testimony.objects.all()
    team = Team.objects.all()


    context = {
        'abouts':about,
        'progresses':progress,
        'processes':process,
        'testimonies':testimony,
        'teams':team
    }
    return render(request, 'main/about.html', context)



@login_required(login_url='/login')
def services(request):
    service = Service.objects.all()

    context = {
        'services':service,
    }
    return render(request, 'main/services.html', context)



@csrf_exempt
@login_required(login_url='/login')
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        content = request.POST['content']

        contact = Contact.objects.create(name=name, email=email, phone=phone, subject=subject, content=content)
        contact.save()
        messages.info(request, 'Enquiries Sent Successfully')
        return redirect('/contact')
    else:
        return render(request, 'main/contact.html')



@login_required(login_url='/login')
def packages(request):
    package = Package.objects.all()

    context = {
        'packages':package
    }
    return render(request, 'main/packages.html', context)


@csrf_exempt
@login_required(login_url='/login')
def application(request):
   
    if request.method == "POST":
        if request.POST.get('package'):
            get_package = request.POST.get('package')
            package = get_package

            get_service = request.POST.get('service')
            service = get_service

            name = request.POST['name']
            contact = request.POST['contact']
            location = request.POST['location']

            application = PackageApplication.objects.create(name=name, contact=contact, service=service, package=package, location=location)
            application.save()
            messages.info(request, "Application for package is Successful. We'll Contact you Soon")
            return redirect('/application')
        else:
            messages.info(request, "Application for package not Submitted. Try Again")
            return redirect('/application')

    package = Package.objects.all()
    service = Service.objects.all()

    context = {
        'packages':package,
        'services':service
    } 
    return render(request, 'main/application.html', context)




@login_required(login_url='/login')
def jobs(request):
    job = Job.objects.all()

    context = {
        'jobs':job,
    }
    return render(request, 'main/list-jobs.html', context)



@login_required(login_url='/login')
def blog(request):
    blog = Post.objects.all()

    context = {
        'blogs':blog
    }
    return render(request, 'main/blog.html', context)




@login_required(login_url='/login')
def employer(request):
    employer = Employer.objects.all()

    context = {
        'employers':employer
    }
    return render(request, 'main/employers.html', context)



@login_required(login_url='/login')
def courier(request):
    person = Personnel.objects.all()
    service = Service.objects.all()

    p = Paginator(Personnel.objects.all(), 20)
    page = request.GET.get('page')
    allpersonnel = p.get_page(page)

    context = {
        'persons':person,
        'services':service,
        'allpersonnels':allpersonnel
    }
    return render(request, 'main/vehicles.html', context)



@login_required(login_url='/login')
def job_details(request, pk):
    job_detail = Job.objects.get(title=pk)

    context = {
        'job_details':job_detail
    }
    return render(request, 'main/details.html', context)



@login_required(login_url='/login')
def privacy_policy(request):
    privacy = Privacy.objects.all()

    context = {
        'privacys':privacy
    }
    return render(request, 'main/privacy.html', context)


@login_required(login_url='/login')
def terms(request):
    term = Term.objects.all()

    context = {
        'terms':term
    }
    return render(request, 'main/terms.html', context)



@login_required(login_url='/login')
def service_details(request, pk):
    service_detail = Service.objects.get(title=pk)

    context = {
        'service_details':service_detail
    }
    return render(request, 'main/service-single.html', context)



@login_required(login_url='/login')
def post_details(request, pk):
    post_detail = Post.objects.get(title=pk)

    context = {
        'post_details':post_detail
    }
    return render(request, 'main/blog-single.html', context)



@login_required(login_url='/login')
def employer_details(request, pk):
    employer_detail = Employer.objects.get(name=pk)

    context = {
        'employer_details':employer_detail
    }
    return render(request, 'main/profile-employers.html', context)



@login_required(login_url='/login')
def personnel_details(request, pk):
    personnel_details = Personnel.objects.get(name=pk)

    context = {
        'personnel_details':personnel_details
    }
    return render(request, 'main/profile-candidates.html', context)




@csrf_exempt
def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('/register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('/register')
            elif len(password) <= 6:
                messages.info(request, f'Password must be more than { len(password) } Characters')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
    
                #log user in and redirect to settings
                individual_login = auth.authenticate(username=username, password=password)
                auth.login(request, individual_login)

                #create a profile object for the new user
                user_model = User.objects.get(username=username)
                individual_profile = Profile.objects.create(firstname=firstname, lastname=lastname, email=email, user=user_model, password=password, phone=phone, id_user=user_model.id)
                individual_profile.save()
                return redirect('/order')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('/dashboard')
    return render(request, 'main/register.html')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/order')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('/login')
    else:
        return render(request, 'main/sign-in.html')



@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return redirect('/login')



@csrf_exempt
@login_required(login_url='/login')
def order(request):
    if request.method == "POST":
        if request.POST.get('service'):
            get_service = request.POST.get('service')
            service = get_service

            get_payment = request.POST.get('payment')
            payment = get_payment

            get_errandby = request.POST.get('errandby')
            errandby = get_errandby

            name = request.POST['name']
            email = request.POST['email']
            contact = request.POST['contact']
            location = request.POST['location']
            errandfrom = request.POST['from']
            errandto = request.POST['destination']
            description = request.POST['note']


            user_model = User.objects.get(username=name)
            personnel_model = Personnel.objects.get(name=errandby)
            new_errand = Errand.objects.create(errandby=personnel_model, email=email, user=user_model, name=name, contact=contact, location=location, errandfrom=errandfrom, errandto=errandto, service=service, description=description, payment=payment)
            new_errand.save
            messages.info(request, "Errand Booking Submitted")


            
            return redirect('/onride')

           
        else:
            return redirect('/order')

    user_object = get_object_or_404(User, username=request.user.username)
    user_profile = get_object_or_404(Profile, user=user_object)
    service = Service.objects.all()
    personnel = Personnel.objects.all()

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'services':service,
        'personnels':personnel,
        
    }

  
    return render(request, 'main/ride.html', context)
    


@login_required(login_url='/login')
def onride(request):
    user_object = get_object_or_404(User, username=request.user.username)
    user_profile = get_object_or_404(Profile, user=user_object)

    import phonenumbers
    import opencage
    import folium


    from phonenumbers import geocoder

    number = "+233506618200"
    pepnumber = phonenumbers.parse(number)
    location = geocoder.description_for_number(pepnumber, "en")
    print(location)

    from phonenumbers import carrier

    service_pro = phonenumbers.parse(number)
    print(carrier.name_for_number(service_pro, "en"))

    from opencage.geocoder import OpenCageGeocode

    key = "3a9e23bb36964323940b1c8081ba2983"

    geocoder = OpenCageGeocode(key)

    query = str(location)
    results = geocoder.geocode(query)
    #print(results)
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    print(lat, lng)

    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(myMap)

    myMap.save("mylocation.html")

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
    }




    return render(request, 'main/on-ride.html', context)



@login_required(login_url='/login')
def dashboard(request, pk):
    user_object = get_object_or_404(User, username=pk)
    user_profile = get_object_or_404(Profile, user=user_object)
    errand = Errand.objects.filter(user=request.user)


    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'errands':errand
    }
    return render(request, 'main/dashboard.html', context)