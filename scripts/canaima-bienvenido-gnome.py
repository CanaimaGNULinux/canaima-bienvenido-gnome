#!/usr/bin/python
import sys
import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
import commands
import os
#import gettext
from user import home
import webkit
import string
import warnings
warnings.filterwarnings('ignore')

class canaimabienvenido():
    def __init__(self):

        gladefile = "/usr/share/canaima-bienvenido-gnome/interfaz.glade"
        wTree = gtk.glade.XML(gladefile,"main_window")
        wTree.get_widget("main_window").set_title("Bienvenido a Canaima GNU Linux")
        #wTree.get_widget("main_window").set_icon_from_file("/usr/share/canaima-bienvenido-gnome/imagenes/logo.svg")
        wTree.get_widget("main_window").connect("destroy", gtk.main_quit)

        browser = webkit.WebView()
        wTree.get_widget("scrolled_welcome").add(browser)
        browser.connect("button-press-event", lambda w, e: e.button == 3)
        subs = {}
        self.codecs_pkg = None
        self.extra_pkg = None
             
        if os.path.exists(home + "/.canaima-bienvenido-gnome/norun.flag"):
            subs['checked'] = ("")
        else:
            subs['checked'] = ("CHECKED")
            
        template = open("/usr/share/canaima-bienvenido-gnome/welcome.html").read()
        html = string.Template(template).safe_substitute(subs)
        browser.load_html_string(html, "file:/")
        browser.connect('title-changed', self.title_changed)
        wTree.get_widget("main_window").show_all()

    def title_changed(self, view, frame, title):
        if title.startswith("nop"):
            return
        # call directive looks like:
        #  "call:func:arg1,arg2"
        #  "call:func"
        if title == "event_irc":
            if os.path.exists("/usr/bin/xchat-gnome"):
                os.system("/usr/bin/xchat-gnome &")
            elif os.path.exists("/usr/bin/xchat"):
                os.system("/usr/bin/xchat &")
            elif os.path.exists("/usr/bin/konversation"):
                os.system("/usr/bin/konversation &")
            elif os.path.exists("/usr/bin/quassel"):
                os.system("/usr/bin/quassel &")
        elif title == "cunaguaro":
            comando="cunaguaro"
            os.system(comando+" &")
        elif title == "abrir_wiki":
            os.system("xdg-open http://wiki.canaima.softwarelibre.gob.ve/")
        elif title == "abrir_portal":
            os.system("xdg-open http://canaima.softwarelibre.gob.ve/")
        elif title == "guacharo":
            comando="guacharo"
            os.system(comando+" &")
        elif title == "turpial":
            comando="turpial"
            os.system(comando+" &")
        elif title == "xchat":
            comando="pidgin"
            os.system(comando+" &")
        elif title == "shotwell":
            comando="shotwell"
            os.system(comando+" &")
        elif title == "escaner":
            comando="simple-scan"
            os.system(comando+" &")
        elif title == "libreof":
            comando="libreoffice -draw"
            os.system(comando+" &")
        elif title == "gpaint":
            comando="gpaint"
            os.system(comando+" &")
        elif title == "procesador_texto":
            comando="libreoffice -writer"
            os.system(comando+" &")
        elif title == "hoja_calculo":
            comando="libreoffice -calc"
            os.system(comando+" &")        
        elif title == "impres":
            comando="libreoffice -impress"
            os.system(comando+" &")           
        elif title == "ofimatica":
            comando="libreoffice"
            os.system(comando+" &")
        elif title == "sonidos":
            comando="gnome-sound-recorder"
            os.system(comando+" &")        
        elif title == "toten":
            comando="totem"
            os.system(comando+" &")      
        elif title == "exaile":
            comando="exaile"
            os.system(comando+" &")
        elif title == "event_close_true":
            if os.path.exists(home + "/.linuxmint/mintWelcome/norun.flag"):
                os.system("rm -rf " + home + "/.linuxmint/mintWelcome/norun.flag")
            gtk.main_quit()
        elif title == "event_close_false":
            os.system("mkdir -p " + home + "/.canaima-bienvenido-gnome")
            os.system("touch " + home + "/.canaima-bienvenido-gnome/norun.flag")
            gtk.main_quit()
        elif title == "checkbox_checked":
            if os.path.exists(home + "/.canaima-bienvenido-gnome/norun.flag"):
                os.system("rm -rf " + home + "/.canaima-bienvenido-gnome/norun.flag")
        elif title == "checkbox_unchecked":
            os.system("mkdir -p " + home + "/.canaima-bienvenido-gnome")
            os.system("touch " + home + "/.canaima-bienvenido-gnome/norun.flag")


if __name__ == "__main__":
    canaimabienvenido()
    gtk.main()
        
