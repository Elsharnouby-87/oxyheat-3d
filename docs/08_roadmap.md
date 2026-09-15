# 08 — Development Roadmap

## M0 — Engineering Architecture Freeze

**Goal:** agree exactly what is being modelled before detailed 3D work.

Deliverables:

- design basis
- process description
- master equipment list
- preliminary plot / scene layout
- control and safety philosophy
- Blender naming / modelling standard
- animation-state definition
- clear separation between base enrichment and future CCUS / oxy-fuel-FGR modules

**Exit criteria:** no major unresolved disagreement on system architecture or heater type.

---

## M1 — 3D Blockout

**Goal:** establish scale, proportions, plot arrangement and camera readability.

Deliverables:

- box-heater massing
- radiant / convection / stack proportions
- electrolyzer package massing
- O2 skid massing
- FD fan and main duct
- O2 mixing section
- major piping corridors
- future CCUS massing
- first overview cameras

**Exit criteria:** process direction and equipment identity are clear using simple geometry only.

---

## M2 — Detailed Box Heater

**Goal:** complete the hero equipment to engineering-visualization quality.

Deliverables:

- structural frame
- casing / refractory layers
- radiant coils
- burner arrangement
- burner details
- convection coils
- shield tubes
- breeching / stack
- platforms / ladders / handrails
- process inlet / outlet representation
- heater cutaway system

**Exit criteria:** heater can support external hero views and internal technical cutaways.

---

## M3 — Oxygen Integration

**Goal:** model the retrofit that differentiates OxyHeat 3D.

Deliverables:

- O2 conditioning skid
- buffer vessel
- pressure-control section
- O2 flow metering
- control / ESD / non-return valves
- O2 distribution header
- O2 injection manifold
- air/O2 mixing section
- mixed-oxidant analyzer
- enriched-air connection to burners

**Exit criteria:** viewer can trace oxygen from electrolyzer outlet to burner oxidant supply without ambiguity.

---

## M4 — Instrumentation & Controls

**Goal:** make operation and safeguards understandable.

Deliverables:

- key transmitter / analyzer geometry
- fuel / air / O2 measurement points
- BMS / SIS panels
- HMI concept
- animated valves / dampers
- permissive visualization
- O2 trip and air-fallback sequence

**Exit criteria:** core control narrative can be demonstrated without verbal explanation.

---

## M5 — Animation & Scientific Visualization

**Goal:** convert the static model into an explanatory engineering demonstrator.

Deliverables:

- 21% / 27% / 30% / 35% operating states
- flow arrows
- composition visualization
- flue-gas volume comparison
- CO2 concentration labels
- heater cutaway animation
- O2 mixer cutaway animation
- temperature / heat-flux overlays
- cinematic camera paths

**Exit criteria:** the enrichment mechanism and fallback philosophy can be understood visually.

---

## M6 — Interactive Web Digital Twin

**Goal:** publish an interactive version of the model.

Potential capabilities:

- GLB / glTF model streaming
- orbit / guided camera modes
- equipment selection
- layer toggles
- cutaway controls
- operating-mode selector
- live labels / tooltips
- process-flow overlays
- future CCUS / FGR toggle
- educational engineering annotations

Performance optimization will require LODs, instancing, material consolidation and texture optimization.

---

## Immediate next action

Begin **M1 blockout only after M0 review**. The first Blender work should focus on the box-heater proportions and overall plot arrangement; detailed valves, handrails and small-bore piping should not be modelled before the blockout is accepted.
