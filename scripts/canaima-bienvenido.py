#!/usr/bin/env python

import sys

try:
        import gtk
        import os, threading, locale
        import gobject
        import pygtk
        import vte
	import webbrowser
        pygtk.require("2.0")
except:
        pass
try:
        import gtk
        import gtk.glade
except:
        sys.exit(1)

class canaimabienvenido:
    encoding = locale.getpreferredencoding()
    utf8conv = lambda x : unicode(x, encoding).encode('utf8')

    fuente = ""
    destino = ""
  
    def __init__(self):
            #Set the Glade file
            self.gladefile = "/usr/share/canaima-bienvenido/interfaz.glade"

            self.wTree = gtk.glade.XML(self.gladefile) 

            #Create our dictionay and connect it
            dic = { "on_cerrar_clicked" : self.cerrar,
                    "on_b1_clicked" : self.b1_clicked,
                    "on_b2_clicked" : self.b2_clicked,
                    "on_b3_clicked" : self.b3_clicked,
                    "on_b4_clicked" : self.b4_clicked,
                    "on_b5_clicked" : self.b5_clicked,
                    "on_b6_clicked" : self.b6_clicked,
                    "on_b7_clicked" : self.b7_clicked,
                    "on_b8_clicked" : self.b8_clicked,
                    "on_mostrar_toggled" : self.checkmostrar,
                    "destroy" : self.cerrar,
                    "on_MainWindow_destroy" : self.cerrar }
            
            self.wTree.get_widget("window1").show(); 
            self.wTree.get_widget("window1").connect("delete-event",self.cerrar); 
            
            self.wTree.signal_autoconnect(dic)
            gtk.main()

    #Get the Main Window, and connect the "destroy" event
 
    def checkmostrar(self, widget):
        print self.wTree.get_widget("mostrar").get_active();
        if self.wTree.get_widget("mostrar").get_active() == True :
            check_cb_conf=open(os.environ['HOME']+"/.config/canaima-bienvenido/usuario.conf","w")			
            check_cb_conf.write("MOSTRAR=0")
            check_cb_conf.close()
        else:
            check_cb_conf=open(os.environ['HOME']+"/.config/canaima-bienvenido/usuario.conf","w")
            check_cb_conf.write("MOSTRAR=1")
            check_cb_conf.close()

    def b1_clicked(self, widget):
        print "Abriendo Cunaguaro"
        comando="cunaguaro"
        os.system(comando+" &")

    def cerrar(self, widget,event=None):
        print "Cerrando"
        self.wTree.get_widget("window1").hide();
        sys.exit(0)

    def b2_clicked(self, widget):
        print "Abriendo Guacharo"
        comando="guacharo"
        os.system(comando+" &")

    def b3_clicked(self, widget):
        print "Abriendo Turpial"
        comando="turpial"
        os.system(comando+" &")

    def b4_clicked(self, widget):
        print "Abriendo Chat"
        comando="pidgin"
        os.system(comando+" &")

    def b5_clicked(self, widget):
        print "Abriendo LibreOffice"
        comando="libreoffice"
        os.system(comando+" &")

    def b6_clicked(self, widget):
        print "Abriendo GIMP"
        comando="gimp"
        os.system(comando+" &")

    def b7_clicked(self, widget):
        print "Abriendo totem"
        comando="totem"
        os.system(comando+" &")

    def b8_clicked(self, widget):
        print "Abriendo Exaile"
        comando="exaile"
        os.system(comando+" &")

if __name__ == "__main__":
        hwg = canaimabienvenido()
        
        
