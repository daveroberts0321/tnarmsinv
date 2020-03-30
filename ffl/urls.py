from django.contrib import admin
from django.urls import path, include
from .views import FFLIndex, UpdateFFL, AddFFL, FFLDetail
app_name = 'ffl'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('fflindex/', FFLIndex.as_view(), name = 'fflindex'),
    path('addffl/', AddFFL.as_view(), name = 'addffl'),
    path('ffldetail-<int:pk>/', FFLDetail.as_view(), name='ffldetail'),
    path('updateffl-<int:pk>/', UpdateFFL.as_view(), name = 'updateffl')
]