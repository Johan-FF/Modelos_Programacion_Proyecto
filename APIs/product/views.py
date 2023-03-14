from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import *
import json

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
            name = jd['name']
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
            name = jd['name'],
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
            resource.name = jd['name']
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
