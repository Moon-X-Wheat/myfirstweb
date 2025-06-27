Django 第一个网站复习笔记

本文档总结了从零开始使用 Django 搭建个人网站的完整流程，适用于初学者。

⸻

🧱 创建虚拟环境

建议为每个 Django 项目创建一个独立的虚拟环境，避免依赖冲突。

# 安装 virtualenv（如果尚未安装）
pip install virtualenv

# 创建虚拟环境（xuni 为环境名）
python -m venv xuni

# 激活虚拟环境
# macOS/Linux
source xuni/bin/activate
# Windows
xuni\Scr


⸻

📦 安装 Django 并创建项目

pip install django

# 创建项目 myfirstweb
django-admin startproject myfirstweb

# 进入项目目录
cd myfirstweb

# 创建 app playground
python manage.py startapp playground

在 settings.py 中注册 app：

INSTALLED_APPS = [
    ...,
    'playground',
]


⸻

🌐 添加 URL 和视图函数

playground/views.py

from django.http import HttpResponse
from django.shortcuts import render

def say_hello(request):
    return HttpResponse("Hello world")

def home(request):
    return render(request, 'home.html')

playground/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('hello/', views.say_hello),
]

在 myfirstweb/urls.py 中引入 app 的 urls：

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('playground.urls')),
]


⸻

📄 创建模板文件
	•	在项目中创建 templates 文件夹，与 playground 平级。
	•	在 settings.py 中配置：

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

创建 templates/home.html：

<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>主页</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>欢迎访问我的网站。</p>
</body>
</html>


⸻

🛢️ 创建模型并迁移数据库

playground/models.py 示例：

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.CharField(max_length=200)

执行以下命令生成迁移文件并应用：

python manage.py makemigrations
python manage.py migrate


⸻

🔐 创建超级用户（用于访问后台）

python manage.py createsuperuser

之后访问 http://127.0.0.1:8000/admin 进入后台管理界面。

⸻

💄 使用 Bootstrap 与模板继承

templates/base.html：

<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}我的网站{% endblock %}</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container">
    {% block content %}{% endblock %}
  </div>
</body>
</html>

home.html 中继承：

{% extends 'base.html' %}

{% block title %}主页{% endblock %}

{% block content %}
<h1>欢迎！</h1>
<p>这是我的第一个 Django 网页。</p>
{% endblock %}


⸻

🚀 启动开发服务器

python manage.py runserver

在浏览器中访问 http://127.0.0.1:8000 查看效果。

⸻

