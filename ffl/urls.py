from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from .views import FFLIndex, UpdateFFL, AddFFL, FFLDetail, SearchFFL, FFLUpload
from django.contrib.staticfiles.urls import static
from django.views.static import serve

app_name = 'ffl'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('fflindex/', FFLIndex.as_view(), name = 'fflindex'),
    path('addffl/', AddFFL.as_view(), name = 'addffl'),
    path('ffldetail-<int:pk>/', FFLDetail.as_view(), name='ffldetail'),
    path('updateffl-<int:pk>/', UpdateFFL.as_view(), name = 'updateffl'),
    path('fflupload', FFLUpload, name= 'fflupload'),
    path('search/', SearchFFL.as_view(), name = 'search')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)