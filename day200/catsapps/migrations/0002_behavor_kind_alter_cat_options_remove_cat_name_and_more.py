# Generated by Django 4.1.5 on 2023-02-15 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catsapps", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Behavor",
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
                ("behavor", models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name="Kind",
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
                ("kind", models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterModelOptions(
            name="cat",
            options={},
        ),
        migrations.RemoveField(
            model_name="cat",
            name="name",
        ),
        migrations.RemoveField(
            model_name="color",
            name="data_added",
        ),
        migrations.AlterField(
            model_name="color",
            name="color",
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name="Name",
        ),
    ]
