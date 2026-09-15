# 01 — Engineering Design Basis

**Document status:** V0.1 / Concept definition  
**Milestone:** M0 — Engineering Architecture Freeze

## 1. Purpose

Define the engineering basis for a detailed 3D representation of an existing refinery **box fired heater** retrofitted for controlled oxygen enrichment using electrolyzer by-product oxygen.

The 3D model shall be technically coherent enough to explain the process, controls, safeguards, flow paths and progressive operating modes without implying that it is a construction-ready design.

## 2. Base process philosophy

The base concept is **oxygen enrichment of combustion air**, not immediate conversion to full oxy-fuel firing.

The intended process sequence is:

1. Green electricity feeds a water electrolyzer.
2. Hydrogen leaves as the primary product.
3. Oxygen leaves as a by-product stream.
4. Oxygen is conditioned for heater service.
5. Conditioned oxygen is introduced into the combustion-air system.
6. Oxygen and air are mixed before distribution to the heater burners.
7. The fired heater operates at progressively elevated oxidant O2 concentration.
8. The heater retains the ability to return to conventional air firing.
9. Flue gas exits through the normal path, with provision for future CO2-capture integration.

## 3. Heater basis

### 3.1 Heater type

A **refinery box heater** is selected as the reference geometry because it gives clear visual access to:

- burner arrangement
- radiant chamber
- radiant coils
- bridge / transition region
- shield tubes
- convection banks
- breeching and stack
- burner-air distribution
- fuel-gas manifold
- access platforms and instrumentation

### 3.2 Representation basis

The heater shall be representative rather than a copy of a specific licensed/OEM design unless project-specific drawings are later provided and approved for use.

### 3.3 Study-scale context

The presentation study used a representative large heater basis of approximately **120 MW useful duty**, natural-gas firing and 8,000 operating hours/year. These values are contextual screening assumptions and do not define final geometry or detailed thermal design.

## 4. Oxygen-enrichment operating envelope for visualization

The following oxidant states will be represented:

| State | Nominal oxidant O2 | Purpose |
|---|---:|---|
| Conventional | ~21% | Baseline air firing |
| Enrichment 1 | ~27% | Initial moderate enrichment |
| Enrichment 2 | ~30% | Intermediate visualization point |
| Enrichment 3 | ~35% | Upper moderate screening point |
| Advanced | High-purity O2 + FGR | Future concept only |

The 27–35% range is treated as the base progressive-enrichment visualization envelope. Detailed burner operability and safe limits remain site-specific.

## 5. Oxygen system design intent

The 3D model shall show a credible oxygen-service chain including, at minimum:

- oxygen take-off from electrolyzer package
- moisture control / drying representation
- buffer capacity
- pressure matching / pressure regulation
- filtration where appropriate
- flow measurement
- control valve
- emergency isolation
- non-return / backflow protection
- oxygen-compatible distribution header
- vent / safe depressurization representation where required
- analyzer / quality indication

Exact materials, valve types, cleaning requirements, velocity limits and oxygen-service design rules are intentionally not frozen at V0.1.

## 6. Combustion-air integration basis

Preferred base visualization arrangement:

**Atmospheric air -> intake/filter -> FD fan -> main air duct -> O2 injection/mixing section -> enriched-air duct/header -> burners**

The model shall visually distinguish the oxygen system from the fuel-gas system. Oxygen shall not be shown injected into the fuel-gas line.

The exact final injection geometry is subject to later CFD / mixing review. The V0.1 model will use an engineered **duct-injection and mixing section** as the preferred concept.

## 7. Control philosophy basis

The model shall support visualization of:

- fuel flow
- combustion-air flow
- oxygen flow
- cross-limited fuel/air/O2 logic
- O2 enrichment ramping
- furnace draft supervision
- stack O2 monitoring
- flame supervision
- O2 isolation on loss of permissive
- fallback to conventional air firing

BMS/SIS representations are educational and architectural, not approved cause-and-effect logic.

## 8. Heater monitoring basis

Instrumentation to be visually represented may include:

- fuel-gas flow and pressure
- combustion-air flow
- oxygen flow and pressure
- mixed-oxidant analyzer
- stack O2
- CO
- NOx
- furnace pressure / draft
- bridgewall temperature
- tube-skin temperature points
- flame scanners
- burner permissive / trip indicators

## 9. Flue-gas basis

The model shall be able to demonstrate the screening trends from the presentation:

- reduced dry flue-gas volume as oxidant O2 rises
- reduced nitrogen dilution
- increased dry CO2 concentration

At the study basis, the presentation indicates approximately:

- 27% O2: ~25% lower dry flue gas versus conventional air firing
- 30% O2: ~33% lower
- 35% O2: ~44% lower
- dry CO2 rising from ~10.6% at conventional air firing to ~19% near 35% O2

These values are screening-model outputs and shall be labelled as such in visualizations.

## 10. Future modules

### 10.1 Post-combustion CO2 capture

A future CCUS block may contain:

- flue-gas take-off / diverter
- booster fan
- cooling / conditioning
- absorber
- solvent loop
- stripper / regenerator
- reboiler
- CO2 compression
- CO2 product/export line

This is optional and downstream of the core oxygen-enrichment concept.

### 10.2 Oxy-fuel + FGR

The future advanced layer may contain:

- FGR take-off
- recycle duct
- FGR fan
- control damper
- O2/FGR mixing section
- high-purity oxygen operating state

It shall be visually distinguished from the base 27–35% enrichment configuration.

## 11. Visual-detail strategy

### High detail

- box heater exterior and internals
- burner front and burner components
- O2 conditioning skid
- O2/air mixing section
- fuel-gas and combustion-air interfaces
- key valves / instruments

### Medium detail

- electrolyzer package
- FD fan
- piping supports / pipe rack
- stack / breeching
- future CCUS main equipment

### Context detail

- renewable-power assets
- roads / paving / lighting
- remote plant background

## 12. Engineering limitations

The model shall not imply that the following have already been completed:

- final heater heat balance
- final fuel-saving prediction
- burner OEM approval
- oxygen-service mechanical design
- detailed CFD
- detailed HAZOP/LOPA/SIL verification
- final BMS cause-and-effect
- final refractory / tube heat-flux check
- final NOx / CO prediction
- final CO2-capture design

These remain validation activities outside the V0.1 visualization basis.
