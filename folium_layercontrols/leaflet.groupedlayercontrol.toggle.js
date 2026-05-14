// Adapted from https://github.com/ismyrnow/leaflet-groupedlayercontrol
// Copyright 2013 Ishmael Smyrnow
//
// Permission is hereby granted, free of charge, to any person obtaining
// a copy of this software and associated documentation files (the
// "Software"), to deal in the Software without restriction, including
// without limitation the rights to use, copy, modify, merge, publish,
// distribute, sublicense, and/or sell copies of the Software, and to
// permit persons to whom the Software is furnished to do so, subject to
// the following conditions:
//
// The above copyright notice and this permission notice shall be
// included in all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
// EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
// MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
// NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
// LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
// OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
// WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

/*
 * leaflet.groupedlayercontro.toggle
 *
 * A layer control which provides for layer groupings, with visibility toggle.
 *
 * Dominic Davis-Foster <dominic@davis-foster.co.uk>
 */

L.Control.GroupedLayersToggle = L.Control.GroupedLayers.extend({
	_initLayout: function() {
		L.Control.GroupedLayers.prototype._initLayout.call(this);
		L.DomEvent.off(this._container, 'mouseover', this._expand, this);
		L.DomEvent.off(this._container, 'mouseout', this._collapse, this);
	},
});

L.control.groupedLayers.toggle = function(baseLayers, groupedOverlays, options) {
	return new L.Control.GroupedLayersToggle(baseLayers, groupedOverlays, options);
};
