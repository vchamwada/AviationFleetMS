from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('aircraft_and_asset_management/', views.aircraft_and_asset_management, name='aircraft_and_asset_management'),
    path('restricted_access_page/', views.restricted_access_page, name='restricted_access_page'),
    path('view_aircraft/', views.view_aircraft, name='view_aircraft'),
    path('edit_aircraft/', views.edit_aircraft, name='edit_aircraft'),
    path('add_aircraft/', views.add_aircraft, name='add_aircraft'),
    path('delete_aircraft/', views.delete_aircraft, name='delete_aircraft'),

    # Add more paths for other views as needed
]
