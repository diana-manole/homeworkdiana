# Generated by Django 4.1.5 on 2023-02-27 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=5, unique=True)),
                ("date_added", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Woman",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("coats", models.CharField(max_length=15)),
                ("dresses", models.CharField(max_length=40)),
                ("tops", models.CharField(max_length=200)),
                ("trousers", models.CharField(max_length=200)),
                ("shorts", models.CharField(max_length=200)),
                ("skirts", models.CharField(max_length=200)),
                ("date_added", models.DateField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Second.menu"
                    ),
                ),
            ],
        ),
    ]
