# Nextflow lint results

- Generated: 2026-01-16T06:34:49.684633654Z
- Nextflow version: 25.12.0-edge
- Summary: 64 errors, 157 warnings

## :x: Errors

- Error: `conf/modules.config:389:5`: Unexpected input: '}'

  ```nextflow
      }
      ^
  ```

- Error: `modules/local/diamond/blastp/main.nf:36:15`: Unexpected input: ':'

  ```nextflow
          case 0:   out_ext = "blast"; break
                ^
  ```

- Error: `modules/local/eggnog/download/main.nf:1:1`: Invalid process definition -- check for missing or out-of-order section labels

  ```nextflow
  process EGGNOG_DOWNLOAD {
  ^
  ```

- Error: `modules/nf-core/samtools/sort/main.nf:68:9`: `reference` is already declared

  ```nextflow
      def reference = fasta ? "--reference ${fasta}" : ""
          ^^^^^^^^^
  ```

- Error: `nextflow.config:372:35`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/metatdenovo ${manifest.version}\033[0m
                                    ^^^^^^^^
  ```

- Error: `nextflow.config:375:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:375:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:375:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:384:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:385:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/eggnog/main.nf:5:1`: Included name 'EGGNOG_DOWNLOAD' is not defined in module '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/metatdenovo/modules/local/eggnog/download/main.nf'

  ```nextflow
  include { EGGNOG_DOWNLOAD } from '../../../modules/local/eggnog/download/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/eggnog/main.nf:17:5`: `EGGNOG_DOWNLOAD` is not defined

  ```nextflow
      EGGNOG_DOWNLOAD()
      ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/eggnog/main.nf:18:35`: `EGGNOG_DOWNLOAD` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(EGGNOG_DOWNLOAD.out.versions)
                                    ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/eggnog/main.nf:20:5`: `EGGNOG_DOWNLOAD` is not defined

  ```nextflow
      EGGNOG_DOWNLOAD.out.eggnog_db
      ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/eggnog/main.nf:21:18`: `EGGNOG_DOWNLOAD` is not defined

  ```nextflow
          .combine(EGGNOG_DOWNLOAD.out.dmnd)
                   ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/eggnog/main.nf:22:18`: `EGGNOG_DOWNLOAD` is not defined

  ```nextflow
          .combine(EGGNOG_DOWNLOAD.out.taxa_db)
                   ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/eggnog/main.nf:23:18`: `EGGNOG_DOWNLOAD` is not defined

  ```nextflow
          .combine(EGGNOG_DOWNLOAD.out.pkl)
                   ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/hmmclassify/main.nf:36:5`: Every emit must be assigned to a name when there are multiple emits

  ```nextflow
      HMMRANK.out.hmmrank
      ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/prokka/subsets/main.nf:19:33`: `contigs` is already declared

  ```nextflow
      PROKKA ( contigs.map{ meta, contigs -> contigs }.splitFasta(size: batchsize, file: true).map { contigs -> [ [ id: contigs.getBaseName() ], contigs] }, [], []  )
                                  ^^^^^^^
  ```

- Error: `subworkflows/local/prokka/subsets/main.nf:19:100`: `contigs` is already declared

  ```nextflow
      PROKKA ( contigs.map{ meta, contigs -> contigs }.splitFasta(size: batchsize, file: true).map { contigs -> [ [ id: contigs.getBaseName() ], contigs] }, [], []  )
                                                                                                     ^^^^^^^
  ```

- Error: `subworkflows/local/prokka/subsets/main.nf:22:24`: `contigs` is already declared

  ```nextflow
      contigs.map{ meta, contigs -> [ id:"${meta.id}.prokka" ] }
                         ^^^^^^^
  ```

- Error: `subworkflows/local/prokka/subsets/main.nf:28:24`: `contigs` is already declared

  ```nextflow
      contigs.map{ meta, contigs -> [ id:"${meta.id}.prokka" ] }
                         ^^^^^^^
  ```

- Error: `subworkflows/local/prokka/subsets/main.nf:34:24`: `contigs` is already declared

  ```nextflow
      contigs.map{ meta, contigs -> [ id:"${meta.id}.prokka" ] }
                         ^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:3:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if ( ( params.assembler && params.user_assembly ) || ( ! params.assembler && ! params.user_assembly ) ) {
  ^
  ```

- Error: `workflows/metatdenovo.nf:6:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if ( ( params.orf_caller && ( params.user_orfs_gff ) ) && ( ! params.orf_caller && ! params.user_orfs_gff ) ) {
  ^
  ```

- Error: `workflows/metatdenovo.nf:11:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if ( params.user_orfs_gff && ! params.user_orfs_faa ) {
  ^
  ```

- Error: `workflows/metatdenovo.nf:18:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if ( params.assembler && ( params.user_orfs_gff || params.user_orfs_faa ) ) {
  ^
  ```

- Error: `workflows/metatdenovo.nf:23:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  assembler     = params.assembler
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:24:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  assembly_name = params.assembler ?: params.user_assembly_name
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:27:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  orf_caller = params.orf_caller
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:28:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  orfs_name  = params.orf_caller ?: params.user_orfs_name
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:31:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_files = Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:35:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_hmmrs = Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:36:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if ( params.hmmdir ) {
  ^
  ```

- Error: `workflows/metatdenovo.nf:58:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/metatdenovo/modules/local/diamond/blastp/main.nf'

  ```nextflow
  include { DIAMOND_BLASTP as DIAMOND_TAXONOMY } from '../modules/local/diamond/blastp/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:237:22`: `fwd` is already declared

  ```nextflow
          .map { meta, fwd, rev -> [ meta, [ fwd, rev ] ] }
                       ^^^
  ```

- Error: `workflows/metatdenovo.nf:237:27`: `rev` is already declared

  ```nextflow
          .map { meta, fwd, rev -> [ meta, [ fwd, rev ] ] }
                            ^^^
  ```

- Error: `workflows/metatdenovo.nf:257:26`: `assembly_name` is not defined

  ```nextflow
          .map { [ [ id:"${assembly_name}.${orfs_name}" ], it ] }
                           ^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:257:43`: `orfs_name` is not defined

  ```nextflow
          .map { [ [ id:"${assembly_name}.${orfs_name}" ], it ] }
                                            ^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:343:34`: `assembly_name` is not defined

  ```nextflow
                  .value ( [ [ id: assembly_name ], file(params.user_assembly) ] )
                                   ^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:345:17`: `assembler` is not defined

  ```nextflow
      } else if ( assembler == 'spades' ) {
                  ^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:357:34`: `assembly_name` is not defined

  ```nextflow
              .map { it -> [ [ id: assembly_name ], it, [], [] ] }
                                   ^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:372:17`: `assembler` is not defined

  ```nextflow
      } else if ( assembler == 'megahit' ) {
                  ^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:379:34`: `assembly_name` is not defined

  ```nextflow
              .map { it -> [ [ id: assembly_name ], it ] }
                                   ^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:416:10`: `orf_caller` is not defined

  ```nextflow
      if ( orf_caller == 'prodigal' ) {
           ^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:417:72`: `assembly_name` is not defined

  ```nextflow
          PRODIGAL( ch_assembly_contigs.map { meta, contigs -> [ [id: "${assembly_name}.${orfs_name}"], contigs  ] } )
                                                                         ^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:417:89`: `orfs_name` is not defined

  ```nextflow
          PRODIGAL( ch_assembly_contigs.map { meta, contigs -> [ [id: "${assembly_name}.${orfs_name}"], contigs  ] } )
                                                                                          ^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:430:10`: `orf_caller` is not defined

  ```nextflow
      if ( orf_caller == 'transdecoder' ) {
           ^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:431:77`: `assembly_name` is not defined

  ```nextflow
          TRANSDECODER ( ch_assembly_contigs.map { meta, contigs -> [ [id: "${assembly_name}.${orfs_name}" ], contigs ] } )
                                                                              ^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:431:94`: `orfs_name` is not defined

  ```nextflow
          TRANSDECODER ( ch_assembly_contigs.map { meta, contigs -> [ [id: "${assembly_name}.${orfs_name}" ], contigs ] } )
                                                                                               ^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:448:45`: `assembly_name` is not defined

  ```nextflow
          ch_gff = Channel.value ( [ [ id: "${assembly_name}.${orfs_name}" ], file(params.user_orfs_gff) ] )
                                              ^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:448:62`: `orfs_name` is not defined

  ```nextflow
          ch_gff = Channel.value ( [ [ id: "${assembly_name}.${orfs_name}" ], file(params.user_orfs_gff) ] )
                                                               ^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:449:49`: `assembly_name` is not defined

  ```nextflow
          ch_protein = Channel.value ( [ [ id: "${assembly_name}.${orfs_name}" ], file(params.user_orfs_faa) ] )
                                                  ^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:449:66`: `orfs_name` is not defined

  ```nextflow
          ch_protein = Channel.value ( [ [ id: "${assembly_name}.${orfs_name}" ], file(params.user_orfs_faa) ] )
                                                                   ^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:467:22`: `ch_hmmrs` is not defined

  ```nextflow
      ch_hmmclassify = ch_hmmrs
                       ^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:469:48`: `assembly_name` is not defined

  ```nextflow
          .map { hmm, meta, protein ->[ [ id: "${assembly_name}.${orfs_name}" ], hmm, protein ] }
                                                 ^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:469:65`: `orfs_name` is not defined

  ```nextflow
          .map { hmm, meta, protein ->[ [ id: "${assembly_name}.${orfs_name}" ], hmm, protein ] }
                                                                  ^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:494:43`: `assembly_name` is not defined

  ```nextflow
          .map { featurecounts -> [ [ id:"${assembly_name}.${orfs_name}" ], featurecounts ] }
                                            ^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:494:60`: `orfs_name` is not defined

  ```nextflow
          .map { featurecounts -> [ [ id:"${assembly_name}.${orfs_name}" ], featurecounts ] }
                                                             ^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:566:5`: `DIAMOND_TAXONOMY` is not defined

  ```nextflow
      DIAMOND_TAXONOMY(
      ^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:572:39`: `DIAMOND_TAXONOMY` is not defined

  ```nextflow
      ch_versions     = ch_versions.mix(DIAMOND_TAXONOMY.out.versions)
                                        ^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:576:27`: `DIAMOND_TAXONOMY` is not defined

  ```nextflow
      ch_taxonkit_lineage = DIAMOND_TAXONOMY.out.tsv
                            ^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:625:37`: `assembly_name` is not defined

  ```nextflow
              .map { it -> [ [ id: "${assembly_name}.${orfs_name}" ], it ] }
                                      ^^^^^^^^^^^^^
  ```

- Error: `workflows/metatdenovo.nf:625:54`: `orfs_name` is not defined

  ```nextflow
              .map { it -> [ [ id: "${assembly_name}.${orfs_name}" ], it ] }
                                                       ^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/collect/featurecounts/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args     = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/collect/stats/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/collect/stats/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/diamond/format_tax/ranklist/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/diamond/format_tax/taxdump/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/eggnog/sum/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/eggnog/sum/main.nf:25:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/eukulele/format_tax/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/format/prodigal/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/local/format/prodigal/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/local/format/spades/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/format/spades/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/kofamscan/download/main.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/kofamscan/scan/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/kofamscan/scan/main.nf:25:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/kofamscan/sum/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/kofamscan/sum/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/kofamscan/unique/main.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/kofamscan/unique/main.nf:54:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/megahit/interleaved/main.nf:27:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: ''
          ^^^^^^
  ```

- Warning: `modules/local/megahit/interleaved/main.nf:53:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: ''
          ^^^^^^
  ```

- Warning: `modules/local/merge/summary/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/prokka/gff2tsv/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/seqtk/hmmhitfaas/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/seqtk/hmmhitfaas/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/spades/writeyaml/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/sumtaxonomy/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bbmap/bbduk/main.nf:45:9`: Variable was declared but not used

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

- Warning: `modules/nf-core/cat/fastq/main.nf:22:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect { it.toString() } : [reads.toString()]
                                                             ^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:77:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect { it.toString() } : [reads.toString()]
                                                             ^^
  ```

- Warning: `modules/nf-core/pigz/compress/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/prodigal/main.nf:49:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/samtools/sort/main.nf:68:9`: Variable was declared but not used

  ```nextflow
      def reference = fasta ? "--reference ${fasta}" : ""
          ^^^^^^^^^
  ```

- Warning: `modules/nf-core/spades/main.nf:80:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/spades/main.nf:82:9`: Variable was declared but not used

  ```nextflow
      def maxmem = task.memory.toGiga()
          ^^^^^^
  ```

- Warning: `modules/nf-core/spades/main.nf:86:9`: Variable was declared but not used

  ```nextflow
      def custom_hmms = hmm ? "--custom-hmms $hmm" : ""
          ^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/spades/main.nf:87:9`: Variable was declared but not used

  ```nextflow
      def reads = yml ? "--dataset $yml" : "$illumina_reads $pacbio_reads $nanopore_reads"
          ^^^^^
  ```

- Warning: `modules/nf-core/taxonkit/lineage/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/trimgalore/main.nf:47:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          args_list.removeAll { it.toLowerCase().contains('_r2 ') }
                                ^^
  ```

- Warning: `nextflow.config:375:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/eggnog/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/eukulele/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/eukulele/main.nf:21:88`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      FORMAT_EUKULELE_TAX( EUKULELE_SEARCH.out.taxonomy_estimation.map { meta, taxonomy, dbname -> [ meta, taxonomy ] } )
                                                                                         ^^^^^^
  ```

- Warning: `subworkflows/local/eukulele/main.nf:26:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, taxonomy, protein, dbname, database -> [ meta, dbname, taxonomy ] }
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/eukulele/main.nf:26:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, taxonomy, protein, dbname, database -> [ meta, dbname, taxonomy ] }
                                                  ^^^^^^^^
  ```

- Warning: `subworkflows/local/fastqc/trimgalore/main.nf:15:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions    = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/fastqc/trimgalore/main.nf:16:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_html    = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/fastqc/trimgalore/main.nf:17:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_zip     = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/fastqc/trimgalore/main.nf:26:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_html  = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/fastqc/trimgalore/main.nf:27:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_zip   = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/fastqc/trimgalore/main.nf:28:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_log   = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/hmmclassify/main.nf:11:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/hmmclassify/main.nf:21:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, hmm, seqdb -> meta }
                           ^^^
  ```

- Warning: `subworkflows/local/hmmclassify/main.nf:21:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, hmm, seqdb -> meta }
                                ^^^^^
  ```

- Warning: `subworkflows/local/hmmclassify/main.nf:23:69`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .combine ( HMMER_HMMSEARCH.out.target_summary.collect { meta, summary -> summary } )
                                                                      ^^^^
  ```

- Warning: `subworkflows/local/hmmclassify/main.nf:24:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [ it[0], it[1..-1] ] }
                       ^^
  ```

- Warning: `subworkflows/local/hmmclassify/main.nf:24:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [ it[0], it[1..-1] ] }
                              ^^
  ```

- Warning: `subworkflows/local/hmmclassify/main.nf:31:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, hmmrank, hmms, faa -> [ meta, hmmrank, faa ] }
                                    ^^^^
  ```

- Warning: `subworkflows/local/kofamscan/main.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prodigal/main.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prokka/subsets/main.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prokka/subsets/main.nf:19:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      PROKKA ( contigs.map{ meta, contigs -> contigs }.splitFasta(size: batchsize, file: true).map { contigs -> [ [ id: contigs.getBaseName() ], contigs] }, [], []  )
                            ^^^^
  ```

- Warning: `subworkflows/local/prokka/subsets/main.nf:21:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_log  = PROKKA.out.txt.map { meta, log -> log }.collect()
                                     ^^^^
  ```

- Warning: `subworkflows/local/prokka/subsets/main.nf:22:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      contigs.map{ meta, contigs -> [ id:"${meta.id}.prokka" ] }
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prokka/subsets/main.nf:23:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .combine(PROKKA.out.gff.collect { meta, gff -> gff }.map { [ it ] })
                                            ^^^^
  ```

- Warning: `subworkflows/local/prokka/subsets/main.nf:23:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .combine(PROKKA.out.gff.collect { meta, gff -> gff }.map { [ it ] })
                                                                       ^^
  ```

- Warning: `subworkflows/local/prokka/subsets/main.nf:28:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      contigs.map{ meta, contigs -> [ id:"${meta.id}.prokka" ] }
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prokka/subsets/main.nf:29:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .combine(PROKKA.out.faa.collect { meta, protein -> protein }.map { [ it ] })
                                            ^^^^
  ```

- Warning: `subworkflows/local/prokka/subsets/main.nf:29:78`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .combine(PROKKA.out.faa.collect { meta, protein -> protein }.map { [ it ] })
                                                                               ^^
  ```

- Warning: `subworkflows/local/prokka/subsets/main.nf:34:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      contigs.map{ meta, contigs -> [ id:"${meta.id}.prokka" ] }
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prokka/subsets/main.nf:35:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .combine(PROKKA.out.ffn.collect { meta, fnn -> fnn }.map { [ it ] })
                                            ^^^^
  ```

- Warning: `subworkflows/local/prokka/subsets/main.nf:35:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .combine(PROKKA.out.ffn.collect { meta, fnn -> fnn }.map { [ it ] })
                                                                       ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_metatdenovo_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_metatdenovo_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_metatdenovo_pipeline/main.nf:39:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_metatdenovo_pipeline/main.nf:76:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_metatdenovo_pipeline/main.nf:99:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_diamond_paths = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_metatdenovo_pipeline/main.nf:101:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_diamond_paths = Channel
                             ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_sort_stats_samtools/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_stats_samtools/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:23:1`: Variable was declared but not used

  ```nextflow
  assembler     = params.assembler
  ^^^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:24:1`: Variable was declared but not used

  ```nextflow
  assembly_name = params.assembler ?: params.user_assembly_name
  ^^^^^^^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:27:1`: Variable was declared but not used

  ```nextflow
  orf_caller = params.orf_caller
  ^^^^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:28:1`: Variable was declared but not used

  ```nextflow
  orfs_name  = params.orf_caller ?: params.user_orfs_name
  ^^^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:31:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_files = Channel.empty()
  ^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:31:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_files = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:35:12`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_hmmrs = Channel.empty()
             ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:37:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:41:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:43:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ file(it) ] }
                        ^^
  ```

- Warning: `workflows/metatdenovo.nf:146:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:147:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:157:92`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  return [[ meta.id, pairs.collect { meta + [id: "${meta.id}_${pairs.indexOf(it) + 1}"] }, fastq_files ]]
                                                                                             ^^
  ```

- Warning: `workflows/metatdenovo.nf:168:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { validateInputSamplesheet(it) }
                                          ^^
  ```

- Warning: `workflows/metatdenovo.nf:194:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, f -> ! meta.single_end }
                          ^
  ```

- Warning: `workflows/metatdenovo.nf:208:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, f -> ! meta.single_end }
                          ^
  ```

- Warning: `workflows/metatdenovo.nf:222:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, f -> meta.single_end }
                          ^
  ```

- Warning: `workflows/metatdenovo.nf:256:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .collect { meta, fasta -> meta }
                           ^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:257:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ [ id:"${assembly_name}.${orfs_name}" ], it ] }
                                                           ^^
  ```

- Warning: `workflows/metatdenovo.nf:267:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      .collect { meta, report ->
                                 ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:274:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .map { [ it ] }
                               ^^
  ```

- Warning: `workflows/metatdenovo.nf:282:52`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          BBMAP_BBDUK ( FASTQC_TRIMGALORE.out.reads, Channel.fromPath(params.sequence_filter).first() )
                                                     ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:284:55`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_bbduk_logs = BBMAP_BBDUK.out.log.collect { meta, log ->  log }.map { [ it ] }
                                                        ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:284:83`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_bbduk_logs = BBMAP_BBDUK.out.log.collect { meta, log ->  log }.map { [ it ] }
                                                                                    ^^
  ```

- Warning: `workflows/metatdenovo.nf:287:78`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(BBMAP_BBDUK.out.log.collect{ meta, log -> log })
                                                                               ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:290:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_bbduk_logs = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:298:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_interleaved = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:312:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      .collect { meta, fastq -> fastq }
                                 ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:313:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .map { [ [id:'all_samples', single_end:true], it ] }
                                                                    ^^
  ```

- Warning: `workflows/metatdenovo.nf:315:68`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_pe_reads_to_assembly = BBMAP_BBNORM.out.fastq.map { meta, fasta -> fasta }
                                                                     ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:316:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_se_reads_to_assembly = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:320:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .filter { meta, fastq -> ! meta.single_end }
                                  ^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:321:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map { meta, fastq -> fastq }
                         ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:323:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .filter { meta, fastq -> meta.single_end }
                                  ^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:324:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map { meta, fastq -> fastq }
                         ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:336:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  Channel
                  ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:338:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .map { [ [ id:params.user_assembly ], it ] }
                                                            ^^
  ```

- Warning: `workflows/metatdenovo.nf:342:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_assembly_contigs = Channel
                                    ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:395:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gff      = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:396:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_protein  = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:417:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          PRODIGAL( ch_assembly_contigs.map { meta, contigs -> [ [id: "${assembly_name}.${orfs_name}"], contigs  ] } )
                                              ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:431:50`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          TRANSDECODER ( ch_assembly_contigs.map { meta, contigs -> [ [id: "${assembly_name}.${orfs_name}" ], contigs ] } )
                                                   ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:448:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_gff = Channel.value ( [ [ id: "${assembly_name}.${orfs_name}" ], file(params.user_orfs_gff) ] )
                   ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:449:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_protein = Channel.value ( [ [ id: "${assembly_name}.${orfs_name}" ], file(params.user_orfs_faa) ] )
                       ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:455:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      BBMAP_INDEX(ch_assembly_contigs.map { meta, contigs -> contigs })
                                            ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:469:21`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { hmm, meta, protein ->[ [ id: "${assembly_name}.${orfs_name}" ], hmm, protein ] }
                      ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:481:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .combine(ch_gff.map { meta, bam -> bam } )
                                ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:484:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .combine(BAM_SORT_STATS_SAMTOOLS.out.idxstats.collect { meta, idxstats -> idxstats }.map { [ it ] } )
                                                                  ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:484:102`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .combine(BAM_SORT_STATS_SAMTOOLS.out.idxstats.collect { meta, idxstats -> idxstats }.map { [ it ] } )
                                                                                                       ^^
  ```

- Warning: `workflows/metatdenovo.nf:493:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .collect() { meta, featurecounts -> featurecounts }
                       ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:498:72`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fcs_for_stats      = COLLECT_FEATURECOUNTS.out.counts.collect { meta, tsv -> tsv }.map { [ it ] }
                                                                         ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:498:99`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_fcs_for_stats      = COLLECT_FEATURECOUNTS.out.counts.collect { meta, tsv -> tsv }.map { [ it ] }
                                                                                                    ^^
  ```

- Warning: `workflows/metatdenovo.nf:499:68`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fcs_for_summary    = COLLECT_FEATURECOUNTS.out.counts.map { meta, tsv -> tsv }
                                                                     ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:503:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_merge_tables = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:511:75`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_merge_tables = ch_merge_tables.mix ( EGGNOG.out.sumtable.map { meta, tsv -> tsv } )
                                                                            ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:521:87`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_merge_tables = ch_merge_tables.mix ( KOFAMSCAN.out.kofamscan_summary.map { meta, tsv -> tsv } )
                                                                                        ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:538:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_eukulele_db = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:548:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_eukulele_db = Channel
                               ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:550:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [ it, file(params.eukulele_dbpath) ] }
                           ^^
  ```

- Warning: `workflows/metatdenovo.nf:552:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_eukulele_db = Channel.fromPath(params.eukulele_dbpath, checkIfExists: true)
                               ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:553:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [ [], it ] }
                               ^^
  ```

- Warning: `workflows/metatdenovo.nf:560:89`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_merge_tables = ch_merge_tables.mix ( SUB_EUKULELE.out.taxonomy_summary.map { meta, tsv -> tsv } )
                                                                                          ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:568:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_diamond_dbs.map { [ it[0], it[1] ] },
                                 ^^
  ```

- Warning: `workflows/metatdenovo.nf:568:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_diamond_dbs.map { [ it[0], it[1] ] },
                                        ^^
  ```

- Warning: `workflows/metatdenovo.nf:617:87`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_merge_tables = ch_merge_tables.mix ( SUM_DIAMONDTAX.out.taxonomy_summary.map { meta, tsv -> tsv } )
                                                                                        ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:631:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.empty()
              ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:632:60`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .mix ( MERGE_TABLES.out.merged_table.map { meta, tblout -> [ tblout ] } )
                                                             ^^^^
  ```

- Warning: `workflows/metatdenovo.nf:654:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:657:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:658:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:660:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:661:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:665:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/metatdenovo.nf:671:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```
