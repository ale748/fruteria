from django.conf.urls import patterns, url

urlpatterns = patterns(
    'fruteria_app.views',
    url('^$', 'index',name='fruteria_index'),
    url('^new_order$','newOrder', name='new_order'),
    url('^new_product$','newProduct', name='new_product'),
    url('^new_type$','newType', name='new_type'),
    url('^new_unit_type$','newUnitType', name='new_unit_type'),




)