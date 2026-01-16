# Nextflow lint results

- Generated: 2026-01-16T06:31:12.832129861Z
- Nextflow version: 25.12.0-edge
- Summary: 69 errors, 80 warnings

## :x: Errors

- Error: `main.nf:19:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/diseasemodulediscovery/subworkflows/local/utils_nfcore_diseasemodulediscovery_pipeline/main.nf'

  ```nextflow
  include { PIPELINE_INITIALISATION } from './subworkflows/local/utils_nfcore_diseasemodulediscovery_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:20:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/diseasemodulediscovery/subworkflows/local/utils_nfcore_diseasemodulediscovery_pipeline/main.nf'

  ```nextflow
  include { PIPELINE_COMPLETION     } from './subworkflows/local/utils_nfcore_diseasemodulediscovery_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:60:5`: Workflow emit `multiqc_report` is already declared

  ```nextflow
      multiqc_report                  = DISEASEMODULEDISCOVERY.out.multiqc_report                // channel: /path/to/multiqc_report.html
      ^^^^^^^^^^^^^^
  ```

- Error: `main.nf:76:5`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
      PIPELINE_INITIALISATION (
      ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:96:36`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
      NFCORE_DISEASEMODULEDISCOVERY (PIPELINE_INITIALISATION.out.seeds, PIPELINE_INITIALISATION.out.network, PIPELINE_INITIALISATION.out.shortest_paths, PIPELINE_INITIALISATION.out.perturbed_networks)
                                     ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:96:71`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
      NFCORE_DISEASEMODULEDISCOVERY (PIPELINE_INITIALISATION.out.seeds, PIPELINE_INITIALISATION.out.network, PIPELINE_INITIALISATION.out.shortest_paths, PIPELINE_INITIALISATION.out.perturbed_networks)
                                                                        ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:96:108`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
      NFCORE_DISEASEMODULEDISCOVERY (PIPELINE_INITIALISATION.out.seeds, PIPELINE_INITIALISATION.out.network, PIPELINE_INITIALISATION.out.shortest_paths, PIPELINE_INITIALISATION.out.perturbed_networks)
                                                                                                             ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:96:152`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
      NFCORE_DISEASEMODULEDISCOVERY (PIPELINE_INITIALISATION.out.seeds, PIPELINE_INITIALISATION.out.network, PIPELINE_INITIALISATION.out.shortest_paths, PIPELINE_INITIALISATION.out.perturbed_networks)
                                                                                                                                                         ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:101:5`: `PIPELINE_COMPLETION` is not defined

  ```nextflow
      PIPELINE_COMPLETION (
      ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/graphtoolparser/main.nf:6:36`: Unexpected input: ','

  ```nextflow
      tuple val(meta), (path(network), stageAs: 'input/*')
                                     ^
  ```

- Error: `modules/local/inputcheck/main.nf:6:35`: Unexpected input: ','

  ```nextflow
      tuple val(meta ), (path(seeds), stageAs: 'check/*'), (path(network), stageAs: 'check/*')
                                    ^
  ```

- Error: `modules/local/networkannotation/main.nf:6:39`: Unexpected input: ','

  ```nextflow
      tuple val(meta), (path(subnetwork), stageAs: 'input/*'), (path (network), stageAs: 'input/*')
                                        ^
  ```

- Error: `subworkflows/local/gt_diamond/main.nf:5:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/diseasemodulediscovery/modules/local/graphtoolparser/main.nf'

  ```nextflow
  include { GRAPHTOOLPARSER   } from '../../../modules/local/graphtoolparser/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_diamond/main.nf:20:5`: `GRAPHTOOLPARSER` is not defined

  ```nextflow
      GRAPHTOOLPARSER(ch_network, "diamond")                                  // Convert gt file to diamond specific format
      ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_diamond/main.nf:21:35`: `GRAPHTOOLPARSER` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(GRAPHTOOLPARSER.out.versions)             // Collect versions
                                    ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_diamond/main.nf:26:18`: `GRAPHTOOLPARSER` is not defined

  ```nextflow
          .combine(GRAPHTOOLPARSER.out.network.map{ meta, network -> [meta.network_id, meta, network]}, by: 0)
                   ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_domino/main.nf:6:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/diseasemodulediscovery/modules/local/graphtoolparser/main.nf'

  ```nextflow
  include { GRAPHTOOLPARSER   } from '../../../modules/local/graphtoolparser/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_domino/main.nf:22:5`: `GRAPHTOOLPARSER` is not defined

  ```nextflow
      GRAPHTOOLPARSER(ch_network, "domino")                                   // Convert gt file to domino specific format, including prefixes
      ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_domino/main.nf:23:35`: `GRAPHTOOLPARSER` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(GRAPHTOOLPARSER.out.versions)             // Collect versions
                                    ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_domino/main.nf:25:19`: `GRAPHTOOLPARSER` is not defined

  ```nextflow
      DOMINO_SLICER(GRAPHTOOLPARSER.out.network)                              // Run the DOMINO preprocessing step on the parsed networks
                    ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_domino/main.nf:28:25`: `GRAPHTOOLPARSER` is not defined

  ```nextflow
      ch_domino_network = GRAPHTOOLPARSER.out.network
                          ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_networkperturbation/main.nf:108:18`: Unexpected input: '->'

  ```nextflow
              item -> "  " + item.text,
                   ^
  ```

- Error: `subworkflows/local/gt_robust/main.nf:5:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/diseasemodulediscovery/modules/local/graphtoolparser/main.nf'

  ```nextflow
  include { GRAPHTOOLPARSER   } from '../../../modules/local/graphtoolparser/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_robust/main.nf:18:5`: `GRAPHTOOLPARSER` is not defined

  ```nextflow
      GRAPHTOOLPARSER(ch_network, "robust")
      ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_robust/main.nf:19:35`: `GRAPHTOOLPARSER` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(GRAPHTOOLPARSER.out.versions)
                                    ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_robust/main.nf:24:18`: `GRAPHTOOLPARSER` is not defined

  ```nextflow
          .combine(GRAPHTOOLPARSER.out.network.map{ meta, network -> [meta.network_id, meta, network]}, by: 0)
                   ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_robust_bias_aware/main.nf:5:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/diseasemodulediscovery/modules/local/graphtoolparser/main.nf'

  ```nextflow
  include { GRAPHTOOLPARSER   } from '../../../modules/local/graphtoolparser/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_robust_bias_aware/main.nf:18:5`: `GRAPHTOOLPARSER` is not defined

  ```nextflow
      GRAPHTOOLPARSER(ch_network, "robust")
      ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_robust_bias_aware/main.nf:19:35`: `GRAPHTOOLPARSER` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(GRAPHTOOLPARSER.out.versions)
                                    ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_robust_bias_aware/main.nf:26:18`: `GRAPHTOOLPARSER` is not defined

  ```nextflow
          .combine(GRAPHTOOLPARSER.out.network.map{ meta, network -> [meta.network_id, meta, network]}, by: 0)
                   ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_rwr/main.nf:5:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/diseasemodulediscovery/modules/local/graphtoolparser/main.nf'

  ```nextflow
  include { GRAPHTOOLPARSER   } from '../../../modules/local/graphtoolparser/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_rwr/main.nf:20:5`: `GRAPHTOOLPARSER` is not defined

  ```nextflow
      GRAPHTOOLPARSER(ch_network, "rwr")                                      // Convert gt file to rwr specific format
      ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_rwr/main.nf:21:35`: `GRAPHTOOLPARSER` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(GRAPHTOOLPARSER.out.versions)             // Collect versions
                                    ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_rwr/main.nf:26:18`: `GRAPHTOOLPARSER` is not defined

  ```nextflow
          .combine(GRAPHTOOLPARSER.out.network.map{ meta, network -> [meta.network_id, meta, network]}, by: 0)
                   ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/gt_seedperturbation/main.nf:118:18`: Unexpected input: '->'

  ```nextflow
              item -> "  " + item.text,
                   ^
  ```

- Error: `subworkflows/local/utils_nfcore_diseasemodulediscovery_pipeline/main.nf:357:36`: Unexpected input: '='

  ```nextflow
          logWarnings(monochrome_logs=monochrome_logs, seeds_empty=seeds_empty, module_empty=module_empty, visualization_skipped=visualization_skipped, drugstone_skipped=drugstone_skipped)
                                     ^
  ```

- Error: `workflows/diseasemodulediscovery.nf:10:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/diseasemodulediscovery/modules/local/inputcheck/main.nf'

  ```nextflow
  include { INPUTCHECK                        } from '../modules/local/inputcheck/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:11:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/diseasemodulediscovery/modules/local/graphtoolparser/main.nf'

  ```nextflow
  include { GRAPHTOOLPARSER                   } from '../modules/local/graphtoolparser/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:12:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/diseasemodulediscovery/modules/local/networkannotation/main.nf'

  ```nextflow
  include { NETWORKANNOTATION                 } from '../modules/local/networkannotation/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:30:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/diseasemodulediscovery/subworkflows/local/gt_seedperturbation/main.nf'

  ```nextflow
  include { GT_SEEDPERTURBATION    } from '../subworkflows/local/gt_seedperturbation/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:31:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/diseasemodulediscovery/subworkflows/local/gt_networkperturbation/main.nf'

  ```nextflow
  include { GT_NETWORKPERTURBATION } from '../subworkflows/local/gt_networkperturbation/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:34:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/diseasemodulediscovery/subworkflows/local/utils_nfcore_diseasemodulediscovery_pipeline/main.nf'

  ```nextflow
  include { readTsvAsListOfMaps   } from '../subworkflows/local/utils_nfcore_diseasemodulediscovery_pipeline/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:50:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/diseasemodulediscovery/subworkflows/local/utils_nfcore_diseasemodulediscovery_pipeline/main.nf'

  ```nextflow
  include { methodsDescriptionText } from '../subworkflows/local/utils_nfcore_diseasemodulediscovery_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:51:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/diseasemodulediscovery/subworkflows/local/utils_nfcore_diseasemodulediscovery_pipeline/main.nf'

  ```nextflow
  include { multiqcTsvFromList     } from '../subworkflows/local/utils_nfcore_diseasemodulediscovery_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:137:5`: `GRAPHTOOLPARSER` is not defined

  ```nextflow
      GRAPHTOOLPARSER(ch_network, 'gt')
      ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:138:35`: `GRAPHTOOLPARSER` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(GRAPHTOOLPARSER.out.versions)
                                    ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:139:26`: `GRAPHTOOLPARSER` is not defined

  ```nextflow
      ch_network_multiqc = GRAPHTOOLPARSER.out.multiqc
                           ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:148:21`: `GRAPHTOOLPARSER` is not defined

  ```nextflow
      ch_network_gt = GRAPHTOOLPARSER.out.network
                      ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:158:5`: `INPUTCHECK` is not defined

  ```nextflow
      INPUTCHECK(ch_seeds_network)
      ^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:159:16`: `INPUTCHECK` is not defined

  ```nextflow
      ch_seeds = INPUTCHECK.out.seeds
                 ^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:160:24`: `INPUTCHECK` is not defined

  ```nextflow
      ch_seeds_multiqc = INPUTCHECK.out.multiqc
                         ^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:173:15`: `INPUTCHECK` is not defined

  ```nextflow
          .join(INPUTCHECK.out.seeds.map{ meta, seeds -> [meta.id, seeds]}, by: 0, remainder: true)
                ^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:178:18`: `INPUTCHECK` is not defined

  ```nextflow
      ch_modules = INPUTCHECK.out.seeds_module
                   ^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:216:35`: `readTsvAsListOfMaps` is not defined

  ```nextflow
          .map{meta, path -> [meta, readTsvAsListOfMaps(path)]}.transpose() // Parse topology information from tsv file
                                    ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:232:5`: `NETWORKANNOTATION` is not defined

  ```nextflow
      NETWORKANNOTATION(ch_module_network)
      ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:233:18`: `NETWORKANNOTATION` is not defined

  ```nextflow
      ch_modules = NETWORKANNOTATION.out.module
                   ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:234:35`: `NETWORKANNOTATION` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(NETWORKANNOTATION.out.versions)
                                    ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:264:13`: `multiqcTsvFromList` is not defined

  ```nextflow
              multiqcTsvFromList(tsv_data, header)
              ^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:295:17`: `multiqcTsvFromList` is not defined

  ```nextflow
                  multiqcTsvFromList(tsv_data, header)
                  ^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:328:17`: `multiqcTsvFromList` is not defined

  ```nextflow
                  multiqcTsvFromList(tsv_data, header)
                  ^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:475:13`: `GT_SEEDPERTURBATION` is not defined

  ```nextflow
              GT_SEEDPERTURBATION(
              ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:480:43`: `GT_SEEDPERTURBATION` is not defined

  ```nextflow
              ch_versions = ch_versions.mix(GT_SEEDPERTURBATION.out.versions)
                                            ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:482:22`: `GT_SEEDPERTURBATION` is not defined

  ```nextflow
                  .mix(GT_SEEDPERTURBATION.out.multiqc_summary)
                       ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:483:22`: `GT_SEEDPERTURBATION` is not defined

  ```nextflow
                  .mix(GT_SEEDPERTURBATION.out.multiqc_jaccard)
                       ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:488:13`: `GT_NETWORKPERTURBATION` is not defined

  ```nextflow
              GT_NETWORKPERTURBATION(
              ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:494:43`: `GT_NETWORKPERTURBATION` is not defined

  ```nextflow
              ch_versions = ch_versions.mix(GT_NETWORKPERTURBATION.out.versions)
                                            ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:496:22`: `GT_NETWORKPERTURBATION` is not defined

  ```nextflow
                  .mix(GT_NETWORKPERTURBATION.out.multiqc_summary)
                       ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:497:22`: `GT_NETWORKPERTURBATION` is not defined

  ```nextflow
                  .mix(GT_NETWORKPERTURBATION.out.multiqc_jaccard)
                       ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/diseasemodulediscovery.nf:617:9`: `methodsDescriptionText` is not defined

  ```nextflow
          methodsDescriptionText(ch_multiqc_custom_methods_description))
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `main.nf:40:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/gt_biopax/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()                                           // For collecting tool versions
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/gt_biopax/main.nf:24:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          module = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/gt_diamond/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()                                           // For collecting tool versions
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/gt_diamond/main.nf:27:14`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{network_id, seeds_meta, seeds, network_meta, network ->
               ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/gt_domino/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()                                           // For collecting tool versions
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/gt_domino/main.nf:35:14`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{network_id, seeds_meta, seeds, network_meta, network, slices ->
               ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/gt_firstneighbor/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/gt_firstneighbor/main.nf:20:14`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{network_id, seeds_meta, seeds, network_meta, network ->
               ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/gt_proximity/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/gt_proximity/main.nf:21:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              no_sp: it[2].name == "NO_FILE"
                     ^^
  ```

- Warning: `subworkflows/local/gt_proximity/main.nf:27:63`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      SHORTEST_PATHS(ch_shortest_paths.no_sp.map{meta, network, sp -> [meta, network]})
                                                                ^^
  ```

- Warning: `subworkflows/local/gt_proximity/main.nf:39:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .multiMap{network_id, meta, module, network, sp ->
                    ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/gt_robust/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/gt_robust/main.nf:25:14`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{network_id, seeds_meta, seeds, network_meta, network ->
               ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/gt_robust_bias_aware/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/gt_robust_bias_aware/main.nf:27:14`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{network_id, seeds_meta, seeds, network_meta, network ->
               ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/gt_rwr/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()                                           // For collecting tool versions
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/gt_rwr/main.nf:27:14`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{network_id, seeds_meta, seeds, network_meta, network ->
               ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/networkexpansion/main.nf:21:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      diamond_n = Channel.value(params.diamond_n)
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/networkexpansion/main.nf:22:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      diamond_alpha = Channel.value(params.diamond_alpha)
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/networkexpansion/main.nf:24:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      rwr_scaling = Channel.value(params.rwr_scaling).map{it ? 1 : 0}
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/networkexpansion/main.nf:24:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      rwr_scaling = Channel.value(params.rwr_scaling).map{it ? 1 : 0}
                                                          ^^
  ```

- Warning: `subworkflows/local/networkexpansion/main.nf:25:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      rwr_symmetrical = Channel.value(params.rwr_symmetrical).map{it ? 1 : 0}
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/networkexpansion/main.nf:25:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      rwr_symmetrical = Channel.value(params.rwr_symmetrical).map{it ? 1 : 0}
                                                                  ^^
  ```

- Warning: `subworkflows/local/networkexpansion/main.nf:26:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      rwr_r = Channel.value(params.rwr_r)
              ^^^^^^^
  ```

- Warning: `subworkflows/local/networkexpansion/main.nf:28:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      id_space = Channel.value(params.id_space)
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/networkexpansion/main.nf:31:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/networkexpansion/main.nf:32:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_modules  = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/networkexpansion/main.nf:33:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_raw_modules = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/networkexpansion/main.nf:76:14`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{seeds_id, network_id, meta, module, seeds ->
               ^^^^^^^^
  ```

- Warning: `subworkflows/local/networkexpansion/main.nf:76:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{seeds_id, network_id, meta, module, seeds ->
                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/networkexpansion/main.nf:86:14`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{network_id, meta, module, seeds, network ->
               ^^^^^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:121:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      id_space = Channel.value(params.id_space)
                 ^^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:122:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      validate_online = Channel.value(params.validate_online)
                        ^^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:129:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:130:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:131:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_seeds_empty_status = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:132:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_module_empty_status = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:133:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_visualization_skipped_status = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:134:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_drugstone_skipped_status = Channel.empty()
                                    ^^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:140:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, path -> path }
                ^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:156:14`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{key, meta, seeds, network -> [meta, seeds, network]}
               ^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:161:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, path -> path }
                ^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:172:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{meta, seeds, network -> meta.id}
                     ^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:172:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{meta, seeds, network -> meta.id}
                            ^^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:204:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, path -> path }
                ^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:230:14`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{newtork_id, meta, module, network -> [meta, module, network]}
               ^^^^^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:240:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter{meta, module -> meta.nodes > 0} // Filter out empty modules
                        ^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:246:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch{ meta, module ->
                         ^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:254:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .mix(ch_modules_empty_not_empty.empty.map {meta, module -> [meta.id, true] })
                                                           ^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:255:62`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .mix(ch_modules_empty_not_empty.not_empty.map {meta, module -> [meta.id, false] })
                                                               ^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:260:21`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map {meta, module -> "$meta.id\t$meta.nodes" }
                      ^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:278:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch {meta, module ->
                             ^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:285:57`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .mix(ch_visualization_input.fail.map {meta, module -> [meta.id, true] })
                                                          ^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:286:57`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .mix(ch_visualization_input.pass.map {meta, module -> [meta.id, false] })
                                                          ^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:291:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map {meta, module -> "$meta.id\t$meta.nodes" }
                          ^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:311:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch {meta, module ->
                             ^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:318:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .mix(ch_drugstone_export_input.fail.map {meta, module -> [meta.id, true] })
                                                         ^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:319:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .mix(ch_drugstone_export_input.pass.map {meta, module -> [meta.id, false] })
                                                         ^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:324:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map {meta, module -> "$meta.id\t$meta.nodes" }
                          ^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:340:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ meta, path -> path }
                    ^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:394:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .multiMap{key, meta, nodes, network ->
                            ^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:416:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .multiMap{key, meta, nodes, network ->
                            ^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:425:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      .map{ meta, path -> path }
                            ^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:438:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      .filter{ meta, nodes -> meta.amim != "no_tool" } // Filter out no_tool modules
                                     ^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:441:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      .multiMap{key, meta, nodes, network ->
                                ^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:450:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      .map{ meta, path -> path }
                            ^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:476:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ch_modules.filter{ meta, path -> meta.amim != "no_tool" }, // Filter out no_tool modules
                                           ^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:489:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ch_modules.filter{ meta, path -> meta.amim != "no_tool" }, // Filter out no_tool modules
                                           ^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:513:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_algorithms_drugs = Channel
                                ^^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:523:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch {meta, module ->
                             ^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:537:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          includeIndirectDrugs = Channel.value(params.includeIndirectDrugs).map{it ? 1 : 0}
                                 ^^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:537:79`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          includeIndirectDrugs = Channel.value(params.includeIndirectDrugs).map{it ? 1 : 0}
                                                                                ^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:538:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          includeNonApprovedDrugs = Channel.value(params.includeNonApprovedDrugs).map{it ? 1 : 0}
                                    ^^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:538:85`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          includeNonApprovedDrugs = Channel.value(params.includeNonApprovedDrugs).map{it ? 1 : 0}
                                                                                      ^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:545:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map{ meta, algorithm, drug_predictions -> [meta, drug_predictions] }
                              ^^^^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:546:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .filter{ meta, drug_predictions -> meta.nodes <= params.visualization_max_nodes }       // Filter out modules with too many nodes
                                 ^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:549:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map{module_id, meta, drug_predictions, module -> [meta, module, drug_predictions] }    // Format for visualization
                       ^^^^^^^^^
  ```

- Warning: `workflows/diseasemodulediscovery.nf:569:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel.topic("versions")
                           ^^^^^^^
  ```
