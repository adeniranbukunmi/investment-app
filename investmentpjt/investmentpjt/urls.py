"""
URL configuration for investmentpjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from investmentpjt.userapp.views import SignUpView
from investmentpjt.investapp.views import marketPlace
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', marketPlace ,name='home'),
    path('about/',TemplateView.as_view(template_name='about.html'),name='about'),
    path('deals/',TemplateView.as_view(template_name='deals.html'),name='deals'),
    path('reservation/',TemplateView.as_view(template_name='reservation.html'),name='reservation'),
    re_path(r'^accounts/',include('django.contrib.auth.urls')),
    re_path(r'^accounts/signup/$',SignUpView.as_view(), name="signup"),
    re_path(r'^userapp/',include('investmentpjt.userapp.urls')),
    re_path(r'^investapp/',include('investmentpjt.investapp.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns() it generate a url pattern that serve static files located in the static root specified in the settings

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static() this ia a function in django that takes two argument
# settings.MEDIA_URL (this is the first argument passed: this is a shortcut to tell django that alaye, check settings.Media_url for media path)
# document_root=settings.MEDIA_ROOT (this is the second argument telling django that the medias are in the system file explorer) question: why are we using this method

# In summary, these lines of code ensure that during development, Django can serve static and media files to the browser when requested by the client. It's important to note that serving static and media files this way during production is not recommended. Instead, you should configure your web server (e.g., Nginx, Apache) or use a content delivery network (CDN) to serve static and media files for better performance and security. 

