from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.solicitacao_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^teleconsultor/new/', views.teleconsultor_new, name='teleconsultor_new'),
    url(r'^solicitante/new/', views.solicitante_new, name='solicitante_new'),
    url(r'^solicitacao/new/', views.solicitacao_new, name='solicitante_new'),
]