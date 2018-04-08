# Generated by Django 2.0.3 on 2018-04-02 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_sheet', '0003_auto_20180330_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='singer_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Singer.name+', to='music_sheet.Singer', verbose_name='歌手'),
        ),
    ]
