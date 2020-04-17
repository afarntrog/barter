from django.shortcuts import render

from django.views.generic.base import View

# review/views.py

class ReviewUser(View):
    def post(self, request, *args, **kwargs):
        return render(request, 'users/settings.html', {})

    def get(self, request, *args, **kwargs):
        # get all his reviews
        # get averagegs etc
        return render(request, 'users/settings.html', {})