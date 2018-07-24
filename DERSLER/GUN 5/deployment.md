## Deployment
https://www.vultr.com/ yada https://www.digitalocean.com/ gibi sitelerde hesap açılır, gerekli server ve server için OS seçilir, server kiralanır.
Server kurulumu bittikten sonra terminalden SSH ile sunucuya bağlanılır.

```
	ssh root@<IP>
```
Bağlandıktan sonra 
```
	sudo apt-get update
	sudo apt-get -y upgrade
```
ile apt ile update alınır
#### Python3, pip3 ve Django  kurulumu

```
	sudo apt-get install python3
	sudo apt-get install -y python3-pip
```
Ardından pip3 ile virtualenv kurulumu yapılır

```
	pip3 install virtualenv
```
Yükleme sonrasında virtualenv yaratılır;
```
	virtualenv <Virtual-Env-Adı>
```
*source* komutu ile virtual environment activate edilir
```
	cd <Virtual-Env-Adı>
	source bin/activate
```
Daha sonrasında yarattığımız virtual environment a django kurulur

```
	pip install django
```
Virtual environmentların dışında projelerin bulunduğu klasöre proje clonelanır yada yaratılır.
```
	//Örnek
	mkdir Projeler
	cd Projeler
	git clone <URI>
```
#### Proje deploymentı
```
	python manage.py runserver
```
#### Migrate işlemi
```
	pyton manage.py migrate
```
#### Superuser oluşturma işlemi
```
	python manage.py createsuperuser
```
#### Alınan domain allowed hosts a eklenir
```python
	ALLOWED_HOSTS = ["elifinokuzu.org"]
```
#### 80 portundan erişim sağlama
```
python manage.py runserver 0.0.0.0:80
```