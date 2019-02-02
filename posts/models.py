from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as _

class Post(models.Model):  
    user = models.ForeignKey(User, verbose_name=_('ユーザー'), on_delete=models.CASCADE)
    content = models.CharField(_('内容'), max_length=140)

    created_at = models.DateTimeField(_('投稿日'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新日'), auto_now=True)
    
    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _('投稿')
        verbose_name_plural = _('投稿')
