# 07 — Preliminary Plot / Scene Layout

## 1. Layout objective

Arrange the system so the **box fired heater remains the visual hero**, while the process path can be understood immediately from a plant-overview camera.

The layout is conceptual and intended for 3D storytelling, not plot-plan approval.

## 2. Preferred top-view composition

```text
                         NORTH / BACKGROUND

        GREEN-POWER CONTEXT
      PV / WIND / TRANSFORMER
                 |
                 v
      +---------------------+
      |    ELECTROLYZER     |
      +---------------------+
          | H2        | O2
          |           |
          v           v
      H2 PRODUCT   +-----------------------+
                   | O2 CONDITIONING SKID  |
                   | dryer / buffer / PCV  |
                   | metering / ESD / NRV  |
                   +-----------+-----------+
                               |
                               | O2
                               v

 AIR INTAKE --> FD FAN --> MAIN AIR DUCT --> O2 MIXING SECTION
                                               |
                                               v
                                      ENRICHED AIR DUCT
                                               |
                                               v
                                +----------------------------+
 FUEL-GAS HEADER -------------> |       BOX FIRED HEATER     |
                                |                            |
                                |  burner front / radiant    |
                                |  convection / stack        |
                                +-------------+--------------+
                                              |
                                           FLUE GAS
                                              |
                            +-----------------+------------------+
                            |                                    |
                            v                                    v
                          STACK                       FUTURE CCUS ISLAND
                                                               |
                                                               v
                                                          CO2 EXPORT

             FUTURE FGR LOOP: behind / side of heater
```

## 3. Visual hierarchy

### Primary hero

**Box fired heater**

It should dominate the central / right-central scene and provide the strongest silhouette.

### Secondary technical hero

**O2 conditioning + air/O2 mixing section**

These should be close enough to the camera path that the viewer can inspect the retrofit logic without travelling across an unrealistic plant distance.

### Context equipment

- electrolyzer
- renewable-power representation
- future CCUS
- remote refinery environment

## 4. Suggested relative zoning

### Zone A — Electrolyzer source area

Place toward the left / rear of the scene.

Purpose:

- establishes origin of H2 and O2
- provides green-hydrogen context
- keeps source equipment visually separate from heater combustion area

### Zone B — O2 conditioning area

Place between electrolyzer and heater, preferably offset from the main air duct so the piping route is readable.

The skid should be visually inspectable from at least two camera angles.

### Zone C — Combustion-air corridor

Run the FD fan and main duct in a clear path toward the heater burner side.

The O2 injection / mixing section should be positioned where it can be exposed with a cutaway without being hidden by other equipment.

### Zone D — Heater island

Central engineering focus.

Provide clear access around:

- burner front
- fuel-gas manifold
- combustion-air connections
- platforms
- heater side elevation
- stack

### Zone E — Future CCUS

Place beyond the heater / stack side so the viewer reads it as downstream.

It should be visibly separable or switchable off.

### Zone F — Future FGR corridor

Reserve space behind or to one side of the heater for:

- FGR take-off
- recycle duct
- FGR fan
- return-to-mixing section

Keep this loop hidden in base mode.

## 5. Initial scale philosophy

Exact dimensions are not frozen at M0.

Blockout should use credible industrial proportions and sufficient spacing to:

- avoid visual collisions
- support maintenance-access storytelling
- show piping / duct routing
- permit camera movement
- preserve clear process direction

Final dimensions should be refined from reference equipment / drawings rather than guessed in detail.

## 6. Camera corridors

Reserve unobstructed camera routes for:

1. left-to-right full process overview
2. electrolyzer -> O2 skid tracking shot
3. O2 skid orbit
4. air duct -> mixing-section tracking shot
5. burner-front approach
6. heater hero orbit
7. heater cutaway push-in
8. flue-gas path rise toward convection / stack
9. future CCUS reveal
10. future FGR reveal

## 7. Readability rule

From the principal overview camera, a technically informed viewer should be able to identify the process direction without labels becoming essential:

**source -> condition -> mix -> burn -> exhaust -> optional capture**.

## 8. What not to do

Avoid:

- placing every unit in one straight unrealistic line solely for presentation
- surrounding the heater with random refinery equipment
- hiding the O2 injection point behind the heater
- mixing future FGR piping into the base mode visually
- making the CCUS island larger / more detailed than the heater at early stages
- adding pipework before the major flow corridors and equipment elevations are frozen
