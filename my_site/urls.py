from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic import TemplateView

# from helloworld

urlpatterns = patterns(
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('helloworld.views',
    (r'^test/', 'hello'),
    (r'^test_ajax/', 'test_ajax'),
    (r'^home/', 'home'),
    (r'^about/', TemplateView.as_view(template_name="helloworld/about.html")),
    (r'^new_check_task/$', 'new_check_task'),
    (r'^add_task/$', 'add_task'),
    (r'^check_task_list/$', 'check_task_list'),
    (r'^task_detail/', 'task_detail'),
    (r'^table_check/', 'get_table_check'),
    (r'^upload_index/', TemplateView.as_view(template_name="helloworld/upload.html")),
    (r'^upload/', 'upload'),
)

urlpatterns += patterns('dealsupplier.views',
    (r'^dealtask/home/', TemplateView.as_view(template_name="dealsupplier/home.html")),
    (r'^dealtask/showpage', 'task_show_page'),
    (r'^dealtask/list/$', TemplateView.as_view(template_name="dealsupplier/task_list.html")),
    (r'^dealtask/$', 'deal_task_list'),
    (r'^dealtask/(?P<id>[0-9]+)/$', 'deal_task'),
    (r'^dealtask/about/', TemplateView.as_view(template_name="dealsupplier/about.html")),
)

urlpatterns += patterns('searchcompare.views',
    (r'^searchcompare/test/$', 'gethtml'),
    (r'^searchcompare/hello/$', TemplateView.as_view(template_name="searchcompare/test.html")),
    (r'^searchcompare', 'comment_record_list'),
)