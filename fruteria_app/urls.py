from django.conf.urls import patterns, url

urlpatterns = patterns('fruteria_app.views',
    url('^$', 'index',name='fruteria_index'),
    url('^new_order$','new', name='make_order')
)