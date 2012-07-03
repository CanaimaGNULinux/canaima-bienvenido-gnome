# Makefile

SHELL := sh -e

SCRIPTS = "debian/postinst configure" "debian/postrm remove"
IMAGES = $(shell ls -1 gui/images/ | grep "\.svg" | sed 's/\.svg//g')

all: test build

test:

	@echo -n "\n===== Comprobando posibles errores de sintaxis en los scripts de mantenedor =====\n\n"

	@for SCRIPT in $(SCRIPTS); \
	do \
		echo -n "$${SCRIPT}\n"; \
		bash -n $${SCRIPT}; \
	done

	@echo -n "\n=================================================================================\nHECHO!\n\n"

build: clean

	@printf "Generando imágenes desde las fuentes [SVG > PNG] ["
	@for IMAGE in $(IMAGES); do \
		$(CONVERT) -background None gui/images/$${IMAGE}.svg gui/images/$${IMAGE}.png; \
		printf "."; \
	done;
	@echo "Nada para compilar!"

install:

	@mkdir -p $(DESTDIR)/usr/bin
	@mkdir -p $(DESTDIR)/usr/share/canaima-bienvenido-gnome/images
	@mkdir -p $(DESTDIR)/etc/skel/Escritorio
	@mkdir -p $(DESTDIR)/etc/skel/.config/autostart
	@mkdir -p $(DESTDIR)/usr/share/applications
	@mkdir -p $(DESTDIR)/etc/skel/.config/canaima-bienvenido-gnome
	@cp -r gui/* $(DESTDIR)/usr/share/canaima-bienvenido-gnome/
	@rm $(DESTDIR)/usr/share/canaima-bienvenido-gnome/images/*.svg
	@cp canaima-bienvenido-gnome.desktop $(DESTDIR)/usr/share/applications/
	@cp canaima-bienvenido-gnome.desktop $(DESTDIR)/etc/skel/Escritorio/
	@cp gui.conf $(DESTDIR)/etc/skel/.config/canaima-bienvenido-gnome/
	@cp canaima-bienvenido-gnome-auto.desktop $(DESTDIR)/etc/skel/.config/autostart/
	@cp canaima-bienvenido-gnome.sh $(DESTDIR)/usr/bin/canaima-bienvenido-gnome

uninstall:

	@rm -rf $(DESTDIR)/usr/share/canaima-bienvenido-gnome/
	@rm -rf $(DESTDIR)/usr/bin/canaima-bienvenido-gnome
	@rm -f $(DESTDIR)/etc/skel/Escritorio/canaima-bienvenido-gnome.desktop
	@rm -f $(DESTDIR)/etc/skel/.config/autostart/canaima-bienvenido-gnome-auto.desktop
	@rm -f $(DESTDIR)/usr/share/applications/canaima-bienvenido-gnome.desktop

clean:

	@printf "Cleaning generated images [PNG] ["
	@for IMAGE in $(IMAGES); do \
		rm -rf gui/images/$${IMAGE}.png; \
		printf "."; \
	done

distclean:

reinstall: uninstall install
