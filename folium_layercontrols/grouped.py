#!/usr/bin/env python3
#
#  __init__.py
"""
Folium addon for leaflet.groupedlayercontrol .
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
import folium
from folium.elements import JSCSSMixin
from folium.map import Layer
from folium.template import Template
from folium.utilities import TypeJsonValue

# this package
from folium_layercontrols import __version__

__all__ = ["GroupedLayerControl", "ToggleGroupedLayerControl"]


class GroupedLayerControl(JSCSSMixin, folium.LayerControl):
	r"""
	Creates a GroupedLayerControl object to be added to a folium map.

	.. note::

		The LayerControl should be added last to the map. Otherwise, the GroupedLayerControl and/or the controlled layers may not appear.

	:param groups: Grouped layers to display in the control.
	:param position: The position of the control (one of the map corners).
		Can be 'topleft', 'topright', 'bottomleft' or 'bottomright'.
	:param collapsed: If :py:obj:`True` the control will be collapsed into an icon and expanded on mouse hover or touch.
	:param autoZIndex: If :py:obj:`True` the control assigns zIndexes in increasing order to all of its layers so that the order is preserved when switching them on/off.
	:param draggable: By default the layer control has a fixed position. Set this argument to :py:obj:`True` to allow dragging the control around.
	:param \*\*kwargs: Additional keyword arguments for the javascript class.
	"""

	control_class_name = "new L.Control.GroupedLayers"

	_template = Template(
			"""
		{% macro script(this, kwargs) %}
			var {{ this.get_name() }}_layers = {
				base_layers : {
					{%- for key, val in this.base_layers.items() %}
					{{ key|tojson }} : {{val}},
					{%- endfor %}
				},
				overlays :  {
					{% for group_name, group_data in this.groups.items() %}
						{{ group_name|tojson }}: {
							{% for layer_name, layer in group_data.items() %}
								{{ layer_name|tojson }}: {{ layer.get_name() }},
							{% endfor %}
						},
					{% endfor %}
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

	default_js = [
			(
					"groupedlayercontrol-js",
					"https://cdn.jsdelivr.net/gh/ismyrnow/leaflet-groupedlayercontrol@0.6.1/dist/leaflet.groupedlayercontrol.min.js",
					),
			]
	default_css = [
			(
					"groupedlayercontrol-css",
					"https://cdn.jsdelivr.net/gh/ismyrnow/leaflet-groupedlayercontrol@0.6.1/dist/leaflet.groupedlayercontrol.min.css",
					),
			]

	def __init__(
			self,
			groups: dict[str, dict[str, Layer]],
			position: str = "topright",
			collapsed: bool = True,
			autoZIndex: bool = True,
			draggable: bool = False,
			**kwargs: TypeJsonValue,
			):
		super().__init__(
				position=position,
				collapsed=collapsed,
				autoZIndex=autoZIndex,
				draggable=draggable,
				**kwargs,
				)
		self._name = "GroupedLayerControl"
		self.groups = groups


class ToggleGroupedLayerControl(GroupedLayerControl):
	r"""
	Customised GroupedLayerControl that is shown/hidden on click rather than mouseover.
	"""

	control_class_name = "new L.Control.GroupedLayersToggle"

	default_js = GroupedLayerControl.default_js + [
			(
					"groupedlayercontrol-toggle-js",
					f"https://cdn.jsdelivr.net/gh/domdfcoding/folium-layercontrols@v{__version__}/folium_layercontrols/leaflet.groupedlayercontrol.toggle.js",
					),
			]
