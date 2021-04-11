"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os  # 导入操作系统模块
# 项目根目录  # /home/python/Python_code/python_django/demo
# __file__代表当前模块文件  __name__而 被导时 是当前模块的名，当前是__main
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# 密钥:后期在做某些功能时,需要进行签名/加密时使用,Django自带
SECRET_KEY = '3hgca2$llke@l@vmy!%a98fly@+_wmriswsa3ey)-#lc0qp4&0'

# SECURITY WARNING: don't run with debug turned on in production!
# Django默认就开启的调试模式,将来项目部署上线时,需要把它改为False
# Django对静态文件的访问不太擅长,只有在DEBUG模式为True时,才会提供静态文件访问的能力,如果DEBUG为False时,
# Django无法会静态文件提供访问的能力, 因为Django框架是动态业务逻辑框架(nginx)
DEBUG = True

# allowed hosts 允许那些host访问Django服务器
ALLOWED_HOSTS = []


# Application definition

# installed apps 注册 应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',  # 新注册的子应用users
    'request_response.apps.RequestResponseConfig',
    'classview.apps.ClassviewConfig',  # 注册新的子应用 测试 类视图
    # 只有在子应用中使用了模型要迁移建表,及子应用中使用了'模板'才需要注册应用,如果应用中只有视图和路由的逻辑,那么此应用可以不注册
    'booktest.apps.BooktestConfig'  # 演示ORM操作数据库
]

# middle ware中间件:类似于flask请求勾子
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Django默认就开启session缓存机制  SessionMiddleware session 中间件
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',  # postman测试 先关闭csrf保护
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 注册中间件 # 请求是自上而下,响应是自下而上
    'middle_ware.my_middleware1',
    'middle_ware.my_middleware2',
]

# root urlconf 工程路由的入口（视图函数定义 url需要进入的入口）
ROOT_URLCONF = 'demo.urls'

# templates 模板文件配置项 !!!  django 不擅长模板文件 一般django用于前后端分离 模板文件 由nginx 服务器处理
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],  # 指定模板文件的加载路径,类似 flask指定templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 项目部署 ‘上线’ 后,程序的启动入口
WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# 数据库的配置项: 默认用是sqlite3,将来换成mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 引擎选择mysql
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'mysql',  # 数据库用户密码
        'NAME': 'django',  # 数据库名字
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

# 密码认证校验配置项目
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# 设置语言 默认是英语 可以调整为简体中文 'zh-Hans'
LANGUAGE_CODE = 'en-us'
# 时区: 默认是世界时区  可以改为亚洲上海  Asia-Shanghai
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
# 静态文件的路由前缀
STATIC_URL = '/static/'

# 指定静态文件夹目录  列表
# 在Djanog中可以访问静态文件的原因是因为开启DEBUG模式
STATICFILES_DIRS = [
    # 设置要访问的查找静态文件的路径 绝对路径 根项目的绝对路径 加上 文件夹名称
    os.path.join(BASE_DIR, 'static_files'),
    # os.path.join(BASE_DIR, 'static_files/goods'),
]

# caches 配置缓存（缓存后端为Redis） 设置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",  # 地址要注意 redis 配置文件conf bind的是什么 这里选择1号数据库
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"  # 会话缓存别名
