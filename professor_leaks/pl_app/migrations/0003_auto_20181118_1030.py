# Generated by Django 2.1 on 2018-11-18 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pl_app', '0002_college_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pl_app.College'),
        ),
    ]