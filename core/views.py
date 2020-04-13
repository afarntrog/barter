from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from core.models import Product, ProductViewCount
# Create your views here.
class ProductDetail(View):
    def get(self, request, *args, **kwargs):
        product = Product.objects.get(uid='eeeefd03-a342-48d2-bb43-74177313135c')#kwargs['pk'])
        record_view(request, kwargs['pk'])
        # product = Product.objects.get(uid=)
        return render(request, 'app-marketplace/app-description.html', {'product': product})



# Count unique views
def record_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if not ProductViewCount.objects.filter(
            product=product,
            ip=request.META['REMOTE_ADDR']):
        view = ProductViewCount(product=product,
                                ip=request.META['REMOTE_ADDR'],)
        view.save()
    return ProductViewCount.objects.filter(product=product).count()
