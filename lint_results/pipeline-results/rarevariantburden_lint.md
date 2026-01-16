# Nextflow lint results

- Generated: 2026-01-16T10:27:07.757239844Z
- Nextflow version: 25.12.0-edge
- Summary: 33 errors, 22 warnings

## :x: Errors

- Error: `conf/test.config:21:1`: Variable declarations cannot be mixed with config statements

  ```nextflow
  def caseRoot = params.pipelines_testdata_base_path + "rarevariantburden/case"
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test.config:32:23`: `caseRoot` is not defined

  ```nextflow
      caseJointVCF = "${caseRoot}/samples.1KG.chr21-22.vcf.gz"
                        ^^^^^^^^
  ```

- Error: `conf/test.config:33:21`: `caseRoot` is not defined

  ```nextflow
      caseSample = "${caseRoot}/samples.txt"
                      ^^^^^^^^
  ```

- Error: `conf/test.config:49:35`: `caseRoot` is not defined

  ```nextflow
      caseAnnotatedVCFFileList = "${caseRoot}/annotationFiles.csv"
                                    ^^^^^^^^
  ```

- Error: `conf/test.config:51:36`: `caseRoot` is not defined

  ```nextflow
      caseAnnotationGDSFileList = "${caseRoot}/annotationGDSFiles.csv"
                                     ^^^^^^^^
  ```

- Error: `conf/test.config:53:34`: `caseRoot` is not defined

  ```nextflow
      caseGenotypeGDSFileList = "${caseRoot}/genotypeGDSFiles.csv"
                                   ^^^^^^^^
  ```

- Error: `conf/test.config:55:25`: `caseRoot` is not defined

  ```nextflow
      casePopulation = "${caseRoot}/casePopulation.txt"
                          ^^^^^^^^
  ```

- Error: `main.nf:104:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  workflow.onComplete {
  ^
  ```

- Error: `modules/local/cocorv/main.nf:6:5`: Invalid process directive

  ```nextflow
      ext.singularity_pull_docker_container = true
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/cocorv/main.nf:33:5`: Invalid process directive

  ```nextflow
      ext.singularity_pull_docker_container = true
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/cocorv/main.nf:56:5`: Invalid process directive

  ```nextflow
      ext.singularity_pull_docker_container = true
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/cocorv/main.nf:81:5`: Invalid process directive

  ```nextflow
      ext.singularity_pull_docker_container = true
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/cocorv/main.nf:103:5`: Invalid process directive

  ```nextflow
      ext.singularity_pull_docker_container = true
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/cocorv/main.nf:136:5`: Invalid process directive

  ```nextflow
      ext.singularity_pull_docker_container = true
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/cocorv/main.nf:206:5`: Invalid process directive

  ```nextflow
      ext.singularity_pull_docker_container = true
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/cocorv/main.nf:228:5`: Invalid process directive

  ```nextflow
      ext.singularity_pull_docker_container = true
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/cocorv/main.nf:253:5`: Invalid process directive

  ```nextflow
      ext.singularity_pull_docker_container = true
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/cocorv/main.nf:278:5`: Invalid process directive

  ```nextflow
      ext.singularity_pull_docker_container = true
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/cocorv/main.nf:301:5`: Invalid process directive

  ```nextflow
      ext.singularity_pull_docker_container = true
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/cocorv/main.nf:322:5`: Invalid process directive

  ```nextflow
      ext.singularity_pull_docker_container = true
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/cocorv/main.nf:352:5`: Invalid process directive

  ```nextflow
      ext.singularity_pull_docker_container = true
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/cocorv/main.nf:374:5`: Invalid process directive

  ```nextflow
      ext.singularity_pull_docker_container = true
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/cocorv/main.nf:480:5`: Invalid process directive

  ```nextflow
      ext.singularity_pull_docker_container = true
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/cocorv/main.nf:522:5`: Invalid process directive

  ```nextflow
      ext.singularity_pull_docker_container = true
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/cocorv/main.nf:552:5`: Invalid process directive

  ```nextflow
      ext.singularity_pull_docker_container = true
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/cocorv/main.nf:585:5`: Invalid process directive

  ```nextflow
      ext.singularity_pull_docker_container = true
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/cocorv/main.nf:612:5`: Invalid process directive

  ```nextflow
      ext.singularity_pull_docker_container = true
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:337:41`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/rarevariantburden ${manifest.version}\033[0m
                                          ^^^^^^^^
  ```

- Error: `nextflow.config:340:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:340:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:340:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:349:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:350:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `main.nf:159:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          it.name.matches(pattern.replace('*', '.*'))
                          ^^
  ```

- Warning: `main.nf:161:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          it.copyTo("${destDir}/${it.name}")
                          ^^
  ```

- Warning: `main.nf:161:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          it.copyTo("${destDir}/${it.name}")
                                                  ^^
  ```

- Warning: `main.nf:162:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          log.info "✓ Copied ${it.name} to ${destDir}"
                                               ^^
  ```

- Warning: `nextflow.config:340:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rarevariantburden_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/rarevariantburden.nf:39:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      caseJointVCF // caseJointVCF read in from --caseJointVCF
      ^^^^^^^^^^^^
  ```

- Warning: `workflows/rarevariantburden.nf:40:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      caseSample // caseSample read in from --caseSample
      ^^^^^^^^^^
  ```

- Warning: `workflows/rarevariantburden.nf:46:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          intersectChannel = Channel.value(params.controlBed)
                             ^^^^^^^
  ```

- Warning: `workflows/rarevariantburden.nf:54:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      chromChannel = Channel.fromList(Arrays.asList(chromosomes))
                     ^^^^^^^
  ```

- Warning: `workflows/rarevariantburden.nf:65:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          caseVCF_ch = Channel
                       ^^^^^^^
  ```

- Warning: `workflows/rarevariantburden.nf:76:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              normalizeQCChannel = Channel
                                   ^^^^^^^
  ```

- Warning: `workflows/rarevariantburden.nf:103:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          annotateChannel = Channel
                            ^^^^^^^
  ```

- Warning: `workflows/rarevariantburden.nf:120:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          caseGenotypeGDSChannel = Channel
                                   ^^^^^^^
  ```

- Warning: `workflows/rarevariantburden.nf:126:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          caseAnnotationGDSChannel = Channel
                                     ^^^^^^^
  ```

- Warning: `workflows/rarevariantburden.nf:152:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          populationChannel = Channel.value(params.casePopulation)
                              ^^^^^^^
  ```

- Warning: `workflows/rarevariantburden.nf:158:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      controlGenotypeGDSChannel = Channel
                                  ^^^^^^^
  ```

- Warning: `workflows/rarevariantburden.nf:163:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      controlAnnotationGDSChannel = Channel
                                    ^^^^^^^
  ```

- Warning: `workflows/rarevariantburden.nf:191:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      mergeCoCoRVResults(cocorvOutChannel.map{it[1]}.collect(), cocorvOutChannel.map{it[2]}.collect(),
                                              ^^
  ```

- Warning: `workflows/rarevariantburden.nf:191:84`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      mergeCoCoRVResults(cocorvOutChannel.map{it[1]}.collect(), cocorvOutChannel.map{it[2]}.collect(),
                                                                                     ^^
  ```

- Warning: `workflows/rarevariantburden.nf:192:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          cocorvOutChannel.map{it[3]}.collect())
                               ^^
  ```
