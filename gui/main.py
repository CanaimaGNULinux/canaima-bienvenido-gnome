#!/usr/bin/python

import sys
import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
import commands
import os
from user import home
import webkit
import string
import warnings
#warnings.filterwarnings('ignore')

class canaimabienvenido():
    def __init__(self):

        gladefile = "/usr/share/canaima-bienvenido-gnome/data/interfaz.glade"
        wTree = gtk.glade.XML(gladefile,"main_window")
        wTree.get_widget("main_window").set_title("Bienvenido a Canaima GNU/Linux")
        wTree.get_widget("main_window").connect("destroy", gtk.main_quit)

        browser = webkit.WebView()
        wTree.get_widget("scrolled_welcome").add(browser)
        browser.connect("button-press-event", lambda w, e: e.button == 3)
        subs = {}
        subs['checked'] = ("")
        self.codecs_pkg = None
        self.extra_pkg = None

        templatefile = "/usr/share/canaima-bienvenido-gnome/data/interfaz.html"
        template = open(templatefile).read()
        html = string.Template(template).safe_substitute(subs)
        browser.load_html_string(html, "file:/")
        browser.connect('title-changed', self.title_changed)
        wTree.get_widget("main_window").show_all()

    def title_changed(self, view, frame, title):
        if title.startswith("nop"):
            return

        if title == "ucumari":
            os.system(title+" &")
        elif title == "wiki":
            os.system("xdg-open http://wiki.canaima.softwarelibre.gob.ve/")
        elif title == "portal":
            os.system("xdg-open http://canaima.softwarelibre.gob.ve/")
        elif title == "canaima-notas-gnome":
            os.system(title+" &")
        elif title == "libreoffice":
            os.system(title+" &")
        elif title == "libreoffice-writer":
            comando="libreoffice --writer"
            os.system(comando+" &")
        elif title == "libreoffice-calc":
            comando="libreoffice --calc"
            os.system(comando+" &")
        elif title == "libreoffice-impress":
            comando="libreoffice --impress"
            os.system(comando+" &")
        elif title == "cunaguaro":
            os.system(title+" &")
        elif title == "guacharo":
            os.system(title+" &")
        elif title == "turpial":
            os.system(title+" &")
        elif title == "pidgin":
            os.system(title+" &")
        elif title == "shotwell":
            os.system(title+" &")
        elif title == "simple-scan":
            os.system(title+" &")
        elif title == "libreoffice-draw":
            comando="libreoffice --draw"
            os.system(comando+" &")
        elif title == "gpaint":
            os.system(title+" &")
        elif title == "exaile":
            os.system(title+" &")
        elif title == "totem":
            os.system(title+" &")
        elif title == "pitivi":
            os.system(title+" &")
        elif title == "brasero":
            os.system(title+" &")
        elif title == "event_close_true":
            os.system("mkdir -p " + home + "/.config/canaima-bienvenido-gnome/")
            os.system("echo 'MOSTRAR=0' > " + home + "/.config/canaima-bienvenido-gnome/gui.conf")
            gtk.main_quit()
        elif title == "event_close_false":
            os.system("mkdir -p " + home + "/.config/canaima-bienvenido-gnome/")
            os.system("echo 'MOSTRAR=1' > " + home + "/.config/canaima-bienvenido-gnome/gui.conf")
            gtk.main_quit()
        elif title == "checkbox_checked":
            os.system("mkdir -p " + home + "/.config/canaima-bienvenido-gnome/")
            os.system("echo 'MOSTRAR=0' > " + home + "/.config/canaima-bienvenido-gnome/gui.conf")
        elif title == "checkbox_unchecked":
            os.system("mkdir -p " + home + "/.config/canaima-bienvenido-gnome/")
            os.system("echo 'MOSTRAR=1' > " + home + "/.config/canaima-bienvenido-gnome/gui.conf")

if __name__ == "__main__":
    canaimabienvenido()
    gtk.main()        
