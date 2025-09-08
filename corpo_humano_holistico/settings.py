# ARQUIVO: corpo_humano_holistico/settings.py

import os
from pathlib import Path

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave Secreta
SECRET_KEY = 'django-insecure-#=q07^$ia8+u%gd(p-cp)#yq%8irgk33d_f9^80wkevwf1rxtm'

# Modo Debug
DEBUG = True

ALLOWED_HOSTS = []

# Aplicações Instaladas (Ordem Correta)
INSTALLED_APPS = [
    # Nossos Apps
    'core.apps.CoreConfig',
    'usuarios.apps.UsuariosConfig',
    'anatomia.apps.AnatomiaConfig',
    'sistema_osseo',
    'sistema_muscular',
    'sistema_nervoso',
    'sistema_cardiovascular',
    'sistema_respiratorio',
    'sistema_digestivo',
    'sistema_urinario',
    'sistema_endocrino',
    'sistema_tegumentar',
    'sistema_reprodutor',
    'sistema_hematopoietico',
    'sistema_circulatorio',
    'sistema_immune',
    'metabolismo',
    'psicologia',
    'simbologia',
    
    # Apps de Terceiros
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    # Apps Padrão do Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', # Não é necessário sem o allauth
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'corpo_humano_holistico.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'corpo_humano_holistico.wsgi.application'

# Banco de Dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

# Validação de Senhas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internacionalização
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Arquivos Estáticos e de Mídia
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# Tipo de Campo de Chave Primária Padrão
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Chave da API do Google AI para a Aura
GEMINI_API_KEY = "SUA_CHAVE_API_AQUI" # Lembre-se de colocar sua chave aqui

# Redirecionamentos de Login e Logout para o nosso sistema
LOGIN_REDIRECT_URL = 'dashboard' 
LOGOUT_REDIRECT_URL = 'core:homepage'
LOGIN_URL = 'usuarios:login'