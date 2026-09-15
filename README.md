# OxyHeat 3D

**Oxygen-Enriched Fired Heater 3D Engineering Visualization and Digital Twin Development**

OxyHeat 3D is an engineering-led 3D visualization project for a refinery **box fired heater** retrofitted for controlled oxygen-enriched combustion using electrolyzer by-product oxygen.

The project is intended to turn the technical concept into a detailed, inspectable and eventually interactive 3D system model covering the path from green-hydrogen oxygen production through oxygen conditioning, combustion-air enrichment, fired-heater operation, flue-gas handling and optional future CCUS / oxy-fuel-FGR integration.

> **Project status:** V0.1 — Engineering Architecture Definition  
> **Current milestone:** M0 — Engineering Architecture Freeze

## Core system

```text
Renewable Power
      |
      v
Electrolyzer --------------------------> H2 product
      |
      v
O2 by-product
      |
      v
O2 Conditioning & Control
      |
      +-----------------------------+
                                    |
Atmospheric Air -> FD Fan -> Air Duct -> O2/Air Mixing -> Enriched Oxidant
                                                     |
Fuel Gas -------------------------------------------+----> Box Fired Heater
                                                           |
                                                           v
                                                       Flue Gas
                                                        /     \
                                                       /       \
                                                    Stack   Future CCUS
                                                               |
                                                               v
                                                          CO2 Product
```

The **base configuration is moderate oxygen enrichment**, not full oxy-fuel operation. The heater must remain capable of conventional air firing if the oxygen system is unavailable or enrichment is not required.

## 3D scope

The model will progressively include:

- Green-power / electrolyzer context
- Electrolyzer H2 and O2 product paths
- Oxygen drying, buffer capacity, pressure matching, metering and isolation
- Oxygen-compatible piping and backflow protection
- Combustion-air intake, FD fan and ducting
- O2 injection and air/O2 mixing section
- Detailed refinery box heater
- Burner, fuel-gas and combustion-air systems
- Radiant and convection sections
- Stack / breeching / analyzers
- BMS / SIS / control visualization
- Optional post-combustion CO2 capture module
- Optional future oxy-fuel + flue-gas-recirculation configuration
- Operating-mode animations and scientific overlays

## Operating states planned

1. Conventional air firing — approximately 21% O2 oxidant
2. Moderate enrichment — approximately 27% O2
3. Higher moderate enrichment — approximately 30% O2
4. Upper screening enrichment — approximately 35% O2
5. O2 trip / automatic isolation
6. Return to conventional air firing
7. Future advanced oxy-fuel + FGR visualization

## Repository structure

```text
docs/        Engineering design basis, process description and modelling rules
blender/     Blender source guidance, scripts and future .blend model structure
assets/      Textures, decals and reference-image guidance
exports/     Future GLB / FBX / renders / video outputs
web/         Future interactive 3D viewer / digital-twin front end
```

## Milestones

- **M0 — Engineering Architecture Freeze**
- **M1 — 3D Blockout**
- **M2 — Detailed Box Heater**
- **M3 — O2 Integration**
- **M4 — Instrumentation & Controls**
- **M5 — Animation & Scientific Visualization**
- **M6 — Interactive Web Digital Twin**

## Engineering disclaimer

This repository currently represents a **conceptual engineering visualization and development model**. It is not an IFC design, approved process design, burner modification package, oxygen-service specification, HAZOP close-out package, operating procedure or construction document. Site-specific heat balance, burner review, CFD/mixing study, oxygen-service materials review, safeguards verification and formal process-safety studies are required before any physical implementation.

## Project direction

The fired heater is the visual and engineering hero of the project. The electrolyzer supplies the opportunity; the 3D model is primarily intended to explain **how an existing refinery box heater can be integrated safely and progressively with electrolyzer by-product oxygen** while preserving conventional air-firing availability.
