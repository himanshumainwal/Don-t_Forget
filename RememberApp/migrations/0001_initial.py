# Generated by Django 5.0 on 2024-01-05 10:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Details",
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
                ("payment_receiver", models.CharField(max_length=100, null=True)),
                ("mode_of_payment", models.CharField(max_length=100, null=True)),
                ("transaction_id", models.CharField(max_length=100, null=True)),
                ("Payment_img", models.ImageField(upload_to="Payment_img")),
            ],
        ),
    ]
