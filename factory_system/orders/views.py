from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderAttachment
from .forms import OrderForm, AttachmentForm
from django.contrib.auth.decorators import login_required

@login_required
def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        attachment_form = AttachmentForm(request.POST, request.FILES)

        if form.is_valid() and attachment_form.is_valid():
            order = form.save()
            file = attachment_form.cleaned_data.get('file')
            if file:
                OrderAttachment.objects.create(order=order, file=file)
            return redirect('order_list')
    else:
        form = OrderForm()
        attachment_form = AttachmentForm()

    return render(request, 'orders/order_form.html', {
        'form': form,
        'attachment_form': attachment_form
    })

@login_required
def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        attachment_form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid() and attachment_form.is_valid():
            order = form.save()
            file = attachment_form.cleaned_data.get('file')
            if file:
                OrderAttachment.objects.create(order=order, file=file)
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
        attachment_form = AttachmentForm()
    return render(request, 'orders/order_form.html', {
        'form': form,
        'attachment_form': attachment_form
    })

@login_required
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'orders/order_confirm_delete.html', {'order': order})
