# urls.py
from django.urls import path
# viewsモジュールをインポート
from . import views
from django.contrib.auth import views as auth_views

# URLパターンを逆引きできるように名前を付ける
app_name = 'accounts'

# URLパターンを登録するための変数
urlpatterns = [
    # サインアップページのビュー呼び出し
    # 「http(s)://<ホスト名>/signup/」へのアクセスに対し,
    # viewsモジュールのSignUpViewをインスタンス化する
    path('signup/', views.SignUpView.as_view(), name='signup'),

    # サインアップ完了ページのビュー呼び出し
    # 「http(s)://<ホスト名>/signup_success/」へのアクセスに対し,
    # viewsモジュールのSignUpSuccessViewをインスタンス化する
    path('signup_success/', views.SignUpSuccessView.as_view(), name='signup_success'),

    # ログインページの表示
    # 「http(s)://<ホスト名>/signup_success/」へのアクセスに対し,
    # django.contrib.auth.views.LoginViewsをインスタンス化して
    # ログインページを表示する
    path('login1/',
         # ログイン用のテンプレート(フォーム)をレンダリング
         auth_views.LoginView.as_view(template_name='login1.html'), name='login1'
         ),
    path('login2/',
         # ログイン用のテンプレート(フォーム)をレンダリング
         auth_views.LoginView.as_view(template_name='login2.html'), name='login2'
         ),
    path('login3/',
         # ログイン用のテンプレート(フォーム)をレンダリング
         auth_views.LoginView.as_view(template_name='login3.html'), name='login3'
         ),

    # ログアウトを実行
    # 「http(s)://<ホスト名>/signup_success/」へのアクセスに対し,
    # django.contrib.auth.views.LogoutViewsをインスタンス化して
    # ログアウトさせる]

    path('logout12/', auth_views.LogoutView.as_view(template_name='logout12.html'), name='logout12'),

    path('logout3/',
         auth_views.LogoutView.as_view(template_name='logout3.html'),
         name='logout3'
         ),
]
