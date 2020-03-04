
from django.contrib import admin
from django.urls import path, include
from inventory.views import (Index, InvListView, StaffIndex, 
StaffListView, AddInvView, UpdateInvView, OrderListView, AddOrderView, UpdateOrderView,
OrderListView, AddConsumables, ConsumablesView, UpdateConsumables, OrderDelete)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name = 'index'),
    path('inventory', InvListView.as_view(), name = 'inventory'),
    path('staff', StaffIndex.as_view(), name = 'staff'),
    path('staff/list', StaffListView.as_view(), name = 'stafflist'),
    path('staff/orders', OrderListView.as_view(), name = 'orderlist'),
    path('staff/consumables', ConsumablesView.as_view(), name = 'consumableslist'),
    path('staff/addinv', AddInvView.as_view(), name = 'addinv'),
    path('staff/addorder', AddOrderView.as_view(), name = 'addorder'),
    path('staff/addconsumables', AddConsumables.as_view(), name = 'addconsumables'),
    path('staff/invupdate-<int:pk>', UpdateInvView.as_view(), name = 'updateinv'),
    path('staff/updateorder-<int:pk>', UpdateOrderView.as_view(), name = 'updateorder'),
    path('staff/orderdelete-<int:pk>', OrderDelete.as_view(), name = 'orderdelete'),
    path('staff/updateconsumables-<int:pk>', UpdateConsumables.as_view(), name = 'updateconsumables'),
    path('login/', include('login.urls')), 
    path('login/', include('django.contrib.auth.urls')), 
]
