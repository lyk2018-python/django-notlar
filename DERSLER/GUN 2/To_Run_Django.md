##virtualenv için
virtualenv --python=python3 <File-Name>
source <File-Name>/bin/activate
virtualenv --python=python3 lyk
source lyk/bin/activate

##ardından o konuma django kurmak için
pip install django

##django projesi oluşturmak için, ama önce klasör dizinini belirle
django-admin startproject <Project-Name>
django-admin startproject Melek

##startprojectten sonra proje dizinine git sonra;
python manage.py runserver

##istenilen Itemın ismini ezmek için models.py a eklenir;
	def __str__(self):
		return self.title

##App başlatmak için
python manage.py startapp <App-Adi>
python manage.py startapp news
	--> Melek/Melek/manage.py dosyasında installed apps güncelle
	--> admin panelde düzenlemek için news/admin.py dosyasına;

		from news.models import NewsItem
		admin.site.register(NewsItem)

		ekle
##migrationsları oluşturma
python manage.py makemigrations
##migrate işlemi
pyton manage.py migrate
##superuser oluşturma işlemi
python manage.py createsuperuser
##80 portundan erişişim sağlama
python manage.py runserver 0.0.0.0:80
	--> Global erişişm için Melek/Melek/settings.py dosyasında

	ALLOWED_HOSTS '*' 
	şeklinde güncellenmeli
##shell kullanma örneği
python manage.py shell
	>>> from news.models import NewsItem
	>>> NewsItem()
		<NewsItem: >
	>>> NewsItem(title="fikibok")
		<NewsItem: fikibok>
	>>> haber = NewsItem()
	>>> haber.title = "fiki fiki"
	>>> haber.content = "emoji"
	>>> haber.save()
	>>> haber.id
