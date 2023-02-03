from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    
    path('',views.index, name='home'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('itr', views.itr, name='itr'),
    path('gst_tax_return', views.gst_tax_return, name='gst_tax_return'),
    path('project_details', views.project, name='project_details'),
    path('eventsBlog', views.eventsBlog, name='eventsBlog'),
    path('blogDetail',views.blogDetail, name='blogDetail'),
    path('blog',views.BlogList.as_view(),name='blog'),
    path('event',views.EventList.as_view(),name='events'),
    path('<slug:slug>',views.EventDetail.as_view(),name='event_detail'),
    path('<slug:slugBlog>',views.BlogDetail.as_view(),name='blog_detail'),
]