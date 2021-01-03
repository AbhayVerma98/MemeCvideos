# Generated by Django 3.0.6 on 2020-06-26 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YFI', '0005_auto_20200626_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=12)),
                ('video', models.FileField(null=True, upload_to='')),
                ('description', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Videos',
        ),
        migrations.AddField(
            model_name='templates',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='templates',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='templates',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
