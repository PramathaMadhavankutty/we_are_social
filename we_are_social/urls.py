"""we_are_social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views
from home import views as home_views
from accounts import views as accounts_views
from products import views as product_views
from magazines import views as magazine_views
from threads import views as forum_views
from polls import api_views
from threads import api_views as thread_api_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_views.get_index, name='index'),
    url(r'^about/$', home_views.get_about, name='about'),
    url(r'^contact/$', home_views.get_contact, name='contact'),

    # Flat pages
    url(r'^pages/', include('django.contrib.flatpages.urls')),

    # Email Auth
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),



    # Pay_pal Urls
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return/$', paypal_views.paypal_return),
    url(r'^paypal-cancel/$', paypal_views.paypal_cancel),
    url(r'^products/$', product_views.all_products),
    url(r'^magazines/$', magazine_views.all_magazines),

    # Blog Urls
    url(r'^blog/', include('reusable_blog.urls')),

    # Thread Forum
    url(r'^forum/$', forum_views.forum),
    url(r'^threads/(?P<subject_id>\d+)/$', forum_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$', forum_views.new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', forum_views.thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', forum_views.new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', forum_views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<post_id>\d+)/$', forum_views.delete_post, name='delete_post'),

    # Poll urls
    url(r'^thread/vote/(?P<thread_id>\d+)/(?P<subject_id>\d+)/$', forum_views.thread_vote, name='cast_vote'),

    # Serializers Url
    url(r'^threads/polls/$', api_views.PollViewSet.as_view()),
    url(r'^threads/polls/(?P<pk>[\d]+)$', api_views.PollInstanceView.as_view(), name='poll-instance'),
    url(r'^threads/polls/vote/(?P<thread_id>\d+)/$', api_views.VoteCreateView.as_view(), name='create_vote'),
    url(r'^threads/$', api_views.ThreadViewSet.as_view()),
    url(r'^post/update/(?P<pk>[\d+]+)/$', thread_api_views.PostUpdateView.as_view(), name='update-poll'),
    url(r'^post/delete/(?P<pk>[\d]+)/$', thread_api_views.PostDeleteView.as_view(), name='delete-poll'),

]
