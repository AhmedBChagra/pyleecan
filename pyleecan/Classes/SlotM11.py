# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/SlotM11.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/SlotM11
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .SlotWind import SlotWind

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.SlotM11._comp_point_coordinate import _comp_point_coordinate
except ImportError as error:
    _comp_point_coordinate = error

try:
    from ..Methods.Slot.SlotM11.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.SlotM11.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Slot.SlotM11.comp_angle_opening import comp_angle_opening
except ImportError as error:
    comp_angle_opening = error

try:
    from ..Methods.Slot.SlotM11.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from ..Methods.Slot.SlotM11.comp_height_active import comp_height_active
except ImportError as error:
    comp_height_active = error

try:
    from ..Methods.Slot.SlotM11.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Slot.SlotM11.comp_surface_active import comp_surface_active
except ImportError as error:
    comp_surface_active = error

try:
    from ..Methods.Slot.SlotM11.get_surface_active import get_surface_active
except ImportError as error:
    get_surface_active = error


from ._check import InitUnKnowClassError


class SlotM11(SlotWind):
    """Polar Slot with Polar magnet"""

    VERSION = 1
    IS_SYMMETRICAL = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.SlotM11._comp_point_coordinate
    if isinstance(_comp_point_coordinate, ImportError):
        _comp_point_coordinate = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotM11 method _comp_point_coordinate: "
                    + str(_comp_point_coordinate)
                )
            )
        )
    else:
        _comp_point_coordinate = _comp_point_coordinate
    # cf Methods.Slot.SlotM11.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotM11 method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.SlotM11.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotM11 method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.SlotM11.comp_angle_opening
    if isinstance(comp_angle_opening, ImportError):
        comp_angle_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotM11 method comp_angle_opening: "
                    + str(comp_angle_opening)
                )
            )
        )
    else:
        comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.SlotM11.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotM11 method comp_height: " + str(comp_height))
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Slot.SlotM11.comp_height_active
    if isinstance(comp_height_active, ImportError):
        comp_height_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotM11 method comp_height_active: "
                    + str(comp_height_active)
                )
            )
        )
    else:
        comp_height_active = comp_height_active
    # cf Methods.Slot.SlotM11.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotM11 method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.SlotM11.comp_surface_active
    if isinstance(comp_surface_active, ImportError):
        comp_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotM11 method comp_surface_active: "
                    + str(comp_surface_active)
                )
            )
        )
    else:
        comp_surface_active = comp_surface_active
    # cf Methods.Slot.SlotM11.get_surface_active
    if isinstance(get_surface_active, ImportError):
        get_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotM11 method get_surface_active: "
                    + str(get_surface_active)
                )
            )
        )
    else:
        get_surface_active = get_surface_active
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        W0=0.0122,
        H0=0.001,
        Wmag=0.0122,
        Hmag=0.001,
        Zs=36,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "W0" in list(init_dict.keys()):
                W0 = init_dict["W0"]
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "Wmag" in list(init_dict.keys()):
                Wmag = init_dict["Wmag"]
            if "Hmag" in list(init_dict.keys()):
                Hmag = init_dict["Hmag"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
        # Set the properties (value check and convertion are done in setter)
        self.W0 = W0
        self.H0 = H0
        self.Wmag = Wmag
        self.Hmag = Hmag
        # Call SlotWind init
        super(SlotM11, self).__init__(Zs=Zs)
        # The class is frozen (in SlotWind init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        SlotM11_str = ""
        # Get the properties inherited from SlotWind
        SlotM11_str += super(SlotM11, self).__str__()
        SlotM11_str += "W0 = " + str(self.W0) + linesep
        SlotM11_str += "H0 = " + str(self.H0) + linesep
        SlotM11_str += "Wmag = " + str(self.Wmag) + linesep
        SlotM11_str += "Hmag = " + str(self.Hmag) + linesep
        return SlotM11_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from SlotWind
        if not super(SlotM11, self).__eq__(other):
            return False
        if other.W0 != self.W0:
            return False
        if other.H0 != self.H0:
            return False
        if other.Wmag != self.Wmag:
            return False
        if other.Hmag != self.Hmag:
            return False
        return True

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from SlotWind
        S += super(SlotM11, self).__sizeof__()
        S += getsizeof(self.W0)
        S += getsizeof(self.H0)
        S += getsizeof(self.Wmag)
        S += getsizeof(self.Hmag)
        return S

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from SlotWind
        SlotM11_dict = super(SlotM11, self).as_dict()
        SlotM11_dict["W0"] = self.W0
        SlotM11_dict["H0"] = self.H0
        SlotM11_dict["Wmag"] = self.Wmag
        SlotM11_dict["Hmag"] = self.Hmag
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        SlotM11_dict["__class__"] = "SlotM11"
        return SlotM11_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.W0 = None
        self.H0 = None
        self.Wmag = None
        self.Hmag = None
        # Set to None the properties inherited from SlotWind
        super(SlotM11, self)._set_None()

    def _get_W0(self):
        """getter of W0"""
        return self._W0

    def _set_W0(self, value):
        """setter of W0"""
        check_var("W0", value, "float", Vmin=0)
        self._W0 = value

    W0 = property(
        fget=_get_W0,
        fset=_set_W0,
        doc=u"""Slot isthmus angular width.

        :Type: float
        :min: 0
        """,
    )

    def _get_H0(self):
        """getter of H0"""
        return self._H0

    def _set_H0(self, value):
        """setter of H0"""
        check_var("H0", value, "float", Vmin=0)
        self._H0 = value

    H0 = property(
        fget=_get_H0,
        fset=_set_H0,
        doc=u"""Slot isthmus height.

        :Type: float
        :min: 0
        """,
    )

    def _get_Wmag(self):
        """getter of Wmag"""
        return self._Wmag

    def _set_Wmag(self, value):
        """setter of Wmag"""
        check_var("Wmag", value, "float", Vmin=0)
        self._Wmag = value

    Wmag = property(
        fget=_get_Wmag,
        fset=_set_Wmag,
        doc=u"""Magnet angular width

        :Type: float
        :min: 0
        """,
    )

    def _get_Hmag(self):
        """getter of Hmag"""
        return self._Hmag

    def _set_Hmag(self, value):
        """setter of Hmag"""
        check_var("Hmag", value, "float", Vmin=0)
        self._Hmag = value

    Hmag = property(
        fget=_get_Hmag,
        fset=_set_Hmag,
        doc=u"""Magnet Height

        :Type: float
        :min: 0
        """,
    )