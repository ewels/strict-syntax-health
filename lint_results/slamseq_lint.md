# Nextflow lint results

- Generated: 2026-01-14T09:26:09.523447450Z
- Nextflow version: 25.12.0-edge
- Summary: 17 errors

## :x: Errors

- Error: `conf/base.config:14:12`: `check_max` is not defined

  ```nextflow
    cpus = { check_max( 1 * task.attempt, 'cpus' ) }
             ^^^^^^^^^
  ```

- Error: `conf/base.config:15:14`: `check_max` is not defined

  ```nextflow
    memory = { check_max( 8.GB * task.attempt, 'memory' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:16:12`: `check_max` is not defined

  ```nextflow
    time = { check_max( 2.h * task.attempt, 'time' ) }
             ^^^^^^^^^
  ```

- Error: `conf/base.config:24:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 10.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:25:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 8.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:29:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 4 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:30:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 10.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:31:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 2.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:34:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 14 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:35:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 30.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:36:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 8.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:40:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 10.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:41:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 8.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:45:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 1.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:46:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 1.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `main.nf:98:24`: Unexpected input: 'from'

  ```nextflow
              file fasta from fastaGunzipChannel
                         ^
  ```

- Error: `nextflow.config:69:3`: Unexpected input: 'includeConfig'

  ```nextflow
    includeConfig "${params.custom_config_base}/nfcore_custom.config"
    ^
  ```
