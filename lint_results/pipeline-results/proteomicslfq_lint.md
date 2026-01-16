# Nextflow lint results

- Generated: 2026-01-16T06:37:41.198501844Z
- Nextflow version: 25.12.0-edge
- Summary: 36 errors

## :x: Errors

- Error: `conf/base.config:14:12`: `check_max` is not defined

  ```nextflow
    cpus = { check_max( 2 * task.attempt, 'cpus' ) }
             ^^^^^^^^^
  ```

- Error: `conf/base.config:15:14`: `check_max` is not defined

  ```nextflow
    memory = { check_max( 8.GB * task.attempt, 'memory' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:16:12`: `check_max` is not defined

  ```nextflow
    time = { check_max( 4.h * task.attempt, 'time' ) }
             ^^^^^^^^^
  ```

- Error: `conf/base.config:30:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 2 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:31:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 6.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:32:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 3.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:35:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 4 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:36:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 10.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:37:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 6.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:40:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 8 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:41:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 32.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:42:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 8.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:45:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 12 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:46:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 64.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:47:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 10.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:50:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 20.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/base.config:53:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 1 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `conf/big-nodes.config:17:12`: `check_max` is not defined

  ```nextflow
    cpus = { check_max( 2 * task.attempt, 'cpus' ) }
             ^^^^^^^^^
  ```

- Error: `conf/big-nodes.config:18:14`: `check_max` is not defined

  ```nextflow
    memory = { check_max( 8.GB * task.attempt, 'memory' ) }
               ^^^^^^^^^
  ```

- Error: `conf/big-nodes.config:19:12`: `check_max` is not defined

  ```nextflow
    time = { check_max( 4.h * task.attempt, 'time' ) }
             ^^^^^^^^^
  ```

- Error: `conf/big-nodes.config:28:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 2 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `conf/big-nodes.config:29:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 6.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/big-nodes.config:30:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 3.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/big-nodes.config:33:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 4 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `conf/big-nodes.config:34:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 32.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/big-nodes.config:35:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 6.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/big-nodes.config:38:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 8 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `conf/big-nodes.config:39:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 64.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/big-nodes.config:40:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 8.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/big-nodes.config:43:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 12 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `conf/big-nodes.config:44:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 100.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/big-nodes.config:45:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 10.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/big-nodes.config:48:14`: `check_max` is not defined

  ```nextflow
      time = { check_max( 20.h * task.attempt, 'time' ) }
               ^^^^^^^^^
  ```

- Error: `conf/big-nodes.config:51:14`: `check_max` is not defined

  ```nextflow
      cpus = { check_max( 1 * task.attempt, 'cpus' ) }
               ^^^^^^^^^
  ```

- Error: `main.nf:143:18`: Unexpected input: 'from'

  ```nextflow
         file sdrf from ch_sdrf
                   ^
  ```

- Error: `nextflow.config:152:3`: Unexpected input: 'includeConfig'

  ```nextflow
    includeConfig "${params.custom_config_base}/nfcore_custom.config"
    ^
  ```
