# Harz, Germany SAR Disturbance Monitor

## Introduction

Between 2018 and 2021, the Harz region of Germany experienced droughts and a bark beetle outbreak, resulting in a large amount of spruce trees killed across the region. When mapping a problem like this, often optical satellite imagery is used; though, in Germany, since dense clouds can cover a region for weeks or even months, clear data is often not available for these time periods.

However, there is a solution. We can use synthetic aperture radar (SAR), which does not have the aforementioned restraint. SAR works independent of cloud coverage and daylight. Instead of color, SAR measures how much a transmitted signal is scattered back from the surface. SAR responds to structure and moisture; thus, when a canopy is removed, the signal will change.

This project seeks to build a pipeline that tracks the Sentinel-1 backscatter through time across a chosen region of Harz. Then, it will flag any sustained departures from each pixel's stable baseline, and emit the disturbance alerts with dates. We will then compare these against the German Aerospace Center's (Deutsches Zentrum für Luft- und Raumfahrt) Forest Canopy Cover Loss product (an independent optically derived record of the monthly canopy loss). The comparison will measure the following: 1. how closely the two agree 2. how many days earlier the radar detects the same event.


## Results

_

## Scope and limitations

The way radar responds to structural change will help detect clearcuts, salvage logging (removing trees from damaged forest), and windthrow (uprooting of trees by strong wind) much better than it would detect deadwood or early-stage beetle infestations. In this scenario, the canopy is still dying but physically present. Moreover, backscatter will also vary with soil moisture, cycles of freezing and thAawing, as well as varying seasonal changes. These will be the main source of a false alarm and will be characterized in the validation report. 

Lastly, this method is going to follow established work on SAR-based disturbance detection (RADD alerts Rüetschi et al. on windthrow and König et al. on the Central European bark beetle). This project aspires to be a reproducible and possibly cloud-native implementation over a temperate AOI (hopefully with explicit latency benchmarking: how many days earlier radar pipeline detects forest disturbance vs optical reference across every event).
