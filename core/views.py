from django.shortcuts import render
from django.views.generic import TemplateView
# from django.shortcuts import redirect


# Home Page - index.html
class HomePageView(TemplateView):

    def get(self, request, **kwargs):
        return render(request, 'index.html', {
            'title': "Knit Witts Global",
            'subTitle': "Coming Soon",
            'visitorMessage': "Knit Witts Global is coming soon. In the meantime, check us out on these social networks",
            'newsletterMessage': "Join the waiting list for the beta. We'll keep you posted.",
            'socialLinks': [
                {
                    'name': "Facebook",
                    'iconClass': "fab fa-facebook-square",
                    'href': "https://www.facebook.com/KnitWittsByPauletteLack/",
                },
                {
                    'name': "Instagram",
                    'iconClass': "fab fa-instagram",
                    'href': "https://www.instagram.com/knitwittsbypaulette/",
                },
                {
                    'name': "Pinterest",
                    'iconClass': "fab fa-pinterest-square",
                    'href': "https://www.pinterest.com/paulettegemjars/",
                },
            ],
        })

# About Page - about.html
# class AboutPageView(TemplateView):
#     template_name = "about.html"
