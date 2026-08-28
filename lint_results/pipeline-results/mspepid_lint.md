# Nextflow lint results

- Generated: 2026-08-28T02:47:30.115412640Z
- Nextflow version: 26.08.0-edge
- Summary: 8 warnings

## :warning: Warnings

- Warning: `modules/local/cometconfig/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/ms2rescore/runms2rescore/main.nf:24:5`: Variable was declared but not used

  ```nextflow
      spectra_file = mzml ?: raw_spectra
      ^^^^^^^^^^^^
  ```

- Warning: `modules/local/ms2rescore/runms2rescore/main.nf:25:5`: Variable was declared but not used

  ```nextflow
      ms2pip_model = meta.ms2pip_model ?: 'HCD'
      ^^^^^^^^^^^^
  ```

- Warning: `modules/local/ms2rescore/runms2rescore/main.nf:26:5`: Variable was declared but not used

  ```nextflow
      spectrum_id_pattern = meta.spectrum_id_pattern ?: '.*scan=(\\d+)$'
      ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/local/ms2rescore/runms2rescore/main.nf:27:5`: Variable was declared but not used

  ```nextflow
      fragment_tol_da = meta.fragment_tol_da ?: 0.02
      ^^^^^^^^^^^^^^^
  ```

- Warning: `modules/local/ms2rescore/runms2rescore/main.nf:28:5`: Variable was declared but not used

  ```nextflow
      chunk_size = task.ext.chunk_size ?: 100000
      ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mspepid_pipeline/main.nf:134:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { validateInputSamplesheet(it) }
                                          ^^
  ```

- Warning: `workflows/mspepid.nf:121:9`: Variable was declared but not used

  ```nextflow
      def ch_collated_versions = softwareVersionsToYAML(ch_versions.mix(topic_versions.versions_file))
          ^^^^^^^^^^^^^^^^^^^^
  ```
