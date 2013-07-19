# Makefile

SHELL := sh -e

SCRIPTS = debian/postinst debian/postrm debian/preinst
IMAGES = $(shell ls -1 gui/images/ | grep "\.svg" | sed 's/\.svg//g')

all: test build

test:

	@printf "Comprobando sintaxis de los scripts de shell ["
	@for SCRIPT in $(SCRIPTS); do \
		sh -n $${SCRIPT}; \
		checkbashisms -f -x $${SCRIPT} || true; \
		printf "."; \
	done
	@printf "]\n"

build: clean

	@printf "Generando imágenes desde las fuentes [SVG > PNG] ["
	@for IMAGE in $(IMAGES); do \
		convert -background None gui/images/$${IMAGE}.svg gui/images/$${IMAGE}.png; \
		printf "."; \
	done;
	@echo "Nada para compilar!"

install:

	@mkdir -p $(DESTDIR)/usr/bin
	@mkdir -p $(DESTDIR)/usr/share/canaima-bienvenido-gnome
	@mkdir -p $(DESTDIR)/etc/skel/.config/autostart
	@mkdir -p $(DESTDIR)/usr/share/applications
	@cp -r gui/* $(DESTDIR)/usr/share/canaima-bienvenido-gnome
	@cp gui.conf $(DESTDIR)/etc/skel/.config/canaima-bienvenido-gnome/
	@cp canaima-bienvenido-gnome-auto.desktop $(DESTDIR)/etc/skel/.config/autostart/
	@cp canaima-bienvenido-gnome.sh $(DESTDIR)/usr/bin/canaima-bienvenido-gnome

uninstall:

	@rm -rf $(DESTDIR)/usr/share/canaima-bienvenido-gnome/
	@rm -rf $(DESTDIR)/usr/bin/canaima-bienvenido-gnome
	@rm -f $(DESTDIR)/etc/skel/.config/autostart/canaima-bienvenido-gnome-auto.desktop

clean:

	@printf "Cleaning generated images [PNG] ["
	@for IMAGE in $(IMAGES); do \
		rm -rf gui/images/$${IMAGE}.png; \
		printf "."; \
	done

distclean:

reinstall: uninstall install
