from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
    return HttpResponse("Hello World :D this is the time " + str(datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))

def hi(request):
    #import pdb; pdb.set_trace()
    arr = request.GET.get("numbers").split(",")
    realArr = []
    for number in arr:
        realArr.append(int(number))
    
    realArr = sorted(realArr)

    toReturn = {
        'status' : 'ok',
        'numbers' : realArr,
        'message' : 'This message is going in json format'
    }

    
    return HttpResponse(json.dumps(toReturn) , content_type='application/json')