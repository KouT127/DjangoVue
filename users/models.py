from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
import uuid as uuid_lib

# Create your models here.

def imageFile(instance, filename):
    return '/'.join( ['static/media/user-images', str(instance.username), filename] )

class Department(models.Model):
    """所属 兼任可"""

    name = models.CharField(_('所属'), max_length=150, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('所属')
        verbose_name_plural = _('所属')


class User(AbstractBaseUser, PermissionsMixin):
    """ユーザー AbstractUserをコピペし編集"""

    # ユニークidを設定
    # uuid4:ランダムなidを生成
    # primarykeyとし、編集できないようにする。
    uuid = models.UUIDField(default=uuid_lib.uuid4,
                            primary_key=True, editable=False)

    # ユーザーネームのvalidator
    # ユーザー名設定時に使用する
    username_validator = UnicodeUsernameValidator()

    # ユーザー名を設定
    # _('username')はverbosename? 列別名?
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    # フルネームを設定
    full_name = models.CharField(_('氏名'), max_length=150, blank=True)
    # emailを設定
    # 空白も可能
    email = models.EmailField(_('email address'), blank=True)
    # 一対多を設定
    # 部門を紐づける
    departments = models.ManyToManyField(
        Department,
        verbose_name=_('所属'),
        blank=True,
        help_text=_('Specific Departments for this user.'),
        related_name="user_set",
        related_query_name="user",
    )

    image = models.ImageField(
        upload_to=imageFile,
        max_length=254, blank=True, null=True
    )

    # defaultでデフォルト値を設定
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    # 入った日付を設定
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    # 下記はオーバーライドしてきたメソッド等
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        # このクラス内のobjects(userManager)を使用して正規化(大文字小文字を区別しなくなる)
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        # emailを送信する？
        send_mail(subject, message, from_email, [self.email], **kwargs)

    # 既存メソッドの変更
    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name

    # Followerを取得する
    def get_followers(self):
        relations = Relationship.objects.filter(follow=self)
        return relations

    def get_follows(self):
        relations = Relationship.objects.filter(follower=self)
        return relations

class Relationship(models.Model):
    follow = models.ForeignKey(User, related_name='follows', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    class Meta:
        # 複合ユニークキー
        unique_together = ('follow', 'follower')