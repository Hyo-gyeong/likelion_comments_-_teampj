from django.contrib import admin
from django.urls import path
from crudapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('<int:post_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('<int:post_id>/edit', views.edit, name="edit"),
    path('<int:post_id>/delete', views.delete, name="delete"),
    path('<int:post_id>/comment/create', views.comment_create, name="comment_create"),
    path('<int:post_id>/comment/<int:comment_id>/delete', views.comment_delete, name="comment_delete"),
    path('<int:post_id>/comment/<int:comment_id>/reply', views.comment_reply, name="comment_reply"),
    path('<int:post_id>/comment/<int:comment_id>/delete/<int:commentReply_id>/comment_reply_delete', views.comment_reply_delete, name="comment_reply_delete"),
]
