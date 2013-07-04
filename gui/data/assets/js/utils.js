/**
 * Copyright (C) 2012 Huayra GNU/Linux
 *
 * Author Miguel Angel Garcia <miguel.garcia@gmail.com>
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; version 2
 * of the License
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
 * USA.
 */

/**
 * Exits the container application.
 *
 * @param start_next_time boolean Indicates wether the application should autostart
 * on next users login.
 */
function finalize(){
	window.location = '[app]finalize';
}

/**
 * Sets autostart
 * 
 */
function set_autostart_on(){
	window.location = '[app]set-autostart-on';
}

function set_autostart_off(){
	window.location = '[app]set-autostart-off';
}

/**
 * Answer active?
 * 
 */
function set_answer_active_on(){
	window.location = '[app]set-answer-active-on';
}

function set_answer_active_off(){
	window.location = '[app]set-answer-active-off';
}
