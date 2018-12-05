# Generated by Django 2.1.3 on 2018-12-03 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SubReddit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('description_html', models.TextField(blank=True, default='', editable=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SubRedditMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subreddit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='subreddits.SubReddit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_subreddits', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='subreddit',
            name='members',
            field=models.ManyToManyField(through='subreddits.SubRedditMember', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='subredditmember',
            unique_together={('subreddit', 'user')},
        ),
    ]