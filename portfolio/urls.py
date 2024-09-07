from django.urls import path
from .views import index,about_us,blog,ContactView,portfolio_detail,portfolio,portfolio,single_blog
from . import views

urlpatterns = [
    path('',index, name="index-page"),
    path('about_us/',about_us, name="about_us-page"),
    path('blog/',blog, name="blog-page"),
    path("contact/",ContactView.as_view(),name="contact-page"),
    path('portfolio/<int:pk>/', views.portfolio_detail, name="portfolio_detail"),
    path('portfolio/',portfolio, name="portfolio-page"),
    path('post/<slug:slug>/',single_blog, name="post_detail"),

]