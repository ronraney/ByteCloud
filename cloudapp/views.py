from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Byte
from django.db.models import Count
from django import forms
from .forms import ByteForm

# Create your views here.
def byte_list(request):
    #some extra logic
    total_bytes = len(Byte.objects.filter())
    each_bytes = Byte.objects.values('text').annotate(c=Count('text')).order_by('-c').exclude(text='') #Previous code... bytes = Byte.objects.order_by('text')
    
    #the word form
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ByteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            post = form.save(commit=False)
            post.save()
            # redirect to a new URL:
            return HttpResponseRedirect('#')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ByteForm()
        
    return render(request, 'cloudapp/byte_list.html', {'bytes': bytes, 'total_bytes': total_bytes, 'each_bytes': each_bytes, 'form': form})

   