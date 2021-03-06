# Generated by Django 2.1.dev20180428173945 on 2019-09-25 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0018_auto_20190924_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='press_aut',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='press_aut', to='data.DataTypeName'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='salin_aut',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='salin_aut', to='data.DataTypeName'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='temp_aut',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='temp_aut', to='data.DataTypeName'),
        ),
    ]
