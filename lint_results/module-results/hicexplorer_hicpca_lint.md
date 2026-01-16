# Nextflow lint results

- Generated: 2026-01-16T02:02:17.582117+00:00
- Nextflow version: 25.12.0-edge
- Summary: 5 warnings

## :warning: Warnings

- Warning: `modules/nf-core/hicexplorer/hicpca/main.nf:26:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def idx  = args.findIndexOf{ it == '--format' | it == '-f' }
                                   ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/hicexplorer/hicpca/main.nf:26:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def idx  = args.findIndexOf{ it == '--format' | it == '-f' }
                                                      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/hicexplorer/hicpca/main.nf:40:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      outfilenames = eigenvectors.tokenize().collect{"${prefix}_pca${it}.${format}"}.join(' ')
                                                                     ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/hicexplorer/hicpca/main.nf:59:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def idx  = args.findIndexOf{ it == '--format' | it == '-f' }
                                   ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/hicexplorer/hicpca/main.nf:59:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def idx  = args.findIndexOf{ it == '--format' | it == '-f' }
                                                      ^^^^^^^^^^
  ```
