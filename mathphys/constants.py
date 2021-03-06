import math as _math
import mathphys.base_units as _u

# temporary auxiliary derived units
_volt    = (_u.kilogram * _u.meter**2) / (_u.ampere * _u.second**2)
_coulomb = _u.second * _u.ampere
_joule   = _u.kilogram * _u.meter**2 / _u.second**2

# physical constants
# ==================
light_speed              = 299792458 * (_u.meter/_u.second)                               # [m/s]   - definition
vacuum_permeability      = 4*_math.pi*1e-7   * (_volt * _u.second / _u.ampere / _u.meter) # [T.m/A] - definition
elementary_charge        = 1.602176565e-19  * _coulomb                                    # [C]     - 2014-06-11
electron_mass            = 9.10938291e-31   * _u.kilogram                                 # [Kg]    - 2014-06-11
electron_rest_energy     = electron_mass * _math.pow(light_speed,2)                       # [Kg.m^2/s^2] - derived
vacuum_permitticity      = 1.0/(vacuum_permeability * _math.pow(light_speed,2))           # [V.s/(A.m)]  - derived
electron_radius          = _math.pow(elementary_charge,2)/(4*_math.pi*vacuum_permitticity*electron_rest_energy) # [m] - derived

_joule_2_eV              = _joule / elementary_charge

reduced_planck_constant  = 1.054571726e-34 * _joule*_u.second                          # [J.s]  - 2014-07-22
rad_cgamma               = 4*_math.pi*electron_radius/_math.pow(electron_rest_energy/elementary_charge/1e9,3)/3         # [m]/[GeV]^3 - derived
Cq                       = (55.0/(32*_math.sqrt(3.0))) * (reduced_planck_constant) * light_speed / electron_rest_energy # [m] - derived
Ca                       = electron_radius*light_speed / (3*_math.pow(electron_rest_energy*_joule_2_eV/1.0e9, 3))       # [m^2/(s.GeV^3)] - derived
