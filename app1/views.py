from django.shortcuts import render
from accounts.models import *
from .models import Reception1, Reception2, Reception3
from .forms import Reception1Form, Reception2Form, Reception3Form
# django.views.genericからTemplateView、ListViewをインポート
from django.views.generic import TemplateView
# django.views.genericからCreateViewをインポート
from django.views.generic import CreateView
# django.urlsからreverse_lazyをインポート
from django.urls import reverse_lazy
# method_decoratorをインポート
from django.utils.decorators import method_decorator
# login_requiredをインポート
from django.contrib.auth.decorators import login_required


class topView(TemplateView):
    '''トップページのビュー
    '''
    # top.htmlをレンダリングする
    template_name = "app1/top.html"


@method_decorator(login_required, name='dispatch')
class Reception1View(CreateView):
    form_class = Reception1Form
    template_name = "app1/Reception1.html"
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('accounts:logout12')

    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーライド

        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録をここで行う

        parameters:
          form(django.forms.Form):
            form_classに格納されているPhotoPostFormオブジェクト
        Return:
          HttpResponseRedirectオブジェクト:
            スーパークラスのform_valid()の戻り値を返すことで、
            success_urlで設定されているURLにリダイレクトさせる
        '''
        # commit=FalseにしてPOSTされたデータを取得
        recept1 = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        recept1.email = self.request.user
        # 投稿データをデータベースに登録
        recept1.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class Reception2View(CreateView):
    form_class = Reception2Form
    template_name = "app1/Reception2.html"
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('accounts:logout12')

    def form_valid(self, form):
        # commit=FalseにしてPOSTされたデータを取得
        recept2 = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        recept2.email = self.request.user
        # 投稿データをデータベースに登録
        recept2.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class Reception3View(CreateView):
    form_class = Reception3Form
    template_name = "app1/Reception3.html"
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('accounts:logout3')

    def form_valid(self, form):
        # commit=FalseにしてPOSTされたデータを取得
        out = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        out.email = self.request.user
        # 投稿データをデータベースに登録
        out.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)
