from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('',views.index,name="index"),
    path("client/",views.client , name="client"),
    path("contact/",views.contact , name="contact"),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('home/', views.home, name='home'),
    path('birth/', views.birth,name='birth_chart'),
    path('comment/', views.comment,name='comment'),
    path('images/', views.images,name='images'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)