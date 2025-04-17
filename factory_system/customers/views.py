from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Customer
from .forms import CustomerForm
from .filters import CustomerFilter

@login_required
def customer_list(request):
    customers = Customer.objects.all().order_by('name')
    return render(request, 'customers/customer_list.html', {'customers': customers})

@login_required
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customers/customer_form.html', {'form': form})

@login_required
def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers/customer_form.html', {'form': form})

@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customers/customer_confirm_delete.html', {'customer': customer})

@login_required
def customer_list(request):
    customer_filter = CustomerFilter(request.GET, queryset=Customer.objects.all().order_by('name'))
    return render(request, 'customers/customer_list.html', {
        'filter': customer_filter,
        'customers': customer_filter.qs
    })
    

@login_required
def customer_detail_list(request):
    customers = Customer.objects.all().order_by('name')
    return render(request, 'customers/customer_detail_list.html', {'customers': customers})


