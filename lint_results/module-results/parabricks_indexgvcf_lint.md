# Nextflow lint results

- Generated: 2026-01-16T02:02:17.616137+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/parabricks/indexgvcf/main.nf:46:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def output_cmd = gvcf.any { it.name.endsWith(".gz") } ? "touch ${prefix}.g.vcf.gz.tbi" : "touch ${prefix}.g.vcf.idx"
                                  ^^^^^^^^^^
  ```
