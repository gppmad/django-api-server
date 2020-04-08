from django.http import JsonResponse
from django.views import View
from api.models import Ram as DBModel
from api.serializers import RamSerializer as DBModelSerializer
from api.serializers import RamDeleteSerializer as DBModelDeleteSerializer
import json


class RamView(View):

    #GET OBJECT(S)
    def get(self, request, id=""):
        
        # Get without Parameter
        if(id == ""):
            query = list(DBModel.objects.values())
            return JsonResponse({"result":query})
        else:

        #Get with ID Parameter    
            try:
                query = DBModel.objects.values().get(pk=id)
            except DBModel.DoesNotExist:
                return JsonResponse({"error":"resource not found" }, status=404)
            return JsonResponse({"result":query})

    #POST OBJECT(S)
    def post(self, request):
        #[{"value":6,"um":"GB"}, {"value":10,"um":"GB"} ]
        #array_data = [{"value":600,"um":"GB"}, {"value":10,"um":"GB"} ]
        array_data = json.loads(request.body)
        
        serializer = DBModelSerializer(data=array_data,many=True)
        
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                print(str(e))
                return JsonResponse({"server_error":str(e) }, status=500) 
            return JsonResponse({"result":"ok"})
        else:
            return JsonResponse({"client_error":serializer.errors }, status=400)  
    
    #UPDATE OBJECT(S)
    def put(self, request):
        #[{"id":12,"um":"TX"}, {"id": 13, "value":111,"um":"GG"}]
        try:
            array_data = json.loads(request.body)
        except Exception as e:
            return JsonResponse({"client_error":str(e) }, status=400)

        for el in array_data:
            ist = DBModel.objects.get(pk=el.get("id",""))
            serializer = DBModelSerializer(ist,data=el,partial=True)
            if(serializer.is_valid()):
                try:
                    serializer.save()
                except Exception as e:
                    return JsonResponse({"server_error":str(e) }, status=500)                 
            else:
                return JsonResponse({"client_error":serializer.errors }, status=400)
        
        return JsonResponse({"result":"ok"})
    
    #DELETE OBJECT(S)
    def delete(self,request):
        # array_data = [{"id":10}, {"id": 11}]

        array_data = json.loads(request.body)
        for el in array_data:
            print(el)
            serializer = DBModelDeleteSerializer(data=el)

            if serializer.is_valid():
                try:
                    DBModel.objects.filter(pk=el.get("id","")).delete()
                except Exception as e:
                    return JsonResponse({"server_error":str(e) }, status=500)

                return JsonResponse({"result":"ok"})    
            else:
                return JsonResponse({"client_error":serializer.errors }, status=400)