# Generated by Django 5.0.6 on 2024-08-12 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('client', models.CharField(max_length=100)),
                ('website', models.URLField(blank=True, null=True)),
                ('completed_date', models.DateField()),
                ('image', models.ImageField(upload_to='portfolio_images/')),
                ('social_links', models.JSONField(blank=True, default=dict)),
                ('categories', models.ManyToManyField(related_name='portfolio_items', to='portfolio.category')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='projects/')),
                ('description', models.CharField(max_length=500)),
                ('details_url', models.URLField(blank=True, null=True)),
                ('category', models.ManyToManyField(to='portfolio.projectcategory')),
            ],
        ),
    ]
