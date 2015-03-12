#!/usr/bin/python
# -*- coding: utf-8 -*-

from parameter import Parameter
from definitions import ParameterDefinitions as Prms

parameter_list = [
  Parameter(name='TS beam energy', group='GIA', is_derived=False, value=Prms.ts_beam_energy, symbol=r'<math>E</math>', units='GeV', deps=[], obs=[], ),
  Parameter(name='TS beam gamma factor', group='FAC', is_derived=False, value=Prms.ts_beam_gamma_factor, symbol=r'<math>\gamma</math>', units='', deps=['TS beam energy'], obs=[], ),
  Parameter(name='TS beam beta factor', group='FAC', is_derived=False, value=Prms.ts_beam_beta_factor, symbol=r'<math>\beta</math>', units='', deps=['TS beam gamma factor'], obs=[], ),
  Parameter(name='TS beam velocity', group='FAC', is_derived=False, value=Prms.ts_beam_velocity, symbol=r'<math>v</math>', units='', deps=['TS beam beta factor'], obs=[], ),
  Parameter(name='TS beam magnetic rigidity', group='FAC', is_derived=False, value=Prms.ts_beam_magnetic_rigidity, symbol=r'<math>(B\rho)</math>', units=unicode('T·m', encoding='utf-8'), deps=['TS beam energy'], obs=[r'<math>(B\rho)=\frac{p}{ec}=\frac{E}{ec^2}</math>'], ),

  Parameter(name='TS lattice length', group='FAC', is_derived=False, value=Prms.ts_total_length, symbol=r'<math>L</math>', units='m', deps=[], obs=['Includes septum.'], ),
  Parameter(name='TS magnet dipole number', group='FAC', is_derived=False, value=Prms.ts_number_of_dipoles, symbol=r'<math>N_\text{DIP}</math>', units='', deps=[], obs=[], ),
  Parameter(name='TS magnet quadrupole number', group='FAC', is_derived=False, value=Prms.ts_number_of_quadrupoles, symbol=r'<math>N_\text{QUAD}</math>', units='', deps=[], obs=[], ),

  Parameter(name='TS magnet quadrupole maximum gradient', group='FAC', is_derived=False, value=Prms.ts_maximum_quadrupole_gradient, symbol=r"<math>B'_\text{max}</math>", units='T/m', deps=[], obs=[], ),
  Parameter(name='TS magnet dipole hardedge length', group='FAC', is_derived=False, value=Prms.ts_hardedge_length_of_dipoles, symbol=r'<math>L_\text{DIP}</math>', units='m', deps=[], obs=[], ),

  Parameter(name='TS magnet septum hardedge length', group='FAC', is_derived=False, value=Prms.ts_hardedge_length_of_extraction_septum, symbol=r'<math>L_\text{sep,ext}</math>', units='m', deps=[], obs=[], ),

  Parameter(name='TS hardedge length of thick injection septum', group='FAC', is_derived=False, value=Prms.ts_hardedge_length_of_thick_injection_septum, symbol=r'<math>L_\text{thick sep,inj}</math>', units='m', deps=[], obs=[], ),



  Parameter(name='TS hardedge length of thin injection septum', group='FAC', is_derived=False, value=Prms.ts_hardedge_length_of_thin_injection_septum, symbol=r'<math>L_\text{thin sep,inj}</math>', units='m', deps=[], obs=[], ),
  Parameter(name='TS deflection angle of dipoles', group='FAC', is_derived=False, value=Prms.ts_dipole_deflection_angle, symbol=r'<math>\theta_\text{DIP}</math>', units=unicode('°',encoding='utf-8'), deps=[], obs=[], ),
  Parameter(name='TS deflection angle of extraction septum', group='FAC', is_derived=False, value=Prms.ts_extraction_septum_deflection_angle, symbol=r'<math>\theta_\text{sep,ext}</math>', units=unicode('°',encoding='utf-8'), deps=[], obs=[], ),
  Parameter(name='TS deflection angle of thick injection septum', group='FAC', is_derived=False, value=Prms.ts_thick_injection_septum_deflection_angle, symbol=r'<math>\theta_\text{thick sep,inj}</math>', units=unicode('°',encoding='utf-8'), deps=[], obs=[], ),
  Parameter(name='TS deflection angle of thin injection septum', group='FAC', is_derived=False, value=Prms.ts_thin_injection_septum_deflection_angle, symbol=r'<math>\theta_\text{thin sep,inj}</math>', units=unicode('°',encoding='utf-8'), deps=[], obs=[], ),
  Parameter(name='TS dipole bending radius', group='FAC', is_derived=False, value=Prms.ts_dipole_bending_radius, symbol=r'<math>\rho_\text{DIP}</math>', units='m', deps=['TS hardedge length of dipoles',        'TS deflection angle of dipoles'],   obs     =[r'<math>\rho_\text{DIP}=\frac{L_\text{DIP}}{\theta_\text{DIP}}</math>'],
  Parameter(name='TS extraction septum bending radius', group='FAC', is_derived=False, value=Prms.ts_extraction_septum_bending_radius, symbol=r'<math>\rho_\text{sep,ext}</math>', units='m', deps=['TS hardedge length of extraction septum',        'TS deflection angle of extraction septum'],   obs     =[r'<math>\rho_\text{sep,ext}=\frac{L_\text{sep,ext}}{\theta_\text{sep,ext}}</math>'],
  Parameter(name='TS thick injection septum bending radius', group='FAC', is_derived=False, value=Prms.ts_thick_injection_septum_bending_radius, symbol=r'<math>\rho_\text{thick sep,inj}</math>', units='m', deps=['TS hardedge length of thick injection septum',        'TS deflection angle of thick injection septum'],   obs     =[r'<math>\rho_\text{thick sep,inj}=\frac{L_\text{thick sep,inj}}{\theta_\text{thick sep,inj}}</math>'],
  Parameter(name='TS thin injection septum bending radius', group='FAC', is_derived=False, value=Prms.ts_thin_injection_septum_bending_radius, symbol=r'<math>\rho_\text{thin sep,inj}</math>', units='m', deps=['TS hardedge length of thin injection septum',        'TS deflection angle of thin injection septum'],   obs     =[r'<math>\rho_\text{thin sep,inj}=\frac{L_\text{thin sep,inj}}{\theta_\text{thin sep,inj}}</math>'],
  Parameter(name='TS dipole magnetic field', group='FAC', is_derived=False, value=Prms.ts_dipole_magnetic_field, symbol=r'<math>B_\text{DIP}</math>', units='T', deps=['TS beam magnetic rigidity',        'TS dipole bending radius'],   obs     =[r'<math>B_\text{DIP}=\frac{(B\rho)}{\rho_\text{DIP}}</math>'],
  Parameter(name='TS extraction septum magnetic field', group='FAC', is_derived=False, value=Prms.ts_extraction_septum_magnetic_field, symbol=r'<math>B_\text{sep,ext}</math>', units='T', deps=['TS beam magnetic rigidity',        'TS extraction septum bending radius'],   obs     =[r'<math>B_\text{sep,ext}=\frac{(B\rho)}{\rho_\text{sep,ext}}</math>'],
  Parameter(name='TS thick injection septum magnetic field', group='FAC', is_derived=False, value=Prms.ts_thick_injection_septum_magnetic_field, symbol=r'<math>B_\text{thick sep,inj}</math>', units='T', deps=['TS beam magnetic rigidity',        'TS thick injection septum bending radius'],   obs     =[r'<math>B_\text{thick sep,inj}=\frac{(B\rho)}{\rho_\text{thick sep,inj}}</math>'],
  Parameter(name='TS thin injection septum magnetic field', group='FAC', is_derived=False, value=Prms.ts_thin_injection_septum_magnetic_field, symbol=r'<math>B_\text{thin sep,inj}</math>', units='T', deps=['TS beam magnetic rigidity',        'TS thin injection septum bending radius'],   obs     =[r'<math>B_\text{thin sep,inj}=\frac{(B\rho)}{\rho_\text{thin sep,inj}}</math>'],
  Parameter(name='TS dipole sagitta', group='FAC', is_derived=False, value=Prms.ts_dipole_sagitta, symbol=r'<math>S_\text{DIP}</math>', units='mm', deps=[], obs=[], ),
  Parameter(name='TS extraction septum sagitta', group='FAC', is_derived=False, value=Prms.ts_extraction_septum_sagitta, symbol=r'<math>S_\text{sep,ext}</math>', units='mm', deps=[], obs=[], ),
  Parameter(name='TS thick injection septum sagitta', group='FAC', is_derived=False, value=Prms.ts_thick_injection_septum_sagitta, symbol=r'<math>S_\text{thick sep,inj}</math>', units='mm', deps=[], obs=[], ),
  Parameter(name='TS thin injection septum sagitta', group='FAC', is_derived=False, value=Prms.ts_thin_injection_septum_sagitta, symbol=r'<math>S_\text{thin sep,inj}</math>', units='mm', deps=[], obs=[], ),
  Parameter(name='TS number of dipoles', group='FAC', is_derived=False, value=Prms.ts_number_of_dipoles, symbol=r'<math>N_\text{DIP}</math>', units='', deps=[], obs=[], ),
  Parameter(name='TS number of extraction septa', group='FAC', is_derived=False, value=Prms.ts_number_of_extraction_septa, symbol=r'<math>N_\text{sep,ext}</math>', units='', deps=[], obs=[], ),
  Parameter(name='TS number of thick injection septa', group='FAC', is_derived=False, value=Prms.ts_number_of_thick_injection_septa, symbol=r'<math>N_\text{thick sep,inj}</math>', units='', deps=[], obs=[], ),
  Parameter(name='TS number of thin injection septa', group='FAC', is_derived=False, value=Prms.ts_number_of_thin_injection_septa, symbol=r'<math>N_\text{thin sep,inj}</math>', units='', deps=[], obs=[], ),
  Parameter(name='TS hardedge length of QA1 quadrupoles', group='FAC', is_derived=False, value=Prms.ts_hardedge_length_of_QA1_quadrupoles, symbol=r'<math>L_\text{QA1}</math>', units='m', deps=[], obs=[], ),
  Parameter(name='TS hardedge length of QA2 quadrupoles', group='FAC', is_derived=False, value=Prms.ts_hardedge_length_of_QA2_quadrupoles, symbol=r'<math>L_\text{QA2}</math>', units='m', deps=[], obs=[], ),
  Parameter(name='TS hardedge length of QB1 quadrupoles', group='FAC', is_derived=False, value=Prms.ts_hardedge_length_of_QB1_quadrupoles, symbol=r'<math>L_\text{QB1}</math>', units='m', deps=[], obs=[], ),
  Parameter(name='TS hardedge length of QB2 quadrupoles', group='FAC', is_derived=False, value=Prms.ts_hardedge_length_of_QB2_quadrupoles, symbol=r'<math>L_\text{QB2}</math>', units='m', deps=[], obs=[], ),
  Parameter(name='TS hardedge length of QC1 quadrupoles', group='FAC', is_derived=False, value=Prms.ts_hardedge_length_of_QC1_quadrupoles, symbol=r'<math>L_\text{QC1}</math>', units='m', deps=[], obs=[], ),
  Parameter(name='TS hardedge length of QC2 quadrupoles', group='FAC', is_derived=False, value=Prms.ts_hardedge_length_of_QC2_quadrupoles, symbol=r'<math>L_\text{QC2}</math>', units='m', deps=[], obs=[], ),
  Parameter(name='TS hardedge length of QC3 quadrupoles', group='FAC', is_derived=False, value=Prms.ts_hardedge_length_of_QC3_quadrupoles, symbol=r'<math>L_\text{QC3}</math>', units='m', deps=[], obs=[], ),
  Parameter(name='TS hardedge length of QC4 quadrupoles', group='FAC', is_derived=False, value=Prms.ts_hardedge_length_of_QC4_quadrupoles, symbol=r'<math>L_\text{QC4}</math>', units='m', deps=[], obs=[], ),






  
  Parameter(name='TS QA1 quadrupole strength', group='FAC', is_derived=False, value=Prms.ts_QA1_quadrupole_strength, symbol=r'<math>K_\text{QA1}</math>', units='m<sup>-2</sup>', deps=[], obs=[], ),
  Parameter(name='TS QA2 quadrupole strength', group='FAC', is_derived=False, value=Prms.ts_QA2_quadrupole_strength, symbol=r'<math>K_\text{QA2}</math>', units='m<sup>-2</sup>', deps=[], obs=[], ),
  Parameter(name='TS QB1 quadrupole strength', group='FAC', is_derived=False, value=Prms.ts_QB1_quadrupole_strength, symbol=r'<math>K_\text{QB1}</math>', units='m<sup>-2</sup>', deps=[], obs=[], ),
  Parameter(name='TS QB2 quadrupole strength', group='FAC', is_derived=False, value=Prms.ts_QB2_quadrupole_strength, symbol=r'<math>K_\text{QB2}</math>', units='m<sup>-2</sup>', deps=[], obs=[], ),
  Parameter(name='TS QC1 quadrupole strength', group='FAC', is_derived=False, value=Prms.ts_QC1_quadrupole_strength, symbol=r'<math>K_\text{QC1}</math>', units='m<sup>-2</sup>', deps=[], obs=[], ),
  Parameter(name='TS QC2 quadrupole strength', group='FAC', is_derived=False, value=Prms.ts_QC2_quadrupole_strength, symbol=r'<math>K_\text{QC2}</math>', units='m<sup>-2</sup>', deps=[], obs=[], ),
  Parameter(name='TS QC3 quadrupole strength', group='FAC', is_derived=False, value=Prms.ts_QC3_quadrupole_strength, symbol=r'<math>K_\text{QC3}</math>', units='m<sup>-2</sup>', deps=[], obs=[], ),
  Parameter(name='TS QC4 quadrupole strength', group='FAC', is_derived=False, value=Prms.ts_QC4_quadrupole_strength, symbol=r'<math>K_\text{QC4}</math>', units='m<sup>-2</sup>', deps=[], obs=[], ),
  Parameter(name='TS QA1 quadrupole gradient', group='FAC', is_derived=False, value=Prms.ts_QA1_quadrupole_gradient, symbol=r"<math>B'_\text{QA1}</math>", units=unicode('T·m<sup>-1</sup>', encoding='utf-8'), deps=['TS QA1 quadrupole strength',        'TS beam magnetic rigidity'],   obs     =[r"<math>B'_\text{QA1}=(B\rho) K_\text{QA1}</math>"],
  Parameter(name='TS QA2 quadrupole gradient', group='FAC', is_derived=False, value=Prms.ts_QA2_quadrupole_gradient, symbol=r"<math>B'_\text{QA2}</math>", units=unicode('T·m<sup>-1</sup>', encoding='utf-8'), deps=['TS QA2 quadrupole strength',        'TS beam magnetic rigidity'],   obs     =[r"<math>B'_\text{QA2}=(B\rho) K_\text{QA2}</math>"],
  Parameter(name='TS QB1 quadrupole gradient', group='FAC', is_derived=False, value=Prms.ts_QB1_quadrupole_gradient, symbol=r"<math>B'_\text{QB1}</math>", units=unicode('T·m<sup>-1</sup>', encoding='utf-8'), deps=['TS QB1 quadrupole strength',        'TS beam magnetic rigidity'],   obs     =[r"<math>B'_\text{QB1}=(B\rho) K_\text{QB1}</math>"],
  Parameter(name='TS QB2 quadrupole gradient', group='FAC', is_derived=False, value=Prms.ts_QB2_quadrupole_gradient, symbol=r"<math>B'_\text{QB2}</math>", units=unicode('T·m<sup>-1</sup>', encoding='utf-8'), deps=['TS QB2 quadrupole strength',        'TS beam magnetic rigidity'],   obs     =[r"<math>B'_\text{QB2}=(B\rho) K_\text{QB2}</math>"],
  Parameter(name='TS QC1 quadrupole gradient', group='FAC', is_derived=False, value=Prms.ts_QC1_quadrupole_gradient, symbol=r"<math>B'_\text{QC1}</math>", units=unicode('T·m<sup>-1</sup>', encoding='utf-8'), deps=['TS QC1 quadrupole strength',        'TS beam magnetic rigidity'],   obs     =[r"<math>B'_\text{QC1}=(B\rho) K_\text{QC1}</math>"],
  Parameter(name='TS QC2 quadrupole gradient', group='FAC', is_derived=False, value=Prms.ts_QC2_quadrupole_gradient, symbol=r"<math>B'_\text{QC2}</math>", units=unicode('T·m<sup>-1</sup>', encoding='utf-8'), deps=['TS QC2 quadrupole strength',        'TS beam magnetic rigidity'],   obs     =[r"<math>B'_\text{QC2}=(B\rho) K_\text{QC2}</math>"],
  Parameter(name='TS QC3 quadrupole gradient', group='FAC', is_derived=False, value=Prms.ts_QC3_quadrupole_gradient, symbol=r"<math>B'_\text{QC3}</math>", units=unicode('T·m<sup>-1</sup>', encoding='utf-8'), deps=['TS QC3 quadrupole strength',        'TS beam magnetic rigidity'],   obs     =[r"<math>B'_\text{QC3}=(B\rho) K_\text{QC3}</math>"],
  Parameter(name='TS QC4 quadrupole gradient', group='FAC', is_derived=False, value=Prms.ts_QC4_quadrupole_gradient, symbol=r"<math>B'_\text{QC4}</math>", units=unicode('T·m<sup>-1</sup>', encoding='utf-8'), deps=['TS QC4 quadrupole strength',        'TS beam magnetic rigidity'],   obs     =[r"<math>B'_\text{QC4}=(B\rho) K_\text{QC4}</math>"],
  Parameter(name='TS number of beam position monitors', group='FAC', is_derived=False, value=Prms.ts_number_of_beam_position_monitors, symbol=r'<math>N_\text{BPM}</math>', units='', deps=[], obs=[], ),
  Parameter(name='TS number of beam position monitors', group='FAC', is_derived=False, value=Prms.ts_number_of_beam_position_monitors, symbol=r'<math>N_\text{BPM}</math>', units='', deps=[], obs=[], ),
  Parameter(name='TS number of horizontal dipole correctors', group='FAC', is_derived=False, value=Prms.ts_number_of_horizontal_dipole_correctors, symbol=r'<math>N_\text{HCM}</math>', units='', deps=[], obs=[], ),
  Parameter(name='TS number of vertical dipole correctors', group='FAC', is_derived=False, value=Prms.ts_number_of_vertical_dipole_correctors, symbol=r'<math>N_\text{VCM}</math>', units='', deps=[], obs=[], ),
  Parameter(name='TS horizontal dipole correctors maximum strength', group='FAC', is_derived=False, value=Prms.ts_horizontal_dipole_corrector_maximum_strength, symbol=r'<math>\theta^\text{x, max}</math>', units=unicode('mrad', encoding='utf-8'), deps=[], obs=[], ),
  Parameter(name='TS vertical dipole correctors maximum strength', group='FAC', is_derived=False, value=Prms.ts_vertical_dipole_corrector_maximum_strength, symbol=r'<math>\theta^\text{y, max}</math>', units=unicode('mrad', encoding='utf-8'), deps=[], obs=[], ),
]
