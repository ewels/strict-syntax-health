# Nextflow lint results

- Generated: 2026-01-16T02:02:17.650809+00:00
- Nextflow version: 25.12.0-edge
- Summary: 7 errors

## :x: Errors

- Error: `modules/nf-core/spaceranger/count/main.nf:27:9`: `probeset` is already declared

  ```nextflow
      def probeset = probeset ? "--probe-set=\"${probeset}\"" : ""
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/spaceranger/count/main.nf:28:9`: `alignment` is already declared

  ```nextflow
      def alignment = alignment ? "--loupe-alignment=\"${alignment}\"" : ""
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/spaceranger/count/main.nf:29:9`: `slidefile` is already declared

  ```nextflow
      def slidefile = slidefile ? "--slidefile=\"${slidefile}\"" : ""
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/spaceranger/count/main.nf:30:9`: `image` is already declared

  ```nextflow
      def image = image ? "--image=\"${image}\"" : ""
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/spaceranger/count/main.nf:31:9`: `cytaimage` is already declared

  ```nextflow
      def cytaimage = cytaimage ? "--cytaimage=\"${cytaimage}\"" : ""
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/spaceranger/count/main.nf:32:9`: `darkimage` is already declared

  ```nextflow
      def darkimage = darkimage ? "--darkimage=\"${darkimage}\"" : ""
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/spaceranger/count/main.nf:33:9`: `colorizedimage` is already declared

  ```nextflow
      def colorizedimage = colorizedimage ? "--colorizedimage=\"${colorizedimage}\"" : ""
          ^^^^^^^^^^
  ```
