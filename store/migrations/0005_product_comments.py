# Generated by Django 4.2.8 on 2024-07-12 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='comments',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.comment'),
            preserve_default=False,
        ),
    ]
