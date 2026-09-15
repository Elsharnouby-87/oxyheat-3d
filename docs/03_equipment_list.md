# 03 — Master Equipment List / Blender Object Hierarchy

**Status:** V0.1  
**Purpose:** define what is to be modelled before detailed Blender work begins.

## 00_SITE

- `Ground_Plane`
- `Concrete_Paving`
- `Roads`
- `Pipe_Racks`
- `Drainage_Channels`
- `Lighting_Poles`
- `Safety_Barriers`
- `Equipment_Nameplates`
- `Area_Signage`

**Detail level:** low to medium. Site objects provide scale and refinery context; they are not the visual focus.

---

## 01_GREEN_POWER

- `PV_Array_Representative`
- `Wind_Turbine_Representative`
- `Power_Transformer`
- `Rectifier_Package`
- `Electrical_Cable_Route`

**Detail level:** low to medium. Only enough geometry to explain the green-power context.

---

## 02_ELECTROLYZER

- `Electrolyzer_Skid`
- `Electrolyzer_Stacks`
- `Water_Inlet_Header`
- `H2_Separator`
- `O2_Separator`
- `H2_Product_Header`
- `O2_Product_Header`
- `Local_Control_Panel`
- `Package_Piping`
- `Package_Structure`

**Detail level:** medium.

The electrolyzer shall look credible as packaged industrial equipment but shall not compete visually with the fired heater.

---

## 03_O2_CONDITIONING

### Main process objects

- `O2_Inlet_Header`
- `O2_Moisture_Separator`
- `O2_Dryer`
- `O2_Buffer_Vessel`
- `O2_Filter`
- `O2_Pressure_Control_Station`
- `O2_Flow_Meter`
- `O2_Control_Valve`
- `O2_ESD_Valve`
- `O2_Check_Valve`
- `O2_DBB_Isolation`
- `O2_Vent_Header`
- `O2_Analyzer`
- `O2_Distribution_Header`

### Supporting objects

- skid frame
- local panel
- pressure gauges
- instrument tubing
- supports
- access grating
- small-bore vent/drain representation

**Detail level:** high.

The O2 conditioning skid is one of the key technical storytelling areas of the project.

---

## 04_COMBUSTION_AIR

- `Air_Intake`
- `Air_Filter`
- `FD_Fan`
- `FD_Fan_Motor`
- `Fan_Inlet_Damper`
- `Fan_Discharge_Damper`
- `Main_Air_Duct`
- `O2_Injection_Manifold`
- `O2_Injection_Lances_or_Ports`
- `Mixing_Chamber`
- `Static_Mixer`
- `Mixed_Oxidant_Analyzer`
- `Enriched_Air_Duct`
- `Burner_Air_Distribution_Header`
- `Expansion_Joints`
- `Duct_Supports`

**Detail level:** high at O2 injection / mixing section; medium elsewhere.

---

## 05_BOX_HEATER

### 05A_STRUCTURE

- `Heater_Steel_Frame`
- `Heater_Casing`
- `Structural_Columns`
- `Structural_Beams`
- `Main_Platforms`
- `Maintenance_Platforms`
- `Ladders`
- `Stairs`
- `Handrails`
- `Toe_Plates`
- `Access_Doors`

### 05B_RADIANT_SECTION

- `Radiant_Box`
- `Radiant_Refractory`
- `Radiant_Wall_Lining`
- `Radiant_Tubes`
- `Radiant_Return_Bends`
- `Tube_Supports`
- `Tube_Guides`
- `Process_Inlet_Nozzle`
- `Process_Outlet_Nozzle`
- `Peep_Doors`
- `Inspection_Ports`

### 05C_BURNERS

- `Burner_01` ... `Burner_N`
- `Burner_Register`
- `Burner_Quarl`
- `Burner_Tile`
- `Burner_Tip`
- `Pilot_Burner`
- `Igniter`
- `Flame_Scanner`
- `Burner_Air_Connection`
- `Burner_Fuel_Connection`

### 05D_FUEL_GAS

- `Fuel_Gas_Main_Header`
- `Fuel_Gas_Filter_or_KO_Representation`
- `Fuel_Gas_PCV`
- `Fuel_Gas_Flow_Meter`
- `Fuel_Gas_ESD_Valve`
- `Burner_Fuel_Manifold`
- `Individual_Burner_Branches`
- `Pilot_Gas_Header`
- `Pilot_Branches`

### 05E_TRANSITION_AND_CONVECTION

- `Bridge_Transition_Zone`
- `Shield_Tubes`
- `Convection_Bank_01`
- `Convection_Bank_02`
- `Convection_Bank_N`
- `Convection_Tube_Supports`
- `Convection_Casing`
- `Access_Doors_Convection`
- `Sootblower_Representation`

### 05F_BREECHING_STACK

- `Breeching`
- `Stack_Damper`
- `Stack_Base`
- `Stack_Shell`
- `Stack_Platforms`
- `Stack_Ladder`
- `Stack_Analyzer_Nozzles`
- `Sampling_Ports`

**Detail level:** very high. This is the hero asset.

---

## 06_INSTRUMENTATION_CONTROL

### Flow / pressure

- `FT_Fuel_Gas`
- `PT_Fuel_Gas`
- `FT_Combustion_Air`
- `PT_Combustion_Air`
- `FT_O2`
- `PT_O2`
- `FIC_O2`

### Combustion / flue gas

- `AIT_Mixed_Oxidant_O2`
- `AIT_Stack_O2`
- `AIT_CO`
- `AIT_NOx`
- `PIT_Furnace_Draft`

### Temperature

- `TT_Bridgewall`
- `TT_Stack`
- `TT_Tube_Skin_01` ... `TT_Tube_Skin_N`

### Safety / control

- `Flame_Scanner_01` ... `Flame_Scanner_N`
- `BMS_Panel`
- `SIS_ESD_Panel`
- `Local_O2_Panel`
- `Operator_HMI`
- `Junction_Boxes`
- `Instrument_Cable_Trays`

**Detail level:** medium to high for instruments that participate in animations.

---

## 07_FLUE_GAS

- `Radiant_Flue_Gas_Volume`
- `Convection_Flue_Gas_Volume`
- `Breeching_Flue_Gas_Path`
- `Stack_Flue_Gas_Path`
- `Flue_Gas_Sampling_Points`
- `Future_CCUS_TieIn`
- `Future_Diverter_Damper`

These may contain invisible helper geometry to drive particles / arrows / scientific overlays.

---

## 08_FUTURE_CCUS

- `CCUS_Booster_Fan`
- `Flue_Gas_Cooler`
- `Flue_Gas_Conditioner`
- `Absorber_Column`
- `Absorber_Packing_Representation`
- `Solvent_Circulation_Pump`
- `Rich_Lean_Exchanger`
- `Stripper_Column`
- `Reboiler`
- `Condenser`
- `CO2_KO_Drum`
- `CO2_Compressor`
- `CO2_Export_Header`

**Detail level:** medium initially. Future optional module.

---

## 09_FUTURE_OXYFUEL_FGR

- `FGR_Takeoff`
- `FGR_Duct`
- `FGR_Isolation_Damper`
- `FGR_Control_Damper`
- `FGR_Fan`
- `FGR_Mixing_Chamber`
- `High_Purity_O2_Header`
- `O2_FGR_Mixing_Section`
- `Advanced_Oxidant_Header`

**Detail level:** medium. Must remain visually identifiable as a future configuration.

---

## 10_ANIMATION_CONTROLLERS

- `CTRL_Mode_21pct`
- `CTRL_Mode_27pct`
- `CTRL_Mode_30pct`
- `CTRL_Mode_35pct`
- `CTRL_O2_Trip`
- `CTRL_Air_Fallback`
- `CTRL_CCUS_OnOff`
- `CTRL_FGR_Future`
- `CTRL_Cutaway_Heater`
- `CTRL_Cutaway_Mixer`
- `CTRL_Flow_Visibility`
- `CTRL_Labels`
- `CTRL_HeatFlux_Overlay`

---

## 11_VISUALIZATION_HELPERS

- `Flow_Arrow_H2`
- `Flow_Arrow_O2`
- `Flow_Arrow_Air`
- `Flow_Arrow_Fuel`
- `Flow_Arrow_FlueGas`
- `Molecule_N2`
- `Molecule_O2`
- `Molecule_CO2`
- `Molecule_H2O`
- `Flame_Volume`
- `Temperature_Overlay`
- `Heat_Flux_Overlay`
- `Equipment_Label_Anchors`
- `Camera_Path_Overview`
- `Camera_Path_O2_Skid`
- `Camera_Path_Mixer`
- `Camera_Path_Heater_Cutaway`

---

## Modelling priority

### Priority A — model first

1. Box heater blockout
2. Radiant / convection split
3. Burner arrangement
4. Combustion-air duct
5. O2 conditioning skid blockout
6. O2 injection / mixing section
7. Fuel-gas manifold
8. Stack / breeching

### Priority B — engineering detail

1. Heater internals
2. valves and meters
3. BMS / SIS visual elements
4. platforms / ladders / access
5. analyzers and temperature points
6. oxygen-service piping supports

### Priority C — context and future modules

1. electrolyzer context
2. renewable-power context
3. CCUS island
4. oxy-fuel / FGR loop
5. full refinery environment
