.PHONY: run static mkcert

run:
	python manage.py runserver_plus --cert-file cert.pem --key-file key.pem 0.0.0.0:8000

static:
	python manage.py collectstatic

mkcert:
	mkcert -cert-file cert.pem -key-file key.pem localhost 127.0.0.1 192.168.1.161