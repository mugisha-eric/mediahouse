# Generated by Django 4.2.2 on 2024-11-12 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_main_abouttxt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('is_member', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='main',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
