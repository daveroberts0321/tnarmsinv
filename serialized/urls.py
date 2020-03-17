from django.contrib import admin
from django.urls import path
from .views import SerializedUpload

app_name = 'serialized'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('upload-csv/', SerializedUpload, name="serialized_upload"),
]