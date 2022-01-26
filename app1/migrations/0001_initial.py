# Generated by Django 3.2.8 on 2022-01-17 09:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reception3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OutHospital', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='帰棟時刻')),
                ('email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '帰院時刻情報',
                'verbose_name_plural': '帰院時刻データ',
            },
        ),
        migrations.CreateModel(
            name='Reception2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(choices=[('患者様と面会', '患者様と面会'), ('荷物の受け渡し', '荷物の受け渡し'), ('医師と面談', '医師と面談')], max_length=20, verbose_name='来院目的')),
                ('accompany', models.BooleanField(blank=True, choices=[(True, 'はい'), (False, 'いいえ')], default='はい', null=True, verbose_name='同伴者はいらっしゃいますか')),
                ('bt1', models.DecimalField(blank=True, decimal_places=1, default=36.0, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(34.0), django.core.validators.MaxValueValidator(43.0)], verbose_name='体温(面会者)')),
                ('bt2', models.DecimalField(blank=True, decimal_places=1, default=36.0, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(34.0), django.core.validators.MaxValueValidator(43.0)], verbose_name='体温(同伴者)')),
                ('companion_last_name', models.CharField(max_length=100, null=True, verbose_name='同伴者様の姓')),
                ('companion_first_name', models.CharField(max_length=100, null=True, verbose_name='同伴者様の名')),
                ('relationship2', models.CharField(choices=[('配偶者', '配偶者'), ('子', '子'), ('父・母', '父・母'), ('兄・弟・姉・妹', '兄・弟・姉・妹'), ('兄・弟・姉・妹の配偶者', '兄・弟・姉・妹の配偶者'), ('子の配偶者', '子の配偶者'), ('配偶者の兄・弟・姉・妹', '配偶者の兄・弟・姉・妹'), ('同伴者なし', '同伴者なし')], max_length=30, null=True, verbose_name='続柄')),
                ('InHospital', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='来棟時刻')),
                ('email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '事前未登録者情報',
                'verbose_name_plural': '事前未登録者データ',
            },
        ),
        migrations.CreateModel(
            name='Reception1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bt1', models.DecimalField(blank=True, decimal_places=1, default=36.0, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(34.0), django.core.validators.MaxValueValidator(43.0)], verbose_name='体温(面会者)')),
                ('bt2', models.DecimalField(blank=True, decimal_places=1, default=36.0, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(34.0), django.core.validators.MaxValueValidator(43.0)], verbose_name='体温(同伴者)')),
                ('InHospital', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='来棟時刻')),
                ('email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '事前登録情報_1',
                'verbose_name_plural': '事前登録者データ(面会時)',
            },
        ),
        migrations.CreateModel(
            name='Reception0',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(choices=[('患者様と面会', '患者様と面会'), ('荷物の受け渡し', '荷物の受け渡し'), ('医師と面談', '医師と面談')], max_length=20, verbose_name='来院目的')),
                ('accompany', models.BooleanField(blank=True, choices=[(True, 'はい'), (False, 'いいえ')], default='はい', null=True, verbose_name='同伴者はいらっしゃいますか')),
                ('companion_last_name', models.CharField(max_length=100, null=True, verbose_name='同行者様の姓')),
                ('companion_first_name', models.CharField(max_length=100, null=True, verbose_name='同行者様の名')),
                ('relationship2', models.CharField(choices=[('配偶者', '配偶者'), ('子', '子'), ('父・母', '父・母'), ('兄・弟・姉・妹', '兄・弟・姉・妹'), ('兄・弟・姉・妹の配偶者', '兄・弟・姉・妹の配偶者'), ('子の配偶者', '子の配偶者'), ('配偶者の兄・弟・姉・妹', '配偶者の兄・弟・姉・妹'), ('同伴者なし', '同伴者なし')], max_length=30, null=True, verbose_name='続柄')),
                ('email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '事前登録情報_0',
                'verbose_name_plural': '事前登録者データ(事前)',
            },
        ),
    ]