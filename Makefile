# Makefile

SHELL := sh -e

SCRIPTS = "debian/preinst install" "debian/postinst configure" "debian/prerm remove" "debian/postrm remove"

all: test build

test:

	@echo -n "\n===== Comprobando posibles errores de sintaxis en los scripts de mantenedor =====\n\n"

	@for SCRIPT in $(SCRIPTS); \
	do \
		echo -n "$${SCRIPT}\n"; \
		bash -n $${SCRIPT}; \
	done

	@echo -n "\n=================================================================================\nHECHO!\n\n"

build:

	@echo "Nada para compilar!"

install:

	mkdir -p $(DESTDIR)/usr/bin/
	mkdir -p $(DESTDIR)/usr/share/canaima-bienvenido-gnome/
	mkdir -p $(DESTDIR)/etc/skel/Escritorio/
	mkdir -p $(DESTDIR)/etc/skel/.config/autostart/
	mkdir -p $(DESTDIR)/usr/share/applications/
	mkdir -p $(DESTDIR)/etc/skel/.config/canaima-bienvenido-gnome/
	cp -r ui imagenes $(DESTDIR)/usr/share/canaima-bienvenido-gnome/
	rm -rf $(DESTDIR)/usr/share/canaima-bienvenido-gnome/imagenes/*.svg
	cp -r scripts/principal.py $(DESTDIR)/usr/share/canaima-bienvenido-gnome/
	cp -r desktop/canaima-bienvenido-gnome.desktop $(DESTDIR)/usr/share/applications/
	cp -r desktop/canaima-bienvenido-gnome.desktop $(DESTDIR)/etc/skel/Escritorio/
	cp -r conf/usuario.conf $(DESTDIR)/etc/skel/.config/canaima-bienvenido-gnome/
	cp -r desktop/canaima-bienvenido-gnome-automatico.desktop $(DESTDIR)/etc/skel/.config/autostart/
	cp -r scripts/canaima-bienvenido-gnome.sh $(DESTDIR)/usr/bin/canaima-bienvenido-gnome
	cp -r scripts/canaima-bienvenido-gnome-automatico.sh $(DESTDIR)/usr/bin/canaima-bienvenido-gnome-automatico

uninstall:

	rm -rf $(DESTDIR)/usr/share/canaima-bienvenido-gnome/
	rm -rf $(DESTDIR)/usr/bin/canaima-bienvenido-gnome
	rm -rf $(DESTDIR)/usr/bin/canaima-bienvenido-gnome-automatico
	rm -f $(DESTDIR)/etc/skel/Escritorio/canaima-bienvenido-gnome.desktop
	rm -f $(DESTDIR)/etc/skel/.config/autostart/canaima-bienvenido-gnome-automatico.desktop
	rm -f $(DESTDIR)/usr/share/applications/canaima-bienvenido-gnome.desktop
clean:

distclean:

reinstall: uninstall install
