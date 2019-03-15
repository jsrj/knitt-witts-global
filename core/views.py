from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect


# Home Page - index.html
class HomePageView(TemplateView):

    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
        # return redirect('http://www.knitwittsbypaulette.com/')

    # def post(request, **kwargs):
    #     return render(request, '', context=None)


# About Page - about.html
# class AboutPageView(TemplateView):
#     template_name = "about.html"
