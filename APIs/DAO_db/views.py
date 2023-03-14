from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import *
import json

# Views User

class User_RolView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    
    def get(self, request, id_u_r=0):
        if id_u_r>0:
            rols = list(User_Rol.objects.filter(id=id_u_r).values())
            if len(rols)>0:
                rol = rols[0]
                data = {'message': "Success", 'user_rol': rol}
            else:
                data = {'message': "User_rol not found..."}
            return JsonResponse(data)
        else:
            rols = list(User_Rol.objects.values())
            if len(rols)>0:
                data = {'message': "Success", 'user_rols': rols}
            else:
                data = {'message': "User_rols not found..."}
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
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
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
            country.name = jd['name']
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

# Views Product

class Software_ProductView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id_s_p=0):
        if id_s_p>0:
            products = list(Software_Product.objects.filter(id=id_s_p).values())
            if len(products)>0:
                product = products[0]
                data = {'message': "Success", 'software_product': product}
            else:
                data = {'message': "Software_product not found..."}
            return JsonResponse(data)
        else:
            products = list(Software_Product.objects.values())
            if len(products)>0:
                data = {'message': "Success", 'software_products': products}
            else:
                data = {'message': "Software_products not found..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Software_Product.objects.create(
            fk_kind_product = jd['fk_kind_product'],
            fk_resources = jd['fk_resources'],
            fk_license = jd['fk_license'],
            fk_technology = jd['fk_technology'],
            fk_developer = jd['fk_developer'],
            name = jd['name'],
            description = jd['description']
        )
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request, id_s_p):
        jd = json.loads(request.body)
        products = list(Software_Product.objects.filter(id=id_s_p).values())
        if len(products)>0:
            product = Software_Product.objects.get(id=id_s_p)
            product.fk_kind_product = jd['fk_kind_product']
            product.fk_resources = jd['fk_resources']
            product.fk_license = jd['fk_license']
            product.fk_technology = jd['fk_technology']
            product.fk_developer = jd['fk_developer']
            product.name = jd['name']
            product.description = jd['description']
            product.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Software_product not found..."}
        return JsonResponse(data)

    def delete(self, request, id_s_p):
        products = list(Software_Product.objects.filter(id=id_s_p).values())
        if len(products)>0:
            Software_Product.objects.filter(id=id_s_p).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Software_product not found..."}
        return JsonResponse(data)

class TechnologyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id_t=0):
        if id_t>0:
            technologies = list(Technology.objects.filter(id=id_t).values())
            if len(technologies)>0:
                technology = technologies[0]
                data = {'message': "Success", 'technology': technology}
            else:
                data = {'message': "Technology not found..."}
            return JsonResponse(data)
        else:
            technologies = list(Technology.objects.values())
            if len(technologies)>0:
                data = {'message': "Success", 'technologies': technologies}
            else:
                data = {'message': "Technologies not found..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Technology.objects.create(
            name = jd['name'],
            description = jd['description']
        )
        data = {'message': "Success"}
        return JsonResponse(data)
        
    def put(self, request, id_t):
        jd = json.loads(request.body)
        technologies = list(Technology.objects.filter(id=id_t).values())
        if len(technologies)>0:
            technology = Technology.objects.get(id=id_t)
            technology.name = jd['name']
            technology.description = jd['description']
            technology.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Technology not found..."}
        return JsonResponse(data)
    
    def delete(self, request, id_t):
        technologies = list(Technology.objects.filter(id=id_t).values())
        if len(technologies)>0:
            Technology.objects.filter(id=id_t).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Technology not found..."}
        return JsonResponse(data)

class LicenseView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id_l=0):
        if id_l>0:
            licenses = list(License.objects.filter(id=id_l).values())
            if len(licenses)>0:
                license = licenses[0]
                data = {'message': "Success", 'license': license}
            else:
                data = {'message': "License not found..."}
            return JsonResponse(data)
        else:
            licenses = list(License.objects.values())
            if len(licenses)>0:
                data = {'message': "Success", 'licenses': licenses}
            else:
                data = {'message': "Licenses not found..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        License.objects.create(
            date_opening = jd['date_opening'],
            date_closing = jd['date_closing']
        )
        data = {'message': "Success"}
        return JsonResponse(data)
        
    def put(self, request, id_l):
        jd = json.loads(request.body)
        licenses = list(License.objects.filter(id=id_l).values())
        if len(licenses)>0:
            license = License.objects.get(id=id_l)
            license.date_opening = jd['date_opening']
            license.date_closing = jd['date_closing']
            license.save()
            data = {'message': "Success"}
        else:
            data = {'message': "License not found..."}
        return JsonResponse(data)
    
    def delete(self, request, id_l):
        licenses = list(License.objects.filter(id=id_l).values())
        if len(licenses)>0:
            License.objects.filter(id=id_l).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "License not found..."}
        return JsonResponse(data)

class ResourcesView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id_r=0):
        if id_r>0:
            resources = list(Resources.objects.filter(id=id_r).values())
            if len(resources)>0:
                resource = resources[0]
                data = {'message': "Success", 'resource': resource}
            else:
                data = {'message': "Resource not found..."}
            return JsonResponse(data)
        else:
            resources = list(Resources.objects.values())
            if len(resources)>0:
                data = {'message': "Success", 'resources': resources}
            else:
                data = {'message': "Resources not found..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Resources.objects.create(
            url = jd['url'],
            description = jd['description']
        )
        data = {'message': "Success"}
        return JsonResponse(data)
        
    def put(self, request, id_r):
        jd = json.loads(request.body)
        resources = list(Resources.objects.filter(id=id_r).values())
        if len(resources)>0:
            resource = Resources.objects.get(id=id_r)
            resource.url = jd['url']
            resource.description = jd['description']
            resource.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Resource not found..."}
        return JsonResponse(data)
    
    def delete(self, request, id_r):
        resources = list(Resources.objects.filter(id=id_r).values())
        if len(resources)>0:
            Resources.objects.filter(id=id_r).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Resource not found..."}
        return JsonResponse(data)

class Kind_ProductView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id_k_p=0):
        if id_k_p>0:
            kinds = list(Kind_Product.objects.filter(id=id_k_p).values())
            if len(kinds)>0:
                kind = kinds[0]
                data = {'message': "Success", 'kind_product': kind}
            else:
                data = {'message': "Kind_product not found..."}
            return JsonResponse(data)
        else:
            kinds = list(Kind_Product.objects.values())
            if len(kinds)>0:
                data = {'message': "Success", 'kind_products': kinds}
            else:
                data = {'message': "Kind_products not found..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Kind_Product.objects.create(
            kind = jd['kind'],
            description = jd['description']
        )
        data = {'message': "Success"}
        return JsonResponse(data)
        
    def put(self, request, id_k_p):
        jd = json.loads(request.body)
        kinds = list(Kind_Product.objects.filter(id=id_k_p).values())
        if len(kinds)>0:
            kind = Kind_Product.objects.get(id=id_k_p)
            kind.kind = jd['kind']
            kind.description = jd['description']
            kind.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Kind_product not found..."}
        return JsonResponse(data)
    
    def delete(self, request, id_k_p):
        kinds = list(Kind_Product.objects.filter(id=id_k_p).values())
        if len(kinds)>0:
            Kind_Product.objects.filter(id=id_k_p).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Kind_product not found..."}
        return JsonResponse(data)

# Views Sale

class StoreView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_s=0):
        if id_s>0:
            warehouses = list(Store.objects.filter(id=id_s).values())
            if len(warehouses)>0:
                store = warehouses[0]
                data = {'message': "Success", 'store': store}
            else:
                data = {'message': "Store not found..."}
            return JsonResponse(data)
        else:
            warehouses = list(Store.objects.values())
            if len(warehouses)>0:
                data = {'message': "Success", 'store': warehouses}
            else:
                data = {'message': "Store not found..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Store.objects.create(
            fk_product = jd['fk_product'],
            repository_url = jd['repository_url']
        )
        data = {'message': "Success"}
        return JsonResponse(data)
        
    def put(self, request, id_s):
        jd = json.loads(request.body)
        warehouses = list(Store.objects.filter(id=id_s).values())
        if len(warehouses)>0:
            store = Store.objects.get(id=id_s)
            store.fk_product = jd['fk_product']
            store.repository_url = jd['repository_url']
            store.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Store not found..."}
        return JsonResponse(data)
    
    def delete(self, request, id_s):
        warehouses = list(Store.objects.filter(id=id_s).values())
        if len(warehouses)>0:
            Store.objects.filter(id=id_s).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Store not found..."}
        return JsonResponse(data)

class StockView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_s=0):
        if id_s>0:
            stock = list(Stock.objects.filter(id=id_s).values())
            if len(stock)>0:
                existence = stock[0]
                data = {'message': "Success", 'stock': existence}
            else:
                data = {'message': "Stock not found..."}
            return JsonResponse(data)
        else:
            stock = list(Stock.objects.values())
            if len(stock)>0:
                data = {'message': "Success", 'stock': stock}
            else:
                data = {'message': "Stock not found..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Stock.objects.create(
            fk_product = jd['fk_product'],
            fk_developer = jd['fk_developer'],
            description = jd['description']
        )
        data = {'message': "Success"}
        return JsonResponse(data)
        
    def put(self, request, id_s):
        jd = json.loads(request.body)
        stock = list(Stock.objects.filter(id=id_s).values())
        if len(stock)>0:
            existence = Stock.objects.get(id=id_s)
            existence.fk_product = jd['fk_product']
            existence.fk_developer = jd['fk_developer']
            existence.description = jd['description']
            existence.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Stock not found..."}
        return JsonResponse(data)
    
    def delete(self, request, id_s):
        stock = list(Stock.objects.filter(id=id_s).values())
        if len(stock)>0:
            Stock.objects.filter(id=id_s).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Stock not found..."}
        return JsonResponse(data)

class BankView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_b=0):
        if id_b>0:
            banks = list(Bank.objects.filter(id=id_b).values())
            if len(banks)>0:
                bank = banks[0]
                data = {'message': "Success", 'bank': bank}
            else:
                data = {'message': "Bank not found..."}
            return JsonResponse(data)
        else:
            banks = list(Bank.objects.values())
            if len(banks)>0:
                data = {'message': "Success", 'banks': banks}
            else:
                data = {'message': "Banks not found..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Bank.objects.create(
            name = jd['name'],
        )
        data = {'message': "Success"}
        return JsonResponse(data)
        
    def put(self, request, id_b):
        jd = json.loads(request.body)
        banks = list(Bank.objects.filter(id=id_b).values())
        if len(banks)>0:
            bank = Bank.objects.get(id=id_b)
            bank.name = jd['name']
            bank.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Bank not found..."}
        return JsonResponse(data)
    
    def delete(self, request, id_b):
        banks = list(Bank.objects.filter(id=id_b).values())
        if len(banks)>0:
            Bank.objects.filter(id=id_b).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Bank not found..."}
        return JsonResponse(data)

class SaleView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_s=0):
        if id_s>0:
            sales = list(Sale.objects.filter(id=id_s).values())
            if len(sales)>0:
                sale = sales[0]
                data = {'message': "Success", 'sale': sale}
            else:
                data = {'message': "Sale not found..."}
            return JsonResponse(data)
        else:
            sales = list(Sale.objects.values())
            if len(sales)>0:
                data = {'message': "Success", 'sales': sales}
            else:
                data = {'message': "Sales not found..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Stock.objects.create(
            fk_stock = jd['fk_stock'],
            fk_store = jd['fk_store'],
            fk_bank = jd['fk_bank'],
            fk_client = jd['fk_client']
        )
        data = {'message': "Success"}
        return JsonResponse(data)
        
    def put(self, request, id_s):
        jd = json.loads(request.body)
        sales = list(Sale.objects.filter(id=id_s).values())
        if len(sales)>0:
            sale = Sale.objects.get(id=id_s)
            sale.fk_stock = jd['fk_stock']
            sale.fk_store = jd['fk_store']
            sale.fk_bank = jd['fk_bank']
            sale.fk_client = jd['fk_client']
            sale.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Sale not found..."}
        return JsonResponse(data)
    
    def delete(self, request, id_s):
        sales = list(Sale.objects.filter(id=id_s).values())
        if len(sales)>0:
            Sale.objects.filter(id=id_s).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Sale not found..."}
        return JsonResponse(data)

class HistoryView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
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
            fk_sale = jd['fk_sale'],
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
            history.fk_sale = jd['fk_sale']
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
