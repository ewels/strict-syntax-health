# Nextflow lint results

- Generated: 2026-01-14T09:20:56.307153317Z
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

- Error: `conf/base.config:24:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 2 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:25:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 14.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:26:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 6.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:29:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 6 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:30:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 42.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:31:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 8.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:34:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 12 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:35:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 84.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:36:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 16.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:39:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 20.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `main.nf:282:17`: Unexpected input: 'from'

  ```nextflow
      file design from ch_input
                  ^
  ```

- Error: `nextflow.config:97:3`: Unexpected input: 'includeConfig'

  ```nextflow
    includeConfig "${params.custom_config_base}/nfcore_custom.config"
    ^
  ```
