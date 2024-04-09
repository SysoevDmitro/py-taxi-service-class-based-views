from django.urls import path

from .views import index, ManufacturerListView, CarListView, DriverListView
from .views import CarDetailView, DriverDetailView

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturer_list"),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path('drivers/<int:pk>/', DriverDetailView.as_view(), name='driver-detail'),
]

app_name = "taxi"
