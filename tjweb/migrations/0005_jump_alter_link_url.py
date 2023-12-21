# Generated by Django 5.0 on 2023-12-21 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tjweb', '0004_alter_article_belong'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jump',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='jump_logo', verbose_name='跳转图标')),
                ('title', models.CharField(max_length=128, verbose_name='显示内容')),
                ('url', models.URLField(blank=True, null=True, verbose_name='跳转地址')),
            ],
        ),
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(blank=True, verbose_name='跳转地址'),
        ),
    ]
