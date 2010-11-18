# Makefile

SHELL := sh -e

all: test build

test:
	@echo "Nada para comprobar!"

build:
	@echo "Nada para compilar!"

install:

	mkdir -p $(DESTDIR)/usr/bin/
	mkdir -p $(DESTDIR)/usr/share/canaima-bienvenido/
	mkdir -p $(DESTDIR)/etc/skel/Escritorio/
	mkdir -p $(DESTDIR)/etc/skel/.config/autostart/
	cp -r desktop/ $(DESTDIR)/usr/share/canaima-bienvenido/
	cp -r images/ $(DESTDIR)/usr/share/canaima-bienvenido/
	cp -r scripts/canaima-bienvenido.py $(DESTDIR)/usr/share/canaima-bienvenido/
	cp -r scripts/interfaz.glade $(DESTDIR)/usr/share/canaima-bienvenido/
	cp -r scripts/canaima-bienvenido.sh $(DESTDIR)/usr/bin/canaima-bienvenido
	cp -r scripts/canaima-bienvenido-automatico.sh $(DESTDIR)/usr/bin/canaima-bienvenido-automatico

uninstall:

	rm -rf $(DESTDIR)/usr/share/canaima-bienvenido/
	rm -rf $(DESTDIR)/usr/bin/canaima-bienvenido
	rm -rf $(DESTDIR)/usr/bin/canaima-bienvenido-automatico

clean:

distclean:

reinstall: uninstall install
