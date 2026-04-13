# Literature Review: Tree-Crop Agroforestry Ecohydrology — Competition, Facilitation, Stochastic Rainfall, and Semi-Arid Africa

**Date:** 2026-04-06
**Query:** Tree-crop agroforestry ecohydrology: stochastic soil moisture modeling, hydraulic redistribution, shade facilitation, rainfall regime effects on competition vs facilitation, semi-arid East Africa maize. Focus on: WaNuLCAS, Hi-sAFe, SWAP/APSIM/HYDRUS agroforestry models; Caldwell/Burgess hydraulic redistribution; Rodriguez-Iturbe & Porporato stochastic framework extensions to agroforestry; yield distributions and drought risk in agroforestry; Faidherbia albida; rainfall intensity vs frequency effects; Garrity/Bayala/Kuyah/Sileshi empirical yields in semi-arid Africa; climate change rainfall intensification and agroforestry. Target journals: WRR, GCB, AgForMet, Nature Sustainability.

---

## Summary

The agroforestry modeling literature is bifurcated into two traditions that have never been integrated. The first tradition—process-based deterministic models (WaNuLCAS, Hi-sAFe, HYDRUS-2D)—captures spatial complexity and multiple resource fluxes, but uses single-trajectory weather inputs and produces point estimates of yield rather than distributions. The second tradition—stochastic ecohydrological models in the Rodriguez-Iturbe/Porporato framework—produces analytical and Monte Carlo yield distributions from probabilistic rainfall forcing, but has never been applied to agroforestry. This gap is the central opportunity.

The empirical literature on mechanisms (hydraulic redistribution, shade-mediated ET reduction, root competition) is extensive but largely qualitative. Field studies confirm that HR transfers 0.04–1.3 mm H₂O/day in natural systems and dramatically boosts millet yields under imposed drought (>900% in extreme cases), but the conditions under which these magnitudes translate into meaningful agronomic benefit—specifically, as a function of storm frequency vs. intensity regime—have never been quantified. The stress-gradient hypothesis (that facilitation intensifies with aridity) has been tested in natural vegetation but not in managed agroforestry systems using mechanistic ecohydrological models.

The critical modeling gap is a two-layer, spatially explicit, stochastic agroforestry model that can produce full yield distributions (not just means) and decompose competition vs. facilitation pathways cleanly—exactly what the present work does. No competitor paper found in this review integrates all three of: (1) stochastic rainfall with rainfall regime (alpha-lambda space), (2) mechanistic competition-facilitation decomposition, and (3) probabilistic yield outcomes including P(crop failure).

---

## Key Papers

### 1. van Noordwijk & Lusiana (1999) — WaNuLCAS
- **Main contribution:** First dedicated agroforestry process model. Four horizontal zones × four soil layers; daily water, N, P and SOM balance; tree and crop roots compete explicitly.
- **Method:** Deterministic simulation with observed weather. Horizontal zonation is its key spatial feature.
- **Key finding:** Applied widely across humid/sub-humid tropical systems; used to evaluate management options (pruning, tree density, mulching).
- **Relevance:** Closest deterministic competitor. Does NOT use stochastic rainfall. Does NOT produce yield distributions. Has been applied to Burkina Faso parklands (Bayala et al. 2014).
- **Citation note:** van Noordwijk & Lusiana (1999), Agroforestry Systems 43:217–242; Bayala et al. (2014), Agroforestry Systems 89(2).

### 2. Talbot et al. (2019) — Hi-sAFe 3D Model
- **Main contribution:** Most spatially sophisticated agroforestry model. 3D voxel-scale root architecture reacting plastically to resource availability; no priority bias for trees vs crops in water/N competition; fluctuating water table support.
- **Method:** Couples STICS crop model to new tree model; 3D opportunistic root growth; deterministic weather inputs.
- **Key finding:** Novel tool for exploring tree spacing, pruning strategies, and long-term system evolution. No stochastic rainfall, no yield distributions, no analytical decomposition of competition vs. facilitation.
- **Relevance:** State-of-the-art deterministic model. Demonstrates exactly what is missing: probabilistic analysis of rainfall regime sensitivity.
- **Citation note:** Talbot et al. (2019), Sustainability 11(8):2293.

### 3. Laio, Porporato, Ridolfi & Rodriguez-Iturbe (2001) — Stochastic Soil Moisture PDFs
- **Main contribution:** Foundational analytical framework. Derives the steady-state probability density function (PDF) of soil moisture under marked Poisson rainfall (characterized by frequency λ and mean depth α). Provides analytical expressions for mean plant water stress and its probability.
- **Method:** Analytical. Single-layer bucket model; linear loss function above s*; rainfall as stochastic impulses.
- **Key finding:** Full PDF of soil moisture as a function of soil, vegetation, and rainfall parameters. Plant stress scales non-linearly with changes in λ vs α.
- **Relevance:** This is the theoretical engine of the present work. Has never been extended to two-layer (deep-shallow root) or multi-species (tree + crop) systems in agroforestry context.
- **Citation note:** Laio et al. (2001), Advances in Water Resources 24:707–723.

### 4. Rodriguez-Iturbe & Porporato (2004) — Ecohydrology of Water-Controlled Ecosystems (Book)
- **Main contribution:** Consolidates the stochastic framework; extends to multiple plant types, seasonality, nutrient cycling. Framework for probabilistic plant water stress, yield estimation, and ecosystem response.
- **Method:** Analytical + Monte Carlo.
- **Key finding:** Rainfall frequency (λ) and mean depth (α) have distinct and non-substitutable effects on soil moisture dynamics and plant stress—even at fixed annual total.
- **Relevance:** Core theoretical foundation of the present work; demonstrates the importance of the alpha-lambda decomposition that we use to define rainfall regimes.

### 5. Bayala, Kalinganire & Prieto (2020) — Water Acquisition and Redistribution in Agroforestry
- **Main contribution:** Comprehensive review of HR in agroforestry systems. Documents deep-rooted tree species passively redistributing water from moist deep soil to dry shallow rhizosphere via root pressure gradients; summarizes empirical evidence from West African parklands and other systems.
- **Method:** Literature review + synthesis. Field data from Vitellaria, Parkia, Faidherbia in Burkina Faso/Sahel.
- **Key finding:** HR is a documented mechanism in tropical agroforestry parklands; deep roots are necessary (Zr > 1000 mm typical); magnitude varies substantially with season, drought severity, and species.
- **Relevance:** Directly validates the HR mechanism in our model. Key gap flagged: quantitative contribution of HR to crop yield as a function of storm regime is unknown.
- **Citation note:** Bayala & Prieto (2020), Plant and Soil 453(1–2):17–28, DOI: 10.1007/s11104-019-04173-z.

### 6. Neumann & Cardon (2012) — Magnitude of Hydraulic Redistribution: Meta-Analysis
- **Main contribution:** First quantitative synthesis of HR magnitude across field and modeling studies. Field range: 0.04–1.3 mm H₂O/day. Modeling range: 0.1–3.23 mm H₂O/day. Notes systematic discrepancy: models overestimate field measurements.
- **Method:** Meta-analysis of empirical and modeling literature.
- **Key finding:** HR varies by nearly two orders of magnitude. Magnitude depends on transpiration demand, soil water gradient, root architecture.
- **Relevance:** Calibrates our hr_max=1.0 mm/day parameter—within the documented range. The model-field discrepancy they flag is relevant for our parameter choices.
- **Citation note:** Neumann & Cardon (2012), New Phytologist 194:337–352.

### 7. Prieto et al. (2022) — Global Synthesis of HR Magnitude and Determinants
- **Main contribution:** Updates Neumann & Cardon with more sites. Mean HR = 0.249 mm H₂O/day (95% CI: 0.113–0.384). Plant transpiration explains 43% of variation. HR = ~27% of transpiration on average.
- **Method:** Global synthesis, 47 sites.
- **Key finding:** Angiosperms > gymnosperms in HR capacity. Temperate forests show highest HR (0.502 mm/day). Limited data from African agroforestry systems specifically.
- **Relevance:** Confirms realistic parameter range; identifies the data gap in African agroforestry settings.
- **Citation note:** Frontiers in Plant Science (2022), DOI: 10.3389/fpls.2022.918585.

### 8. Bayala et al. (2008) — HR in West African Parkland Species (Field)
- **Main contribution:** First direct field measurement of HR in West African agroforestry parkland species (Vitellaria paradoxa, Lannea microcarpa). Demonstrates nocturnal water efflux from shallow roots during drought.
- **Method:** Sap flow measurement, isotope tracing.
- **Key finding:** HR confirmed in both species; magnitude small relative to transpiration, but sufficient to maintain rhizosphere moisture during interstorm drought periods.
- **Relevance:** Provides direct field evidence for HR in the geographic/ecological context of our model.
- **Citation note:** Bayala et al. (2008), Acta Oecologica 34:341–349.

### 9. Prieto et al. (2018) — Sahelian Shrubs: Bioirrigation to Resist In-Season Drought
- **Main contribution:** Deuterium tracer confirms water transfer from shrub (Guiera senegalensis) roots to intercropped millet within 12–96 hours during experimentally imposed drought. Millet biomass 900%+ higher with shrubs vs. without.
- **Method:** Isotope tracer (enriched 2H), field experiment in Sahel.
- **Key finding:** HR is the only viable pathway for water transfer; effect is most dramatic under drought stress.
- **Relevance:** Strongest empirical evidence that HR in the agroforestry context produces agronomic benefit—and that the benefit is drought-regime dependent, directly motivating our regime analysis.
- **Citation note:** Frontiers in Environmental Science (2018), DOI: 10.3389/fenvs.2018.00098.

### 10. Lin (2010) — Shade and ET Reduction in Coffee Agroforestry
- **Main contribution:** Quantifies demand-side facilitation via shade. 60–80% shade cover reduces soil evaporation by 41% and crop transpiration demand by 32% relative to low-shade systems.
- **Method:** Field measurement across shade gradient in Mexican coffee agroforestry (Chiapas).
- **Key finding:** ET reduction is driven by microclimate (reduced radiation, VPD) within the canopy; effect scales with shade cover fraction.
- **Relevance:** Provides empirical grounding for our Beer-Lambert shade model. Critical gap: no analogous study for cereal crops in semi-arid Africa, and no study disentangles demand-side shade facilitation from root competition in the same framework.
- **Citation note:** Lin (2010), Agricultural and Forest Meteorology 150:510–518.

### 11. Garrity et al. (2010) — Evergreen Agriculture
- **Main contribution:** Landmark synthesis of agroforestry outcomes across sub-Saharan Africa. Documents Faidherbia albida doubling or tripling maize yields in Malawi, Zambia, Niger. Defines "Evergreen Agriculture" concept. Key mechanisms: N fixation, nutrient cycling, microclimate.
- **Method:** Review and case study synthesis.
- **Key finding:** Maize yield doubled or tripled near F. albida in Malawi; unfertilized maize 4.1 t/ha near trees vs. 1.3 t/ha without in Zambia. Mechanisms are primarily nitrogen-based.
- **Relevance:** Sets the empirical benchmark. Note: F. albida is reverse-phenology (leafless during crop season), so competition for water is minimal and water-mediated facilitation (HR + reduced ET demand) is effectively absent during crop season. Our co-season tree is a fundamentally different and harder test case.
- **Citation note:** Garrity et al. (2010), Food Security 2:197–214.

### 12. Kuyah et al. (2019) — Agroforestry Win-Win Meta-Analysis
- **Main contribution:** Meta-analysis of 1,106 observations from 126 publications in sub-Saharan Africa. Agroforestry increases crop yield AND maintains soil N, SOC, available P, reduces runoff and soil loss. First meta-analysis showing simultaneous provisioning + regulating service gains.
- **Method:** Meta-analysis, sub-Saharan Africa.
- **Key finding:** Mean positive yield effect; mechanisms flagged include HR, soil fertility, and microclimate—but not separated quantitatively.
- **Relevance:** Establishes that yield effect is real on average; does not isolate water-mediated vs. nutrient-mediated mechanisms. Our model provides the water-mechanism decomposition that empirical meta-analyses cannot.
- **Citation note:** Kuyah et al. (2019), Agronomy for Sustainable Development 39(6):1–12.

### 13. Sileshi et al. (2008) — Maize Yield Response to Legume Trees: Meta-Analysis
- **Main contribution:** Synthesizes 94 publications on legume fallow/green manure effects on maize in sub-Saharan Africa. Positive yield response across herbaceous and woody legumes; N fixation is primary driver.
- **Method:** Meta-analysis.
- **Key finding:** Legume trees significantly improve maize yields; effect stronger on N-depleted soils. Water mechanisms not separated.
- **Relevance:** Shows the strength of N-based facilitation; contrast with our system where the tree is NOT an N-fixer, isolating the pure water and shade mechanisms.

### 14. Barrow-et al. (2023) — Global Maize Agroforestry Meta-Analysis
- **Main contribution:** Global meta-analysis of 1,215 data entries from 95 studies. Median maize yield increase: +0.24 Mg/ha (7%); tropics/subtropics: +0.30 Mg/ha (+16%). Sandy soils and N-poor soils show strongest gains.
- **Method:** Meta-analysis, global scope.
- **Key finding:** "Tree-crop-soil interactions are inherently location-specific and management-sensitive." Does NOT decompose competition vs. facilitation mechanistically.
- **Relevance:** Quantifies the average effect; confirms that water-limited, sandy-soil settings (like semi-arid East Africa) show stronger gains. Explicitly does NOT address storm regime sensitivity or yield distributions.
- **Citation note:** Frontiers in Sustainable Food Systems (2023), DOI: 10.3389/fsufs.2023.1167686.

### 15. Barron-Gafford et al. (2017) — HR and Grass-Tree Competition vs. Facilitation
- **Main contribution:** Direct field test of whether HR from trees shifts grass-tree interactions toward facilitation in a semi-arid savanna. Tracks sap flux in lateral and tap roots, leaf-level photosynthesis, ecosystem C exchange across a growing season.
- **Method:** Multi-sensor field campaign, Arizona semi-arid savanna.
- **Key finding:** "Alleviating water stress is not the reason grasses are growing in the understory of woody plants; rather, other stresses are being ameliorated." HR changes competition-facilitation balance, but shade and microclimate effects dominate.
- **Relevance:** The only paper directly addressing HR's role in shifting the competition-facilitation balance at seasonal scale. Results are system- and species-specific. Our modeling framework can generalize this question.
- **Citation note:** New Phytologist 215(4):1451–1461 (2017).

### 16. Feldman et al. (2024) — Plant Responses to Changing Rainfall Frequency and Intensity (Nature Reviews)
- **Main contribution:** Synthesizes global evidence that plants respond differently to changes in rainfall frequency vs. intensity even at fixed annual totals. In drylands, fewer but larger events tend to increase productivity (46% positive responses). The review frames the rainfall distribution problem as central to predicting ecosystem response to climate change.
- **Method:** Literature synthesis + global data analysis.
- **Key finding:** Plant function responses range from −28% to +29% across ecosystems under fewer, larger events. Dry ecosystems tend to benefit; wet ecosystems tend to suffer.
- **Relevance:** The highest-impact framing context for our rainfall regime analysis. Positions our work within a major contemporary scientific question. Their synthesis is empirical; our model provides mechanism.
- **Citation note:** Nature Reviews Earth & Environment 5:276 (2024).

### 17. Feldman et al. (2024b) — Large Global-Scale Vegetation Sensitivity to Daily Rainfall Variability (Nature)
- **Main contribution:** Satellite-based vegetation indices are sensitive to daily rainfall variability (frequency × intensity) independent of annual totals, across 42% of vegetated land surfaces. Sensitivity is ~95% as large as sensitivity to annual rainfall amount.
- **Method:** Satellite (NDVI/EVI) × field observations, global scale.
- **Key finding:** Daily rainfall regime is almost as important as annual total for vegetation. Drylands are most sensitive.
- **Relevance:** Provides global-scale empirical motivation for our rainfall regime decomposition. None of this work is mechanistic at the plot or crop level.
- **Citation note:** Nature 636 (December 2024).

### 18. Chemura et al. (2021) — Agroforestry Yield Buffering Under Climate Change, Ethiopia
- **Main contribution:** Uses APSIM to simulate agroforestry shade effects on maize yield under RCP2.6 and RCP8.5. Shows 10–20% shade reduces projected yield losses by 4–12% in Ethiopian zones with projected decline.
- **Method:** APSIM with shade and microclimate modifications; deterministic climate scenario analysis.
- **Key finding:** Agroforestry buffers yield under warming, primarily via shade-mediated temperature reduction. Does NOT use stochastic rainfall, does NOT produce yield distributions, does NOT decompose competition vs. facilitation.
- **Relevance:** Closest application to our research question using APSIM. But deterministic, single-climate-scenario approach; cannot address rainfall regime (alpha-lambda) sensitivity or P(crop failure).
- **Citation note:** Frontiers in Agronomy (2021), DOI: 10.3389/fagro.2021.609536.

### 19. Siteur et al. (2014) — Rainfall Intensity and Semi-Arid Ecosystems (WRR)
- **Main contribution:** Spatially explicit ecohydrological model to test how rainfall intensity (not just total) affects patterned semi-arid vegetation. Higher intensity → more runoff lost through vegetated bands; lower intensity → infiltration loss in bare interbands. Non-monotonic productivity response.
- **Method:** Mechanistic model, runoff-runon dynamics, spatially explicit.
- **Key finding:** Annual productivity depends non-linearly on storm intensity even at fixed annual total; there is no simple substitution between frequency and intensity.
- **Relevance:** Direct WRR precedent for the alpha-lambda sensitivity analysis in our model, but in a natural vegetation (not agricultural) system without tree-crop interactions.
- **Citation note:** Siteur et al. (2014), Water Resources Research 50:5980–6001.

### 20. Vervoort & van der Zee (2012) — Stochastic Groundwater Uptake and Root Depth
- **Main contribution:** Extends the Laio et al. (2001) framework to include deep roots tapping groundwater, with analytical PDFs for soil moisture and ET. Shows that root depth and seasonal groundwater feedbacks fundamentally alter the stress distribution.
- **Method:** Analytical stochastic model, two-layer implied by groundwater feedback.
- **Key finding:** Groundwater uptake can substantially stabilize soil moisture and reduce plant stress; the feedback structure (how uptake responds to root zone wetness) governs the PDF shape.
- **Relevance:** Closest theoretical precedent to our two-layer stochastic model. However: (1) addresses groundwater, not a tree-crop competition system; (2) no spatial decomposition; (3) no agronomic yield output.
- **Citation note:** Ecohydrology 5(5):579–591 (2012).

### 21. Roupsard et al. (1999) — Reverse Phenology of Faidherbia albida
- **Main contribution:** Direct field measurement of F. albida's dry-season leaf flush and wet-season dormancy in Sudano-Sahelian West Africa. Confirms that all major leaf area is accumulated during the dry season; negligible canopy during crop growing season.
- **Method:** Phenological observation, sap flow, isotope water uptake tracing.
- **Key finding:** F. albida uses deep soil water (>8 m) during dry season; effectively a null competitor during crop season. Nutrient benefits dominate its agroforestry impact.
- **Relevance:** The logical null/comparison case for our co-season tree. In our model, Faidherbia is the leaf_fraction=0 archetype. This paper grounds that comparison.
- **Citation note:** Roupsard et al. (1999), Functional Ecology 13:460–472.

### 22. Porporato et al. (2015) — Ecohydrological Modeling in Agroecosystems (WRR)
- **Main contribution:** Reviews ecohydrological modeling approaches applicable to agricultural systems; advocates for stochastic soil moisture frameworks as tools for crop stress analysis. Notes that probabilistic treatment of soil moisture is essential for characterizing crop water stress distributions.
- **Method:** Review + analytical examples.
- **Key finding:** Stochastic ecohydrology has rarely been applied to managed agricultural systems despite the appropriateness of the framework.
- **Relevance:** Direct WRR precedent and conceptual framing for our paper. Explicitly identifies the gap we fill.
- **Citation note:** Porporato et al. (2015), Water Resources Research 51:4579–4590.

---

## Thematic Organization

### Theoretical Contributions

**The Porporato-Rodriguez-Iturbe stochastic framework** (Laio et al. 2001, Rodriguez-Iturbe & Porporato 2004, Porporato et al. 2015) has been extended to groundwater-dependent systems (Laio et al. 2009, Vervoort & van der Zee 2012) and seasonal climates (Feng et al. 2015), but **never to agroforestry** — a multi-species system with deep and shallow root competition, HR, and canopy shading. This is the core theoretical gap.

The stress-gradient hypothesis (Maestre et al. 2009, Bertness & Callaway 1994) predicts facilitation dominates under high stress (drought), competition under low stress (mesic conditions). A 2024 mechanistic model (Scientific Reports) confirms this for natural vegetation using deterministic rainfall gradients, but with non-linear caveats (facilitation peaks at intermediate stress, then wanes). This has never been tested in agroforestry with stochastic rainfall across alpha-lambda parameter space.

**Hi-sAFe** (Talbot et al. 2019) is the most physically complete agroforestry model: 3D root architecture, voxel-scale competition, no plant priority, water table dynamics. But it is deterministic and produces single yield trajectories, not distributions.

### Empirical Findings

**Yield effects in semi-arid Africa:** Garrity et al. (2010) documents 2–3x maize yield increase under F. albida (primarily N-mediated). Kuyah et al. (2019) finds mean positive yield across 1,106 observations. The 2023 global meta-analysis shows +7% median increase in maize yield, with stronger effects in tropics (+16%), sandy soils (+23%), and N-poor soils (+81%). Competition effects dominate at high tree density; facilitation dominates at moderate density.

**Hydraulic redistribution magnitude:** Field range is 0.04–1.3 mm/day (Neumann & Cardon 2012); global synthesis mean is 0.249 mm/day (Prieto et al. 2022), ~27% of transpiration. In Sahelian shrub systems, HR is confirmed by tracer with dramatic millet yield benefits under drought (>900% biomass increase: Prieto et al. 2018). West African parkland species (Vitellaria, Lannea) show modest but confirmed HR (Bayala et al. 2008).

**Shade and ET:** Lin (2010) quantifies 32–41% reduction in ET demand with 60–80% shade cover in coffee systems. The mechanism is microclimate (reduced VPD and radiation). No equivalent study exists for semi-arid cereal systems in Africa.

**Rainfall regime and vegetation:** Feldman et al. (2024, Nature) shows that satellite vegetation indices respond to daily rainfall distribution nearly as strongly as to annual totals, with drylands showing the strongest sensitivity. Siteur et al. (2014, WRR) shows non-monotonic productivity under changing rainfall intensity in natural semi-arid vegetation. **Neither study addresses agroforestry or mechanistically decomposes competition vs. facilitation.**

### Methodological Innovations

The key methodological advance of our work is the combination of:
1. **Two-layer stochastic soil moisture** (extending Laio et al. 2001) with deep tree-only roots feeding HR
2. **Spatially explicit zoning** (under-canopy vs outside-canopy) enabling clean competition-facilitation decomposition
3. **Full yield distributions** from N=300 Monte Carlo realizations per regime
4. **Rainfall regime sweep** across alpha-lambda space (few intense vs. many small events at fixed annual total)

The ALLEY model (USDA Forest Service) applies stochastic methods to agroforestry economics (price, cost, yield distributions) but is not process-based and does not represent soil-water physics.

APSIM and DSSAT have been extended to include tree effects (Chemura et al. 2021), but these are deterministic and aggregate shade/temperature effects without hydraulic mechanisms or stochastic rainfall.

### Open Debates

1. **Does HR translate to meaningful crop yield benefit in non-extreme drought years?** Prieto et al. (2018) shows dramatic effects under imposed drought; Bayala et al. (2008) shows smaller effects in normal years. The transition between "background HR" and "drought-rescue HR" as a function of storm regime is unresolved.

2. **Does the stress-gradient hypothesis hold in managed agroforestry?** The 2024 mechanistic paper (Scientific Reports) shows facilitation peaks at intermediate aridity, then declines. But this uses deterministic rainfall. The stochastic equivalent—how the distribution of dry spell lengths (controlled by λ) shifts the competition-facilitation balance—is untested.

3. **Are yield means or yield variances more important for food security?** Meta-analyses focus on mean yield effects. Our framework produces both, enabling the first direct test of whether agroforestry reduces P(crop failure)—arguably more important for smallholder food security than mean yield.

---

## Gaps and Opportunities

1. **No stochastic agroforestry model exists.** All existing process models (WaNuLCAS, Hi-sAFe, HYDRUS-2D, APSIM-agroforestry, SWAP) use deterministic weather inputs. The Rodriguez-Iturbe/Porporato stochastic framework has never been extended to tree-crop systems. This is the foundational gap that our work fills. Publishable in WRR.

2. **Competition vs. facilitation has never been mechanically decomposed in a process model.** Empirical meta-analyses report net yield effects. Field studies rarely achieve the spatial separation needed to isolate shade from root competition (under-canopy mixes both; outside-canopy isolates root competition). Our three-zone design (under-canopy, outside-canopy, monoculture) provides clean decompositions unavailable in field data. Publishable in AgForMet.

3. **Rainfall regime (alpha vs. lambda) effects on competition-facilitation balance are unstudied.** The Feldman et al. (2024) Nature paper establishes that storm distribution matters nearly as much as annual total. But this is correlative and aggregate. No mechanistic model has tested whether the competition-facilitation balance in agroforestry shifts as storms become fewer and more intense—a central prediction of the stress-gradient hypothesis applied to intra-seasonal dry spell dynamics. This is a high-impact gap. Publishable in WRR, GCB, or Nature Sustainability.

4. **P(crop failure) in agroforestry has never been computed.** Meta-analyses report mean yield change. The probabilistic question—does agroforestry reduce the frequency of catastrophic (near-zero) yield years?—is directly answerable with our stochastic framework and is of direct food security relevance. This gap is flagged implicitly by Chemura et al. (2021) but not addressed. Publishable in GCB or Nature Sustainability.

5. **HR magnitude-to-yield effect as a function of storm regime is unquantified.** Neumann & Cardon (2012) and Prieto et al. (2022) quantify HR magnitude. Prieto et al. (2018) shows dramatic drought-year HR benefits. But the relationship between inter-storm dry spell length (governed by λ) and HR's agronomic contribution has never been modeled. Our sensitivity to lambda-scaled regimes directly addresses this.

6. **Co-season leafed tree agroforestry is underrepresented.** The vast majority of African agroforestry research features F. albida (reverse phenology) or N-fixing legume trees (Gliricidia, Leucaena). A co-season leafed, non-N-fixing tree presents the most physically interesting case (full competition + shade + HR simultaneously) but has received least mechanistic attention.

---

## Competitor Assessment

**Direct competitors** (papers that most closely overlap with our approach):

| Paper | Overlap | Key difference |
|-------|---------|---------------|
| Porporato et al. (2015) WRR | Stochastic ecohydrology for agroecosystems | No tree layer; no HR; no spatial decomposition |
| Vervoort & van der Zee (2012) | Two-layer stochastic model with deep roots | Single-species; no crop; no competition/facilitation |
| Chemura et al. (2021) | Agroforestry shade effects on maize yield under CC | APSIM, deterministic, no HR, no yield distributions |
| Siteur et al. (2014) WRR | Rainfall regime effects on semi-arid productivity in WRR | Natural vegetation, no agriculture, no tree-crop interaction |
| Bayala et al. (2014) Agrofor. Sys. | WaNuLCAS applied to Burkina Faso parklands | Deterministic, no yield distributions, no regime sweep |

**No existing paper combines all three of:** stochastic rainfall regime, mechanistic competition-facilitation decomposition, and crop yield probability distributions in an agroforestry context.

---

## Recommended Manuscript Directions

### Direction 1 (PRIMARY RECOMMENDATION): Rainfall Regime Sensitivity of the Competition-Facilitation Balance
**Target:** Water Resources Research or Global Change Biology

This is the most novel angle and most clearly motivated by the current literature moment (Feldman et al. 2024 Nature, Siteur et al. 2014 WRR). The central question—does agroforestry become more facilitative when storms are fewer and more intense?—sits at the intersection of a high-profile open scientific question and a direct policy need (climate change adaptation). The mechanistic decomposition (outside−mono = competition; under−mono = net effect; under−outside = shade facilitation) is unique and fills an explicit gap identified by multiple meta-analyses.

The current results (few-intense: +361 kg/acre under-canopy; many-small: +4 kg/acre) already provide a compelling and interpretable answer: agroforestry net benefit is highly sensitive to storm regime, switching from strongly facilitative to effectively neutral as storms become smaller and more frequent. This is a publishable finding.

**Proposed title:** *Rainfall regime governs the competition-facilitation balance in semi-arid tree-crop agroforestry: a stochastic ecohydrological analysis*

**3-sentence abstract:** We develop a spatially explicit, two-layer stochastic ecohydrological model of tree-crop agroforestry grounded in the Rodriguez-Iturbe/Porporato soil moisture framework and apply it to a co-season leafed tree with maize in semi-arid East Africa (Laikipia, Kenya). By separating under-canopy and outside-canopy crop zones from a monoculture baseline across 300 stochastic rainfall realizations per regime, we mechanically decompose root competition from shade-mediated demand facilitation and hydraulic redistribution across three rainfall regimes that hold annual total constant while varying storm frequency and intensity. We show that the competition-facilitation balance is acutely sensitive to rainfall regime: fewer, more intense storms strongly favor net facilitation (under-canopy yield +361 kg/acre vs. monoculture), while many small events shift the system toward net-competitive conditions—a finding with direct implications for predicting agroforestry outcomes under climate change.

### Direction 2 (SECONDARY): Yield Variance and P(Crop Failure) Reduction
**Target:** Global Change Biology or Nature Sustainability

This angle addresses RQ3 directly and is the most policy-relevant framing. The question—does agroforestry reduce catastrophic yield years?—has never been asked with a process-based probabilistic model. It reframes the agroforestry question from "does the average go up?" (already answered by meta-analyses) to "does the risk of food insecurity go down?" (not answered). This framing is ideal for GCB or Nature Sustainability because it connects mechanism to human welfare outcomes.

**Proposed title:** *Stochastic ecohydrological modeling reveals that tree-crop agroforestry reduces catastrophic maize yield failure under semi-arid rainfall variability*

**3-sentence abstract:** Smallholder food security depends not only on mean crop yields but on the probability of catastrophic harvest failure, yet existing agroforestry models cannot produce yield probability distributions. Using a two-layer stochastic soil moisture model applied to tree-maize agroforestry in semi-arid East Africa, we generate full yield distributions across 300 simulated seasons and three rainfall regimes to quantify how agroforestry shifts P(yield = 0) and the lower tail of the yield distribution relative to monoculture. We find that agroforestry systematically compresses the lower tail of the yield distribution—reducing catastrophic failure probability—most strongly under high-variance rainfall regimes (few intense storms), with direct implications for designing climate-resilient smallholder systems.

---

## Suggested Next Steps

1. **Complete the P(zero yield) and yield variance analysis** for all three regimes and both under-canopy and outside-canopy zones. This is the core data needed for Direction 2 and strengthens Direction 1.

2. **Sweep T_MAX** (1.0–4.0 mm/day) to identify the competition→facilitation transition. This clarifies the parameter regime in which the model operates and identifies when co-season leafed trees go from beneficial to harmful.

3. **Read Porporato et al. (2015) WRR** in full — this is the paper most directly cited as establishing the stochastic agroecosystem modeling context.

4. **Read Feldman et al. (2024) Nature Reviews** in full — this is the highest-profile framing paper for the alpha-lambda sensitivity analysis.

5. **Obtain Siteur et al. (2014) WRR** — key WRR precedent for rainfall regime ecohydrology; useful for positioning statement in introduction.

6. **Consider Faidherbia comparison experiment** (leaf_fraction=0 archetype) for supplement. The contrast between co-season (competition + shade + HR) and reverse-phenology (HR only, no competition during crop season) is directly interpretable using our framework.

---

## BibTeX Entries

```bibtex
@article{laio2001plants,
  title={Plants in water-controlled ecosystems: active role in hydrologic processes and response to water stress: II. Probabilistic soil moisture dynamics},
  author={Laio, Francesco and Porporato, Amilcare and Ridolfi, Luca and Rodriguez-Iturbe, Ignacio},
  journal={Advances in Water Resources},
  volume={24},
  pages={707--723},
  year={2001},
  doi={10.1016/S0309-1708(01)00005-7}
}

@book{rodriguez2004ecohydrology,
  title={Ecohydrology of Water-Controlled Ecosystems: Soil Moisture and Plant Dynamics},
  author={Rodriguez-Iturbe, Ignacio and Porporato, Amilcare},
  publisher={Cambridge University Press},
  year={2004}
}

@article{talbot2019hisafe,
  title={Hi-sAFe: A 3D Agroforestry Model for Integrating Dynamic Tree--Crop Interactions},
  author={Talbot, G. and Dupraz, C. and others},
  journal={Sustainability},
  volume={11},
  number={8},
  pages={2293},
  year={2019},
  doi={10.3390/su11082293}
}

@article{bayala2020water,
  title={Water acquisition, sharing and redistribution by roots: applications to agroforestry systems},
  author={Bayala, Jules and Prieto, Iñaki},
  journal={Plant and Soil},
  volume={453},
  pages={17--28},
  year={2020},
  doi={10.1007/s11104-019-04173-z}
}

@article{neumann2012magnitude,
  title={The magnitude of hydraulic redistribution by plant roots: a review and synthesis of empirical and modeling studies},
  author={Neumann, Rebecca B. and Cardon, Zoe G.},
  journal={New Phytologist},
  volume={194},
  pages={337--352},
  year={2012},
  doi={10.1111/j.1469-8137.2012.04088.x}
}

@article{prieto2022global,
  title={Magnitude and determinants of plant root hydraulic redistribution: A global synthesis analysis},
  author={Prieto, Iñaki and others},
  journal={Frontiers in Plant Science},
  volume={13},
  pages={918585},
  year={2022},
  doi={10.3389/fpls.2022.918585}
}

@article{prieto2018sahelian,
  title={Hydraulic Redistribution by Native Sahelian Shrubs: Bioirrigation to Resist In-Season Drought},
  author={Prieto, Iñaki and others},
  journal={Frontiers in Environmental Science},
  volume={6},
  pages={98},
  year={2018},
  doi={10.3389/fenvs.2018.00098}
}

@article{bayala2008hydraulic,
  title={Hydraulic redistribution study in two native tree species of agroforestry parklands of West African dry savanna},
  author={Bayala, Jules and others},
  journal={Acta Oecologica},
  volume={34},
  pages={341--349},
  year={2008},
  doi={10.1016/j.actao.2008.06.010}
}

@article{lin2010role,
  title={The role of agroforestry in reducing water loss through soil evaporation and crop transpiration in coffee agroecosystems},
  author={Lin, Brenda B.},
  journal={Agricultural and Forest Meteorology},
  volume={150},
  pages={510--518},
  year={2010},
  doi={10.1016/j.agrformet.2009.11.010}
}

@article{garrity2010evergreen,
  title={Evergreen Agriculture: a robust approach to sustainable food security in Africa},
  author={Garrity, D.P. and Akinnifesi, F.K. and Ajayi, O.C. and Weldesemayat, S.G. and Mowo, J.G. and Kalinganire, A. and Larwanou, M. and Bayala, J.},
  journal={Food Security},
  volume={2},
  pages={197--214},
  year={2010},
  doi={10.1007/s12571-010-0070-7}
}

@article{kuyah2019agroforestry,
  title={Agroforestry delivers a win-win solution for ecosystem services in sub-Saharan Africa. A meta-analysis},
  author={Kuyah, Shem and Whitney, Cory W. and Jonsson, Mattias and Sileshi, Gudeta W. and Öborn, Ingrid and Muthuri, Catherine W. and Luedeling, Eike},
  journal={Agronomy for Sustainable Development},
  volume={39},
  number={6},
  pages={1--12},
  year={2019},
  doi={10.1007/s13593-019-0589-8}
}

@article{sileshi2008meta,
  title={Meta-analysis of maize yield response to woody and herbaceous legumes in sub-Saharan Africa},
  author={Sileshi, Gudeta and Akinnifesi, Festus K. and Ajayi, Oluyede C. and Place, Frank},
  journal={Plant and Soil},
  volume={307},
  pages={1--19},
  year={2008},
  doi={10.1007/s11104-008-9547-y}
}

@article{barron2023global,
  title={Effects of agroforestry on grain yield of maize (Zea mays L.)—A global meta-analysis},
  author={others},
  journal={Frontiers in Sustainable Food Systems},
  volume={7},
  pages={1167686},
  year={2023},
  doi={10.3389/fsufs.2023.1167686}
}

@article{barrongafford2017hydraulic,
  title={Impacts of hydraulic redistribution on grass--tree competition vs facilitation in a semi-arid savanna},
  author={Barron-Gafford, G.A. and Sanchez-Cañete, E.P. and Minor, R.L. and Hendryx, S.M. and Lee, E. and Sutter, L.F. and others},
  journal={New Phytologist},
  volume={215},
  number={4},
  pages={1451--1461},
  year={2017},
  doi={10.1111/nph.14693}
}

@article{feldman2024plant,
  title={Plant responses to changing rainfall frequency and intensity},
  author={Feldman, A.F. and Feng, X. and Nippert, J.B. and others},
  journal={Nature Reviews Earth \& Environment},
  volume={5},
  pages={276},
  year={2024},
  doi={10.1038/s43017-024-00534-0}
}

@article{feldman2024global,
  title={Large global-scale vegetation sensitivity to daily rainfall variability},
  author={Feldman, A.F. and others},
  journal={Nature},
  volume={636},
  year={2024},
  doi={10.1038/s41586-024-08232-z}
}

@article{siteur2014rainfall,
  title={How will increases in rainfall intensity affect semiarid ecosystems?},
  author={Siteur, K. and others},
  journal={Water Resources Research},
  volume={50},
  pages={5980--6001},
  year={2014},
  doi={10.1002/2013WR014955}
}

@article{vervoort2012stochastic,
  title={On stochastic modelling of groundwater uptake in semi-arid water-limited systems: root density and seasonality effects},
  author={Vervoort, R. Willem and van der Zee, Sjoerd E.A.T.M.},
  journal={Ecohydrology},
  volume={5},
  number={5},
  pages={579--591},
  year={2012},
  doi={10.1002/eco.1288}
}

@article{roupsard1999reverse,
  title={Reverse phenology and dry-season water uptake by Faidherbia albida (Del.) A. Chev. in an agroforestry parkland of Sudanese West Africa},
  author={Roupsard, O. and Ferhi, A. and Granier, A. and Pallo, F. and Depommier, D. and Mallet, B. and Joly, H. I. and Dreyer, E.},
  journal={Functional Ecology},
  volume={13},
  pages={460--472},
  year={1999},
  doi={10.1046/j.1365-2435.1999.00345.x}
}

@article{porporato2015ecohydrological,
  title={Ecohydrological modeling in agroecosystems: Examples and challenges},
  author={Porporato, Amilcare and others},
  journal={Water Resources Research},
  volume={51},
  pages={4579--4590},
  year={2015},
  doi={10.1002/2015WR017289}
}

@article{chemura2021quantifying,
  title={Quantifying Agroforestry Yield Buffering Potential Under Climate Change in the Smallholder Maize Farming Systems of Ethiopia},
  author={Chemura, Abel and Yalew, Amsalu Woldie and Gornott, Christoph},
  journal={Frontiers in Agronomy},
  volume={3},
  pages={609536},
  year={2021},
  doi={10.3389/fagro.2021.609536}
}

@article{vannoordwijk1999wanulcas,
  title={WaNuLCAS, a model of Water, Nutrient and Light Capture in Agroforestry Systems},
  author={van Noordwijk, Meine and Lusiana, Betha},
  journal={Agroforestry Systems},
  volume={43},
  pages={217--242},
  year={1999},
  doi={10.1023/A:1026417120254}
}
```
