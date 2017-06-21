from django.shortcuts import render
from .models import Byte
from django.db.models import Count

# Create your views here.
def byte_list(request):
    # bytes = Byte.objects.order_by('text')
    total_bytes = len(Byte.objects.filter())
    each_bytes = Byte.objects.values('text').annotate(c=Count('text')).order_by('c').exclude(text='')
    return render(request, 'cloudapp/byte_list.html', {'bytes': bytes, 'total_bytes': total_bytes, 'each_bytes': each_bytes})
    