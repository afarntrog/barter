from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView
from django.views.generic.base import View

from core.models import Product, ProductViewCount, ProductImages
from .forms import ProductPostForm
from django.db.models import F
import json


class ProductList(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        return render(request, 'core/product_listing.html', {'products': products, })


class ProductDetail(View):
    def get(self, request, *args, **kwargs):
        product = Product.objects.get(uid= kwargs['pk'])
        total_views = record_view(request, kwargs['pk'])
        product.view_count = F('view_count') + total_views
        product.save()
        return render(request, 'app-marketplace/app-description.html', {'product': product, 'total_views': total_views})


# Count unique views. If it is new view then return 1 and update the counter table with ip etc.
def record_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if not ProductViewCount.objects.filter(product=product, ip=request.META['REMOTE_ADDR']):
        view = ProductViewCount(product=product, ip=request.META['REMOTE_ADDR'], )
        view.save()
        return 1
    return 0  # ProductViewCount.objects.filter(product=product).count()


class PostProduct(LoginRequiredMixin, FormView):
    form_class = ProductPostForm
    # initial = {'hide_post': False}
    template_name = 'core/post_product.html'  # Replace with your template.
    success_url = '/'  # Replace with your URL or reverse().

    def form_valid(self, request, form, files):
        """ Enters here iff form is valid in the post() method """
        print(request.user)
        tags = form.cleaned_data[
            'tags']  # Returns a string representation of a  dictionaries: [{"value":"i'm_a_tag"},{"value":"tag_me"}]
        tags = json.loads(tags)  # Use json to convert it into a dic
        product = Product(
            owner=request.user,
            title=form.cleaned_data['product_title'],
            desc=form.cleaned_data['product_description'],
        )
        product.save()

        # Add tag list to taggit
        [product.tags.add(tag['value']) for tag in tags]
        product.save()

        for image in files:
            ProductImages(product=product, image=image).save()

        return super(PostProduct, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('images')
        print([f for f in files])
        if form.is_valid():
            return self.form_valid(request, form, files)
        else:
            print("Not valid")
            return self.form_invalid(form)

# from .forms import MyForm

# class MyFormView(View):
#     form_class = MyForm
#     initial = {'key': 'value'}
#     template_name = 'form_template.html'
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             # <process form cleaned data>
#             return HttpResponseRedirect('/success/')
#
#         return render(request, self.template_name, {'form': form})
