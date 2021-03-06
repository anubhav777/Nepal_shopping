"""nepal_shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Ecom_data, Ecom_Data_List, Searchdata, Seachdataind, Web_scrapper,ObjectView
# router = routers.DefaultRouter()
# router.register(r'postecom', Ecom_data)

urlpatterns = [
    path('ecom/', Ecom_data.as_view()),
    path('ecom/<int:id>', Ecom_Data_List.as_view()),
    path('searchdata/', Searchdata.as_view()),
    path('searchdata/<int:id>', Seachdataind.as_view()),
    path('object/',ObjectView.as_view(),)
    # path('web/',Web_scrapper.as_view(),)
    
]
