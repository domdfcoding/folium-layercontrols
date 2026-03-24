#!/usr/bin/env python3
#
#  __init__.py
"""
Folium addon for leaflet.layerscontrol-minimap
"""
#
#  Copyright © 2026 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2026 Dominic Davis-Foster"
__license__: str = "MIT License"
__version__: str = "0.0.0"
__email__: str = "dominic@davis-foster.co.uk"

# 3rd party
from folium import LayerControl, Template
from folium.elements import JSCSSMixin

__all__ = ["MinimapLayerControl"]


class MinimapLayerControl(JSCSSMixin, LayerControl):

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
            let {{ this.get_name() }} = L.control.layers.minimap.toggle(
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
