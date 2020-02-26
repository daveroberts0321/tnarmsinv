
from django.contrib import admin
from django.urls import path, include
from inventory.views import Index, InvListView, StaffIndex, StaffListView, AddInvView, UpdateInvView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name = 'index'),
    path('inventory', InvListView.as_view(), name = 'inventory'),
    path('staff', StaffIndex.as_view(), name = 'staff'),
    path('staff/list', StaffListView.as_view(), name = 'stafflist'),
    path('staff/addinv', AddInvView.as_view(), name = 'addinv'),
    path('staff/invupdate-<int:pk>', UpdateInvView.as_view(), name = 'updateinv'),
    path('login/', include('login.urls')), # new
    path('login/', include('django.contrib.auth.urls')), # new
]
