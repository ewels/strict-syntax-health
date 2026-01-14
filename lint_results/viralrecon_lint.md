# Nextflow lint results

- Generated: 2026-01-14T09:27:59.349668232Z
- Nextflow version: 25.12.0-edge
- Summary: 43 errors, 98 warnings

## :x: Errors

- Error: `conf/modules.config:43:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig 'modules_nanopore.config'
      ^
  ```

- Error: `conf/modules_illumina.config:13:1`: Variable declarations cannot be mixed with config statements

  ```nextflow
  def variant_caller = params.variant_caller
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/modules_illumina.config:14:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!variant_caller) { variant_caller = params.protocol == 'amplicon' ? 'ivar' : 'bcftools' }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/modules_illumina.config:16:1`: Variable declarations cannot be mixed with config statements

  ```nextflow
  def assemblers = params.assemblers ? params.assemblers.split(',').collect{ it.trim().toLowerCase() } : []
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/modules_illumina.config:59:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_fastqc) {
  ^
  ```

- Error: `conf/modules_illumina.config:72:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_fastp) {
  ^
  ```

- Error: `conf/modules_illumina.config:111:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_kraken2) {
  ^
  ```

- Error: `conf/modules_illumina.config:137:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_variants) {
  ^
  ```

- Error: `conf/modules_illumina.config:736:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_assembly) {
  ^
  ```

- Error: `conf/modules_illumina.config:1083:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_multiqc) {
  ^
  ```

- Error: `conf/modules_nanopore.config:111:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.sequencing_summary && !params.skip_pycoqc) {
  ^
  ```

- Error: `conf/modules_nanopore.config:124:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_nanoplot) {
  ^
  ```

- Error: `conf/modules_nanopore.config:136:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_mosdepth) {
  ^
  ```

- Error: `conf/modules_nanopore.config:185:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_pangolin) {
  ^
  ```

- Error: `conf/modules_nanopore.config:210:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_nextclade) {
  ^
  ```

- Error: `conf/modules_nanopore.config:240:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_freyja) {
  ^
  ```

- Error: `conf/modules_nanopore.config:283:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_variants_quast) {
  ^
  ```

- Error: `conf/modules_nanopore.config:295:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_snpeff) {
  ^
  ```

- Error: `conf/modules_nanopore.config:381:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_multiqc) {
  ^
  ```

- Error: `main.nf:18:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  def primer_set         = ''
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:19:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  def primer_set_version = 0
  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:22:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  if( !params.platform ) {
  ^
  ```

- Error: `main.nf:27:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  def valid_platforms = ["illumina","nanopore"]
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:28:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  if( !(params.platform in valid_platforms) ) {
  ^
  ```

- Error: `main.nf:32:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  if (params.platform == 'illumina' && params.protocol == 'amplicon') {
  ^
  ```

- Error: `main.nf:41:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  def artic_scheme = params.platform == 'nanopore' ? params.artic_scheme : null
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:46:57`: `primer_set` is not defined

  ```nextflow
  params.primer_bed    = getGenomeAttribute('primer_bed', primer_set, primer_set_version)
                                                          ^^^^^^^^^^
  ```

- Error: `main.nf:46:69`: `primer_set_version` is not defined

  ```nextflow
  params.primer_bed    = getGenomeAttribute('primer_bed', primer_set, primer_set_version)
                                                                      ^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:58:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/viralrecon/workflows/viralrecon.nf'

  ```nextflow
  include { VIRALRECON              } from './workflows/viralrecon'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:83:9`: `VIRALRECON` is not defined

  ```nextflow
          VIRALRECON (
          ^^^^^^^^^^
  ```

- Error: `main.nf:92:13`: `artic_scheme` is not defined

  ```nextflow
              artic_scheme
              ^^^^^^^^^^^^
  ```

- Error: `main.nf:95:26`: `VIRALRECON` is not defined

  ```nextflow
          multiqc_report = VIRALRECON.out.multiqc_report
                           ^^^^^^^^^^
  ```

- Error: `main.nf:176:29`: `Nextflow` is not defined

  ```nextflow
                              Nextflow.error("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" +
                              ^^^^^^^^
  ```

- Error: `main.nf:186:25`: `Nextflow` is not defined

  ```nextflow
                          Nextflow.error("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" +
                          ^^^^^^^^
  ```

- Error: `main.nf:195:21`: `Nextflow` is not defined

  ```nextflow
                      Nextflow.error("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" +
                      ^^^^^^^^
  ```

- Error: `nextflow.config:253:26`: Invalid include source: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/viralrecon/conf/test_full_sispa.config'

  ```nextflow
      test_full_sispa    { includeConfig 'conf/test_full_sispa.config'    }
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/consensus_bcftools/main.nf:73:26`: `vcf` is already declared

  ```nextflow
              .map { meta, vcf, tbi, fasta -> tuple(meta, vcf, tbi, fasta, []) }
                           ^^^
  ```

- Error: `subworkflows/local/consensus_bcftools/main.nf:73:31`: `tbi` is already declared

  ```nextflow
              .map { meta, vcf, tbi, fasta -> tuple(meta, vcf, tbi, fasta, []) }
                                ^^^
  ```

- Error: `subworkflows/local/consensus_bcftools/main.nf:73:36`: `fasta` is already declared

  ```nextflow
              .map { meta, vcf, tbi, fasta -> tuple(meta, vcf, tbi, fasta, []) }
                                     ^^^^^
  ```

- Error: `subworkflows/local/fastq_trim_fastp_fastqc/main.nf:15:26`: Unexpected input: 'new'

  ```nextflow
      def Map json = (Map) new JsonSlurper().parseText(json_file.text).get('summary')
                           ^
  ```

- Error: `subworkflows/local/variants_bcftools/main.nf:40:44`: `WorkflowCommons` is not defined

  ```nextflow
          .filter { meta, vcf, tbi, stats -> WorkflowCommons.getNumVariantsFromBCFToolsStats(stats) > 0 }
                                             ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/variants_ivar/main.nf:43:32`: `WorkflowCommons` is not defined

  ```nextflow
          .filter { meta, tsv -> WorkflowCommons.getNumLinesInFile(tsv) > 1 }
                                 ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralrecon.nf:92:5`: Unexpected input: 'include'

  ```nextflow
      include { PREPARE_GENOME_ILLUMINA as PREPARE_GENOME } from '../subworkflows/local/prepare_genome_illumina'
      ^
  ```

## :warning: Warnings

- Warning: `main.nf:38:5`: Params should be declared at the top-level (i.e. outside the workflow)

  ```nextflow
      params.artic_scheme = getGenomeAttribute('scheme', primer_set, primer_set_version)
      ^^^^^^
  ```

- Warning: `main.nf:41:5`: Variable was declared but not used

  ```nextflow
  def artic_scheme = params.platform == 'nanopore' ? params.artic_scheme : null
      ^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/bcftools/consensus/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bcftools/consensus/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def masking = mask ? "-m $mask" : ""
          ^^^^^^^
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

- Warning: `modules/nf-core/blast/blastn/main.nf:65:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/blast/makeblastdb/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args           = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:22:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect { it.toString() } : [reads.toString()]
                                                             ^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:58:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect { it.toString() } : [reads.toString()]
                                                             ^^
  ```

- Warning: `modules/nf-core/custom/getchromsizes/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/freyja/update/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ivar/trim/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def paired       = meta.single_end ? "" : "--paired"
          ^^^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:65:9`: Variable was declared but not used

  ```nextflow
      def readclassification_option = save_reads_assignment ? "--output ${prefix}.kraken2.classifiedreads.txt" : "--output /dev/null"
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:66:9`: Variable was declared but not used

  ```nextflow
      def compress_reads_command = save_output_fastqs ? "pigz -p $task.cpus *.fastq" : ""
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/quast/main.nf:52:9`: Variable was declared but not used

  ```nextflow
      def args      = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/quast/main.nf:54:9`: Variable was declared but not used

  ```nextflow
      def features  = gff             ? "--features $gff" : ''
          ^^^^^^^^
  ```

- Warning: `modules/nf-core/quast/main.nf:55:9`: Variable was declared but not used

  ```nextflow
      def reference = fasta           ? "-r $fasta" : ''
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

- Warning: `subworkflows/local/additional_annotation/main.nf:35:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_annot       = GUNZIP_GFF.out.gunzip.map { it[1] }
                                                       ^^
  ```

- Warning: `subworkflows/local/additional_annotation/main.nf:82:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          BCFTOOLS_QUERY.out.output.collect{it[1]},
                                            ^^
  ```

- Warning: `subworkflows/local/additional_annotation/main.nf:83:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          SNPSIFT_EXTRACTFIELDS.out.txt.collect{it[1]}.ifEmpty([]),
                                                ^^
  ```

- Warning: `subworkflows/local/additional_annotation/main.nf:84:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          pangolin.collect{it[1]}.ifEmpty([])
                           ^^
  ```

- Warning: `subworkflows/local/assembly_minia/main.nf:37:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, contig -> contig.size() > 0 }
                    ^^^^
  ```

- Warning: `subworkflows/local/assembly_qc/main.nf:56:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .collect{ it[1] }
                        ^^
  ```

- Warning: `subworkflows/local/assembly_qc/main.nf:62:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              fasta.map { [ [:], it ] },
                                 ^^
  ```

- Warning: `subworkflows/local/assembly_qc/main.nf:77:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              fasta.map { [ [:], it ] }
                                 ^^
  ```

- Warning: `subworkflows/local/assembly_spades/main.nf:34:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, illumina, pacbio, nanopore -> !meta.single_end }
                              ^^^^^^^^
  ```

- Warning: `subworkflows/local/assembly_spades/main.nf:34:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, illumina, pacbio, nanopore -> !meta.single_end }
                                        ^^^^^^
  ```

- Warning: `subworkflows/local/assembly_spades/main.nf:34:47`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, illumina, pacbio, nanopore -> !meta.single_end }
                                                ^^^^^^^^
  ```

- Warning: `subworkflows/local/assembly_spades/main.nf:69:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, scaffold -> scaffold.size() > 0 }
                    ^^^^
  ```

- Warning: `subworkflows/local/assembly_spades/main.nf:75:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, gfa -> gfa.size() > 0 }
                    ^^^^
  ```

- Warning: `subworkflows/local/assembly_unicycler/main.nf:55:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, scaffold -> scaffold.size() > 0 }
                    ^^^^
  ```

- Warning: `subworkflows/local/assembly_unicycler/main.nf:61:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, gfa -> gfa.size() > 0 }
                    ^^^^
  ```

- Warning: `subworkflows/local/consensus_qc/main.nf:30:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect{ it[1] }
                    ^^
  ```

- Warning: `subworkflows/local/consensus_qc/main.nf:36:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              fasta.map { [ [:], it ] },
                                 ^^
  ```

- Warning: `subworkflows/local/consensus_qc/main.nf:60:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_pango_database = UNTAR_PANGODB.out.untar.map { it[1] }
                                                                    ^^
  ```

- Warning: `subworkflows/local/filter_bam_samtools/main.nf:25:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          bam_bai.map { it[2].getName().tokenize('.')[-1] }
                        ^^
  ```

- Warning: `subworkflows/local/prepare_genome_illumina/main.nf:45:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta    = GUNZIP_FASTA.out.gunzip.map { it[1] }
                                                      ^^
  ```

- Warning: `subworkflows/local/prepare_genome_illumina/main.nf:60:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gff      = GUNZIP_GFF.out.gunzip.map { it[1] }
                                                        ^^
  ```

- Warning: `subworkflows/local/prepare_genome_illumina/main.nf:71:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta.map { [ [:], it ] }
                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome_illumina/main.nf:73:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_fai         = CUSTOM_GETCHROMSIZES.out.fai.map { it[1] }
                                                          ^^
  ```

- Warning: `subworkflows/local/prepare_genome_illumina/main.nf:74:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_chrom_sizes = CUSTOM_GETCHROMSIZES.out.sizes.map { it[1] }
                                                            ^^
  ```

- Warning: `subworkflows/local/prepare_genome_illumina/main.nf:87:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_kraken2_db = UNTAR_KRAKEN2_DB.out.untar.map { it[1] }
                                                                   ^^
  ```

- Warning: `subworkflows/local/prepare_genome_illumina/main.nf:112:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_primer_bed = GUNZIP_PRIMER_BED.out.gunzip.map { it[1] }
                                                                     ^^
  ```

- Warning: `subworkflows/local/prepare_genome_illumina/main.nf:134:76`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      ch_primer_fasta = GUNZIP_PRIMER_FASTA.out.gunzip.map { it[1] }
                                                                             ^^
  ```

- Warning: `subworkflows/local/prepare_genome_illumina/main.nf:141:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      ch_primer_bed.map { [ [:], it ] },
                                                 ^^
  ```

- Warning: `subworkflows/local/prepare_genome_illumina/main.nf:167:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_fasta.map { [ [:], it ] }
                                        ^^
  ```

- Warning: `subworkflows/local/prepare_genome_illumina/main.nf:184:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_nextclade_db = UNTAR_NEXTCLADE_DB.out.untar.map { it[1] }
                                                                       ^^
  ```

- Warning: `subworkflows/local/prepare_genome_illumina/main.nf:219:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      ch_fasta.map { [ [:], it ] }
                                            ^^
  ```

- Warning: `subworkflows/local/prepare_genome_nanopore/main.nf:22:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      bowtie2_index
      ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome_nanopore/main.nf:38:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta    = GUNZIP_FASTA.out.gunzip.map { it[1] }
                                                      ^^
  ```

- Warning: `subworkflows/local/prepare_genome_nanopore/main.nf:53:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gff      = GUNZIP_GFF.out.gunzip.map { it[1] }
                                                        ^^
  ```

- Warning: `subworkflows/local/prepare_genome_nanopore/main.nf:64:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta.map { [ [:], it ] }
                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome_nanopore/main.nf:66:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_fai         = CUSTOM_GETCHROMSIZES.out.fai.map { it[1] }
                                                          ^^
  ```

- Warning: `subworkflows/local/prepare_genome_nanopore/main.nf:67:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_chrom_sizes = CUSTOM_GETCHROMSIZES.out.sizes.map { it[1] }
                                                            ^^
  ```

- Warning: `subworkflows/local/prepare_genome_nanopore/main.nf:80:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_kraken2_db = UNTAR_KRAKEN2_DB.out.untar.map { it[1] }
                                                                   ^^
  ```

- Warning: `subworkflows/local/prepare_genome_nanopore/main.nf:102:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_primer_bed = GUNZIP_PRIMER_BED.out.gunzip.map { it[1] }
                                                                 ^^
  ```

- Warning: `subworkflows/local/prepare_genome_nanopore/main.nf:132:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_nextclade_db = UNTAR.out.untar.map { it[1] }
                                                          ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_viralrecon_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_viralrecon_pipeline/main.nf:102:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, fastq_1, fastq_2, barcode->
                                          ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_viralrecon_pipeline/main.nf:111:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  validateInputSamplesheet(it)
                                           ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_viralrecon_pipeline/main.nf:124:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      meta, fastq_1, fastq_2, barcode->
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_viralrecon_pipeline/main.nf:124:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      meta, fastq_1, fastq_2, barcode->
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_viralrecon_pipeline/main.nf:297:9`: Variable was declared but not used

  ```nextflow
      def logname = flagstat_file.getBaseName() - 'flagstat'
          ^^^^^^^
  ```

- Warning: `subworkflows/local/variants_bcftools/main.nf:29:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          fasta.map { [ [:], it ] },
                             ^^
  ```

- Warning: `subworkflows/local/variants_bcftools/main.nf:40:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, vcf, tbi, stats -> WorkflowCommons.getNumVariantsFromBCFToolsStats(stats) > 0 }
                    ^^^^
  ```

- Warning: `subworkflows/local/variants_bcftools/main.nf:40:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, vcf, tbi, stats -> WorkflowCommons.getNumVariantsFromBCFToolsStats(stats) > 0 }
                          ^^^
  ```

- Warning: `subworkflows/local/variants_bcftools/main.nf:40:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, vcf, tbi, stats -> WorkflowCommons.getNumVariantsFromBCFToolsStats(stats) > 0 }
                               ^^^
  ```

- Warning: `subworkflows/local/variants_bcftools/main.nf:44:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, vcf, tbi, stats -> [ meta, vcf ] }
                            ^^^
  ```

- Warning: `subworkflows/local/variants_bcftools/main.nf:44:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, vcf, tbi, stats -> [ meta, vcf ] }
                                 ^^^^^
  ```

- Warning: `subworkflows/local/variants_bcftools/main.nf:48:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, vcf, tbi, stats -> [ meta, tbi ] }
                       ^^^
  ```

- Warning: `subworkflows/local/variants_bcftools/main.nf:48:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, vcf, tbi, stats -> [ meta, tbi ] }
                                 ^^^^^
  ```

- Warning: `subworkflows/local/variants_bcftools/main.nf:52:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, vcf, tbi, stats -> [ meta, stats ] }
                       ^^^
  ```

- Warning: `subworkflows/local/variants_bcftools/main.nf:52:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, vcf, tbi, stats -> [ meta, stats ] }
                            ^^^
  ```

- Warning: `subworkflows/local/variants_bcftools/main.nf:60:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          fasta.map { [ [:], it ] }
                             ^^
  ```

- Warning: `subworkflows/local/variants_ivar/main.nf:43:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, tsv -> WorkflowCommons.getNumLinesInFile(tsv) > 1 }
                    ^^^^
  ```

- Warning: `subworkflows/local/variants_long_table/main.nf:28:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          BCFTOOLS_QUERY.out.output.collect{it[1]},
                                            ^^
  ```

- Warning: `subworkflows/local/variants_long_table/main.nf:29:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          snpsift.collect{it[1]}.ifEmpty([]),
                          ^^
  ```

- Warning: `subworkflows/local/variants_long_table/main.nf:30:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          pangolin.collect{it[1]}.ifEmpty([])
                           ^^
  ```

- Warning: `subworkflows/local/variants_qc/main.nf:9:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      bam           // channel: [ val(meta), [ bam ] ]
      ^^^
  ```

- Warning: `subworkflows/local/variants_qc/main.nf:11:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      stats         // channel: [ val(meta), [ bcftools_stats ] ]
      ^^^^^
  ```

- Warning: `subworkflows/local/variants_qc/main.nf:13:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      sizes         // channel: /path/to/genome.sizes
      ^^^^^
  ```

- Warning: `subworkflows/local/variants_qc/main.nf:15:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      bed           // channel: /path/to/primers.bed
      ^^^
  ```

- Warning: `subworkflows/nf-core/bam_markduplicates_picard/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
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

- Warning: `subworkflows/nf-core/bam_variant_demix_boot_freyja/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_variant_demix_boot_freyja/main.nf:51:5`: Variable was declared but not used

  ```nextflow
      ch_freyja_demix = FREYJA_DEMIX.out.demix
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_variant_demix_boot_freyja/main.nf:58:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_lineages   = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_variant_demix_boot_freyja/main.nf:59:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_summarized = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_bowtie2/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```
