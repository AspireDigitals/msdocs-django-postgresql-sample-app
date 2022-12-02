from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('order', views.order, name="order"),
    path('dashboard/<str:pk>', views.dashboard, name="dashboard"),
    path('onride', views.onride, name="onride"),
    path('privacy-policy', views.privacy_policy, name="privacy-policy"),
    path('terms', views.terms, name="help"),
    path('application', views.application, name="application"),


    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('packages', views.packages, name="packages"),
    path('contact', views.contact, name="contact"),
    path('jobs', views.jobs, name="jobs"),
    path('blog', views.blog, name="blogs"),
    path('courier', views.courier, name="courier"),
    path('employer', views.employer, name="employer"),
    path('employers/<str:pk>', views.employer_details, name="employers"),
    path('personnels/<str:pk>', views.personnel_details, name="personnels"),

    path('jobs/<str:pk>', views.job_details, name="jobs"),
    path('services/<str:pk>', views.service_details, name="services-details"),
    path('posts/<str:pk>', views.post_details, name="posts-details"),
]
