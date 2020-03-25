from django.contrib import admin
from django.urls import path
from .views import SerializedUpload, AddSerialized, SerializedListView

app_name = 'serialized'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('upload', SerializedUpload, name="serialized_upload"),
    path('addserialized', AddSerialized.as_view(), name = 'addserialized'),
    path('list', SerializedListView.as_view(), name = 'serializedlist'),
]