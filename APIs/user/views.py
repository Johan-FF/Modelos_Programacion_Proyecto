from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import User
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