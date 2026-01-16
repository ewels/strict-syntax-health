# Nextflow lint results

- Generated: 2026-01-16T02:02:17.579216+00:00
- Nextflow version: 25.12.0-edge
- Summary: 4 warnings

## :warning: Warnings

- Warning: `modules/nf-core/gt/ltrharvest/main.nf:27:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      out_name        = (args.split('-').find { it =~ /out .*\.(fa|fsa|fasta)/ } ?: 'out.fasta').replace('out ', '').trim()
                                                ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/gt/ltrharvest/main.nf:28:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      outinner_name   = (args.split('-').find { it =~ /outinner .*\.(fa|fsa|fasta)/ } ?: 'outinner.fasta').replace('outinner ', '').trim()
                                                ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/gt/ltrharvest/main.nf:47:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      out_name        = (args.split('-').find { it =~ /out .*\.(fa|fsa|fasta)/ } ?: 'out.fasta').replace('out ', '').trim()
                                                ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/gt/ltrharvest/main.nf:48:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      outinner_name   = (args.split('-').find { it =~ /outinner .*\.(fa|fsa|fasta)/ } ?: 'outinner.fasta').replace('outinner ', '').trim()
                                                ^^^^^^^^^^
  ```
