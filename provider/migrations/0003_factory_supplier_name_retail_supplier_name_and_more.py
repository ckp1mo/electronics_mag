# Generated by Django 5.0.4 on 2024-05-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("provider", "0002_alter_entrepreneur_product_alter_retail_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="factory",
            name="supplier_name",
            field=models.CharField(default="Factory"),
        ),
        migrations.AddField(
            model_name="retail",
            name="supplier_name",
            field=models.CharField(default="Retail"),
        ),
        migrations.AlterField(
            model_name="entrepreneur",
            name="product",
            field=models.ManyToManyField(
                blank=True,
                related_name="entrepreneurs",
                to="provider.product",
                verbose_name="Продукты",
            ),
        ),
        migrations.AlterField(
            model_name="retail",
            name="product",
            field=models.ManyToManyField(
                blank=True,
                related_name="retails",
                to="provider.product",
                verbose_name="Продукты",
            ),
        ),
    ]
