# Generated by Django 4.2.7 on 2024-02-20 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("investapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Wallet_Account_table",
            fields=[
                ("wallet_id", models.AutoField(primary_key=True, serialize=False)),
                ("wallet_balance", models.IntegerField()),
                ("wallet_address", models.CharField(max_length=10)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Wallet_Transaction_table",
            fields=[
                ("transaction_id", models.AutoField(primary_key=True, serialize=False)),
                ("transaction_type", models.CharField(max_length=20)),
                ("transaction_date", models.DateTimeField(auto_now_add=True)),
                ("wallet_address", models.CharField(max_length=10)),
                ("transaction_amount", models.BigIntegerField(null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "wallet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="transactionapp.wallet_account_table",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Investment_Update_table",
            fields=[
                ("update_id", models.AutoField(primary_key=True, serialize=False)),
                ("interest", models.IntegerField()),
                ("investment_balance", models.IntegerField()),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "investment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="investapp.investment_product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Investment_order_table",
            fields=[
                ("order_id", models.AutoField(primary_key=True, serialize=False)),
                ("unit_price", models.IntegerField()),
                ("total_price", models.IntegerField()),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("unit_ordered", models.IntegerField()),
                ("due_date", models.DateField()),
                ("amount_paid", models.IntegerField()),
                (
                    "investment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="investapp.investment_product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]