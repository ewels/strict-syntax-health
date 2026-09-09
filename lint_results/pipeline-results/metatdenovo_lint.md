# Nextflow lint results

- Generated: 2026-09-09T00:20:54.693775730Z
- Nextflow version: 26.08.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `workflows/metatdenovo.nf:171:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def duplicate_user_orf_names = user_orf_names.countBy { it }.findAll { _name, count -> count > 1 }.keySet()
                                                              ^^
  ```
