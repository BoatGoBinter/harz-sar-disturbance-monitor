# Harz, Germany SAR Disturbance Monitor

## Introduction

From 2018 to 2021, Germany's Harz region was hit with droughts followed by a bark beetle outbreak which killed large amounts of spruce across the region. Usually mapping the where and when of a problem like this is done using optical satellite imagery; however, optical sensors cannot see through clouds. Therefore, in times like a wet autumn season, there is likely no clear data for weeks or even months.

In whim of this, we can use synthetic aperture radar as this has no constraint. The way it works is independent of cloud cover and daylight. Instead of color, it measures how much a transmitted signal is scattered back from the surface. This does in fact respond to structure and moisture. Thus, when a canopy is removed, the signal will change. 

This project is going to build a pipeline that tracks the Sentinel-1 backscatter through time across a study area of Harz. It will then flag sustained departures from each pixel's stable baseline, and emit disturbance alerts with dates. Those alerts will then be compared against the German Aerospace Center's (Deutsches Zentrum für Luft- und Raumfahrt) Forest Canopy Cover Loss product (an independent optically derived record of the monthly canopy loss). The comparison will measure the following: 1. how closely the two agree 2. how many days earlier the radar detects the same event.

## Results

_

## Scope and limitations

The way radar responds to structural change will help detect clearcuts, salvage logging (removing trees from damaged forest), and windthrow (uprooting of trees by strong wind) much better than it would detect deadwood or early-stage beetle infestations. In this scenario, the canopy is still dying but physically present. Moreover, backscatter will also vary with soil moisture, cycles of freezing and thAawing, as well as varying seasonal changes. These will be the main source of a false alarm and will be characterized in the validation report. 

Lastly, this method is going to follow established work on SAR-based disturbance detection (RADD alerts Rüetschi et al. on windthrow and König et al. on the Central European bark beetle). This project aspires to be a reproducible and possibly cloud-native implementation over a temperate AOI (hopefully with explicit latency benchmarking: how many days earlier radar pipeline detects forest disturbance vs optical reference across every event).
