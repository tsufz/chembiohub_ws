prefix = "test"
port = "8081"
base_folder = "/var/www"
password = ""
secret_key = ""
anaconda_base = ""

apache_template = '''   ProxyPass /{prefix}/reg !
    Alias /{prefix}/reg {base_folder}/{prefix}/chembiohub_ws/deployment/static/dist

    <Directory {base_folder}/{prefix}/chembiohub_ws/deployment/static/dist>
        Options Indexes FollowSymLinks Includes
        AllowOverride All
        Order allow,deny
        Allow from all
    </Directory>
  ProxyPass /{prefix}/ http://localhost:{port}/{prefix}/
  ProxyPassReverse /{prefix}/ http://localhost:{port}/{prefix}/
  #Protect the static directory
  <Location /{prefix}/>
    WebAuthExtraRedirect on
    AuthType WebAuth
    require valid-user
    RequestHeader set "X-WEBAUTH-USER" "%{WEBAUTH_USER}e"
    RequestHeader set "X-REMOTE-USER" "%{REMOTE_USER}e"
    # strip the X-Forwarded-Proto header from incoming requests
    RequestHeader unset X-Forwarded-Proto
    # set the header for requests using HTTPS
    RequestHeader set X-Forwarded-Proto https env=HTTPS
</location>
  #Protect the webservice 
  <Location /{prefix}_ws/>
    WebAuthExtraRedirect on
    AuthType WebAuth
    require valid-user
    RequestHeader set "X-WEBAUTH-USER" "%{WEBAUTH_USER}e"
    RequestHeader set "X-REMOTE-USER" "%{REMOTE_USER}e"
    # strip the X-Forwarded-Proto header from incoming requests
    RequestHeader unset X-Forwarded-Proto
    # set the header for requests using HTTPS
    RequestHeader set X-Forwarded-Proto https env=HTTPS
</location>
'''

local_settings_template = '''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{prefix}_db',
        'USER': '{prefix}_user',
        'PASSWORD': '{password}',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
SECRET_KEY = '{secret_key}'
SESSION_COOKIE_PATH = '{prefix}'

LOGIN_REDIRECT_URL = '/{prefix}/reg/#/projects/list'
WS_BASE_URL='/{prefix}_ws'

STATIC_ROOT = '{base_folder}/{prefix}/chembiohub_ws/deployment/static'
MEDIA_ROOT = '{media_folder}/{prefix}'

STATIC_URL = '/{prefix}/reg/'

STATICFILES_DIRS = (
'{base_folder}/{prefix}/src/ng-chem',
)

'''

datatbase_creation_script = '''
CREATE DATABASE {prefix}_reg_db;
CREATE USER {prefix}_reg_user;
GRANT ALL PRIVILEGES on DATABASE {prefix}_reg_db to {prefix}_reg_user;
'''

supervisor_config = '''
[program:{prefix}_reg]
directory={base_folder}/{prefix}/chembiohub_ws
command=/home/chembiohub/miniconda/envs/{prefix}/bin/gunicorn  chembiocrunch.wsgi:application -b 127.0.0.1:{port}  --workers 8 --settings=chembiocrunch.settings.{prefix} --error-logfile -
user=astretton
autostart=true
autorestart=true
redirect_stderr=True'''
