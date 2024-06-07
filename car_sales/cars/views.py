from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Car, Brand, Order
from .forms import CommentForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class HomeView(View):
    def get(self, request):
        brands = Brand.objects.all()
        cars = Car.objects.all()
        selected_brand = request.GET.get('brand')
        if selected_brand:
            cars = cars.filter(brand__name=selected_brand)
        context = {
            'brands': brands,
            'cars': cars,
        }
        return render(request, 'cars/home.html', context)

class CarDetailView(View):
    def get(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        form = CommentForm()
        context = {
            'car': car,
            'form': form,
        }
        return render(request, 'cars/car_detail.html', context)

    def post(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.save()
            return redirect('car-detail', pk=car.pk)
        context = {
            'car': car,
            'form': form,
        }
        return render(request, 'cars/car_detail.html', context)

@method_decorator(login_required, name='dispatch')
class BuyCarView(View):
    def post(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        if car.quantity > 0:
            order = Order(user=request.user, car=car)
            order.save()
            car.quantity -= 1
            car.save()
        return redirect('order-history')
    
@method_decorator(login_required, name='dispatch')
class OrderHistoryView(View):
    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        context = {
            'orders': orders,
        }
        return render(request, 'cars/order_history.html', context)

