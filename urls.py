from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # 系统应用
    path('sys/', include(('system.urls', 'system'), namespace="sys")),
    # 文章应用
    path('article/', include(('article.urls', 'article'), namespace='article')),
    # 评论应用
    path('comment/', include(('comment.urls', 'comment'), namespace='comment'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

