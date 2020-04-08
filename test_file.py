#exec(open('test_file.py').read())
from api.models import Ram
from api.serializers import RamSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
import json


# array_data = [{"value":600,"um":"GB"}, {"value":10,"um":"GB"} ]
# serializer = RamSerializer(data=array_data,many=True)
# if serializer.is_valid():
#     serializer.save()
#     print(str(200) + " OK")
# else:
#     print(serializer.errors)
#     print(str(400) + " Bad Request")


#POST MULTIPLE VALUES - DRF
# array_data = [{"value":6,"um":"GB"}, {"value":10,"um":"GB"} ]
# el_inserted = 0
# for el in array_data:
#     serializer = RamSerializer(data=el)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         el_inserted +=1 
#     else:
#         print(serializer.errors)

# if len(array_data) == el_inserted:
#     print("Ok")
# else:
#     print("Problem")
        

#UPDATE MULTIPLE VALUES - DRF
# array_data = [{"id":12,"um":"TX"}, {"id": 13, "value":111,"um":"GG"}]
# for el in array_data:
#     ist = Ram.objects.get(pk=el.get("id",""))
#     serializer = RamSerializer(ist,data=el,partial=True)
#     if serializer.is_valid():
#         serializer.save()

#DELETE MULTIPLE VALUES - DRF
# array_data = [{"id":10}, {"id": 11}]
# for el in array_data:
#     print(el)
#     serializer = RamDeleteSerializer(data=el)

#     if serializer.is_valid():
#         Ram.objects.filter(pk=el.get("id","")).delete() 