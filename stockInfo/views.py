from django.shortcuts import render, redirect
from stockInfo.stockmanage import getStockData
from .models import StockData


def detail(request):
    """
    db 데이터출력
    :param request:
    """
    print("detail1")
    data: str
    period = request.GET.get('period')
    if request.GET.get('period') is not None:
        data = StockData.objects.all().order_by('-date', 'top30')[0:int(period)*30]
    else:
        data = StockData.objects.all().order_by('-date', 'top30')
    context = {'data': data}
    return render(request, 'test.html', context)


def detail2(request):
    """
    db 데이터출력
    :param request:
    """
    data: str
    info = request.GET.get('info')
    if info == 'info':
        getStockData.getStockData()

    return redirect('/stock')
