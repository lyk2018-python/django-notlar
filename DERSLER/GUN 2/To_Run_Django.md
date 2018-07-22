#### Virtualenv için
*virtualenv --python=python3 <File-Name>*
*source <File-Name>/bin/activate*
*virtualenv --python=python3 lyk*
*source lyk/bin/activate*

#### Ardından o konuma django kurmak için
*pip install django*

#### Django projesi oluşturmak için, ama önce klasör dizinini belirle
*django-admin startproject <Project-Name>*
*django-admin startproject Melek*

#### Startprojectten sonra proje dizinine git sonra;
*python manage.py runserver*

#### İstenilen Itemın ismini ezmek için models.py a eklenir;
	def __str__(self):
		return self.title

#### App başlatmak için
*python manage.py startapp <App-Adi>*
*python manage.py startapp news*
* Melek/Melek/settings.py dosyasında installed apps güncelle(modeli ekle)


	INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news',
	]

admin panelde düzenlemek için news/admin.py dosyasına;

	from news.models import NewsItem
	admin.site.register(NewsItem)
ekle

#### Migrationsları oluşturma
*python manage.py makemigrations*
#### Migrate işlemi
*pyton manage.py migrate*
#### Superuser oluşturma işlemi
*python manage.py createsuperuser*
#### 80 portundan erişim sağlama
*python manage.py runserver 0.0.0.0:80*
* Global erişişm için Melek/Melek/settings.py dosyasında


	ALLOWED_HOSTS = ['*']
* şeklinde güncellenmeli
#### Shell kullanma örneği
*python manage.py shell*

	from news.models import NewsItem
	NewsItem()
	NewsItem(title="fikibok")
	<NewsItem: fikibok>
	haber = NewsItem()
	haber.title = "fiki fiki"
	haber.content = "emoji"
	haber.save()
	haber.id
