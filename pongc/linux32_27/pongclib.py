# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pongclib', [dirname(__file__)])
        except ImportError:
            import _pongclib
            return _pongclib
        if fp is not None:
            try:
                _mod = imp.load_module('_pongclib', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pongclib = swig_import_helper()
    del swig_import_helper
else:
    import _pongclib
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def clear_image(img):
    return _pongclib.clear_image(img)
clear_image = _pongclib.clear_image

def draw_line_2x(img, x0, y0, x1, y1, color):
    return _pongclib.draw_line_2x(img, x0, y0, x1, y1, color)
draw_line_2x = _pongclib.draw_line_2x

def draw_ellipse_2x(img, x, y, rx, ry, color):
    return _pongclib.draw_ellipse_2x(img, x, y, rx, ry, color)
draw_ellipse_2x = _pongclib.draw_ellipse_2x

def fill_ellipse_2x(img, x, y, rx, ry, color):
    return _pongclib.fill_ellipse_2x(img, x, y, rx, ry, color)
fill_ellipse_2x = _pongclib.fill_ellipse_2x

def set_3d_params(actual_screen_width, actual_screen_height, viewport_scale):
    return _pongclib.set_3d_params(actual_screen_width, actual_screen_height, viewport_scale)
set_3d_params = _pongclib.set_3d_params

def to_fixed(x):
    return _pongclib.to_fixed(x)
to_fixed = _pongclib.to_fixed

def project_x(x, y, z):
    return _pongclib.project_x(x, y, z)
project_x = _pongclib.project_x

def project_y(x, y, z):
    return _pongclib.project_y(x, y, z)
project_y = _pongclib.project_y

def draw_line_3d(img, x0, y0, z0, x1, y1, z1, c):
    return _pongclib.draw_line_3d(img, x0, y0, z0, x1, y1, z1, c)
draw_line_3d = _pongclib.draw_line_3d

def draw_rect_3d(img, x0, y0, x1, y1, depth, c):
    return _pongclib.draw_rect_3d(img, x0, y0, x1, y1, depth, c)
draw_rect_3d = _pongclib.draw_rect_3d

def draw_circle_3d(img, x, y, z, radius, c):
    return _pongclib.draw_circle_3d(img, x, y, z, radius, c)
draw_circle_3d = _pongclib.draw_circle_3d

def fill_circle_3d(img, x, y, z, radius, c):
    return _pongclib.fill_circle_3d(img, x, y, z, radius, c)
fill_circle_3d = _pongclib.fill_circle_3d

def draw_ellipse_3d(img, x, y, z, rx, ry, c):
    return _pongclib.draw_ellipse_3d(img, x, y, z, rx, ry, c)
draw_ellipse_3d = _pongclib.draw_ellipse_3d
# This file is compatible with both classic and new-style classes.


