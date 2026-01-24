# Nextflow lint results

- Generated: 2026-01-24T00:17:58.665727272Z
- Nextflow version: 25.12.0-edge
- Summary: 17 warnings

## :warning: Warnings

- Warning: `modules/nf-core/bcftools/concat/main.nf:32:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        def input = vcfs.sort{it.toString()}.join(" ")
                              ^^
    ```

- Warning: `modules/nf-core/bcftools/isec/main.nf:35:9`: Variable was declared but not used

    ```nextflow
        def args = task.ext.args   ?: ''
            ^^^^
    ```

- Warning: `modules/nf-core/gatk4/baserecalibrator/main.nf:29:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        def sites_command = known_sites.collect { "--known-sites ${it}" }.join(' ')
                                                                   ^^
    ```

- Warning: `modules/nf-core/gatk4/gatherbqsrreports/main.nf:23:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        def input_list = table.collect { "--input ${it}" }.join(' ')
                                                    ^^
    ```

- Warning: `modules/nf-core/gatk4/markduplicates/main.nf:33:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        def input_list = bam.collect { "--INPUT ${it}" }.join(' ')
                                                  ^^
    ```

- Warning: `modules/nf-core/gatk4/mergevcfs/main.nf:25:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        def input_list = vcf.collect { "--INPUT ${it}" }.join(' ')
                                                  ^^
    ```

- Warning: `modules/nf-core/preseq/ccurve/main.nf:42:9`: Variable was declared but not used

    ```nextflow
        def args = task.ext.args ?: ''
            ^^^^
    ```

- Warning: `modules/nf-core/vcftools/main.nf:97:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        args_list.removeIf { it.contains('--bed') }
                             ^^
    ```

- Warning: `modules/nf-core/vcftools/main.nf:98:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        args_list.removeIf { it.contains('--exclude-bed') }
                             ^^
    ```

- Warning: `modules/nf-core/vcftools/main.nf:99:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        args_list.removeIf { it.contains('--hapcount') }
                             ^^
    ```

- Warning: `modules/nf-core/vcftools/main.nf:100:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        args_list.removeIf { it.contains('--positions') }
                             ^^
    ```

- Warning: `modules/nf-core/vcftools/main.nf:101:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        args_list.removeIf { it.contains('--exclude-positions') }
                             ^^
    ```

- Warning: `modules/nf-core/vcftools/main.nf:106:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        args_list.removeIf { it.contains('--diff') }
                             ^^
    ```

- Warning: `modules/nf-core/vcftools/main.nf:107:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        args_list.removeIf { it.contains('--gzdiff') }
                             ^^
    ```

- Warning: `modules/nf-core/vcftools/main.nf:108:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        args_list.removeIf { it.contains('--diff-bcf') }
                             ^^
    ```

- Warning: `subworkflows/local/utils_nfcore_genomicrelatedness_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

    ```nextflow
        monochrome_logs   // boolean: Do not use coloured log outputs
        ^^^^^^^^^^^^^^^
    ```

- Warning: `subworkflows/local/utils_nfcore_genomicrelatedness_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

    ```nextflow
        input             //  string: Path to input samplesheet
        ^^^^^
    ```
