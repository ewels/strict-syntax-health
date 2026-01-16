# Nextflow lint results

- Generated: 2026-01-16T10:27:02.409002370Z
- Nextflow version: 25.12.0-edge
- Summary: 30 errors, 55 warnings

## :x: Errors

- Error: `modules/nf-core/bcftools/view/main.nf:60:9`: `index` is already declared

  ```nextflow
      def index = args.contains("--write-index=tbi") || args.contains("-W=tbi") ? "tbi" :
          ^^^^^
  ```

- Error: `modules/nf-core/bwa/index/main.nf:14:27`: `bwa` is not defined

  ```nextflow
      tuple val(meta), path(bwa) , emit: index
                            ^^^
  ```

- Error: `modules/nf-core/cnvnator/cnvnator/main.nf:59:9`: `calls_cmd` is already declared

  ```nextflow
      def calls_cmd = args.contains("-call") ? "touch ${prefix}.tab" : ''
          ^^^^^^^^^
  ```

- Error: `modules/nf-core/eklipse/main.nf:28:9`: `ref_gb` is already declared

  ```nextflow
      def ref_gb = ref_gb ? "$ref_gb" : "/usr/local/bin/data/NC_012920.1.gb"
          ^^^^^^
  ```

- Error: `modules/nf-core/picard/renamesampleinvcf/main.nf:23:62`: `$args` is not defined

  ```nextflow
      def extended_args = args.contains("--NEW_SAMPLE_NAME") ? $args : "${args} --NEW_SAMPLE_NAME ${meta.id}"
                                                               ^^^^^
  ```

- Error: `modules/nf-core/sentieon/bwaindex/tests/nextflow.config:3:24`: `$SENTIEON_LICSRVR_IP` is not defined

  ```nextflow
      SENTIEON_LICENSE = $SENTIEON_LICSRVR_IP
                         ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/bwaindex/tests/nextflow.config:5:26`: `$SENTIEON_AUTH_MECH` is not defined

  ```nextflow
      SENTIEON_AUTH_MECH = $SENTIEON_AUTH_MECH
                           ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/bwamem/tests/nextflow.config:3:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/bwamem/tests/nextflow.config:5:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/bwamem/tests/nextflow_out_cram.config:3:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/bwamem/tests/nextflow_out_cram.config:5:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/datametrics/tests/nextflow.config:3:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/datametrics/tests/nextflow.config:5:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/dedup/tests/nextflow.config:3:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/dedup/tests/nextflow.config:5:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/dedup/tests/nextflow_rmdup.config:3:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/dedup/tests/nextflow_rmdup.config:5:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/dnamodelapply/tests/nextflow.config:3:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/dnamodelapply/tests/nextflow.config:5:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/dnascope/tests/nextflow.config:3:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/dnascope/tests/nextflow.config:5:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/readwriter/tests/nextflow.config:3:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/readwriter/tests/nextflow.config:5:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/readwriter/tests/nextflow_outputcram.config:3:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/readwriter/tests/nextflow_outputcram.config:5:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/wgsmetrics/tests/nextflow.config:3:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/wgsmetrics/tests/nextflow.config:5:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/call_snv.nf:112:54`: `run_mt_for_wes` is not defined

  ```nextflow
          if (val_analysis_type.matches("wgs|mito") || run_mt_for_wes) {
                                                       ^^^^^^^^^^^^^^
  ```

- Error: `tests/nextflow.config:28:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/raredisease.nf:771:23`: `analysis_type` is not defined

  ```nextflow
      if (!skip_gens && analysis_type.equals("wgs")) {
                        ^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/bcftools/merge/main.nf:28:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input = (vcfs.collect().size() > 1) ? vcfs.sort{ it.name } : vcfs
                                                           ^^
  ```

- Warning: `modules/nf-core/bcftools/norm/main.nf:56:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          if (['--write-index=tbi', '-W=tbi'].any { args.contains(it) }  && extension == 'vcf.gz') {
                                                                  ^^
  ```

- Warning: `modules/nf-core/bcftools/norm/main.nf:58:126`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          } else if (['--write-index=tbi', '-W=tbi', '--write-index=csi', '-W=csi', '--write-index', '-W'].any { args.contains(it) }) {
                                                                                                                               ^^
  ```

- Warning: `modules/nf-core/bwa/mem/main.nf:56:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bwa/mem/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def samtools_command = sort_bam ? 'sort' : 'view'
          ^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/bwamem2/mem/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bwamem2/mem/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def samtools_command = sort_bam ? 'sort' : 'view'
          ^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/bwamem2/mem/main.nf:66:9`: Variable was declared but not used

  ```nextflow
      def reference = fasta && extension=="cram"  ? "--reference ${fasta}" : ""
          ^^^^^^^^^
  ```

- Warning: `modules/nf-core/bwameme/mem/main.nf:75:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bwameme/mem/main.nf:78:9`: Variable was declared but not used

  ```nextflow
      def samtools_command = sort_bam ? 'sort' : 'view'
          ^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/bwameme/mem/main.nf:82:9`: Variable was declared but not used

  ```nextflow
      def reference = fasta && extension=="cram"  ? "--reference ${fasta}" : ""
          ^^^^^^^^^
  ```

- Warning: `modules/nf-core/cadd/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/cat/cat/main.nf:23:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def file_list = files_in.collect { it.toString() }
                                         ^^
  ```

- Warning: `modules/nf-core/cat/cat/main.nf:58:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def file_list   = files_in.collect { it.toString() }
                                           ^^
  ```

- Warning: `modules/nf-core/chromograph/main.nf:70:9`: Variable was declared but not used

  ```nextflow
      def args               = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/cnvnator/convert2vcf/main.nf:36:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/custom/addmostsevereconsequence/main.nf:48:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/custom/addmostsevereconsequence/main.nf:49:9`: Variable was declared but not used

  ```nextflow
      def args2 = task.ext.args2 ?: ''
          ^^^^^
  ```

- Warning: `modules/nf-core/custom/addmostseverepli/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/custom/addmostseverepli/main.nf:46:9`: Variable was declared but not used

  ```nextflow
      def args2 = task.ext.args2 ?: ''
          ^^^^^
  ```

- Warning: `modules/nf-core/gatk4/denoisereadcounts/main.nf:49:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/gatk4/determinegermlinecontigploidy/main.nf:27:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def exclude = exclude_beds ? exclude_beds.collect { "--exclude-intervals ${it}" }.join(" ") : ""
                                                                                 ^^
  ```

- Warning: `modules/nf-core/gatk4/determinegermlinecontigploidy/main.nf:30:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = counts.collect { "--input ${it}" }.join(" ")
                                                   ^^
  ```

- Warning: `modules/nf-core/gatk4/filtermutectcalls/main.nf:29:113`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def orientationbias_command = orientationbias ? orientationbias.collect{"--orientation-bias-artifact-priors $it"}.join(' ') : ''
                                                                                                                  ^^
  ```

- Warning: `modules/nf-core/gatk4/filtermutectcalls/main.nf:30:96`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def segmentation_command    = segmentation    ? segmentation.collect{"--tumor-segmentation $it"}.join(' ')                  : ''
                                                                                                 ^^
  ```

- Warning: `modules/nf-core/gatk4/filtermutectcalls/main.nf:32:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def table_command           = table           ? table.collect{"--contamination-table $it"}.join(' ')                        : ''
                                                                                           ^^
  ```

- Warning: `modules/nf-core/gatk4/germlinecnvcaller/main.nf:28:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = tsv.collect { "--input ${it}" }.join(' ')
                                                ^^
  ```

- Warning: `modules/nf-core/gatk4/mergevcfs/main.nf:25:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = vcf.collect{ "--INPUT $it"}.join(' ')
                                             ^^
  ```

- Warning: `modules/nf-core/gatk4/mutect2/main.nf:33:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def inputs = input.collect{ "--input $it"}.join(" ")
                                           ^^
  ```

- Warning: `modules/nf-core/gatk4/postprocessgermlinecnvcalls/main.nf:25:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/gatk4/postprocessgermlinecnvcalls/main.nf:27:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def calls_command  = calls   ? calls.collect{"--calls-shard-path $it"}.join(' ')  : ""
                                                                       ^^
  ```

- Warning: `modules/nf-core/gatk4/postprocessgermlinecnvcalls/main.nf:28:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def model_command  = model   ? model.collect{"--model-shard-path $it"}.join(' ')  : ""
                                                                       ^^
  ```

- Warning: `modules/nf-core/glnexus/main.nf:27:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input = gvcfs.collect { it.toString() }
                                  ^^
  ```

- Warning: `modules/nf-core/haplocheck/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/manta/germline/main.nf:33:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_files = input.collect{"--bam ${it}"}.join(' ')
                                               ^^
  ```

- Warning: `modules/nf-core/picard/renamesampleinvcf/main.nf:47:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/samtools/stats/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/sentieon/datametrics/main.nf:36:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input  = bam.sort().collect{"-i $it"}.join(' ')
                                          ^^
  ```

- Warning: `modules/nf-core/sentieon/dedup/main.nf:36:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = bam.collect{"-i $it"}.join(' ')
                                       ^^
  ```

- Warning: `modules/nf-core/sentieon/readwriter/main.nf:30:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_str       = input.sort{ it.getName() }.collect{"-i $it"}.join(' ')
                                        ^^
  ```

- Warning: `modules/nf-core/sentieon/readwriter/main.nf:30:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_str       = input.sort{ it.getName() }.collect{"-i $it"}.join(' ')
                                                                   ^^
  ```

- Warning: `modules/nf-core/sentieon/wgsmetrics/main.nf:28:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input    = bam.sort().collect{"-i $it"}.join(' ')
                                            ^^
  ```

- Warning: `modules/nf-core/svdb/merge/main.nf:38:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def pairs = vcfs.indices.collect { [vcfs[it], input_priority[it]] }
                                                      ^^
  ```

- Warning: `modules/nf-core/svdb/merge/main.nf:38:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def pairs = vcfs.indices.collect { [vcfs[it], input_priority[it]] }
                                                                          ^^
  ```

- Warning: `modules/nf-core/svdb/merge/main.nf:40:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              vcfs = pairs.collect { it[0] }
                                     ^^
  ```

- Warning: `modules/nf-core/svdb/merge/main.nf:41:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              priority = pairs.collect { it[1] }
                                         ^^
  ```

- Warning: `modules/nf-core/svdb/merge/main.nf:55:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          input = (vcfs.collect().size() > 1 && sort_inputs) ? vcfs.sort { it.name } : vcfs
                                                                           ^^
  ```

- Warning: `modules/nf-core/vcf2cytosure/main.nf:51:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/vcf2cytosure/main.nf:52:9`: Variable was declared but not used

  ```nextflow
      def coverage = coverage_bed ? "--coverage ${coverage_bed}" : ''
          ^^^^^^^^
  ```

- Warning: `modules/nf-core/vcf2cytosure/main.nf:53:9`: Variable was declared but not used

  ```nextflow
      def cnvkit = cns ? ( coverage_bed ? '' : "--cn ${cns}" ) : ''
          ^^^^^^
  ```

- Warning: `modules/nf-core/vcf2cytosure/main.nf:54:9`: Variable was declared but not used

  ```nextflow
      def snv = snv_vcf ? ( coverage_bed ? '' : "--snv ${snv_vcf}" ) : ''
          ^^^
  ```

- Warning: `modules/nf-core/vcf2cytosure/main.nf:55:9`: Variable was declared but not used

  ```nextflow
      def blacklist = blacklist_bed ? "--blacklist ${blacklist_bed}" : ''
          ^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_snv.nf:41:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          val_run_mt_for_wes        // boolean
          ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/vcf_filter_bcftools_ensemblvep/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/vcf_filter_bcftools_ensemblvep/main.nf:15:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_tbi = Channel.empty()
               ^^^^^^^
  ```
