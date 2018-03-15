from django.shortcuts import render

from database.models import Orders, Quotes

from .forms import AddQuoteForm
# Create your views here.


def quotes(request):
    add_quote_form = AddQuoteForm()
    return render(request,
                  'quotes/index.html',
                  {'username': request.user.get_username(),
                   'quotes_table': Quotes.objects.select_related().all(),
                   'add_quote_form': add_quote_form})


def add_quotes(request):
    if request.method == 'GET':
        add_quote_form = AddQuoteForm()
        return render(request,
                      'quotes/index.html',
                      {'username': request.user.get_username(),
                       'quotes_table': Quotes.objects.select_related().all(),
                       'add_quote_form': add_quote_form})
    else:
        add_quote_form = AddQuoteForm(request.POST)
        new_quote = Quotes()
        if add_quote_form.is_valid():
            project_num = request.POST.get('project_num')
            unit_price = request.POST.get('unit_price')
            amount = request.POST.get('amount')
            new_quote.project_num = project_num
            new_quote.unit_price = unit_price
            new_quote.total_price = int(unit_price) * int(amount)
            new_quote.save()
            return render(request,
                          'quotes/index.html',
                          {'username': request.user.get_username(),
                           'quotes_table': Quotes.objects.select_related().all(),
                           'add_quote_form': add_quote_form,
                           'info': u'添加成功!'})
        else:
            return render(request,
                          'quotes/index.html',
                          {'username': request.user.get_username(),
                           'quotes_table': Quotes.objects.select_related().all(),
                           'add_quote_form': add_quote_form,
                           'error': u'添加失败！'})
