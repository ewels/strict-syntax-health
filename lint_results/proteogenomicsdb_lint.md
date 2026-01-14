# Nextflow lint results

- Generated: 2026-01-14T09:23:01.809276055Z
- Nextflow version: 25.12.0-edge
- Summary: 15 errors

## :x: Errors

- Error: `conf/base.config:14:12`: `check_max` is not defined

  ```nextflow
    cpus = { check_max( 1 * task.attempt, 'cpus' ) }
             ^^^^^^^^^
  ```

- Error: `conf/base.config:15:14`: `check_max` is not defined

  ```nextflow
    memory = { check_max( 7.GB * task.attempt, 'memory' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:16:12`: `check_max` is not defined

  ```nextflow
    time = { check_max( 4.h * task.attempt, 'time' ) }
             ^^^^^^^^^
  ```

- Error: `conf/base.config:28:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 2 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:29:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 6.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:30:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 6.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:33:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 6 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:34:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 12.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:35:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 8.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:38:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 12 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:39:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 32.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:40:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 10.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:43:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 20.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `main.nf:134:39`: Unexpected input: 'into'

  ```nextflow
      file 'software_versions_mqc.yaml' into ch_software_versions_yaml
                                        ^
  ```

- Error: `nextflow.config:118:3`: Unexpected input: 'includeConfig'

  ```nextflow
    includeConfig "${params.custom_config_base}/nfcore_custom.config"
    ^
  ```
