from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Pet
from django.shortcuts import render
from django.http import Http404

def home_view(request):
    return HttpResponse('Hello, This is Home!')


#writing more views

def detail(request, pet_id):
    #return HttpResponse("You're looking at PET %s." % pet_id)
    try:
        pet = Pet.objects.get(pk=pet_id)
    except Pet.DoesNotExist:
        raise Http404("Pet does not exist")
    return render(request, 'myapp/detail.html', {'pet': pet})

def results(request, pet_id):
    response = "You're looking at RESULT of PET {}."
    return HttpResponse(response.format(pet_id))

def registerPet(request, pet_id):
    return HttpResponse("You're registering at PET %s." % pet_id)

#pet list

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'myapp/pet_list.html', {'pets': pets})


#index
def index(request):
    pet_list = Pet.objects.all()
    context = {
        'pet_list': pet_list
    }
    return render(request, 'myapp/pet_list.html', context)





def indexShortcut(request):
    latest_pet_list = Pet.objects.order_by('-pub_date')[:5]
    context = {'latest_pet_list': latest_pet_list}
    return render(request, 'polls/index.html', context)


