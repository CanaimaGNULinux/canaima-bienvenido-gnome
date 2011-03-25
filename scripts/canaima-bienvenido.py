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
                    "multimedia1" : self.multimedia1,
                    "multimedia2" : self.multimedia2,
                    "multimedia3" : self.multimedia3,
                    "multimedia4" : self.multimedia4,
                    "multimedia5" : self.multimedia5,
                    "multimedia6" : self.multimedia6,
                    "multimedia7" : self.multimedia7,
                    "multimedia8" : self.multimedia8,
                    "oficina1" : self.oficina1,
                    "oficina2" : self.oficina2,
                    "oficina3" : self.oficina3,
                    "oficina4" : self.oficina4,
                    "oficina5" : self.oficina5,
                    "oficina6" : self.oficina6,
                    "oficina7" : self.oficina7,
                    "oficina8" : self.oficina8,
                    "internet1" : self.internet1,
                    "internet2" : self.internet2,
                    "internet3" : self.internet3,
                    "internet4" : self.internet4,
                    "internet5" : self.internet5,
                    "internet6" : self.internet6,
                    "internet7" : self.internet7,
                    "internet8" : self.internet8,
                    "graficos1" : self.graficos1,
                    "graficos2" : self.graficos2,
                    "graficos3" : self.graficos3,
                    "graficos4" : self.graficos4,
                    "graficos5" : self.graficos5,
                    "graficos6" : self.graficos6,
                    "graficos7" : self.graficos7,
                    "graficos8" : self.graficos8,
                    "volver" : self.volver,
                    "cambiar" : self.cambiar,
                    "mostrar_internet" : self.mostrar_internet,
                    "mostrar_graficos" : self.mostrar_graficos,
                    "mostrar_multimedia" : self.mostrar_multimedia,
                    "mostrar_oficina" : self.mostrar_oficina,
                    "on_mostrar_toggled" : self.checkmostrar,
                    "destroy" : self.cerrar,
                    "cerrar" : self.cerrar,
                    "on_MainWindow_destroy" : self.cerrar }
            
            self.wTree.get_widget("principal").show(); 
            self.wTree.get_widget("multimedia").connect("delete-event",self.cerrar); 
            self.wTree.get_widget("graficos").connect("delete-event",self.cerrar); 
            self.wTree.get_widget("internet").connect("delete-event",self.cerrar); 
            self.wTree.get_widget("oficina").connect("delete-event",self.cerrar); 
            
            self.wTree.signal_autoconnect(dic)
            gtk.main()

    #Get the Main Window, and connect the "destroy" event

    def volver(self,widget):
        self.wTree.get_widget("principal").show()
        self.wTree.get_widget("multimedia").hide()
        self.wTree.get_widget("graficos").hide()
        self.wTree.get_widget("oficina").hide()
        self.wTree.get_widget("internet").hide()

    def cambiar(self,widget):
        view=self.wTree.get_widget("window2")
        view.show()

    def mostrar_internet(self,widget):
        self.wTree.get_widget("multimedia").hide()
        self.wTree.get_widget("graficos").hide()
        self.wTree.get_widget("oficina").hide()
        self.wTree.get_widget("internet").show()
        self.wTree.get_widget("principal").hide()

    def mostrar_oficina(self,widget):
        self.wTree.get_widget("multimedia").hide()
        self.wTree.get_widget("graficos").hide()
        self.wTree.get_widget("oficina").show()
        self.wTree.get_widget("internet").hide()
        self.wTree.get_widget("principal").hide()

    def mostrar_graficos(self,widget):
        self.wTree.get_widget("multimedia").hide()
        self.wTree.get_widget("graficos").show()
        self.wTree.get_widget("oficina").hide()
        self.wTree.get_widget("internet").hide()
        self.wTree.get_widget("principal").hide()

    def mostrar_multimedia(self,widget):
        self.wTree.get_widget("multimedia").show()
        self.wTree.get_widget("graficos").hide()
        self.wTree.get_widget("oficina").hide()
        self.wTree.get_widget("internet").hide()
        self.wTree.get_widget("principal").hide()
 
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

    def internet1(self, widget):
        comando=""
        os.system(comando+" &")

    def internet2(self, widget):
        comando=""
        os.system(comando+" &")

    def internet3(self, widget):
        comando=""
        os.system(comando+" &")

    def internet4(self, widget):
        comando=""
        os.system(comando+" &")

    def internet4(self, widget):
        comando=""
        os.system(comando+" &")

    def internet5(self, widget):
        comando=""
        os.system(comando+" &")

    def internet6(self, widget):
        comando=""
        os.system(comando+" &")

    def internet7(self, widget):
        comando=""
        os.system(comando+" &")

    def internet8(self, widget):
        comando=""
        os.system(comando+" &")


    def oficina1(self, widget):
        comando=""
        os.system(comando+" &")


    def oficina2(self, widget):
        comando=""
        os.system(comando+" &")

    def oficina3(self, widget):
        comando=""
        os.system(comando+" &")

    def oficina4(self, widget):
        comando=""
        os.system(comando+" &")

    def oficina5(self, widget):
        comando=""
        os.system(comando+" &")

    def oficina6(self, widget):
        comando=""
        os.system(comando+" &")

    def oficina7(self, widget):
        comando=""
        os.system(comando+" &")

    def oficina8(self, widget):
        comando=""
        os.system(comando+" &")

    def graficos1(self, widget):
        comando=""
        os.system(comando+" &")

    def graficos2(self, widget):
        comando=""
        os.system(comando+" &")

    def graficos3(self, widget):
        comando=""
        os.system(comando+" &")

    def graficos4(self, widget):
        comando=""
        os.system(comando+" &")

    def graficos5(self, widget):
        comando=""
        os.system(comando+" &")

    def graficos6(self, widget):
        comando=""
        os.system(comando+" &")

    def graficos7(self, widget):
        comando=""
        os.system(comando+" &")

    def graficos8(self, widget):
        comando=""
        os.system(comando+" &")

    def multimedia1(self, widget):
        comando=""
        os.system(comando+" &")

    def multimedia2(self, widget):
        comando=""
        os.system(comando+" &")

    def multimedia3(self, widget):
        comando=""
        os.system(comando+" &")

    def multimedia4(self, widget):
        comando=""
        os.system(comando+" &")

    def multimedia5(self, widget):
        comando=""
        os.system(comando+" &")

    def multimedia6(self, widget):
        comando=""
        os.system(comando+" &")

    def multimedia7(self, widget):
        comando=""
        os.system(comando+" &")

    def multimedia8(self, widget):
        comando=""
        os.system(comando+" &")



if __name__ == "__main__":
        hwg = canaimabienvenido()
        
        
