from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone



class AboutSection(models.Model):
    title = models.CharField(max_length=200, default="about myself")
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    content = models.TextField()
    additional_content = models.TextField(blank=True, null=True)
    button_text = models.CharField(max_length=50, default="More Info")
    button_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    


class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/')
    description = models.CharField(max_length=500)
    category = models.ManyToManyField(ProjectCategory)
    details_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    


class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    client = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    completed_date = models.DateField()
    image = models.ImageField(upload_to='portfolio_images/')
    detail_image = models.ImageField(upload_to='portfolio_detail_images/', blank=True, null=True)
    social_links = models.JSONField(default=dict, blank=True)  # Store social links as a dictionary

    def __str__(self):
        return self.title
    


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog_images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()  # Ensure this field exists
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
    

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.first_name
