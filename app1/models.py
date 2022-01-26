# import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from accounts.models import *
from django.contrib.auth import get_user_model

# receptionクラス


class Reception0(models.Model):
    email = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    P_CHOICES = [
        ("患者様と面会", "患者様と面会"),
        ("荷物の受け渡し", "荷物の受け渡し"),
        ("医師と面談", "医師と面談")
    ]
    purpose = models.CharField(
        verbose_name='来院目的', max_length=20, choices=P_CHOICES)
    A_CHOICES = [
        (True, "はい"),
        (False, "いいえ"),
    ]
    accompany = models.BooleanField(
        verbose_name="同伴者はいらっしゃいますか",
        choices=A_CHOICES,
        blank=True,
        null=True,
        default="はい"
    )
    companion_last_name = models.CharField(
        verbose_name='同行者様の姓', max_length=100, null=True)
    companion_first_name = models.CharField(
        verbose_name='同行者様の名', max_length=100, null=True)
    R2_CHOICES = [
        ("配偶者", "配偶者"),
        ("子", "子"),
        ("父・母", "父・母"),
        ("兄・弟・姉・妹", "兄・弟・姉・妹"),
        ("兄・弟・姉・妹の配偶者", "兄・弟・姉・妹の配偶者"),
        ("子の配偶者", "子の配偶者"),
        ("配偶者の兄・弟・姉・妹", "配偶者の兄・弟・姉・妹"),
        ("同伴者なし", "同伴者なし")
    ]
    relationship2 = models.CharField(
        verbose_name='続柄', max_length=30, choices=R2_CHOICES,
        null=True)

    class Meta:
        verbose_name = '0.事前登録情報'
        verbose_name_plural = '0.事前登録者データ(事前)'


class Reception1(models.Model):
    email = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    bt1 = models.DecimalField(
        verbose_name="体温(面会者)",
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True,
        default=36.0,
        validators=[MinValueValidator(34.0), MaxValueValidator(43.0), ]
    )
    bt2 = models.DecimalField(
        verbose_name="体温(同伴者)",
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True,
        default=36.0,
        validators=[MinValueValidator(34.0), MaxValueValidator(43.0), ]
    )
    InHospital = models.DateTimeField(
        verbose_name='来棟時刻',
        default=timezone.now, null=True)

    class Meta:
        verbose_name = '1.事前登録情報'
        verbose_name_plural = '1.事前登録者データ(面会時)'


class Reception2(models.Model):
    email = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    P_CHOICES = [
        ("患者様と面会", "患者様と面会"),
        ("荷物の受け渡し", "荷物の受け渡し"),
        ("医師と面談", "医師と面談")
    ]
    purpose = models.CharField(
        verbose_name='来院目的', max_length=20, choices=P_CHOICES)
    A_CHOICES = [
        (True, "はい"),
        (False, "いいえ"),
    ]
    accompany = models.BooleanField(
        verbose_name="同伴者はいらっしゃいますか",
        choices=A_CHOICES,
        blank=True,
        null=True,
        default="はい"
    )
    bt1 = models.DecimalField(
        verbose_name="体温(面会者)",
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True,
        default=36.0,
        validators=[MinValueValidator(34.0), MaxValueValidator(43.0), ]
    )
    bt2 = models.DecimalField(
        verbose_name="体温(同伴者)",
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True,
        default=36.0,
        validators=[MinValueValidator(34.0), MaxValueValidator(43.0), ]
    )
    companion_last_name = models.CharField(
        verbose_name='同伴者様の姓', max_length=100, null=True)
    companion_first_name = models.CharField(
        verbose_name='同伴者様の名', max_length=100, null=True)
    R2_CHOICES = [
        ("配偶者", "配偶者"),
        ("子", "子"),
        ("父・母", "父・母"),
        ("兄・弟・姉・妹", "兄・弟・姉・妹"),
        ("祖父・祖母", "祖父・祖母"),
        ("兄・弟・姉・妹の配偶者", "兄・弟・姉・妹の配偶者"),
        ("子の配偶者", "子の配偶者"),
        ("配偶者の兄・弟・姉・妹", "配偶者の兄・弟・姉・妹"),
        ("同伴者なし", "同伴者なし")
    ]
    relationship2 = models.CharField(
        verbose_name='続柄', max_length=30, choices=R2_CHOICES,
        null=True)
    InHospital = models.DateTimeField(
        verbose_name='来棟時刻',
        default=timezone.now, null=True)

    class Meta:
        verbose_name = '2.事前未登録者情報'
        verbose_name_plural = '2.事前未登録者データ'


class Reception3(models.Model):
    email = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    OutHospital = models.DateTimeField(
        verbose_name='帰棟時刻',
        default=timezone.now, null=True)

    class Meta:
        verbose_name = '3.帰院時刻情報'
        verbose_name_plural = '3.帰院時刻データ'
