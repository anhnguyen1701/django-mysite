from django.http import HttpResponse
from django.shortcuts import render
from contact.forms import contact_Form

# Create your views here.


def contact(request):
    cf = contact_Form
    return render(request, 'contact/contact.html', {'cf': cf})


def getContact(request):
    if request.method == "POST":
        cf = contact_Form(request.POST)
        if cf.is_valid():
            cf.save()
            return HttpResponse("save success")
    else:
        return HttpResponse("not POST")
