# 02 — Process Description

## 1. Overall concept

OxyHeat 3D represents the integration of electrolyzer by-product oxygen with an existing refinery box fired heater. The oxygen is treated as an additional controlled combustion utility, not as a replacement for normal combustion air at the base stage.

## 2. Green-hydrogen / oxygen source

Water electrolysis produces hydrogen and oxygen simultaneously. Hydrogen is routed to its intended user or export destination. Oxygen is routed toward the heater-integration system.

The electrolyzer is shown in the 3D model primarily to establish the source and value chain. Detailed electrolyzer internals are outside the initial modelling scope.

## 3. Oxygen conditioning

The oxygen stream passes through a dedicated conditioning and control package before any connection to the heater combustion system.

The model will represent the following functional sequence:

```text
Electrolyzer O2
    |
    v
Separation / moisture control
    |
    v
Drying
    |
    v
Buffer capacity
    |
    v
Pressure regulation
    |
    v
Flow measurement
    |
    v
Control + ESD isolation
    |
    v
Backflow prevention
    |
    v
O2 distribution header
```

The exact process-equipment arrangement may be refined later when a specific electrolyzer package and oxygen delivery conditions are selected.

## 4. Combustion-air path

The base model uses a forced-draft representation:

```text
Atmosphere
   |
Air intake / filter
   |
FD fan
   |
Main air duct
   |
O2 injection manifold
   |
Mixing section / static mixer
   |
Mixed-oxidant analyzer
   |
Enriched-air distribution
   |
Burners
```

Oxygen addition is controlled so that oxidant concentration can be increased progressively rather than changed in one step.

## 5. Fuel-gas path

Fuel gas remains an independent system:

```text
Fuel-gas source
   |
Pressure control / metering
   |
Fuel ESD isolation
   |
Main burner manifold
   |
Individual burner branches
   |
Burners
```

Pilot gas may be shown as a separate small-bore manifold where required for visual clarity.

The model shall never visually imply that oxygen and fuel are premixed upstream in the same process line.

## 6. Box fired heater

The heater consists of:

- burner zone
- radiant chamber
- refractory-lined enclosure
- radiant process coils
- transition / shield area
- convection section
- breeching
- stack

The process fluid enters the heater coil system, receives heat, and leaves at elevated temperature. Detailed process-fluid composition is intentionally generic at the current stage.

## 7. Combustion and enrichment states

### Conventional air firing

The heater operates using atmospheric air as oxidant. This is the base operating condition and fallback state.

### Moderate enrichment

Conditioned O2 is introduced into the combustion-air stream. The mixed oxidant is distributed to the burners. The nominal visualization stages are approximately 27%, 30% and 35% O2 in the oxidant.

The expected first-order effect is less nitrogen entering with the required combustion oxygen. This reduces inert-gas throughput and increases CO2 concentration in the dry flue gas.

### O2-system fault / unavailable state

Oxygen isolation valves close and enrichment demand is removed. Provided all conventional heater permissives remain satisfied, the visualized operating philosophy returns the heater to normal air firing rather than making heater availability dependent on the electrolyzer.

## 8. Flue-gas path

Combustion products flow from the radiant section through the convection section and onward to breeching / stack.

The visualization should make the following trends understandable:

- lower N2 throughput with enrichment
- lower dry flue-gas volume
- higher dry CO2 concentration
- changing furnace / stack heat-loss behaviour

The visualization shall not present a fixed fuel-saving percentage as a proven outcome.

## 9. Future post-combustion capture path

A future take-off from the flue-gas system can route gas toward a post-combustion CO2-capture island.

Conceptual sequence:

```text
Flue gas
   |
Diverter / tie-in
   |
Booster fan
   |
Cooling / conditioning
   |
Absorber
   |
Solvent regeneration
   |
CO2 separation
   |
Compression / export
```

The normal stack path remains visible to preserve the distinction between the base heater retrofit and optional downstream capture.

## 10. Future oxy-fuel / FGR layer

At a later stage the project may show a different advanced configuration in which high-purity oxygen is combined with recycled flue gas to control combustion temperature and heat-transfer behaviour.

That mode is intentionally separated from the base oxygen-enrichment design and shall use clearly different visual states, piping and labels.
