from django.shortcuts import render
from django.views.generic import TemplateView


# Home Page - index.html
class HomePageView(TemplateView):

    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

    # def post(request, **kwargs):
    #     return render(request, '', context=None)


# About Page - about.html
class AboutPageView(TemplateView):
    template_name = "about.html"
