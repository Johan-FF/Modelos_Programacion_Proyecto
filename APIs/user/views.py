from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import *
import json

class UserView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_u=0):
        if id_u>0:
            users = list(User.objects.filter(id=id_u).values())
            if len(users)>0:
                user = users[0]
                data = {'message': "Success", 'user': user}
            else:
                data = {'message': "User not found..."}
            return JsonResponse(data)
        else:
            users = list(User.objects.values())
            if len(users)>0:
                data = {'message': "Success", 'users': users}
            else:
                data = {'message': "Users not found..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        User.objects.create(
            fk_rol = jd['fk_rol'],
            fk_country = jd['fk_country'],
            fk_history = jd['fk_history'],
            name = jd['name'],
            last_name = jd['last_name'],
            nickname = jd['nickname'],
            password = jd['password'],
            email = jd['email'],
            cell_number = jd['cell_number']
        )
        data = {'message': "Success"}
        return JsonResponse(data)
        
    def put(self, request, id_u):
        jd = json.loads(request.body)
        users = list(User.objects.filter(id=id_u).values())
        if len(users)>0:
            user = User.objects.get(id=id_u)
            user.fk_rol = jd['fk_rol']
            user.fk_country = jd['fk_country']
            user.fk_history = jd['fk_history']
            user.name = jd['name']
            user.last_name = jd['last_name']
            user.nickname = jd['nickname']
            user.password = jd['password']
            user.email = jd['email']
            user.cell_number = jd['cell_number']
            user.save()
            data = {'message': "Success"}
        else:
            data = {'message': "User not found..."}
        return JsonResponse(data)
    
    def delete(self, request, id_u):
        users = list(User.objects.filter(id=id_u).values())
        if len(users)>0:
            User.objects.filter(id=id_u).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "User not found..."}
        return JsonResponse(data)
    
class User_RolView(View):
    def get(self, request, id_u_r=0):
        if id_u_r>0:
            rols = list(User_Rol.objects.filter(id=id_u_r).values())
            if len(rols)>0:
                rol = rols[0]
                data = {'message': "Success", 'user_rol': rol}
            else:
                data = {'message': "User not found..."}
            return JsonResponse(data)
        else:
            rols = list(User_Rol.objects.values())
            if len(rols)>0:
                data = {'message': "Success", 'user_rols': rols}
            else:
                data = {'message': "Users not found..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        User_Rol.objects.create(
            rol = jd['rol'],
        )
        data = {'message': "Success"}
        return JsonResponse(data)
        
    def put(self, request, id_u_r):
        jd = json.loads(request.body)
        rols = list(User_Rol.objects.filter(id=id_u_r).values())
        if len(rols)>0:
            rol = User_Rol.objects.get(id=id_u_r)
            rol.rol = jd['rol']
            rol.save()
            data = {'message': "Success"}
        else:
            data = {'message': "User_Rol not found..."}
        return JsonResponse(data)
    
    def delete(self, request, id_u_r):
        rols = list(User_Rol.objects.filter(id=id_u_r).values())
        if len(rols)>0:
            User_Rol.objects.filter(id=id_u_r).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "User_Rol not found..."}
        return JsonResponse(data)

class CountryView(View):
    def get(self, request, id_c=0):
        if id_c>0:
            countrys = list(Country.objects.filter(id=id_c).values())
            if len(countrys)>0:
                country = countrys[0]
                data = {'message': "Success", 'country': country}
            else:
                data = {'message': "Country not found..."}
            return JsonResponse(data)
        else:
            countrys = list(Country.objects.values())
            if len(countrys)>0:
                data = {'message': "Success", 'countrys': countrys}
            else:
                data = {'message': "Countrys not found..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Country.objects.create(
            name = jd['name'],
        )
        data = {'message': "Success"}
        return JsonResponse(data)
        
    def put(self, request, id_c):
        jd = json.loads(request.body)
        countrys = list(Country.objects.filter(id=id_c).values())
        if len(countrys)>0:
            country = Country.objects.get(id=id_c)
            country.rol = jd['name']
            country.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Country not found..."}
        return JsonResponse(data)
    
    def delete(self, request, id_c):
        countrys = list(Country.objects.filter(id=id_c).values())
        if len(countrys)>0:
            Country.objects.filter(id=id_c).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Country not found..."}
        return JsonResponse(data)

class HistoryView(View):
    def get(self, request, id_h=0):
        if id_h>0:
            historys = list(History.objects.filter(id=id_h).values())
            if len(historys)>0:
                history = historys[0]
                data = {'message': "Success", 'history': history}
            else:
                data = {'message': "History not found..."}
            return JsonResponse(data)
        else:
            historys = list(History.objects.values())
            if len(historys)>0:
                data = {'message': "Success", 'historys': historys}
            else:
                data = {'message': "Historys not found..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        History.objects.create(
            fk_date_record = jd['fk_date_record'],
            fk_date_sale = jd['fk_date_sale'],
            fk_client = jd['fk_client'],
            fk_developer = jd['fk_developer'],
            fk_sale = jd['fk_sale'],
            fk_bank = jd['fk_bank'],
            fk_history = jd['fk_history'],
        )
        data = {'message': "Success"}
        return JsonResponse(data)
        
    def put(self, request, id_h):
        jd = json.loads(request.body)
        historys = list(History.objects.filter(id=id_h).values())
        if len(historys)>0:
            history = History.objects.get(id=id_h)
            history.fk_date_record = jd['fk_date_record']
            history.fk_date_sale = jd['fk_date_sale']
            history.fk_client = jd['fk_client']
            history.fk_developer = jd['fk_developer']
            history.fk_sale = jd['fk_sale']
            history.fk_bank = jd['fk_bank']
            history.fk_history = jd['fk_history']
            history.save()
            data = {'message': "Success"}
        else:
            data = {'message': "History not found..."}
        return JsonResponse(data)
    
    def delete(self, request, id_h):
        historys = list(History.objects.filter(id=id_h).values())
        if len(historys)>0:
            History.objects.filter(id=id_h).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "History not found..."}
        return JsonResponse(data)

