from django.shortcuts import render

# Create your views here.

def measurements_view(request):
    if request.method == 'GET':
        measurements = vl.get_variables()
        measurements_dto = serializers.serialize('json', variables)
        return HttpResponse(measurements_dto, 'application/json')

def measurement_view(request, pk):
    if request.method == 'GET':
        measurement = vl.get_measurement(pk)
        measurement_dto = serializers.serialize('json', measurement)
        return HttpResponse(measurement_dto, 'application/json')