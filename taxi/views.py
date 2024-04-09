from django.shortcuts import render

from taxi.models import Driver, Car, Manufacturer

from django.views import generic


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    queryset = model.objects.order_by("name")
    paginate_by = 5
    template_name = "manufacturers"


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5


class CarDetailView(generic.DetailView):
    model = Car


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars")
