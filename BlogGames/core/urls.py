from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'core'

urlpatterns = [
    path('home', views.index, name='home'),
    path('', views.index, name='index'),
    path('contato', views.contato, name='contato'),
    path('sobre', views.sobre, name='sobre'),
    path('blog', views.blog, name='blog'),
    path('post/<int:id>/', views.detail, name="detail"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
