# Generated by Django 4.2.7 on 2024-02-13 14:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userapp", "0002_alter_profile_identity_card_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="position",
            field=models.CharField(
                choices=[
                    ("MD", "MD"),
                    ("CEO", "CEO"),
                    ("HOD", "HOD"),
                    ("Accountant", "Accountant"),
                    ("Secretary", "Secretary"),
                    ("Admin", "Admin"),
                    ("Store keeper", "Store keeper"),
                    ("product Manager", "product Manager"),
                    ("Delivery Agent", "Delivery Agent"),
                ],
                max_length=25,
                null=True,
            ),
        ),
    ]