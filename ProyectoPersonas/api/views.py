from django.http import JsonResponse
from django.views import View
from .models import Persona

# Create your views here.


class PersonaView(View):
    
    def get(self, request):
        personas= list(Persona.objects.values())
        if len(personas)>0:
            datos={'message':"Success",'personas':personas}
        else:
            datos={'message':"Personas not found..."}
        return JsonResponse(datos)
        
    def post(self, request):
        pass
    def put(self, request):
        pass
    def delete(self, request):
        pass