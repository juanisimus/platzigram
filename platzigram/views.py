"""Pltazigram views """
"""Este archivo es el Encargado de la logica de traer los datos"""
#Utilities
import pdb 
import json
from datetime import datetime



from django.http import HttpResponse, JsonResponse


def hello_world(request):
    """ Return a greeting """
    now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
    return HttpResponse('Hello, world!, Current server time is {now}'.format(now=str(now)))

def sort_integers(request):
    """Returns a JSON response with sorted integers."""
    #print(request)
    #pdb.set_trace()
    numbers = sorted(int(number) for number in request.GET['numbers'].split(','))
    
    #METODO LARGO
    data = {
        'status': 'ok',
        'numbers': numbers,
        'message': 'input succesfully converted from string to json ',
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')
    #METODO CORTO
    """
    response = JsonResponse({'numbers':numbers})
    print(response)
    print(response.content)
    return response
    """

def say_hi(request, name, age):
    """Return greeting"""
    if age < 12:
        message = 'Sorry {}, you are not alloved here'.format(name)
    else:
        message = '{}, welcome to Platzigram'.format(name)
    
    return HttpResponse(message)