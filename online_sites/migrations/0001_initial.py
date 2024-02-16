# Generated by Django 4.2.7 on 2023-12-14 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=25)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('profile_img', models.ImageField(default=None, upload_to='')),
                ('description', models.CharField(max_length=50)),
                ('dob', models.DateField(default=None)),
                ('loginUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='online_sites.loginuser')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('post_img', models.ImageField(default=None, upload_to=None)),
                ('song', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('tag', models.CharField(max_length=50)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_sites.profile')),
            ],
        ),
        migrations.AddField(
            model_name='loginuser',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_sites.site'),
        ),
    ]