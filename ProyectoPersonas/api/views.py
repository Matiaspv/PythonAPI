from django.http import JsonResponse
from django.views import View
from .models import Persona
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


class PersonaView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request,id=0):
        if(id>0):
            personas= list(Persona.objects.filter(id=id).values())
            if len(personas) > 0:
                persona = personas[0]
                datos={'message':"Success",'personas':persona}
            else:
                datos={'message':"Persona not found..."}
            return JsonResponse(datos)
        else:
            personas= list(Persona.objects.values())
            if len(personas)>0:
                datos={'message':"Success",'personas':personas}
            else:
                datos={'message':"Personas not found..."}
            return JsonResponse(datos)
        
    def post(self, request):
        ## print(request.body)
        jd= json.loads(request.body)
        ##print(jd)
        Persona.objects.create(name=jd['name'],lastname=jd['lastname'],age=jd['age'])
        datos={'message':"Success"}
        return JsonResponse(datos)
    
    
    def put(self, request,id):
        
        jd= json.loads(request.body)
        
        personas= list(Persona.objects.filter(id=id).values())
        
        if len(personas) > 0:
            persona = Persona.objects.get(id=id)
            persona.name=jd['name']
            persona.lastname=jd['lastname']
            persona.age=jd['age']
            persona.save()
            datos={'message':"Success"}
        else:
            datos={'message':"Persona not found..."}
        return JsonResponse(datos)


    def delete(self, request,id):
        
        personas= list(Persona.objects.filter(id=id).values())
        
        if len(personas) > 0:
            Persona.objects.filter(id=id).delete()
            datos={'message':"Success"}
        else:
            datos={'message':"Persona not found..."}
        return JsonResponse(datos)
