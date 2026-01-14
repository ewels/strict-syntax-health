# Nextflow lint results

- Generated: 2026-01-14T09:10:26.140542642Z
- Nextflow version: 25.12.0-edge
- Summary: 15 errors

## :x: Errors

- Error: `conf/base.config:15:12`: `check_max` is not defined

  ```nextflow
    cpus = { check_max( 1 * task.attempt, 'cpus' ) }
             ^^^^^^^^^
  ```

- Error: `conf/base.config:16:14`: `check_max` is not defined

  ```nextflow
    memory = { check_max( 7.GB * task.attempt, 'memory' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:17:12`: `check_max` is not defined

  ```nextflow
    time = { check_max( 4.h * task.attempt, 'time' ) }
             ^^^^^^^^^
  ```

- Error: `conf/base.config:25:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 2 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:26:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 14.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:27:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 6.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:30:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 6 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:31:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 42.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:32:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 8.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:35:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 12 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:36:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 84.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:37:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 10.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:40:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 20.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `main.nf:254:39`: Unexpected input: 'into'

  ```nextflow
      file 'software_versions_mqc.yaml' into ch_software_versions_yaml
                                        ^
  ```

- Error: `nextflow.config:88:3`: Unexpected input: 'includeConfig'

  ```nextflow
    includeConfig "${params.custom_config_base}/nfcore_custom.config"
    ^
  ```
