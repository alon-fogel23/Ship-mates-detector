from django.conf.urls import url
from . import views


app_name = 'ship'

urlpatterns = [
    # /ship/
    url(r'^$', views.index, name='index'),

    # /search/
    url(r'^search_soldier/', views.search_soldier, name='search soldier'),

    # /ship/departments/
    url(r'^departments$', views.departments, name='departments'),

    # /ship/departments/<department.id>/
    url(r'^departments/(?P<department_id>[0-9]+)/$', views.details, name='details'),


    url(r'^records$', views.records, name='records'),

    # /ship/<department.id>/
    # url(r'^(?P<department_id>[0-9]+)/baknaz_team/$', views.baknaz_team, name='baknaz_team'),

    # /ship/
    # url(r'^$', views.records, name='records'),
]
