from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Board
from .forms import BoardForm
from .filters import BoardFilter
from django.utils.decorators import method_decorator


@login_required
class BoardListView(View):
    def get(self, request):
        board_filter = BoardFilter(request.GET, queryset=Board.objects.all().order_by('name'))
        return render(request, 'inventory/board_list.html', {
            'boards': board_filter.qs,
            'filter': board_filter
        })


@login_required
def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_list')  # 👈 correct redirect name
    else:
        form = BoardForm()
    return render(request, 'inventory/board_form.html', {'form': form})


@login_required
def board_update(request, pk):
    board_item = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board_item)
        if form.is_valid():
            form.save()
            return redirect('board_list')
    else:
        form = BoardForm(instance=board_item)
    return render(request, 'inventory/board_form.html', {'form': form})


@login_required
def board_delete(request, pk):
    board_item = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        board_item.delete()
        return redirect('board_list')
    return render(request, 'inventory/board_confirm_delete.html', {'board': board_item})
