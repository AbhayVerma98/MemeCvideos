# Generated by Django 3.0.6 on 2020-06-26 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YFI', '0006_auto_20200626_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templates',
            name='category',
            field=models.CharField(choices=[('All', 'All'), ('New', 'New'), ('Popular', 'Popular'), ('Random', 'Random'), ('Anime', 'Anime'), ('Cartoon', 'cartoon'), ('Celebrity', 'Celebrity'), ('Web series', 'Web series')], max_length=12),
        ),
        migrations.AlterField(
            model_name='video',
            name='category',
            field=models.CharField(choices=[('All', 'All'), ('New', 'New'), ('Popular', 'Popular'), ('Celebrity', 'Celebrity'), ('Vira', 'Viral'), ('Movies', 'Movies'), ('Web series', 'Web series'), ('Funny', 'Funny'), ('Abusive', 'Abusive')], max_length=12),
        ),
    ]
