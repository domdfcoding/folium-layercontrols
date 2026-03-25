#!/usr/bin/env python3
#
#  __init__.py
"""
Folium addon for leaflet.layerscontrol-minimap .
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

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2026 Dominic Davis-Foster"
__license__: str = "BSD-2-Clause License"
__version__: str = "0.0.0"
__email__: str = "dominic@davis-foster.co.uk"

# 3rd party
from folium import LayerControl
from folium.elements import JSCSSMixin
from folium.template import Template

__all__ = ["MinimapLayerControl"]


class MinimapLayerControl(JSCSSMixin, LayerControl):
	"""
	Leaflet layer control widget which displays minimap previews of the basemap layers.
	"""

	control_class_name = "L.control.layers.minimap"

	default_js = [
			(
					"layerscontrol-minimap-js",
					"https://cdn.jsdelivr.net/npm/leaflet.layerscontrol-minimap@1.0.21/L.Control.Layers.Minimap.min.js",
					),
			]

	default_css = [
			(
					"layerscontrol-minimap-css",
					"https://cdn.jsdelivr.net/npm/leaflet.layerscontrol-minimap@1.0.21/control.layers.minimap.min.css",
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
        """,
			)
