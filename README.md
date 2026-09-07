# Harz, Germany SAR Disturbance Monitor

## Introduction

Between 2018 and 2021, the Harz region of Germany experienced droughts and a bark beetle outbreak, resulting in a large amount of spruce trees killed across the region. 
When mapping a problem like this, often optical satellite imagery is used; though, in Germany, since dense clouds can cover a region for weeks or even months, 
clear data is often not available for these time periods.

However, there is a solution. We can use synthetic aperture radar (SAR), which does not have the aforementioned restraint. SAR works independent of cloud coverage and daylight. 
Instead of color, SAR measures how much a transmitted signal is scattered back from the surface. SAR responds to structure and moisture; thus, when a canopy is removed, the signal will change.

This project seeks to build a pipeline that tracks the Sentinel-1 backscatter through time across a chosen region of Harz. 
Then, it will flag any sustained departures from each pixel's stable baseline, and emit the disturbance alerts with dates. 
We will then compare these against the German Aerospace Center's (Deutsches Zentrum für Luft- und Raumfahrt) Forest Canopy Cover Loss product
(an independent optically derived record of the monthly canopy loss). The comparison will measure the following: 
1. how closely the two agree 2. how many days earlier the radar detects the same event.

## Reference data

Forest Canopy Cover Loss (FCCL), Germany — monthly, 10 m, Sept 2017 – Oct 2025.
DLR/EOC. CC BY 4.0. DOI: 10.15489/ef9wwc5sff75
File: FCCL_DE_P1M.tif (downloaded 2026-09-07)

Derived from Sentinel-2A/B and Landsat-8/9, clipped to the Thünen-Institute
stocked area 2018 (Langner et al. 2022).

Thonfeld, F., Kacic, P., Holzwarth, S., Wegler, M., Asam, S., Kuenzer, C. (2026).
Forest canopy cover loss dynamics in Germany between 2017 and 2024 — Revealing
regional differences. Int. J. Applied Earth Observation and Geoinformation 146, 105157.

## Study area

Harz core, Germany. Bounding box (EPSG:4326): 10.3635, 51.6196, 10.7794, 51.8868
(~30 × 29 km, 870 km²). 83% forest by area within the Thünen stocked-area mask;
35,150 ha recorded as disturbed against 37,118 ha intact. Study period 2019–2022,
holding 82% of the AOI's total recorded disturbance.

## Results

_

## Scope and limitations

The way radar responds to structural change will help detect clearcuts, salvage logging (removing trees from damaged forest), 
and windthrow (uprooting of trees by strong wind) much better than it would detect deadwood or early-stage beetle infestations. 
In this scenario, the canopy is still dying but physically present. Moreover, backscatter will also vary with soil moisture, 
cycles of freezing and thawing, as well as varying seasonal changes. These will be the main source of a false alarm and will be characterized in the validation report. 

### Reference product confirmation lag

The FCCL product labels a pixel only after a threshold is exceeded in six
consecutive observations, so its recorded date reflects **confirmation** rather
than the moment of loss. Any lead time reported here must therefore be
decomposed into two components:

1. delay from cloud-driven observation gaps
2. delay from the confirmation requirement

The SAR detector applies a comparable persistence requirement so the comparison
is like-for-like.

Lastly, this method is going to follow established work on SAR-based disturbance detection:
RADD alerts (Reiche et al.), Rüetschi et al. on windthrow in Switzerland, and König et al. on bark beetle in Central Europe.
This project aspires to be a reproducible and possibly cloud-native implementation over a temperate AOI
(hopefully with explicit latency benchmarking: how many days earlier radar pipeline detects forest disturbance vs optical reference across every event).
