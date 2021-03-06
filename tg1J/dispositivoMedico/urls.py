from django.conf.urls import url, include
from dispositivoMedico.views import *

urlpatterns = [

    url(r'index', index, name='index'),
    #url(r'crearDispositivoMedico', crearDispositivoMedico, name='crearDispositivoMedico'),
    #url(r'listarDispositivosMedicos', listarDispositivosMedeicos, name='listarDispositivosMedicos'),

    url(r'crearDispositivoMedico', DispositivoMedicoCreate.as_view(), name='crearDispositivoMedico'),
    url(r'listarDispositivosMedicos', DispositivoMedicoList.as_view(), name='listarDispositivosMedicos'),
    url(r'actualizarDispositivoMedico/(?P<pk>\d+)/$', DispositivoMedicoUpdate.as_view(), name='actualizarDispositivoMedico'),
    url(r'eliminarDispositivoMedico/(?P<pk>\d+)/$', DispositivoMedicoDelete.as_view(), name='eliminarDispositivoMedico'),
    url(r'^buscarDispositivoMedico/', buscarDispositivoMedico, name="buscarDispositivoMedico"),

]