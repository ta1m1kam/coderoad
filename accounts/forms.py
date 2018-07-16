from django import forms
from django.contrib.auth.forms import (
  AuthenticationForm
)

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateForm(UserCreationForm):
  """ユーザー登録用フォーム"""

  class Meta:
    model = User
    if User.USERNAME_FIELD == 'email':
      fields = ('email',)
    else:
      fields = ('username', 'email',)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs['class'] = 'form-control'

class LoginForm(AuthenticationForm):
  """ログインフォーム"""
  class Meta:
    model = User
    fields = ('email', 'password',)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs['class'] = 'form-control'
      if field.label == 'ユーザー名':
        field.widget.attrs['placeholder'] = 'ユーザー名 or メールアドレス'  # placeholderにフィールドのラベルを入れる
      else:
        field.widget.attrs['placeholder'] = field.label