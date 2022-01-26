from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    '''サインアップページのビュー

    '''
    # forms.pyで完成したフォームのクラス
    form_class = CustomUserCreationForm
    # レンダリングするテンプレート
    template_name = 'signup.html'
    # サインアップ完了後のリダイレクト先のURLパターン
    success_url = reverse_lazy('accounts:signup_success')

    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーライド

        フォームのバリデーションを通過した時に呼ばれる
        フォームデータの登録を行う

        parameters:
            form(django.forms.Form):
                form_classに格納されているCustomUserCreationFormオブジェクト
        Return:
            HttpResponseRedirectオブジェクト:
                スーパークラスのform_valid()の戻り値を返すことで、success_urlで設定されているURLにリダイレクトさせる
        '''
        # formオブジェクトのフィールドの値をデータベースに保存
        user = form.save()
        self.object = user
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpRseponseRedirect)
        return super().form_valid(form)


class SignUpSuccessView(TemplateView):
    '''
    '''
    template_name = "signup_success.html"
