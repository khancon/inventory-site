from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect, render

from .models import Item
from .forms import ItemForm

# Create your views here.
def add_item(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ItemForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print('Form valid')
            obj = Item(
                item_name=form.cleaned_data["item_name"], 
                price=form.cleaned_data["price"],
                stock_quantity=form.cleaned_data["stock_quantity"],
                description=form.cleaned_data["description"],
                photo=form.cleaned_data["photo"],
            )
            obj.save()
            # redirect to a new URL:
            return redirect('home')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ItemForm()

    return render(request, 'add_item.html', {'form': form})

def home_display_items(request):
    items = Item.objects.all()
    print(items)
    return render(request, 'home.html', {'items': items, 'item_count': Item.objects.count()})

def item_checkout(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'item_checkout.html', {'item': item})