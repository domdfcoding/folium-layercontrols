#!/usr/bin/env python3
#
#  toggle.py
"""
Customised folium layer control that is shown/hidden on click rather than mouseover.
"""
#
#  Copyright © 2026 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#  2. Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

# 3rd party
from folium import LayerControl
from folium.elements import JSCSSMixin
from folium.template import Template

# this package
from folium_layerscontrol_minimap import __version__

__all__ = ["MinimapLayerControl"]


class ToggleLayerControl(JSCSSMixin, LayerControl):
	"""
	Customised folium layer control that is shown/hidden on click rather than mouseover.
	"""

	control_class_name = "new L.Control.Layers.Toggle"

	default_js = [
			(
					"layercontrol-toggle-js",
					f"https://cdn.jsdelivr.net/gh/domdfcoding/folium-layerscontrol-minimap@v{__version__}/folium_layerscontrol_minimap/L.Control.Layers.Toggle.min.js",
					),
			]

	_template = Template(
			"""
		{% macro script(this,kwargs) %}
			var {{ this.get_name() }}_layers = {
				base_layers : {
					{%- for key, val in this.base_layers.items() %}
					{{ key|tojson }} : {{val}},
					{%- endfor %}
				},
				overlays :  {
					{%- for key, val in this.overlays.items() %}
					{{ key|tojson }} : {{val}},
					{%- endfor %}
				},
			};
			let {{ this.get_name() }} = {{ this.control_class_name }}(
				{{ this.get_name() }}_layers.base_layers,
				{{ this.get_name() }}_layers.overlays,
				{{ this.options|tojavascript }}
			).addTo({{this._parent.get_name()}});

			{%- if this.draggable %}
			new L.Draggable({{ this.get_name() }}.getContainer()).enable();
			{%- endif %}

		{% endmacro %}
		""".replace('\t', "    "),
			)
