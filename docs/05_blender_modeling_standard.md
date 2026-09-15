# 05 — Blender Modeling Standard

## 1. Objective

Create a detailed industrial model that remains understandable, maintainable, animation-ready and exportable to a future web viewer.

The project should avoid uncontrolled mesh growth, inconsistent naming and visually impressive but technically confusing geometry.

## 2. Units and coordinate system

- Blender scene units: **Metric**
- Primary working unit: **metres**
- Apply object scale before final export where practical.
- Establish one permanent plant origin during blockout and do not move it casually after piping / camera animation begins.
- Recommended convention:
  - X = plant east/west
  - Y = plant north/south
  - Z = elevation

## 3. Collection hierarchy

Top-level collections shall follow the engineering breakdown:

```text
00_SITE
01_GREEN_POWER
02_ELECTROLYZER
03_O2_CONDITIONING
04_COMBUSTION_AIR
05_BOX_HEATER
06_INSTRUMENTATION_CONTROL
07_FLUE_GAS
08_FUTURE_CCUS
09_FUTURE_OXYFUEL_FGR
10_ANIMATION
11_VISUALIZATION
```

The box heater collection shall contain subcollections for structure, radiant section, burners, fuel gas, convection and stack.

## 4. Naming convention

Use descriptive names instead of Blender defaults.

Good:

- `H05_RadiantTube_L01`
- `O2_CV_001`
- `AIR_Duct_Main_01`
- `BURNER_01_Quarl`
- `STACK_AIT_O2_001`

Avoid:

- `Cube.023`
- `Cylinder.115`
- `Plane.009`

Objects that belong to a repeated family should use numeric suffixes with leading zeroes.

## 5. Geometry strategy

### Hero geometry

High detail is justified for:

- fired heater
- burners
- oxygen-conditioning skid
- O2 injection / mixing section
- key valves / analyzers

### Context geometry

Use lower detail for:

- PV arrays
- wind turbine
- remote pipe racks
- remote CCUS context
- background refinery structures

## 6. Modifiers

Prefer non-destructive modelling where reasonable:

- Mirror
- Array
- Bevel
- Solidify
- Curve
- Geometry Nodes

Keep modifier stacks readable and document any unusual dependency.

## 7. Repeated equipment

Use linked duplicates / instancing for repeated items where feasible:

- burners
- handrail posts
- ladder rungs
- tube rows
- bolts
- repeated valves
- instrumentation fittings

This is important for later GLB / web optimization.

## 8. Piping

Piping should generally use curve-based or procedural workflows during development.

Each major service should be separable by collection / object naming:

- `H2_`
- `O2_`
- `FG_` for fuel gas
- `AIR_`
- `FLUE_`
- `PROC_` for heater process fluid
- `FGR_`
- `CO2_`

Do not rely only on material colour to identify service.

## 9. Ducting

Combustion-air and flue-gas ducts should use physically plausible rectangular / circular sections with:

- transitions
- expansion joints where useful
- support points
- dampers
- access sections

The O2-air mixing duct is a hero object and shall support cutaway visualization.

## 10. Fired-heater cutaway design

The heater shall be built so that external shell / refractory / internal process coils can be shown separately.

Recommended visibility groups:

- outer casing
- structural frame
- refractory
- radiant tubes
- burners
- convection coils
- flue-gas volume

This enables exploded views and sectional animation without destructive mesh editing.

## 11. Burner model strategy

Burners should have separate objects for:

- outer register
- quarl / tile
- fuel tip representation
- pilot
- igniter
- flame scanner
- flame volume

The flame itself shall remain an animation / VFX object rather than being fused permanently into the burner mesh.

## 12. Materials

Materials should communicate industrial reality rather than create a stylized game environment.

Typical material families:

- painted structural steel
- weathered carbon steel
- stainless steel
- refractory / ceramic
- hot oxidized metal
- galvanized grating
- insulated / clad piping
- glass / instrument lens
- concrete

Service identity may be supported by restrained engineering accent colours and labels, but process correctness shall not depend on colour alone.

## 13. Level of detail

Plan at least three future export levels:

- **LOD0** — cinematic / engineering close-up
- **LOD1** — interactive desktop model
- **LOD2** — lightweight web overview

LOD generation does not need to be completed during M0/M1, but object organization must not prevent it.

## 14. Animation readiness

Objects that will animate must not be merged unnecessarily.

Keep separate:

- control valves
- ESD valves
- dampers
- fan rotor
- flame volumes
- flow arrows
- cutaway shells
- future FGR loop visibility
- CCUS route visibility

## 15. Scientific visualization helpers

Use dedicated helper objects for:

- flow arrows
- molecule / composition particles
- temperature gradients
- heat-flux indicators
- analyzer labels
- callouts

These helpers shall not contaminate engineering geometry.

## 16. Cameras

Minimum planned camera groups:

1. Plant overview
2. Electrolyzer-to-O2 skid path
3. O2 conditioning close-up
4. O2 injection / mixing cutaway
5. Burner-front close-up
6. Heater external hero shot
7. Heater internal cutaway
8. Flue-gas composition visualization
9. Future CCUS path
10. Future FGR loop

## 17. Export readiness

For future GLB / web export:

- avoid unnecessary high-poly hidden geometry
- minimize unique materials
- instance repeated objects
- keep object pivots meaningful
- use web-safe texture sizes where possible
- bake procedural materials when required
- test normals and transforms before export

## 18. File strategy

Recommended development files:

```text
blender/main/OxyHeat_Master.blend
blender/equipment/Heater.blend
blender/equipment/O2_Skid.blend
blender/equipment/Electrolyzer.blend
blender/equipment/CCUS.blend
```

Large binary files should use Git LFS once the first `.blend` assets are added.

## 19. Quality rule

No object should be added only because it "looks refinery-like" if its function cannot be explained. Every prominent object should either:

1. perform a defined process / control / safety function, or
2. provide required access / support / visual context.
