# 06 — Animation & Operating States

## 1. Purpose

Define the visual operating states that the Blender model and future web viewer should support.

The intention is to make the engineering mechanism understandable by changing the same physical system between controlled modes rather than showing disconnected diagrams.

## 2. State A — Conventional air firing

**Nominal oxidant:** ~21% O2

Visual state:

- O2 enrichment valve closed
- O2 flow indication = zero
- FD fan operating
- normal combustion-air flow visible
- burners firing on fuel gas + atmospheric air
- baseline flue-gas flow shown
- N2 fraction visually dominant in dry flue gas
- baseline CO2 concentration label

This is the reference and fallback state.

## 3. State B — Initial moderate enrichment

**Nominal oxidant:** ~27% O2

Visual state:

- O2 system permissives healthy
- O2 ESD path open
- O2 control valve partially open
- oxygen enters mixing section
- mixed-oxidant indicator rises toward 27%
- burner flame / furnace visualization changes subtly
- dry flue-gas visual flow reduces relative to baseline
- CO2 concentration indicator increases

Screening trend to label when required: approximately 25% lower dry flue gas versus conventional air firing under the presentation basis.

## 4. State C — Intermediate enrichment

**Nominal oxidant:** ~30% O2

Visual state:

- higher O2 flow
- continued reduction in air / nitrogen contribution
- smaller dry flue-gas flow visualization
- increased dry CO2 concentration indication
- temperature / heat-flux monitoring overlays become more prominent

Screening trend to label when required: approximately 33% lower dry flue gas versus conventional air firing under the presentation basis.

## 5. State D — Upper moderate screening enrichment

**Nominal oxidant:** ~35% O2

Visual state:

- O2 flow increased to upper base-study level
- dry flue-gas visual flow substantially reduced
- N2 dilution visibly reduced
- dry CO2 indicator approaches the screening value of ~19%
- burner / tube-skin / bridgewall / refractory monitoring indicators clearly visible

Screening trend to label when required: approximately 44% lower dry flue gas versus conventional air firing under the presentation basis.

This state must not visually imply that 35% is universally safe or automatically achievable on every heater.

## 6. State E — O2-system fault

Possible trigger categories for educational animation:

- O2 supply pressure low
- analyzer unhealthy
- enrichment permissive lost
- O2 ESD activated

Sequence:

1. Alarm indicator appears.
2. O2 control demand ramps down / trips as appropriate.
3. O2 isolation valve closes.
4. O2 flow arrows disappear.
5. Air system returns to conventional condition.
6. Operating-mode indicator changes to `AIR FIRING`.

## 7. State F — Conventional-air fallback

The heater remains represented as operating only if the base fired-heater permissives are healthy.

Visual emphasis:

- O2 line isolated
- normal air path active
- fuel + air remain coordinated
- stack returns to baseline flue-gas representation

This state is important to communicate that oxygen enrichment is an optional operating mode rather than a dependency for heater availability.

## 8. State G — Future post-combustion capture

This should be a visibility / routing layer rather than a permanent base state.

Sequence:

- future CCUS module becomes visible
- flue-gas diverter route highlights
- booster fan activates
- gas path enters absorber
- CO2 product stream becomes visible
- treated-gas path is shown

The animation should label the module as `FUTURE / OPTIONAL CCUS INTEGRATION`.

## 9. State H — Future oxy-fuel + FGR

This is a distinct advanced configuration.

Visual sequence:

- FGR loop becomes visible
- recycle fan / damper activates
- flue gas returns toward oxidant-mixing section
- high-purity O2 route becomes active
- conventional-air contribution is reduced / removed according to the future concept animation

The scene must clearly label this as different from base moderate enrichment.

## 10. Cutaway states

### Heater cutaway

Progressively hide:

1. external casing
2. refractory section
3. selected structural elements

Then reveal:

- burners
- flames
- radiant tubes
- convection banks
- internal flue-gas path

### O2 mixing cutaway

Reveal:

- main air duct
- O2 injection ports
- static-mixing geometry
- mixing progression
- downstream analyzer point

## 11. Scientific overlays

Optional layers:

- `FLOW` — direction and relative flow indication
- `COMPOSITION` — relative N2 / O2 / CO2 visualization
- `TEMPERATURE` — qualitative temperature field
- `HEAT_FLUX` — qualitative radiant heat-transfer view
- `CONTROLS` — live instrument tags / valves / permissives
- `SAFETY` — trip path and isolation logic

## 12. Animation design rule

Numbers must be visually identified as either:

- measured / actual site data,
- calculated screening values, or
- purely illustrative animation values.

The initial project contains screening values only; it shall not present them as measured site performance.
