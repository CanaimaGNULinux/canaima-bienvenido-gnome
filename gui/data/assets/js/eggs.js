/*
 * Keystrokes event for jQuery
 * http://www.boedesign.com/
 */ 

easter_eggs = new Array();

easter_eggs['equipo_huayra'] = "\
<div class='easter-egg-wrapper'>\
	<h1>Huayra GNU/Linux</h1>\
	<div class='personas' id='directores-huayra'>\
		<h3>Presidenta de la Nación:</h3>\
		<p>Dra. Cristina Fernández de Kirchner</p>\
		<h3>Director Ejecutivo de la ANSES:</h3>\
		<p>Lic. Diego Bossio</p>\
		<h3>Directora Ejecutiva del Programa Conectar Igualdad:</h3>\
		<p>Lic. Silvina Gvirtz</p>\
		<h3>Directora de Comunicación y Contenidos del Programa Conectar Igualdad:</h3>\
		<p>Lic. Constanza Necuzzi</p>\
	</div>\
\
	<h2>Los integrantes de Huayra somos:</h2>\
	<div class='personas' id='equipo-huayra'>\
		<h3>Coordinador General:</h3>\
		<p>Javier Castrillo</p>\
		<h3>Jefe de Proyecto:</h3>\
		<p>Vladimir di Fiore Prieto</p>\
		<h3>Equipo Desarrollo:</h3>\
		<p>Héctor Sanchez - Fernando Toledo, Miguel García, Luciano Baraglia, Mauro Lizaur, Julia Palandri</p>\
		<h3>Equipo de Documentación:</h3>\
		<p>Felipe Diego González - Ornella Lotito, Celeste Mandrut</p>\
		<h3>Equipo Arte y Diseño:</h3>\
		<p>Claudio Andaur - Carolina Hortal, Mercedes Elgarte, Iván Hoffmann</p>\
	</div>\
	<h3>Agradecemos:</h3>\
	<p>A <strong>Pablo Fontdevila</strong> que desde el inicio creyó en este proyecto</p>\
	<p>A <strong>Laura Penacca</strong> por su empuje y trabajo incansable día a día</p>\
	<p>A todos los colaboradores de la <strong>comunidad educativa</strong></p>\
	<p>A la comunidad del <strong>Software Libre</strong></p>\
</div>\
";

$(document).ready(function(){
	$(document).bind('keystrokes', {
		keys: ['h', 'u', 'a', 'y', 'r', 'a', 'space', 't', 'e', 'a', 'm']
	}, function(event){
		jQuery('<div class="egg" id="easter-egg-equipo-huayra">' + easter_eggs['equipo_huayra'] + '</div>').appendTo('body').fadeIn().click(function(){jQuery(this).fadeOut()});
					
	});
});
    
