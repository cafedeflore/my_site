from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

# from helloworld

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', 'helloworld.views.hello'),
    url(r'^test_ajax/', 'helloworld.views.test_ajax', name="testajax"),

    url(r'^home/', 'helloworld.views.home'),
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
    url(r'^new_check_task/$', 'helloworld.views.new_check_task'),
    url(r'^add_task/$', 'helloworld.views.add_task'),
    url(r'^check_task_list/$', 'helloworld.views.check_task_list'),
    url(r'^task_detail/', 'helloworld.views.task_detail'),
    url(r'^table_check/', 'helloworld.views.get_table_check'),

    url(r'^upload_index/', TemplateView.as_view(template_name="upload.html")),
    url(r'^upload/', 'helloworld.views.upload'),
]
