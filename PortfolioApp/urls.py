"""
URL configuration for Dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import applicant_list_view, ApplicantDetailView, ApplicantDeleteView

app_name = 'PortfolioApp'

urlpatterns = [
    path('', applicant_list_view, name='applicant_list'),
    path('portfolio/<str:username>/', ApplicantDetailView.as_view(), name='applicant_detail'),
    path('portfolio/<str:username>/delete/', ApplicantDeleteView.as_view(), name='applicant_delete'),
]