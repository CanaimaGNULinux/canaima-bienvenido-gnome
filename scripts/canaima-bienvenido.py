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
        
def read_output(view, buffer, command):
        stdin, stdouterr = os.popen4(command)
        while 1:
                line = stdouterr.readline()
                if not line:
                        break
                gtk.gdk.threads_enter()
                iter = buffer.get_end_iter()
                buffer.place_cursor(iter)
                buffer.insert(iter, str(line))
                view.scroll_to_mark(buffer.get_insert(), 0.1)
                gtk.gdk.threads_leave() 
               
def abrir_paralelo(view, buffer, comando):
                os.system(comando)

class HellowWorldGTK:
        gobject.threads_init()
        gtk.gdk.threads_init()

        encoding = locale.getpreferredencoding()
        utf8conv = lambda x : unicode(x, encoding).encode('utf8')

        fuente = ""
        destino = ""
      
        
        def __init__(self):
                #Set the Glade file
                self.gladefile = "/usr/share/canaima-bienvenido/interfaz.glade"  

                self.wTree = gtk.glade.XML(self.gladefile) 

                #Create our dictionay and connect it
                dic = { "on_cerrar_clicked" : self.btnHelloWorld_clicked,
                        "on_volver_clicked" : self.volver_clicked,
                        "on_b1_clicked" : self.b1_clicked,
                        "on_b2_clicked" : self.b2_clicked,
                        "on_b3_clicked" : self.b3_clicked,
                        "on_b4_clicked" : self.b4_clicked,
                        "on_b5_clicked" : self.b5_clicked,
                        "on_b6_clicked" : self.b6_clicked,
                        "on_b7_clicked" : self.b7_clicked,
                        "on_b8_clicked" : self.b8_clicked,
                        "on_mostrar_toggled" : self.checkmostrar,
                        "on_MainWindow_destroy" : gtk.main_quit }
                
                self.wTree.get_widget("window1").show(); 
                
                self.wTree.signal_autoconnect(dic)
                gtk.main()
                
	def btnHelloWorld_clicked(self, widget):
                print "Hasta la proxima!"
                self.wTree.get_widget("window1").hide();
		exit(0);

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
                print "Abriendo Firefox"
		comando="firefox"
	        thr = threading.Thread(target= abrir_paralelo, args=(0,0,comando));
                thr.start()

	def b2_clicked(self, widget):
                print "Abriendo aMSN"
		comando="amsn"
	        thr = threading.Thread(target= abrir_paralelo, args=(0,0,comando));
                thr.start()


	def b3_clicked(self, widget):
                print "Abriendo Pidgin"
		comando="pidgin"
	        thr = threading.Thread(target= abrir_paralelo, args=(0,0,comando));
                thr.start()


	def b5_clicked(self, widget):
                print "Abriendo OpenOffice.org Writer"
		comando="ooffice -writer"
	        thr = threading.Thread(target= abrir_paralelo, args=(0,0,comando));
                thr.start()

	def b6_clicked(self, widget):
                print "Abriendo OpenOffice.org Calc"
		comando="ooffice -calc"
	        thr = threading.Thread(target= abrir_paralelo, args=(0,0,comando));
                thr.start()



	def b7_clicked(self, widget):
                print "Abriendo OpenOffice.org Impress"
		comando="ooffice -impress"
	        thr = threading.Thread(target= abrir_paralelo, args=(0,0,comando));
                thr.start()

	def b8_clicked(self, widget):
                print "Abriendo OpenOffice.org Draw"
		comando="ooffice -draw"
	        thr = threading.Thread(target= abrir_paralelo, args=(0,0,comando));
                thr.start()

	def b4_clicked(self, widget):
                print "Para Aprender!"
		webbrowser.open_new("http://wiki.canaima.softwarelibre.gob.ve/")

#                self.wTree.get_widget("window1").hide();
#                self.wTree.get_widget("window2").show();

	def volver_clicked(self, widget):
                print "Menu de Nuevo..."
                self.wTree.get_widget("window2").hide();
                self.wTree.get_widget("window1").show();

if __name__ == "__main__":
        hwg = HellowWorldGTK()
        
        
