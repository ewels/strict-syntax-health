# nf-core Strict Syntax Health Report

This repository tracks the health of nf-core pipelines, modules, and subworkflows with respect to Nextflow's _strict syntax_ linting.

The [Nextflow docs](https://www.nextflow.io/docs/latest/strict-syntax.html) describes the differences from standard Nextflow syntax and includes many examples to help with migration and fixing errors.
Strict syntax is backwards compatible with existing Nextflow code, but enforces stricter rules to catch common errors and improve code quality.

The goal is for all nf-core pipelines to run without errors using strict syntax.

> [!IMPORTANT]
> See the [nf-core blog post](https://nf-co.re/blog/2025/nextflow_syntax_nf-core_roadmap) for details on the migration timeline.
> **Fixing all errors from `nextflow lint` will be a requirement by early spring 2026.**

- **Last updated:** 2026-08-31 00:23:30 UTC
- **Nextflow version:** 26.08.0-edge

## Pipelines

- **Total:** 0 parse errors, 1238 errors, 6162 warnings across 143 pipelines
- **Zero errors:** 95 pipelines (66.4%)

|                    Errors                    |                     Warnings                     |
| :------------------------------------------: | :----------------------------------------------: |
| ![Errors](lint_results/pipelines_errors.png) | ![Warnings](lint_results/pipelines_warnings.png) |

<details>
<summary>Pipeline Results (143 pipelines)</summary>

| Pipeline                                                                                       | Parse Error | Errors | Warnings | Prints Help |                               Lint Output                               |                               Help Output                                |
| ---------------------------------------------------------------------------------------------- | :---------: | -----: | -------: | :---------: | :---------------------------------------------------------------------: | :----------------------------------------------------------------------: |
| :x: [genomeannotator](https://github.com/nf-core/genomeannotator)                              |     No      |     79 |      148 |      -      |      [View](lint_results/pipeline-results/genomeannotator_lint.md)      |                                    -                                     |
| :x: [hicar](https://github.com/nf-core/hicar)                                                  |     No      |     78 |      122 |      -      |           [View](lint_results/pipeline-results/hicar_lint.md)           |                                    -                                     |
| :x: [evexplorer](https://github.com/nf-core/evexplorer)                                        |     No      |     74 |       53 |      -      |        [View](lint_results/pipeline-results/evexplorer_lint.md)         |                                    -                                     |
| :x: [viralintegration](https://github.com/nf-core/viralintegration)                            |     No      |     64 |       15 |      -      |     [View](lint_results/pipeline-results/viralintegration_lint.md)      |                                    -                                     |
| :x: [phageannotator](https://github.com/nf-core/phageannotator)                                |     No      |     58 |       98 |      -      |      [View](lint_results/pipeline-results/phageannotator_lint.md)       |                                    -                                     |
| :x: [readsimulator](https://github.com/nf-core/readsimulator)                                  |     No      |     53 |       53 |      -      |       [View](lint_results/pipeline-results/readsimulator_lint.md)       |                                    -                                     |
| :x: [metaboigniter](https://github.com/nf-core/metaboigniter)                                  |     No      |     52 |      125 |      -      |       [View](lint_results/pipeline-results/metaboigniter_lint.md)       |                                    -                                     |
| :x: [spinningjenny](https://github.com/nf-core/spinningjenny)                                  |     No      |     50 |        9 |      -      |       [View](lint_results/pipeline-results/spinningjenny_lint.md)       |                                    -                                     |
| :x: [variantcatalogue](https://github.com/nf-core/variantcatalogue)                            |     No      |     46 |       48 |      -      |     [View](lint_results/pipeline-results/variantcatalogue_lint.md)      |                                    -                                     |
| :x: [imcyto](https://github.com/nf-core/imcyto)                                                |     No      |     45 |       14 |      -      |          [View](lint_results/pipeline-results/imcyto_lint.md)           |                                    -                                     |
| :x: [meerpipe](https://github.com/nf-core/meerpipe)                                            |     No      |     44 |       84 |      -      |         [View](lint_results/pipeline-results/meerpipe_lint.md)          |                                    -                                     |
| :x: [callingcards](https://github.com/nf-core/callingcards)                                    |     No      |     41 |      177 |      -      |       [View](lint_results/pipeline-results/callingcards_lint.md)        |                                    -                                     |
| :x: [radseq](https://github.com/nf-core/radseq)                                                |     No      |     41 |       42 |      -      |          [View](lint_results/pipeline-results/radseq_lint.md)           |                                    -                                     |
| :x: [lncpipe](https://github.com/nf-core/lncpipe)                                              |     No      |     40 |      176 |      -      |          [View](lint_results/pipeline-results/lncpipe_lint.md)          |                                    -                                     |
| :x: [marsseq](https://github.com/nf-core/marsseq)                                              |     No      |     37 |       69 |      -      |          [View](lint_results/pipeline-results/marsseq_lint.md)          |                                    -                                     |
| :x: [nanoseq](https://github.com/nf-core/nanoseq)                                              |     No      |     36 |       80 |      -      |          [View](lint_results/pipeline-results/nanoseq_lint.md)          |                                    -                                     |
| :x: [omicsgenetraitassociation](https://github.com/nf-core/omicsgenetraitassociation)          |     No      |     33 |       30 |      -      | [View](lint_results/pipeline-results/omicsgenetraitassociation_lint.md) |                                    -                                     |
| :x: [genomeskim](https://github.com/nf-core/genomeskim)                                        |     No      |     33 |       13 |      -      |        [View](lint_results/pipeline-results/genomeskim_lint.md)         |                                    -                                     |
| :x: [denovotranscript](https://github.com/nf-core/denovotranscript)                            |     No      |     31 |       56 |      -      |     [View](lint_results/pipeline-results/denovotranscript_lint.md)      |                                    -                                     |
| :x: [sammyseq](https://github.com/nf-core/sammyseq)                                            |     No      |     21 |      159 |      -      |         [View](lint_results/pipeline-results/sammyseq_lint.md)          |                                    -                                     |
| :x: [metapep](https://github.com/nf-core/metapep)                                              |     No      |     20 |       56 |      -      |          [View](lint_results/pipeline-results/metapep_lint.md)          |                                    -                                     |
| :x: [bactmap](https://github.com/nf-core/bactmap)                                              |     No      |     17 |       31 |      -      |          [View](lint_results/pipeline-results/bactmap_lint.md)          |                                    -                                     |
| :x: [slamseq](https://github.com/nf-core/slamseq)                                              |     No      |     17 |        0 |      -      |          [View](lint_results/pipeline-results/slamseq_lint.md)          |                                    -                                     |
| :x: [deepmodeloptim](https://github.com/nf-core/deepmodeloptim)                                |     No      |     16 |       50 |      -      |      [View](lint_results/pipeline-results/deepmodeloptim_lint.md)       |                                    -                                     |
| :x: [diaproteomics](https://github.com/nf-core/diaproteomics)                                  |     No      |     16 |        0 |      -      |       [View](lint_results/pipeline-results/diaproteomics_lint.md)       |                                    -                                     |
| :x: [clipseq](https://github.com/nf-core/clipseq)                                              |     No      |     15 |        0 |      -      |          [View](lint_results/pipeline-results/clipseq_lint.md)          |                                    -                                     |
| :x: [mnaseseq](https://github.com/nf-core/mnaseseq)                                            |     No      |     15 |        0 |      -      |         [View](lint_results/pipeline-results/mnaseseq_lint.md)          |                                    -                                     |
| :x: [proteogenomicsdb](https://github.com/nf-core/proteogenomicsdb)                            |     No      |     15 |        0 |      -      |     [View](lint_results/pipeline-results/proteogenomicsdb_lint.md)      |                                    -                                     |
| :x: [pangenome](https://github.com/nf-core/pangenome)                                          |     No      |     14 |       67 |      -      |         [View](lint_results/pipeline-results/pangenome_lint.md)         |                                    -                                     |
| :x: [rnasplice](https://github.com/nf-core/rnasplice)                                          |     No      |     14 |       19 |      -      |         [View](lint_results/pipeline-results/rnasplice_lint.md)         |                                    -                                     |
| :x: [detaxizer](https://github.com/nf-core/detaxizer)                                          |     No      |     13 |       65 |      -      |         [View](lint_results/pipeline-results/detaxizer_lint.md)         |                                    -                                     |
| :x: [crisprseq](https://github.com/nf-core/crisprseq)                                          |     No      |     13 |       50 |      -      |         [View](lint_results/pipeline-results/crisprseq_lint.md)         |                                    -                                     |
| :x: [coproid](https://github.com/nf-core/coproid)                                              |     No      |     12 |       52 |      -      |          [View](lint_results/pipeline-results/coproid_lint.md)          |                                    -                                     |
| :x: [hic](https://github.com/nf-core/hic)                                                      |     No      |     12 |       31 |      -      |            [View](lint_results/pipeline-results/hic_lint.md)            |                                    -                                     |
| :x: [panoramaseq](https://github.com/nf-core/panoramaseq)                                      |     No      |     11 |       24 |      -      |        [View](lint_results/pipeline-results/panoramaseq_lint.md)        |                                    -                                     |
| :x: [hgtseq](https://github.com/nf-core/hgtseq)                                                |     No      |     10 |       74 |      -      |          [View](lint_results/pipeline-results/hgtseq_lint.md)           |                                    -                                     |
| :x: [pacsomatic](https://github.com/nf-core/pacsomatic)                                        |     No      |      7 |      120 |      -      |        [View](lint_results/pipeline-results/pacsomatic_lint.md)         |                                    -                                     |
| :x: [pacvar](https://github.com/nf-core/pacvar)                                                |     No      |      6 |       34 |      -      |          [View](lint_results/pipeline-results/pacvar_lint.md)           |                                    -                                     |
| :x: [kmermaid](https://github.com/nf-core/kmermaid)                                            |     No      |      6 |       16 |      -      |         [View](lint_results/pipeline-results/kmermaid_lint.md)          |                                    -                                     |
| :x: [mitodetect](https://github.com/nf-core/mitodetect)                                        |     No      |      6 |       16 |      -      |        [View](lint_results/pipeline-results/mitodetect_lint.md)         |                                    -                                     |
| :x: [troughgraph](https://github.com/nf-core/troughgraph)                                      |     No      |      6 |       16 |      -      |        [View](lint_results/pipeline-results/troughgraph_lint.md)        |                                    -                                     |
| :x: [nascent](https://github.com/nf-core/nascent)                                              |     No      |      5 |      157 |      -      |          [View](lint_results/pipeline-results/nascent_lint.md)          |                                    -                                     |
| :x: [circdna](https://github.com/nf-core/circdna)                                              |     No      |      4 |       62 |      -      |          [View](lint_results/pipeline-results/circdna_lint.md)          |                                    -                                     |
| :x: [methylarray](https://github.com/nf-core/methylarray)                                      |     No      |      4 |       19 |      -      |        [View](lint_results/pipeline-results/methylarray_lint.md)        |                                    -                                     |
| :x: [rnadnavar](https://github.com/nf-core/rnadnavar)                                          |     No      |      3 |      351 |      -      |         [View](lint_results/pipeline-results/rnadnavar_lint.md)         |                                    -                                     |
| :x: [dualrnaseq](https://github.com/nf-core/dualrnaseq)                                        |     No      |      2 |       57 |      -      |        [View](lint_results/pipeline-results/dualrnaseq_lint.md)         |                                    -                                     |
| :x: [tbanalyzer](https://github.com/nf-core/tbanalyzer)                                        |     No      |      2 |       23 |      -      |        [View](lint_results/pipeline-results/tbanalyzer_lint.md)         |                                    -                                     |
| :x: [daamicrobiome](https://github.com/nf-core/daamicrobiome)                                  |     No      |      1 |       12 |      -      |       [View](lint_results/pipeline-results/daamicrobiome_lint.md)       |                                    -                                     |
| :white_check_mark: [pathogensurveillance](https://github.com/nf-core/pathogensurveillance)     |     No      |      0 |      436 |     Yes     |   [View](lint_results/pipeline-results/pathogensurveillance_lint.md)    |  [View](lint_results/prints-help-results/pathogensurveillance_help.txt)  |
| :white_check_mark: [eager](https://github.com/nf-core/eager)                                   |     No      |      0 |      410 |     Yes     |           [View](lint_results/pipeline-results/eager_lint.md)           |         [View](lint_results/prints-help-results/eager_help.txt)          |
| :white_check_mark: [multiplesequencealign](https://github.com/nf-core/multiplesequencealign)   |     No      |      0 |      178 |     Yes     |   [View](lint_results/pipeline-results/multiplesequencealign_lint.md)   | [View](lint_results/prints-help-results/multiplesequencealign_help.txt)  |
| :x: [longraredisease](https://github.com/nf-core/longraredisease)                              |     No      |      0 |      161 |     No      |      [View](lint_results/pipeline-results/longraredisease_lint.md)      |    [View](lint_results/prints-help-results/longraredisease_help.txt)     |
| :x: [cutandrun](https://github.com/nf-core/cutandrun)                                          |     No      |      0 |      160 |     No      |         [View](lint_results/pipeline-results/cutandrun_lint.md)         |       [View](lint_results/prints-help-results/cutandrun_help.txt)        |
| :white_check_mark: [riboseq](https://github.com/nf-core/riboseq)                               |     No      |      0 |      149 |     Yes     |          [View](lint_results/pipeline-results/riboseq_lint.md)          |        [View](lint_results/prints-help-results/riboseq_help.txt)         |
| :x: [deepmutscan](https://github.com/nf-core/deepmutscan)                                      |     No      |      0 |      117 |     No      |        [View](lint_results/pipeline-results/deepmutscan_lint.md)        |      [View](lint_results/prints-help-results/deepmutscan_help.txt)       |
| :white_check_mark: [differentialabundance](https://github.com/nf-core/differentialabundance)   |     No      |      0 |      109 |     Yes     |   [View](lint_results/pipeline-results/differentialabundance_lint.md)   | [View](lint_results/prints-help-results/differentialabundance_help.txt)  |
| :x: [oncoanalyser](https://github.com/nf-core/oncoanalyser)                                    |     No      |      0 |      106 |     No      |       [View](lint_results/pipeline-results/oncoanalyser_lint.md)        |      [View](lint_results/prints-help-results/oncoanalyser_help.txt)      |
| :white_check_mark: [diseasemodulediscovery](https://github.com/nf-core/diseasemodulediscovery) |     No      |      0 |      105 |     Yes     |  [View](lint_results/pipeline-results/diseasemodulediscovery_lint.md)   | [View](lint_results/prints-help-results/diseasemodulediscovery_help.txt) |
| :white_check_mark: [taxprofiler](https://github.com/nf-core/taxprofiler)                       |     No      |      0 |      100 |     Yes     |        [View](lint_results/pipeline-results/taxprofiler_lint.md)        |      [View](lint_results/prints-help-results/taxprofiler_help.txt)       |
| :white_check_mark: [mcmicro](https://github.com/nf-core/mcmicro)                               |     No      |      0 |       72 |     Yes     |          [View](lint_results/pipeline-results/mcmicro_lint.md)          |        [View](lint_results/prints-help-results/mcmicro_help.txt)         |
| :white_check_mark: [funcscan](https://github.com/nf-core/funcscan)                             |     No      |      0 |       64 |     Yes     |         [View](lint_results/pipeline-results/funcscan_lint.md)          |        [View](lint_results/prints-help-results/funcscan_help.txt)        |
| :white_check_mark: [abotyper](https://github.com/nf-core/abotyper)                             |     No      |      0 |       60 |     Yes     |         [View](lint_results/pipeline-results/abotyper_lint.md)          |        [View](lint_results/prints-help-results/abotyper_help.txt)        |
| :x: [epigenomesegmentation](https://github.com/nf-core/epigenomesegmentation)                  |     No      |      0 |       59 |     No      |   [View](lint_results/pipeline-results/epigenomesegmentation_lint.md)   | [View](lint_results/prints-help-results/epigenomesegmentation_help.txt)  |
| :white_check_mark: [bacmodel](https://github.com/nf-core/bacmodel)                             |     No      |      0 |       58 |     Yes     |         [View](lint_results/pipeline-results/bacmodel_lint.md)          |        [View](lint_results/prints-help-results/bacmodel_help.txt)        |
| :white_check_mark: [chipseq](https://github.com/nf-core/chipseq)                               |     No      |      0 |       57 |     Yes     |          [View](lint_results/pipeline-results/chipseq_lint.md)          |        [View](lint_results/prints-help-results/chipseq_help.txt)         |
| :x: [tumourevo](https://github.com/nf-core/tumourevo)                                          |     No      |      0 |       48 |     No      |         [View](lint_results/pipeline-results/tumourevo_lint.md)         |       [View](lint_results/prints-help-results/tumourevo_help.txt)        |
| :x: [methylong](https://github.com/nf-core/methylong)                                          |     No      |      0 |       45 |     No      |         [View](lint_results/pipeline-results/methylong_lint.md)         |       [View](lint_results/prints-help-results/methylong_help.txt)        |
| :white_check_mark: [mhcquant](https://github.com/nf-core/mhcquant)                             |     No      |      0 |       45 |     Yes     |         [View](lint_results/pipeline-results/mhcquant_lint.md)          |        [View](lint_results/prints-help-results/mhcquant_help.txt)        |
| :white_check_mark: [molkart](https://github.com/nf-core/molkart)                               |     No      |      0 |       43 |     Yes     |          [View](lint_results/pipeline-results/molkart_lint.md)          |        [View](lint_results/prints-help-results/molkart_help.txt)         |
| :white_check_mark: [airrflow](https://github.com/nf-core/airrflow)                             |     No      |      0 |       34 |     Yes     |         [View](lint_results/pipeline-results/airrflow_lint.md)          |        [View](lint_results/prints-help-results/airrflow_help.txt)        |
| :white_check_mark: [stableexpression](https://github.com/nf-core/stableexpression)             |     No      |      0 |       33 |     Yes     |     [View](lint_results/pipeline-results/stableexpression_lint.md)      |    [View](lint_results/prints-help-results/stableexpression_help.txt)    |
| :white_check_mark: [hadge](https://github.com/nf-core/hadge)                                   |     No      |      0 |       27 |     Yes     |           [View](lint_results/pipeline-results/hadge_lint.md)           |         [View](lint_results/prints-help-results/hadge_help.txt)          |
| :white_check_mark: [drugresponseeval](https://github.com/nf-core/drugresponseeval)             |     No      |      0 |       26 |     Yes     |     [View](lint_results/pipeline-results/drugresponseeval_lint.md)      |    [View](lint_results/prints-help-results/drugresponseeval_help.txt)    |
| :white_check_mark: [methylseq](https://github.com/nf-core/methylseq)                           |     No      |      0 |       25 |     Yes     |         [View](lint_results/pipeline-results/methylseq_lint.md)         |       [View](lint_results/prints-help-results/methylseq_help.txt)        |
| :white_check_mark: [ampliseq](https://github.com/nf-core/ampliseq)                             |     No      |      0 |       23 |     Yes     |         [View](lint_results/pipeline-results/ampliseq_lint.md)          |        [View](lint_results/prints-help-results/ampliseq_help.txt)        |
| :white_check_mark: [pathogenepidemiology](https://github.com/nf-core/pathogenepidemiology)     |     No      |      0 |       23 |     Yes     |   [View](lint_results/pipeline-results/pathogenepidemiology_lint.md)    |  [View](lint_results/prints-help-results/pathogenepidemiology_help.txt)  |
| :x: [rarevariantburden](https://github.com/nf-core/rarevariantburden)                          |     No      |      0 |       22 |     No      |     [View](lint_results/pipeline-results/rarevariantburden_lint.md)     |   [View](lint_results/prints-help-results/rarevariantburden_help.txt)    |
| :white_check_mark: [scdownstream](https://github.com/nf-core/scdownstream)                     |     No      |      0 |       22 |     Yes     |       [View](lint_results/pipeline-results/scdownstream_lint.md)        |      [View](lint_results/prints-help-results/scdownstream_help.txt)      |
| :x: [alleleexpression](https://github.com/nf-core/alleleexpression)                            |     No      |      0 |       20 |     No      |     [View](lint_results/pipeline-results/alleleexpression_lint.md)      |    [View](lint_results/prints-help-results/alleleexpression_help.txt)    |
| :white_check_mark: [circrna](https://github.com/nf-core/circrna)                               |     No      |      0 |       20 |     Yes     |          [View](lint_results/pipeline-results/circrna_lint.md)          |        [View](lint_results/prints-help-results/circrna_help.txt)         |
| :white_check_mark: [mag](https://github.com/nf-core/mag)                                       |     No      |      0 |       20 |     Yes     |            [View](lint_results/pipeline-results/mag_lint.md)            |          [View](lint_results/prints-help-results/mag_help.txt)           |
| :white_check_mark: [plasmodiumdrugres](https://github.com/nf-core/plasmodiumdrugres)           |     No      |      0 |       20 |     Yes     |     [View](lint_results/pipeline-results/plasmodiumdrugres_lint.md)     |   [View](lint_results/prints-help-results/plasmodiumdrugres_help.txt)    |
| :white_check_mark: [lsmquant](https://github.com/nf-core/lsmquant)                             |     No      |      0 |       19 |     Yes     |         [View](lint_results/pipeline-results/lsmquant_lint.md)          |        [View](lint_results/prints-help-results/lsmquant_help.txt)        |
| :x: [dartseq](https://github.com/nf-core/dartseq)                                              |     No      |      0 |       18 |     No      |          [View](lint_results/pipeline-results/dartseq_lint.md)          |        [View](lint_results/prints-help-results/dartseq_help.txt)         |
| :white_check_mark: [atacseq](https://github.com/nf-core/atacseq)                               |     No      |      0 |       16 |     Yes     |          [View](lint_results/pipeline-results/atacseq_lint.md)          |        [View](lint_results/prints-help-results/atacseq_help.txt)         |
| :white_check_mark: [bacass](https://github.com/nf-core/bacass)                                 |     No      |      0 |       16 |     Yes     |          [View](lint_results/pipeline-results/bacass_lint.md)           |         [View](lint_results/prints-help-results/bacass_help.txt)         |
| :white_check_mark: [pixelator](https://github.com/nf-core/pixelator)                           |     No      |      0 |       16 |     Yes     |         [View](lint_results/pipeline-results/pixelator_lint.md)         |       [View](lint_results/prints-help-results/pixelator_help.txt)        |
| :white_check_mark: [magmap](https://github.com/nf-core/magmap)                                 |     No      |      0 |       13 |     Yes     |          [View](lint_results/pipeline-results/magmap_lint.md)           |         [View](lint_results/prints-help-results/magmap_help.txt)         |
| :white_check_mark: [funcprofiler](https://github.com/nf-core/funcprofiler)                     |     No      |      0 |       12 |     Yes     |       [View](lint_results/pipeline-results/funcprofiler_lint.md)        |      [View](lint_results/prints-help-results/funcprofiler_help.txt)      |
| :x: [genephylomodeler](https://github.com/nf-core/genephylomodeler)                            |     No      |      0 |       12 |     No      |     [View](lint_results/pipeline-results/genephylomodeler_lint.md)      |    [View](lint_results/prints-help-results/genephylomodeler_help.txt)    |
| :white_check_mark: [pairgenomealign](https://github.com/nf-core/pairgenomealign)               |     No      |      0 |       12 |     Yes     |      [View](lint_results/pipeline-results/pairgenomealign_lint.md)      |    [View](lint_results/prints-help-results/pairgenomealign_help.txt)     |
| :white_check_mark: [raredisease](https://github.com/nf-core/raredisease)                       |     No      |      0 |       12 |     Yes     |        [View](lint_results/pipeline-results/raredisease_lint.md)        |      [View](lint_results/prints-help-results/raredisease_help.txt)       |
| :white_check_mark: [sopa](https://github.com/nf-core/sopa)                                     |     No      |      0 |       11 |     Yes     |           [View](lint_results/pipeline-results/sopa_lint.md)            |          [View](lint_results/prints-help-results/sopa_help.txt)          |
| :white_check_mark: [seqsubmit](https://github.com/nf-core/seqsubmit)                           |     No      |      0 |       10 |     Yes     |         [View](lint_results/pipeline-results/seqsubmit_lint.md)         |       [View](lint_results/prints-help-results/seqsubmit_help.txt)        |
| :white_check_mark: [tfactivity](https://github.com/nf-core/tfactivity)                         |     No      |      0 |       10 |     Yes     |        [View](lint_results/pipeline-results/tfactivity_lint.md)         |       [View](lint_results/prints-help-results/tfactivity_help.txt)       |
| :white_check_mark: [fastqrepair](https://github.com/nf-core/fastqrepair)                       |     No      |      0 |        9 |     Yes     |        [View](lint_results/pipeline-results/fastqrepair_lint.md)        |      [View](lint_results/prints-help-results/fastqrepair_help.txt)       |
| :white_check_mark: [isoseq](https://github.com/nf-core/isoseq)                                 |     No      |      0 |        9 |     Yes     |          [View](lint_results/pipeline-results/isoseq_lint.md)           |         [View](lint_results/prints-help-results/isoseq_help.txt)         |
| :white_check_mark: [genomeassembler](https://github.com/nf-core/genomeassembler)               |     No      |      0 |        8 |     Yes     |      [View](lint_results/pipeline-results/genomeassembler_lint.md)      |    [View](lint_results/prints-help-results/genomeassembler_help.txt)     |
| :white_check_mark: [mspepid](https://github.com/nf-core/mspepid)                               |     No      |      0 |        8 |     Yes     |          [View](lint_results/pipeline-results/mspepid_lint.md)          |        [View](lint_results/prints-help-results/mspepid_help.txt)         |
| :white_check_mark: [cageseq](https://github.com/nf-core/cageseq)                               |     No      |      0 |        6 |     Yes     |          [View](lint_results/pipeline-results/cageseq_lint.md)          |        [View](lint_results/prints-help-results/cageseq_help.txt)         |
| :white_check_mark: [createtaxdb](https://github.com/nf-core/createtaxdb)                       |     No      |      0 |        6 |     Yes     |        [View](lint_results/pipeline-results/createtaxdb_lint.md)        |      [View](lint_results/prints-help-results/createtaxdb_help.txt)       |
| :x: [rnafusion](https://github.com/nf-core/rnafusion)                                          |     No      |      0 |        6 |     No      |         [View](lint_results/pipeline-results/rnafusion_lint.md)         |       [View](lint_results/prints-help-results/rnafusion_help.txt)        |
| :white_check_mark: [variantbenchmarking](https://github.com/nf-core/variantbenchmarking)       |     No      |      0 |        6 |     Yes     |    [View](lint_results/pipeline-results/variantbenchmarking_lint.md)    |  [View](lint_results/prints-help-results/variantbenchmarking_help.txt)   |
| :white_check_mark: [drop](https://github.com/nf-core/drop)                                     |     No      |      0 |        5 |     Yes     |           [View](lint_results/pipeline-results/drop_lint.md)            |          [View](lint_results/prints-help-results/drop_help.txt)          |
| :white_check_mark: [fastquorum](https://github.com/nf-core/fastquorum)                         |     No      |      0 |        5 |     Yes     |        [View](lint_results/pipeline-results/fastquorum_lint.md)         |       [View](lint_results/prints-help-results/fastquorum_help.txt)       |
| :white_check_mark: [nanostring](https://github.com/nf-core/nanostring)                         |     No      |      0 |        5 |     Yes     |        [View](lint_results/pipeline-results/nanostring_lint.md)         |       [View](lint_results/prints-help-results/nanostring_help.txt)       |
| :white_check_mark: [scnanoseq](https://github.com/nf-core/scnanoseq)                           |     No      |      0 |        5 |     Yes     |         [View](lint_results/pipeline-results/scnanoseq_lint.md)         |       [View](lint_results/prints-help-results/scnanoseq_help.txt)        |
| :white_check_mark: [demo](https://github.com/nf-core/demo)                                     |     No      |      0 |        4 |     Yes     |           [View](lint_results/pipeline-results/demo_lint.md)            |          [View](lint_results/prints-help-results/demo_help.txt)          |
| :white_check_mark: [hlatyping](https://github.com/nf-core/hlatyping)                           |     No      |      0 |        4 |     Yes     |         [View](lint_results/pipeline-results/hlatyping_lint.md)         |       [View](lint_results/prints-help-results/hlatyping_help.txt)        |
| :x: [ncrnannotator](https://github.com/nf-core/ncrnannotator)                                  |     No      |      0 |        4 |     No      |       [View](lint_results/pipeline-results/ncrnannotator_lint.md)       |     [View](lint_results/prints-help-results/ncrnannotator_help.txt)      |
| :white_check_mark: [viralmetagenome](https://github.com/nf-core/viralmetagenome)               |     No      |      0 |        4 |     Yes     |      [View](lint_results/pipeline-results/viralmetagenome_lint.md)      |    [View](lint_results/prints-help-results/viralmetagenome_help.txt)     |
| :white_check_mark: [proteinfold](https://github.com/nf-core/proteinfold)                       |     No      |      0 |        3 |     Yes     |        [View](lint_results/pipeline-results/proteinfold_lint.md)        |      [View](lint_results/prints-help-results/proteinfold_help.txt)       |
| :white_check_mark: [rnaseq](https://github.com/nf-core/rnaseq)                                 |     No      |      0 |        3 |     Yes     |          [View](lint_results/pipeline-results/rnaseq_lint.md)           |         [View](lint_results/prints-help-results/rnaseq_help.txt)         |
| :white_check_mark: [smrnaseq](https://github.com/nf-core/smrnaseq)                             |     No      |      0 |        3 |     Yes     |         [View](lint_results/pipeline-results/smrnaseq_lint.md)          |        [View](lint_results/prints-help-results/smrnaseq_help.txt)        |
| :white_check_mark: [demultiplex](https://github.com/nf-core/demultiplex)                       |     No      |      0 |        2 |     Yes     |        [View](lint_results/pipeline-results/demultiplex_lint.md)        |      [View](lint_results/prints-help-results/demultiplex_help.txt)       |
| :x: [ribomsqc](https://github.com/nf-core/ribomsqc)                                            |     No      |      0 |        2 |     No      |         [View](lint_results/pipeline-results/ribomsqc_lint.md)          |        [View](lint_results/prints-help-results/ribomsqc_help.txt)        |
| :white_check_mark: [variantprioritization](https://github.com/nf-core/variantprioritization)   |     No      |      0 |        2 |     Yes     |   [View](lint_results/pipeline-results/variantprioritization_lint.md)   | [View](lint_results/prints-help-results/variantprioritization_help.txt)  |
| :white_check_mark: [gwas](https://github.com/nf-core/gwas)                                     |     No      |      0 |        1 |     Yes     |           [View](lint_results/pipeline-results/gwas_lint.md)            |          [View](lint_results/prints-help-results/gwas_help.txt)          |
| :x: [phaseimpute](https://github.com/nf-core/phaseimpute)                                      |     No      |      0 |        1 |     No      |        [View](lint_results/pipeline-results/phaseimpute_lint.md)        |      [View](lint_results/prints-help-results/phaseimpute_help.txt)       |
| :white_check_mark: [phyloplace](https://github.com/nf-core/phyloplace)                         |     No      |      0 |        1 |     Yes     |        [View](lint_results/pipeline-results/phyloplace_lint.md)         |       [View](lint_results/prints-help-results/phyloplace_help.txt)       |
| :white_check_mark: [rangeland](https://github.com/nf-core/rangeland)                           |     No      |      0 |        1 |     Yes     |         [View](lint_results/pipeline-results/rangeland_lint.md)         |       [View](lint_results/prints-help-results/rangeland_help.txt)        |
| :white_check_mark: [scrnaseq](https://github.com/nf-core/scrnaseq)                             |     No      |      0 |        1 |     Yes     |         [View](lint_results/pipeline-results/scrnaseq_lint.md)          |        [View](lint_results/prints-help-results/scrnaseq_help.txt)        |
| :white_check_mark: [spatialaxe](https://github.com/nf-core/spatialaxe)                         |     No      |      0 |        1 |     Yes     |        [View](lint_results/pipeline-results/spatialaxe_lint.md)         |       [View](lint_results/prints-help-results/spatialaxe_help.txt)       |
| :white_check_mark: [bamtofastq](https://github.com/nf-core/bamtofastq)                         |     No      |      0 |        0 |     Yes     |        [View](lint_results/pipeline-results/bamtofastq_lint.md)         |       [View](lint_results/prints-help-results/bamtofastq_help.txt)       |
| :white_check_mark: [cellpainting](https://github.com/nf-core/cellpainting)                     |     No      |      0 |        0 |     Yes     |       [View](lint_results/pipeline-results/cellpainting_lint.md)        |      [View](lint_results/prints-help-results/cellpainting_help.txt)      |
| :white_check_mark: [createpanelrefs](https://github.com/nf-core/createpanelrefs)               |     No      |      0 |        0 |     Yes     |      [View](lint_results/pipeline-results/createpanelrefs_lint.md)      |    [View](lint_results/prints-help-results/createpanelrefs_help.txt)     |
| :white_check_mark: [datasync](https://github.com/nf-core/datasync)                             |     No      |      0 |        0 |     Yes     |         [View](lint_results/pipeline-results/datasync_lint.md)          |        [View](lint_results/prints-help-results/datasync_help.txt)        |
| :white_check_mark: [epitopeprediction](https://github.com/nf-core/epitopeprediction)           |     No      |      0 |        0 |     Yes     |     [View](lint_results/pipeline-results/epitopeprediction_lint.md)     |   [View](lint_results/prints-help-results/epitopeprediction_help.txt)    |
| :white_check_mark: [fetchngs](https://github.com/nf-core/fetchngs)                             |     No      |      0 |        0 |     Yes     |         [View](lint_results/pipeline-results/fetchngs_lint.md)          |        [View](lint_results/prints-help-results/fetchngs_help.txt)        |
| :white_check_mark: [genomeqc](https://github.com/nf-core/genomeqc)                             |     No      |      0 |        0 |     Yes     |         [View](lint_results/pipeline-results/genomeqc_lint.md)          |        [View](lint_results/prints-help-results/genomeqc_help.txt)        |
| :white_check_mark: [genomicrelatedness](https://github.com/nf-core/genomicrelatedness)         |     No      |      0 |        0 |     Yes     |    [View](lint_results/pipeline-results/genomicrelatedness_lint.md)     |   [View](lint_results/prints-help-results/genomicrelatedness_help.txt)   |
| :white_check_mark: [metatdenovo](https://github.com/nf-core/metatdenovo)                       |     No      |      0 |        0 |     Yes     |        [View](lint_results/pipeline-results/metatdenovo_lint.md)        |      [View](lint_results/prints-help-results/metatdenovo_help.txt)       |
| :white_check_mark: [proteinannotator](https://github.com/nf-core/proteinannotator)             |     No      |      0 |        0 |     Yes     |     [View](lint_results/pipeline-results/proteinannotator_lint.md)      |    [View](lint_results/prints-help-results/proteinannotator_help.txt)    |
| :white_check_mark: [proteinfamilies](https://github.com/nf-core/proteinfamilies)               |     No      |      0 |        0 |     Yes     |      [View](lint_results/pipeline-results/proteinfamilies_lint.md)      |    [View](lint_results/prints-help-results/proteinfamilies_help.txt)     |
| :white_check_mark: [provenancereport](https://github.com/nf-core/provenancereport)             |     No      |      0 |        0 |     Yes     |     [View](lint_results/pipeline-results/provenancereport_lint.md)      |    [View](lint_results/prints-help-results/provenancereport_help.txt)    |
| :x: [references](https://github.com/nf-core/references)                                        |     No      |      0 |        0 |     No      |        [View](lint_results/pipeline-results/references_lint.md)         |       [View](lint_results/prints-help-results/references_help.txt)       |
| :white_check_mark: [reportho](https://github.com/nf-core/reportho)                             |     No      |      0 |        0 |     Yes     |         [View](lint_results/pipeline-results/reportho_lint.md)          |        [View](lint_results/prints-help-results/reportho_help.txt)        |
| :white_check_mark: [rnastructurome](https://github.com/nf-core/rnastructurome)                 |     No      |      0 |        0 |     Yes     |      [View](lint_results/pipeline-results/rnastructurome_lint.md)       |     [View](lint_results/prints-help-results/rnastructurome_help.txt)     |
| :white_check_mark: [rnavar](https://github.com/nf-core/rnavar)                                 |     No      |      0 |        0 |     Yes     |          [View](lint_results/pipeline-results/rnavar_lint.md)           |         [View](lint_results/prints-help-results/rnavar_help.txt)         |
| :white_check_mark: [sarek](https://github.com/nf-core/sarek)                                   |     No      |      0 |        0 |     Yes     |           [View](lint_results/pipeline-results/sarek_lint.md)           |         [View](lint_results/prints-help-results/sarek_help.txt)          |
| :white_check_mark: [seqinspector](https://github.com/nf-core/seqinspector)                     |     No      |      0 |        0 |     Yes     |       [View](lint_results/pipeline-results/seqinspector_lint.md)        |      [View](lint_results/prints-help-results/seqinspector_help.txt)      |
| :white_check_mark: [spatialvi](https://github.com/nf-core/spatialvi)                           |     No      |      0 |        0 |     Yes     |         [View](lint_results/pipeline-results/spatialvi_lint.md)         |       [View](lint_results/prints-help-results/spatialvi_help.txt)        |
| :white_check_mark: [viralrecon](https://github.com/nf-core/viralrecon)                         |     No      |      0 |        0 |     Yes     |        [View](lint_results/pipeline-results/viralrecon_lint.md)         |       [View](lint_results/prints-help-results/viralrecon_help.txt)       |

</details>

## Workflow Outputs Migration

Adoption of the new [workflow outputs](https://docs.seqera.io/nextflow/tutorials/workflow-outputs) syntax (a top-level `output {}` block) and migration away from the legacy `publishDir` directive. This is a separate dataset from the lint errors and warnings above.

- **Uses `output {}`:** 11 pipelines (7.7%)
- **Still uses `publishDir`:** 139 pipelines (97.2%)
- **Fully migrated** (`output {}`, no `publishDir`): 4 pipelines (2.8%)

![Workflow outputs migration](lint_results/pipelines_workflow_outputs.png)

<details>
<summary>Workflow Outputs Migration (143 pipelines)</summary>

The status emoji next to each pipeline shows its migration state: :white_check_mark: fully migrated (only `output {}`), :warning: in progress (`output {}` and `publishDir`), :x: not started (only `publishDir`).

| Pipeline                                                                              | `output {}` | `publishDir` |                                       Report                                       |
| ------------------------------------------------------------------------------------- | :---------: | :----------: | :--------------------------------------------------------------------------------: |
| :white_check_mark: [createpanelrefs](https://github.com/nf-core/createpanelrefs)      |     Yes     |      No      |      [View](lint_results/workflow-outputs-results/createpanelrefs_outputs.md)      |
| :white_check_mark: [oncoanalyser](https://github.com/nf-core/oncoanalyser)            |     Yes     |      No      |       [View](lint_results/workflow-outputs-results/oncoanalyser_outputs.md)        |
| :white_check_mark: [references](https://github.com/nf-core/references)                |     Yes     |      No      |        [View](lint_results/workflow-outputs-results/references_outputs.md)         |
| :white_check_mark: [seqinspector](https://github.com/nf-core/seqinspector)            |     Yes     |      No      |       [View](lint_results/workflow-outputs-results/seqinspector_outputs.md)        |
| :warning: [demultiplex](https://github.com/nf-core/demultiplex)                       |     Yes     |   Yes (5)    |        [View](lint_results/workflow-outputs-results/demultiplex_outputs.md)        |
| :warning: [differentialabundance](https://github.com/nf-core/differentialabundance)   |     Yes     |   Yes (10)   |   [View](lint_results/workflow-outputs-results/differentialabundance_outputs.md)   |
| :warning: [proteinfamilies](https://github.com/nf-core/proteinfamilies)               |     Yes     |   Yes (79)   |      [View](lint_results/workflow-outputs-results/proteinfamilies_outputs.md)      |
| :warning: [raredisease](https://github.com/nf-core/raredisease)                       |     Yes     |   Yes (2)    |        [View](lint_results/workflow-outputs-results/raredisease_outputs.md)        |
| :warning: [rnavar](https://github.com/nf-core/rnavar)                                 |     Yes     |   Yes (33)   |          [View](lint_results/workflow-outputs-results/rnavar_outputs.md)           |
| :warning: [sarek](https://github.com/nf-core/sarek)                                   |     Yes     |  Yes (193)   |           [View](lint_results/workflow-outputs-results/sarek_outputs.md)           |
| :warning: [stableexpression](https://github.com/nf-core/stableexpression)             |     Yes     |   Yes (1)    |     [View](lint_results/workflow-outputs-results/stableexpression_outputs.md)      |
| :x: [abotyper](https://github.com/nf-core/abotyper)                                   |     No      |   Yes (14)   |         [View](lint_results/workflow-outputs-results/abotyper_outputs.md)          |
| :x: [airrflow](https://github.com/nf-core/airrflow)                                   |     No      |   Yes (84)   |         [View](lint_results/workflow-outputs-results/airrflow_outputs.md)          |
| :x: [alleleexpression](https://github.com/nf-core/alleleexpression)                   |     No      |   Yes (15)   |     [View](lint_results/workflow-outputs-results/alleleexpression_outputs.md)      |
| :x: [ampliseq](https://github.com/nf-core/ampliseq)                                   |     No      |  Yes (104)   |         [View](lint_results/workflow-outputs-results/ampliseq_outputs.md)          |
| :x: [atacseq](https://github.com/nf-core/atacseq)                                     |     No      |   Yes (79)   |          [View](lint_results/workflow-outputs-results/atacseq_outputs.md)          |
| :x: [bacass](https://github.com/nf-core/bacass)                                       |     No      |   Yes (35)   |          [View](lint_results/workflow-outputs-results/bacass_outputs.md)           |
| :x: [bacmodel](https://github.com/nf-core/bacmodel)                                   |     No      |   Yes (20)   |         [View](lint_results/workflow-outputs-results/bacmodel_outputs.md)          |
| :x: [bactmap](https://github.com/nf-core/bactmap)                                     |     No      |   Yes (53)   |          [View](lint_results/workflow-outputs-results/bactmap_outputs.md)          |
| :x: [bamtofastq](https://github.com/nf-core/bamtofastq)                               |     No      |   Yes (17)   |        [View](lint_results/workflow-outputs-results/bamtofastq_outputs.md)         |
| :x: [cageseq](https://github.com/nf-core/cageseq)                                     |     No      |   Yes (30)   |          [View](lint_results/workflow-outputs-results/cageseq_outputs.md)          |
| :x: [callingcards](https://github.com/nf-core/callingcards)                           |     No      |   Yes (38)   |       [View](lint_results/workflow-outputs-results/callingcards_outputs.md)        |
| :x: [cellpainting](https://github.com/nf-core/cellpainting)                           |     No      |   Yes (7)    |       [View](lint_results/workflow-outputs-results/cellpainting_outputs.md)        |
| :x: [chipseq](https://github.com/nf-core/chipseq)                                     |     No      |   Yes (57)   |          [View](lint_results/workflow-outputs-results/chipseq_outputs.md)          |
| :x: [circdna](https://github.com/nf-core/circdna)                                     |     No      |   Yes (35)   |          [View](lint_results/workflow-outputs-results/circdna_outputs.md)          |
| :x: [circrna](https://github.com/nf-core/circrna)                                     |     No      |  Yes (127)   |          [View](lint_results/workflow-outputs-results/circrna_outputs.md)          |
| :x: [clipseq](https://github.com/nf-core/clipseq)                                     |     No      |   Yes (24)   |          [View](lint_results/workflow-outputs-results/clipseq_outputs.md)          |
| :x: [coproid](https://github.com/nf-core/coproid)                                     |     No      |   Yes (11)   |          [View](lint_results/workflow-outputs-results/coproid_outputs.md)          |
| :x: [createtaxdb](https://github.com/nf-core/createtaxdb)                             |     No      |   Yes (17)   |        [View](lint_results/workflow-outputs-results/createtaxdb_outputs.md)        |
| :x: [crisprseq](https://github.com/nf-core/crisprseq)                                 |     No      |   Yes (45)   |         [View](lint_results/workflow-outputs-results/crisprseq_outputs.md)         |
| :x: [cutandrun](https://github.com/nf-core/cutandrun)                                 |     No      |   Yes (81)   |         [View](lint_results/workflow-outputs-results/cutandrun_outputs.md)         |
| :x: [daamicrobiome](https://github.com/nf-core/daamicrobiome)                         |     No      |   Yes (18)   |       [View](lint_results/workflow-outputs-results/daamicrobiome_outputs.md)       |
| :x: [dartseq](https://github.com/nf-core/dartseq)                                     |     No      |   Yes (14)   |          [View](lint_results/workflow-outputs-results/dartseq_outputs.md)          |
| :x: [datasync](https://github.com/nf-core/datasync)                                   |     No      |   Yes (5)    |         [View](lint_results/workflow-outputs-results/datasync_outputs.md)          |
| :x: [deepmodeloptim](https://github.com/nf-core/deepmodeloptim)                       |     No      |   Yes (12)   |      [View](lint_results/workflow-outputs-results/deepmodeloptim_outputs.md)       |
| :x: [deepmutscan](https://github.com/nf-core/deepmutscan)                             |     No      |   Yes (29)   |        [View](lint_results/workflow-outputs-results/deepmutscan_outputs.md)        |
| :x: [demo](https://github.com/nf-core/demo)                                           |     No      |   Yes (5)    |           [View](lint_results/workflow-outputs-results/demo_outputs.md)            |
| :x: [denovotranscript](https://github.com/nf-core/denovotranscript)                   |     No      |   Yes (7)    |     [View](lint_results/workflow-outputs-results/denovotranscript_outputs.md)      |
| :x: [detaxizer](https://github.com/nf-core/detaxizer)                                 |     No      |   Yes (20)   |         [View](lint_results/workflow-outputs-results/detaxizer_outputs.md)         |
| :x: [diaproteomics](https://github.com/nf-core/diaproteomics)                         |     No      |   Yes (13)   |       [View](lint_results/workflow-outputs-results/diaproteomics_outputs.md)       |
| :x: [diseasemodulediscovery](https://github.com/nf-core/diseasemodulediscovery)       |     No      |   Yes (19)   |  [View](lint_results/workflow-outputs-results/diseasemodulediscovery_outputs.md)   |
| :x: [drop](https://github.com/nf-core/drop)                                           |     No      |   Yes (28)   |           [View](lint_results/workflow-outputs-results/drop_outputs.md)            |
| :x: [drugresponseeval](https://github.com/nf-core/drugresponseeval)                   |     No      |   Yes (26)   |     [View](lint_results/workflow-outputs-results/drugresponseeval_outputs.md)      |
| :x: [dualrnaseq](https://github.com/nf-core/dualrnaseq)                               |     No      |   Yes (30)   |        [View](lint_results/workflow-outputs-results/dualrnaseq_outputs.md)         |
| :x: [eager](https://github.com/nf-core/eager)                                         |     No      |  Yes (126)   |           [View](lint_results/workflow-outputs-results/eager_outputs.md)           |
| :x: [epigenomesegmentation](https://github.com/nf-core/epigenomesegmentation)         |     No      |   Yes (13)   |   [View](lint_results/workflow-outputs-results/epigenomesegmentation_outputs.md)   |
| :x: [epitopeprediction](https://github.com/nf-core/epitopeprediction)                 |     No      |   Yes (18)   |     [View](lint_results/workflow-outputs-results/epitopeprediction_outputs.md)     |
| :x: [evexplorer](https://github.com/nf-core/evexplorer)                               |     No      |   Yes (9)    |        [View](lint_results/workflow-outputs-results/evexplorer_outputs.md)         |
| :x: [fastqrepair](https://github.com/nf-core/fastqrepair)                             |     No      |   Yes (6)    |        [View](lint_results/workflow-outputs-results/fastqrepair_outputs.md)        |
| :x: [fastquorum](https://github.com/nf-core/fastquorum)                               |     No      |   Yes (15)   |        [View](lint_results/workflow-outputs-results/fastquorum_outputs.md)         |
| :x: [fetchngs](https://github.com/nf-core/fetchngs)                                   |     No      |   Yes (9)    |         [View](lint_results/workflow-outputs-results/fetchngs_outputs.md)          |
| :x: [funcprofiler](https://github.com/nf-core/funcprofiler)                           |     No      |   Yes (9)    |       [View](lint_results/workflow-outputs-results/funcprofiler_outputs.md)        |
| :x: [funcscan](https://github.com/nf-core/funcscan)                                   |     No      |   Yes (22)   |         [View](lint_results/workflow-outputs-results/funcscan_outputs.md)          |
| :x: [genephylomodeler](https://github.com/nf-core/genephylomodeler)                   |     No      |   Yes (12)   |     [View](lint_results/workflow-outputs-results/genephylomodeler_outputs.md)      |
| :x: [genomeannotator](https://github.com/nf-core/genomeannotator)                     |     No      |   Yes (14)   |      [View](lint_results/workflow-outputs-results/genomeannotator_outputs.md)      |
| :x: [genomeassembler](https://github.com/nf-core/genomeassembler)                     |     No      |   Yes (93)   |      [View](lint_results/workflow-outputs-results/genomeassembler_outputs.md)      |
| :x: [genomeqc](https://github.com/nf-core/genomeqc)                                   |     No      |   Yes (55)   |         [View](lint_results/workflow-outputs-results/genomeqc_outputs.md)          |
| :x: [genomeskim](https://github.com/nf-core/genomeskim)                               |     No      |   Yes (3)    |        [View](lint_results/workflow-outputs-results/genomeskim_outputs.md)         |
| :x: [genomicrelatedness](https://github.com/nf-core/genomicrelatedness)               |     No      |   Yes (61)   |    [View](lint_results/workflow-outputs-results/genomicrelatedness_outputs.md)     |
| :x: [gwas](https://github.com/nf-core/gwas)                                           |     No      |   Yes (3)    |           [View](lint_results/workflow-outputs-results/gwas_outputs.md)            |
| :x: [hadge](https://github.com/nf-core/hadge)                                         |     No      |   Yes (33)   |           [View](lint_results/workflow-outputs-results/hadge_outputs.md)           |
| :x: [hgtseq](https://github.com/nf-core/hgtseq)                                       |     No      |   Yes (50)   |          [View](lint_results/workflow-outputs-results/hgtseq_outputs.md)           |
| :x: [hic](https://github.com/nf-core/hic)                                             |     No      |   Yes (39)   |            [View](lint_results/workflow-outputs-results/hic_outputs.md)            |
| :x: [hicar](https://github.com/nf-core/hicar)                                         |     No      |  Yes (156)   |           [View](lint_results/workflow-outputs-results/hicar_outputs.md)           |
| :x: [hlatyping](https://github.com/nf-core/hlatyping)                                 |     No      |   Yes (20)   |         [View](lint_results/workflow-outputs-results/hlatyping_outputs.md)         |
| :x: [imcyto](https://github.com/nf-core/imcyto)                                       |     No      |   Yes (7)    |          [View](lint_results/workflow-outputs-results/imcyto_outputs.md)           |
| :x: [isoseq](https://github.com/nf-core/isoseq)                                       |     No      |   Yes (15)   |          [View](lint_results/workflow-outputs-results/isoseq_outputs.md)           |
| :x: [kmermaid](https://github.com/nf-core/kmermaid)                                   |     No      |   Yes (2)    |         [View](lint_results/workflow-outputs-results/kmermaid_outputs.md)          |
| :x: [lncpipe](https://github.com/nf-core/lncpipe)                                     |     No      |   Yes (39)   |          [View](lint_results/workflow-outputs-results/lncpipe_outputs.md)          |
| :x: [longraredisease](https://github.com/nf-core/longraredisease)                     |     No      |   Yes (76)   |      [View](lint_results/workflow-outputs-results/longraredisease_outputs.md)      |
| :x: [lsmquant](https://github.com/nf-core/lsmquant)                                   |     No      |   Yes (5)    |         [View](lint_results/workflow-outputs-results/lsmquant_outputs.md)          |
| :x: [mag](https://github.com/nf-core/mag)                                             |     No      |   Yes (74)   |            [View](lint_results/workflow-outputs-results/mag_outputs.md)            |
| :x: [magmap](https://github.com/nf-core/magmap)                                       |     No      |   Yes (26)   |          [View](lint_results/workflow-outputs-results/magmap_outputs.md)           |
| :x: [marsseq](https://github.com/nf-core/marsseq)                                     |     No      |   Yes (23)   |          [View](lint_results/workflow-outputs-results/marsseq_outputs.md)          |
| :x: [mcmicro](https://github.com/nf-core/mcmicro)                                     |     No      |   Yes (10)   |          [View](lint_results/workflow-outputs-results/mcmicro_outputs.md)          |
| :x: [meerpipe](https://github.com/nf-core/meerpipe)                                   |     No      |   Yes (9)    |         [View](lint_results/workflow-outputs-results/meerpipe_outputs.md)          |
| :x: [metaboigniter](https://github.com/nf-core/metaboigniter)                         |     No      |   Yes (31)   |       [View](lint_results/workflow-outputs-results/metaboigniter_outputs.md)       |
| :x: [metapep](https://github.com/nf-core/metapep)                                     |     No      |   Yes (21)   |          [View](lint_results/workflow-outputs-results/metapep_outputs.md)          |
| :x: [metatdenovo](https://github.com/nf-core/metatdenovo)                             |     No      |   Yes (18)   |        [View](lint_results/workflow-outputs-results/metatdenovo_outputs.md)        |
| :x: [methylarray](https://github.com/nf-core/methylarray)                             |     No      |   Yes (2)    |        [View](lint_results/workflow-outputs-results/methylarray_outputs.md)        |
| :x: [methylong](https://github.com/nf-core/methylong)                                 |     No      |   Yes (42)   |         [View](lint_results/workflow-outputs-results/methylong_outputs.md)         |
| :x: [methylseq](https://github.com/nf-core/methylseq)                                 |     No      |   Yes (47)   |         [View](lint_results/workflow-outputs-results/methylseq_outputs.md)         |
| :x: [mhcquant](https://github.com/nf-core/mhcquant)                                   |     No      |   Yes (46)   |         [View](lint_results/workflow-outputs-results/mhcquant_outputs.md)          |
| :x: [mitodetect](https://github.com/nf-core/mitodetect)                               |     No      |   Yes (2)    |        [View](lint_results/workflow-outputs-results/mitodetect_outputs.md)         |
| :x: [mnaseseq](https://github.com/nf-core/mnaseseq)                                   |     No      |   Yes (26)   |         [View](lint_results/workflow-outputs-results/mnaseseq_outputs.md)          |
| :x: [molkart](https://github.com/nf-core/molkart)                                     |     No      |   Yes (18)   |          [View](lint_results/workflow-outputs-results/molkart_outputs.md)          |
| :x: [mspepid](https://github.com/nf-core/mspepid)                                     |     No      |   Yes (9)    |          [View](lint_results/workflow-outputs-results/mspepid_outputs.md)          |
| :x: [multiplesequencealign](https://github.com/nf-core/multiplesequencealign)         |     No      |   Yes (17)   |   [View](lint_results/workflow-outputs-results/multiplesequencealign_outputs.md)   |
| :x: [nanoseq](https://github.com/nf-core/nanoseq)                                     |     No      |   Yes (3)    |          [View](lint_results/workflow-outputs-results/nanoseq_outputs.md)          |
| :x: [nanostring](https://github.com/nf-core/nanostring)                               |     No      |   Yes (7)    |        [View](lint_results/workflow-outputs-results/nanostring_outputs.md)         |
| :x: [nascent](https://github.com/nf-core/nascent)                                     |     No      |   Yes (42)   |          [View](lint_results/workflow-outputs-results/nascent_outputs.md)          |
| :x: [ncrnannotator](https://github.com/nf-core/ncrnannotator)                         |     No      |   Yes (6)    |       [View](lint_results/workflow-outputs-results/ncrnannotator_outputs.md)       |
| :x: [omicsgenetraitassociation](https://github.com/nf-core/omicsgenetraitassociation) |     No      |   Yes (11)   | [View](lint_results/workflow-outputs-results/omicsgenetraitassociation_outputs.md) |
| :x: [pacsomatic](https://github.com/nf-core/pacsomatic)                               |     No      |   Yes (40)   |        [View](lint_results/workflow-outputs-results/pacsomatic_outputs.md)         |
| :x: [pacvar](https://github.com/nf-core/pacvar)                                       |     No      |   Yes (15)   |          [View](lint_results/workflow-outputs-results/pacvar_outputs.md)           |
| :x: [pairgenomealign](https://github.com/nf-core/pairgenomealign)                     |     No      |   Yes (11)   |      [View](lint_results/workflow-outputs-results/pairgenomealign_outputs.md)      |
| :x: [pangenome](https://github.com/nf-core/pangenome)                                 |     No      |   Yes (30)   |         [View](lint_results/workflow-outputs-results/pangenome_outputs.md)         |
| :x: [panoramaseq](https://github.com/nf-core/panoramaseq)                             |     No      |   Yes (15)   |        [View](lint_results/workflow-outputs-results/panoramaseq_outputs.md)        |
| :x: [pathogenepidemiology](https://github.com/nf-core/pathogenepidemiology)           |     No      |   Yes (15)   |   [View](lint_results/workflow-outputs-results/pathogenepidemiology_outputs.md)    |
| :x: [pathogensurveillance](https://github.com/nf-core/pathogensurveillance)           |     No      |   Yes (52)   |   [View](lint_results/workflow-outputs-results/pathogensurveillance_outputs.md)    |
| :x: [phageannotator](https://github.com/nf-core/phageannotator)                       |     No      |   Yes (39)   |      [View](lint_results/workflow-outputs-results/phageannotator_outputs.md)       |
| :x: [phaseimpute](https://github.com/nf-core/phaseimpute)                             |     No      |   Yes (90)   |        [View](lint_results/workflow-outputs-results/phaseimpute_outputs.md)        |
| :x: [phyloplace](https://github.com/nf-core/phyloplace)                               |     No      |   Yes (3)    |        [View](lint_results/workflow-outputs-results/phyloplace_outputs.md)         |
| :x: [pixelator](https://github.com/nf-core/pixelator)                                 |     No      |   Yes (12)   |         [View](lint_results/workflow-outputs-results/pixelator_outputs.md)         |
| :x: [plasmodiumdrugres](https://github.com/nf-core/plasmodiumdrugres)                 |     No      |   Yes (3)    |     [View](lint_results/workflow-outputs-results/plasmodiumdrugres_outputs.md)     |
| :x: [proteinannotator](https://github.com/nf-core/proteinannotator)                   |     No      |   Yes (24)   |     [View](lint_results/workflow-outputs-results/proteinannotator_outputs.md)      |
| :x: [proteinfold](https://github.com/nf-core/proteinfold)                             |     No      |   Yes (51)   |        [View](lint_results/workflow-outputs-results/proteinfold_outputs.md)        |
| :x: [proteogenomicsdb](https://github.com/nf-core/proteogenomicsdb)                   |     No      |   Yes (5)    |     [View](lint_results/workflow-outputs-results/proteogenomicsdb_outputs.md)      |
| :x: [provenancereport](https://github.com/nf-core/provenancereport)                   |     No      |   Yes (4)    |     [View](lint_results/workflow-outputs-results/provenancereport_outputs.md)      |
| :x: [radseq](https://github.com/nf-core/radseq)                                       |     No      |   Yes (25)   |          [View](lint_results/workflow-outputs-results/radseq_outputs.md)           |
| :x: [rangeland](https://github.com/nf-core/rangeland)                                 |     No      |   Yes (5)    |         [View](lint_results/workflow-outputs-results/rangeland_outputs.md)         |
| :x: [rarevariantburden](https://github.com/nf-core/rarevariantburden)                 |     No      |   Yes (17)   |     [View](lint_results/workflow-outputs-results/rarevariantburden_outputs.md)     |
| :x: [readsimulator](https://github.com/nf-core/readsimulator)                         |     No      |   Yes (18)   |       [View](lint_results/workflow-outputs-results/readsimulator_outputs.md)       |
| :x: [reportho](https://github.com/nf-core/reportho)                                   |     No      |   Yes (38)   |         [View](lint_results/workflow-outputs-results/reportho_outputs.md)          |
| :x: [ribomsqc](https://github.com/nf-core/ribomsqc)                                   |     No      |   Yes (1)    |         [View](lint_results/workflow-outputs-results/ribomsqc_outputs.md)          |
| :x: [riboseq](https://github.com/nf-core/riboseq)                                     |     No      |  Yes (139)   |          [View](lint_results/workflow-outputs-results/riboseq_outputs.md)          |
| :x: [rnadnavar](https://github.com/nf-core/rnadnavar)                                 |     No      |   Yes (98)   |         [View](lint_results/workflow-outputs-results/rnadnavar_outputs.md)         |
| :x: [rnafusion](https://github.com/nf-core/rnafusion)                                 |     No      |   Yes (35)   |         [View](lint_results/workflow-outputs-results/rnafusion_outputs.md)         |
| :x: [rnaseq](https://github.com/nf-core/rnaseq)                                       |     No      |  Yes (115)   |          [View](lint_results/workflow-outputs-results/rnaseq_outputs.md)           |
| :x: [rnasplice](https://github.com/nf-core/rnasplice)                                 |     No      |   Yes (70)   |         [View](lint_results/workflow-outputs-results/rnasplice_outputs.md)         |
| :x: [rnastructurome](https://github.com/nf-core/rnastructurome)                       |     No      |   Yes (53)   |      [View](lint_results/workflow-outputs-results/rnastructurome_outputs.md)       |
| :x: [sammyseq](https://github.com/nf-core/sammyseq)                                   |     No      |   Yes (34)   |         [View](lint_results/workflow-outputs-results/sammyseq_outputs.md)          |
| :x: [scdownstream](https://github.com/nf-core/scdownstream)                           |     No      |   Yes (75)   |       [View](lint_results/workflow-outputs-results/scdownstream_outputs.md)        |
| :x: [scnanoseq](https://github.com/nf-core/scnanoseq)                                 |     No      |   Yes (92)   |         [View](lint_results/workflow-outputs-results/scnanoseq_outputs.md)         |
| :x: [scrnaseq](https://github.com/nf-core/scrnaseq)                                   |     No      |   Yes (26)   |         [View](lint_results/workflow-outputs-results/scrnaseq_outputs.md)          |
| :x: [seqsubmit](https://github.com/nf-core/seqsubmit)                                 |     No      |   Yes (19)   |         [View](lint_results/workflow-outputs-results/seqsubmit_outputs.md)         |
| :x: [slamseq](https://github.com/nf-core/slamseq)                                     |     No      |   Yes (8)    |          [View](lint_results/workflow-outputs-results/slamseq_outputs.md)          |
| :x: [smrnaseq](https://github.com/nf-core/smrnaseq)                                   |     No      |   Yes (53)   |         [View](lint_results/workflow-outputs-results/smrnaseq_outputs.md)          |
| :x: [sopa](https://github.com/nf-core/sopa)                                           |     No      |   Yes (4)    |           [View](lint_results/workflow-outputs-results/sopa_outputs.md)            |
| :x: [spatialaxe](https://github.com/nf-core/spatialaxe)                               |     No      |   Yes (40)   |        [View](lint_results/workflow-outputs-results/spatialaxe_outputs.md)         |
| :x: [spatialvi](https://github.com/nf-core/spatialvi)                                 |     No      |   Yes (7)    |         [View](lint_results/workflow-outputs-results/spatialvi_outputs.md)         |
| :x: [spinningjenny](https://github.com/nf-core/spinningjenny)                         |     No      |   Yes (6)    |       [View](lint_results/workflow-outputs-results/spinningjenny_outputs.md)       |
| :x: [taxprofiler](https://github.com/nf-core/taxprofiler)                             |     No      |   Yes (91)   |        [View](lint_results/workflow-outputs-results/taxprofiler_outputs.md)        |
| :x: [tbanalyzer](https://github.com/nf-core/tbanalyzer)                               |     No      |   Yes (2)    |        [View](lint_results/workflow-outputs-results/tbanalyzer_outputs.md)         |
| :x: [tfactivity](https://github.com/nf-core/tfactivity)                               |     No      |   Yes (75)   |        [View](lint_results/workflow-outputs-results/tfactivity_outputs.md)         |
| :x: [troughgraph](https://github.com/nf-core/troughgraph)                             |     No      |   Yes (2)    |        [View](lint_results/workflow-outputs-results/troughgraph_outputs.md)        |
| :x: [tumourevo](https://github.com/nf-core/tumourevo)                                 |     No      |   Yes (18)   |         [View](lint_results/workflow-outputs-results/tumourevo_outputs.md)         |
| :x: [variantbenchmarking](https://github.com/nf-core/variantbenchmarking)             |     No      |   Yes (79)   |    [View](lint_results/workflow-outputs-results/variantbenchmarking_outputs.md)    |
| :x: [variantcatalogue](https://github.com/nf-core/variantcatalogue)                   |     No      |   Yes (33)   |     [View](lint_results/workflow-outputs-results/variantcatalogue_outputs.md)      |
| :x: [variantprioritization](https://github.com/nf-core/variantprioritization)         |     No      |   Yes (13)   |   [View](lint_results/workflow-outputs-results/variantprioritization_outputs.md)   |
| :x: [viralintegration](https://github.com/nf-core/viralintegration)                   |     No      |   Yes (2)    |     [View](lint_results/workflow-outputs-results/viralintegration_outputs.md)      |
| :x: [viralmetagenome](https://github.com/nf-core/viralmetagenome)                     |     No      |  Yes (117)   |      [View](lint_results/workflow-outputs-results/viralmetagenome_outputs.md)      |
| :x: [viralrecon](https://github.com/nf-core/viralrecon)                               |     No      |  Yes (173)   |        [View](lint_results/workflow-outputs-results/viralrecon_outputs.md)         |

</details>

## Modules

- **Total:** 0 parse errors, 0 errors, 25 warnings across 2048 modules
- **Zero errors:** 2048 modules (100.0%)

|                   Errors                   |                    Warnings                    |
| :----------------------------------------: | :--------------------------------------------: |
| ![Errors](lint_results/modules_errors.png) | ![Warnings](lint_results/modules_warnings.png) |

<details>
<summary>Module Results (0 modules with errors)</summary>

| Module | Parse Error | Errors | Warnings | Lint Output |
| ------ | :---------: | -----: | -------: | :---------: |

_Modules with zero errors are not shown above (2048 modules). They may still have warnings. See the [modules results directory](lint_results/module-results/) for all lint outputs._

</details>

## Subworkflows

- **Total:** 0 parse errors, 0 errors, 7 warnings across 122 subworkflows
- **Zero errors:** 122 subworkflows (100.0%)

|                     Errors                      |                      Warnings                       |
| :---------------------------------------------: | :-------------------------------------------------: |
| ![Errors](lint_results/subworkflows_errors.png) | ![Warnings](lint_results/subworkflows_warnings.png) |

<details>
<summary>Subworkflow Results (0 subworkflows with errors)</summary>

| Subworkflow | Parse Error | Errors | Warnings | Lint Output |
| ----------- | :---------: | -----: | -------: | :---------: |

_Subworkflows with zero errors are not shown above (122 subworkflows). They may still have warnings. See the [subworkflows results directory](lint_results/subworkflow-results/) for all lint outputs._

</details>

## About

This report is generated daily by running `nextflow lint` on each nf-core pipeline, module, and subworkflow.
The linting checks for strict syntax compliance in Nextflow DSL2 code.

- **Parse errors** indicate items where `nextflow lint` could not run at all, typically due to syntax errors that prevent Nextflow from parsing the code
- **Errors** indicate syntax issues that will cause problems in future Nextflow versions
- **Warnings** indicate deprecated patterns that should be updated, but having warnings is fine (though it's nice to fix those as well if possible)
- **Prints Help** (pipelines only) tests whether the pipeline can print its help message using the v2 syntax parser (`NXF_SYNTAX_PARSER=v2 nextflow run . --help`). This test only runs for pipelines with zero lint errors.
- **Workflow Outputs Migration** (pipelines only, shown in its own section) tracks adoption of the new [workflow outputs](https://docs.seqera.io/nextflow/tutorials/workflow-outputs) syntax (a top-level `output {}` block) and migration away from the legacy `publishDir` directive (detected in both `.nf` and `conf/*.config` files). A pipeline is fully migrated once it uses `output {}` with no `publishDir`. Each pipeline links to a report listing exactly where both were found.

## Running Locally

You can run `nextflow lint` on your own pipeline to check for strict syntax issues:

```bash
nextflow lint .
```

> **Note:** Until [this fix](https://github.com/nextflow-io/nextflow/pull/6716) is included in a Nextflow edge release, you may need to exclude nf-test files manually:
>
> ```bash
> nextflow lint . -exclude ".git,.nf-test,nf-test.config"
> ```

See the [strict syntax documentation](https://www.nextflow.io/docs/latest/strict-syntax.html) for more information about the rules being checked.

## Getting Help

If you need help fixing strict syntax errors in your pipeline, the [Nextflow community forum](https://community.seqera.io/) is a great place to ask questions.
