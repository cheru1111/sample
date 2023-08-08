# Generated by Django 4.2.3 on 2023-08-06 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eco_app', '0004_subcategorymodel_cartmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eco_app.categorymodel')),
                ('Customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eco_app.customermodel')),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eco_app.product')),
                ('SubCategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eco_app.subcategorymodel')),
            ],
        ),
    ]
