from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import Meeting,Room

# def detail(request,id):
#     meeting =meeting.objects.get(pk=id)
#     return render(request, "meetings/detail.html", {"meeting":meeting})

def detail(request,id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting":meeting})

def rooms_list(request):
    return render(request, "meetings/rooms_list.html",
                  {"rooms":Room.objects.all()}
                  )