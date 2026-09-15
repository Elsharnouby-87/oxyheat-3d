# 04 — Control & Safety Philosophy

## 1. Purpose

Define the control and safeguard concepts that the 3D model should be able to explain visually.

This document is a conceptual visualization basis only. It is not an approved cause-and-effect matrix, BMS logic diagram, SIS design or operating procedure.

## 2. Normal operating philosophy

The heater retains normal combustion-air capability. Oxygen enrichment is treated as an additional controlled operating mode.

The control architecture should visually communicate three coordinated manipulated flows:

- fuel gas
- combustion air
- supplemental oxygen

The base visualization concept is a **fuel-air-oxygen cross-limited control philosophy** with enrichment introduced only when required permissives are healthy.

## 3. Key measured variables

The 3D scene should include visible measurement points for:

- fuel-gas flow
- fuel-gas pressure
- combustion-air flow
- oxygen flow
- oxygen pressure
- mixed-oxidant O2 concentration
- stack O2
- furnace pressure / draft
- bridgewall temperature
- tube-skin temperatures
- flame status
- CO
- NOx

Not every signal needs to be animated in V0.1, but geometry / tag points should allow later activation.

## 4. Enrichment ramping

Oxygen enrichment shall be represented as a controlled ramp rather than an instantaneous switch.

Suggested visualization sequence:

1. Heater stable in conventional air firing.
2. O2 system permissives become healthy.
3. O2 isolation valve opens.
4. O2 flow controller ramps from zero.
5. Mixed-oxidant O2 rises gradually.
6. Air / fuel / O2 control settles at target enrichment level.
7. Heater monitoring variables remain visible.

The nominal educational targets are ~27%, ~30% and ~35% oxidant O2.

## 5. Example permissive categories

The 3D animation logic may use representative permissive groups such as:

- BMS healthy
- established flame
- combustion-air flow proven
- furnace draft within allowable range
- fuel-gas pressure healthy
- O2 supply pressure healthy
- O2 analyzer healthy
- O2-flow measurement healthy
- no active O2-system ESD
- key heater temperatures below defined operating limits

The final permissive list must not be interpreted as complete for a real installation.

## 6. Oxygen trip / fallback philosophy

A central project requirement is that failure of the enrichment system should not automatically make the heater dependent on O2 availability.

Conceptual visualization:

```text
O2 fault / loss of permissive
        |
        v
Close O2 control / isolation path
        |
        v
Remove enrichment demand
        |
        v
Restore conventional air-firing condition
        |
        v
Continue only if normal heater BMS permissives remain satisfied
```

If the underlying heater itself loses a critical combustion permissive, normal BMS trip logic takes precedence.

## 7. Backflow prevention

The oxygen system shall visibly include non-return / isolation architecture so that the viewer understands that reverse migration from the combustion-air system toward the O2 source is not acceptable.

The final mechanical arrangement will require specialist oxygen-service engineering.

## 8. Burner / furnace monitoring

The animation should be able to highlight:

- flame shape
- flame stability
- flame scanner status
- refractory exposure
- bridgewall temperature
- radiant tube-skin temperature
- furnace draft

These variables are particularly important during transitions between enrichment levels.

## 9. BMS and SIS representation

The 3D environment should distinguish:

### BMS

Used to represent combustion permissives, burner light-off status, flame supervision and authority over fuel / oxygen admission.

### SIS / ESD

Used to represent independent emergency isolation / protective functions where applicable.

The visual hierarchy should make clear that supplemental O2 never bypasses burner-management authority.

## 10. Human-machine interface

A future interactive HMI panel may show:

- selected operating mode
- current mixed-oxidant O2
- fuel flow
- air flow
- O2 flow
- stack O2
- furnace draft
- bridgewall temperature
- tube-skin temperature
- CO / NOx indicators
- active permissives
- active alarms
- O2 ESD status

## 11. Safety visualization principles

The model should teach the following ideas without pretending to be a complete safety study:

- oxygen service requires dedicated materials / cleanliness / components
- uncontrolled O2 addition is not acceptable
- enrichment must be progressive and monitored
- combustion stability and furnace heat flux must be verified
- oxygen admission must be isolatable
- oxygen system failure should return to normal air firing when otherwise safe
- the BMS retains authority over combustion

## 12. Not yet defined

The following are deliberately left open pending detailed engineering:

- SIL targets
- trip set points
- exact valve fail positions
- exact voting logic
- exact response times
- alarm priorities
- final analyzer redundancy
- final oxygen-cleaning specification
- final relief / vent design
- final startup and shutdown sequence
