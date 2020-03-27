
from django.contrib import admin
from django.urls import path, include
from inventory.views import (Index, InvListView, StaffIndex, 
StaffListView, AddInvView, UpdateInvView, OrderListView, AddOrderView, UpdateOrderView,
OrderListView, AddConsumables,ConsumablesView, UpdateConsumables, OrderDelete, Supplier, SupplierDelete, SupplierListView, AddSupplier, UpdateSupplierView, AdvantageList)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name = 'index'),
    path('inventory', InvListView.as_view(), name = 'inventory'),
    path('staff', StaffIndex.as_view(), name = 'staff'),
    path('staff/list', StaffListView.as_view(), name = 'stafflist'),
    path('staff/orderlist', OrderListView.as_view(), name = 'orderlist'),
    path('staff/supplierlist', SupplierListView.as_view(), name = 'supplierlist'),
    path('staff/consumables', ConsumablesView.as_view(), name = 'consumableslist'),
    path('staff/addinv', AddInvView.as_view(), name = 'addinv'),
    path('staff/addsupplier', AddSupplier.as_view(), name = 'addsupplier'),
    path('staff/addorder', AddOrderView.as_view(), name = 'addorder'),
    path('staff/addconsumables', AddConsumables.as_view(), name = 'addconsumables'),
    path('staff/invupdate-<int:pk>', UpdateInvView.as_view(), name = 'updateinv'),
    path('staff/updatesupplier-<int:pk>', UpdateSupplierView.as_view(), name = 'updatesupplier'),
    path('staff/updateorder-<int:pk>', UpdateOrderView.as_view(), name = 'updateorder'),
    path('staff/updatesupplier-<int:pk>', SupplierDelete.as_view(), name = 'supplierdelete'),
    path('staff/orderdelete-<int:pk>', OrderDelete.as_view(), name = 'orderdelete'),
    path('staff/updateconsumables-<int:pk>', UpdateConsumables.as_view(), name = 'updateconsumables'),
    path('serialized/', include('serialized.urls')),
    path('advantage', AdvantageList.as_view(), name = 'advantage'),
    path('login/', include('login.urls')), 
    path('login/', include('django.contrib.auth.urls')), 
]
