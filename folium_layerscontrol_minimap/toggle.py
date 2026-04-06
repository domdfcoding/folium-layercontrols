#!/usr/bin/env python3
#
#  __init__.py
"""
Customised minimap layer control that is shown/hidden on click rather than mouseover.
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

# this package
from folium_layerscontrol_minimap import MinimapLayerControl, __version__

__all__ = ["ToggleMinimapLayerControl"]


class ToggleMinimapLayerControl(MinimapLayerControl):
	"""
	Customised minimap layer control that is shown/hidden on click rather than mouseover.
	"""

	control_class_name = "L.control.layers.minimap.toggle"
	default_js = MinimapLayerControl.default_js + [
			(
					"layerscontrol-minimap-toggle-js",
					f"https://cdn.jsdelivr.net/gh/domdfcoding/folium-layerscontrol-minimap@v{__version__}/folium_layerscontrol_minimap/L.Control.Layers.Minimap.Toggle.js",
					),
			]
	default_css = MinimapLayerControl.default_css + [
			(
					"layerscontrol-minimap-toggle-css",
					f"https://cdn.jsdelivr.net/gh/domdfcoding/folium-layerscontrol-minimap@v{__version__}/folium_layerscontrol_minimap/control.layers.minimap.css",
					),
			]
