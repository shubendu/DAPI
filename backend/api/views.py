from django.http import JsonResponse
import json

#its an httprequest from django
def api_home(request, *args, **kwargs):
    # request -> HTTPRequest ->Django
    sam = request.body 
    #request.body #byte string of json data   
    data = {}
    try:
         data = json.loads(sam) #string of json data -> python dict
    except:
        pass
    return JsonResponse(data)

