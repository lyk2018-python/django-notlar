#### Views model.view.template
Kullanıcının göreceği kısım

#### Basit bir view;
"views.py" dosyasına eklenir
```python
	from django.http import HttpResponse
	import datetime

	def current_datetime(request):
	    now = datetime.datetime.now()
	    html = "<html><body>It is now %s.</body></html>" % now
	    return HttpResponse(html)
```
Ardından eklenen view "urls.py" dosyasına eklenir
```python
	urlpatterns = [
	    path('', views.current_datetime, name="home"),
	    path('admin/', admin.site.urls),
	]
```
#### Template eklemek için;
Proje rootuna 'templates' klasörü eklenir.
Ardından içerisine html dosyası eklenir
```python
#views.py
def home(request):
    return render(request, "home.html", {
    		"title": "Öküzün Elifi"
    	})
```
settings.py dosyasında 
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
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
```
kısmına
```python
 'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ]
```
eklenir