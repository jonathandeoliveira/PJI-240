# Generated by Django 5.1.1 on 2024-10-30 01:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Agenda",
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
                ("professor", models.CharField(max_length=100)),
                ("aluno", models.CharField(max_length=100)),
                ("valor", models.DecimalField(decimal_places=2, max_digits=10)),
                ("data", models.DateField()),
                ("hora", models.TimeField()),
                ("descricao", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
