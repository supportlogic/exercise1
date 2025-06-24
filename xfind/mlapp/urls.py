from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('data-sources/', views.get_data_sources, name='get_data_sources'),
    path('data-sources/add/', views.add_data_source, name='add_data_source'),
    path('token/', obtain_auth_token, name='api_token_auth'),
]
