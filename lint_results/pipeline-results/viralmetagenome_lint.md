# Nextflow lint results

- Generated: 2026-01-24T00:19:57.294055112Z
- Nextflow version: 25.12.0-edge
- Summary: 18 errors, 207 warnings

## :x: Errors

- Error: `conf/modules.config:16:170`: Unexpected input: '='

  ```nextflow
  save_final_reads            = params.save_final_reads ? (!params.skip_hostremoval ? 'host' : (!params.skip_complexity_filtering ? 'complexity' : (params.umi_deduplicate = 'read' ? 'deduplication' : 'trimming')))  : 'nothing'
                                                                                                                                                                           ^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:29:9`: `add` is already declared

  ```nextflow
      def add          = add             ? "--add <(unpigz -cdf ${add})"                   : ''
          ^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:30:9`: `addfragments` is already declared

  ```nextflow
      def addfragments = addfragments    ? "--addfragments <(unpigz -cdf ${addfragments})" : ''
          ^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:31:9`: `addfull` is already declared

  ```nextflow
      def addfull      = addfull         ? "--addfull <(unpigz -cdf ${addfull})"           : ''
          ^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:32:9`: `addprofile` is already declared

  ```nextflow
      def addprofile   = addprofile      ? "--addprofile <(unpigz -cdf ${addprofile})"     : ''
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:33:9`: `addlong` is already declared

  ```nextflow
      def addlong      = addlong         ? "--addlong <(unpigz -cdf ${addlong})"           : ''
          ^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:59:9`: `add` is already declared

  ```nextflow
      def add          = add             ? "--add ${add}"                   : ''
          ^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:60:9`: `addfragments` is already declared

  ```nextflow
      def addfragments = addfragments    ? "--addfragments ${addfragments}" : ''
          ^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:61:9`: `addfull` is already declared

  ```nextflow
      def addfull      = addfull         ? "--addfull ${addfull}"           : ''
          ^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:62:9`: `addprofile` is already declared

  ```nextflow
      def addprofile   = addprofile      ? "--addprofile ${addprofile}"     : ''
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:63:9`: `addlong` is already declared

  ```nextflow
      def addlong      = addlong         ? "--addlong ${addlong}"           : ''
          ^^^^^^^
  ```

- Error: `modules/nf-core/prinseqplusplus/main.nf:27:9`: `fasta` is already declared

  ```nextflow
      def fasta = fasta ? "-fastq ${fasta} -FASTA" : ''
          ^^^^^
  ```

- Error: `modules/nf-core/trinity/main.nf:26:20`: Unexpected input: ','

  ```nextflow
      def reads1 = [], reads2 = []
                     ^
  ```

- Error: `nextflow.config:104:39`: `mapper` is not defined

  ```nextflow
      intermediate_mapper             = mapper
                                        ^^^^^^
  ```

- Error: `nextflow.config:111:39`: `variant_caller` is not defined

  ```nextflow
      intermediate_variant_caller     = variant_caller
                                        ^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/fastq_assembly/main.nf:6:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/viralmetagenome/modules/nf-core/trinity/main.nf'

  ```nextflow
  include { TRINITY                                    } from '../../../modules/nf-core/trinity/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/fastq_assembly/main.nf:53:9`: `TRINITY` is not defined

  ```nextflow
          TRINITY(ch_reads)
          ^^^^^^^
  ```

- Error: `subworkflows/local/fastq_assembly/main.nf:55:35`: `TRINITY` is not defined

  ```nextflow
          EXTEND_TRINITY( ch_reads, TRINITY.out.transcript_fasta, "trinity")
                                    ^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/blast_filter/main.nf:48:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/custom_mpileup/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/custom_multiqc/main.nf:79:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/extract_cluster/main.nf:46:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/extract_precluster/main.nf:49:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/ivar_variants_to_vcf/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/make_bed_mask/main.nf:50:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/make_bed_mask/main.nf:51:9`: Variable was declared but not used

  ```nextflow
      def args2 = task.ext.args2 ?: 5
          ^^^^^
  ```

- Warning: `modules/local/make_bed_mask/main.nf:53:9`: Variable was declared but not used

  ```nextflow
      def mpileup = save_mpileup ? "| tee ${prefix}.mpileup" : ""
          ^^^^^^^
  ```

- Warning: `modules/local/select_reference/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/snpeff_build/main.nf:64:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/snpsift_extractfields/main.nf:55:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bbmap/bbduk/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
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

- Warning: `modules/nf-core/bracken/bracken/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/cat/cat/main.nf:23:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def file_list = files_in.collect { it.toString() }
                                         ^^
  ```

- Warning: `modules/nf-core/cat/cat/main.nf:37:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      in_zip   = file_list.any { it.endsWith('.gz') }
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

- Warning: `modules/nf-core/cat/fastq/main.nf:58:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect { it.toString() } : [reads.toString()]
                                                             ^^
  ```

- Warning: `modules/nf-core/cdhit/cdhitest/main.nf:47:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/checkv/downloaddatabase/main.nf:32:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/checkv/endtoend/main.nf:46:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/humid/main.nf:48:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/humid/main.nf:50:9`: Variable was declared but not used

  ```nextflow
      def umis = umi_file ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kaiju/kaiju/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kaiju/kaiju/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def input = meta.single_end ? "-i ${reads}" : "-i ${reads[0]} -j ${reads[1]}"
          ^^^^^
  ```

- Warning: `modules/nf-core/kaiju/kaiju2krona/main.nf:41:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kaiju/kaiju2table/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:61:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:63:9`: Variable was declared but not used

  ```nextflow
      def paired       = meta.single_end ? "" : "--paired"
          ^^^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:66:9`: Variable was declared but not used

  ```nextflow
      def readclassification_option = save_reads_assignment ? "--output ${prefix}.kraken2.classifiedreads.txt" : "--output /dev/null"
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:67:9`: Variable was declared but not used

  ```nextflow
      def compress_reads_command = save_output_fastqs ? "pigz -p $task.cpus *.fastq" : ""
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/krakentools/kreport2krona/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:57:9`: Variable was declared but not used

  ```nextflow
      def args         = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def add          = add             ? "--add ${add}"                   : ''
          ^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def addfragments = addfragments    ? "--addfragments ${addfragments}" : ''
          ^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:61:9`: Variable was declared but not used

  ```nextflow
      def addfull      = addfull         ? "--addfull ${addfull}"           : ''
          ^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def addprofile   = addprofile      ? "--addprofile ${addprofile}"     : ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:63:9`: Variable was declared but not used

  ```nextflow
      def addlong      = addlong         ? "--addlong ${addlong}"           : ''
          ^^^^^^^
  ```

- Warning: `modules/nf-core/mash/screen/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mash/sketch/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/megahit/main.nf:52:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/megahit/main.nf:53:9`: Variable was declared but not used

  ```nextflow
      def args2 = task.ext.args2 ?: ''
          ^^^^^
  ```

- Warning: `modules/nf-core/megahit/main.nf:55:9`: Variable was declared but not used

  ```nextflow
      def reads_command = meta.single_end || !reads2 ? "-r ${reads1}" : "-1 ${reads1.join(',')} -2 ${reads2.join(',')}"
          ^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/minimap2/align/main.nf:67:9`: Variable was declared but not used

  ```nextflow
      def target = reference ?: (bam_input ? error("BAM input requires reference") : reads)
          ^^^^^^
  ```

- Warning: `modules/nf-core/quast/main.nf:53:9`: Variable was declared but not used

  ```nextflow
      def args      = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/quast/main.nf:55:9`: Variable was declared but not used

  ```nextflow
      def features  = gff             ? "--features $gff" : ''
          ^^^^^^^^
  ```

- Warning: `modules/nf-core/quast/main.nf:56:9`: Variable was declared but not used

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

- Warning: `modules/nf-core/vsearch/cluster/main.nf:78:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/align_collapse_contigs/main.nf:12:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/align_collapse_contigs/main.nf:25:67`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_references = ch_references_members.map { meta, references, members -> [meta, references] }
                                                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_call_consensus/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_call_consensus/main.nf:15:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_bam = ch_bam_ref.map { meta, bam, fasta -> [meta, bam] }
                                           ^^^^^
  ```

- Warning: `subworkflows/local/bam_call_consensus/main.nf:16:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta = ch_bam_ref.map { meta, bam, fasta -> [meta, fasta] }
                                        ^^^
  ```

- Warning: `subworkflows/local/bam_call_consensus/main.nf:31:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta.map { it[1] },
                             ^^
  ```

- Warning: `subworkflows/local/bam_call_variants/main.nf:12:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_tbi = Channel.empty()
               ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_call_variants/main.nf:13:5`: Variable was declared but not used

  ```nextflow
      ch_csi = Channel.empty()
      ^^^^^^
  ```

- Warning: `subworkflows/local/bam_call_variants/main.nf:13:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_csi = Channel.empty()
               ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_call_variants/main.nf:14:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_stats = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_call_variants/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_call_variants/main.nf:16:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_deduplicate/main.nf:8:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      umi            // val: [ true | false ]
      ^^^
  ```

- Warning: `subworkflows/local/bam_deduplicate/main.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_deduplicate/main.nf:14:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_stats_filter/main.nf:17:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions             = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_stats_filter/main.nf:18:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fail_mapping_multiqc = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_stats_metrics/main.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_stats_metrics/main.nf:14:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variants_bcftools/main.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variants_ivar/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_vcf_consensus_bcftools/main.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/consensus_qc/main.nf:21:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions        = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/consensus_qc/main.nf:22:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files   = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/consensus_qc/main.nf:23:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_blast           = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/consensus_qc/main.nf:24:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_checkv          = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/consensus_qc/main.nf:25:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_quast           = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/consensus_qc/main.nf:26:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_annotation      = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/consensus_qc/main.nf:27:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_genome_grouped  = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/consensus_qc/main.nf:31:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collectFile(name: "all_genomes.fa") { it[1] }
                                                 ^^
  ```

- Warning: `subworkflows/local/consensus_qc/main.nf:46:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { id, genome, meta -> [meta, genome] }
                 ^^
  ```

- Warning: `subworkflows/local/fasta_contig_preclust/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fasta_contig_preclust/main.nf:19:53`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_contigs = ch_contigs_reads.map{ meta, fasta, reads -> [meta + [single_end:true, og_single_end:meta.single_end], fasta] }
                                                      ^^^^^
  ```

- Warning: `subworkflows/local/fasta_contig_preclust/main.nf:21:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_kaiju = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/fasta_contig_preclust/main.nf:28:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_kraken        = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/fasta_contig_preclust/main.nf:29:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_kraken_report = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/fasta_contig_preclust/main.nf:37:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_classifications = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/fasta_contig_preclust/main.nf:73:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_reads = ch_contigs_reads.map{ meta, fasta, reads -> [meta.sample, meta, reads] }
                                             ^^^^^
  ```

- Warning: `subworkflows/local/fasta_contig_preclust/main.nf:88:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample, meta, fasta ->
                    ^^^^^^
  ```

- Warning: `subworkflows/local/fasta_contig_preclust/main.nf:88:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample, meta, fasta ->
                                  ^^^^^
  ```

- Warning: `subworkflows/local/fasta_contig_preclust/main.nf:92:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample, meta_contig, fasta, meta_reads, reads -> [meta_contig, fasta, reads] }            // select only meta of contigs
                ^^^^^^
  ```

- Warning: `subworkflows/local/fasta_contig_preclust/main.nf:92:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample, meta_contig, fasta, meta_reads, reads -> [meta_contig, fasta, reads] }            // select only meta of contigs
                                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_assembly/main.nf:24:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions    = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_assembly/main.nf:25:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_scaffolds   = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_assembly/main.nf:26:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_coverages   = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_assembly/main.nf:27:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc     = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_assembly/main.nf:28:5`: Variable was declared but not used

  ```nextflow
      bad_assemblies = Channel.empty()
      ^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_assembly/main.nf:28:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bad_assemblies = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_assembly/main.nf:29:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      assemblers     = params.assemblers ? params.assemblers.split(',').collect{ it.trim().toLowerCase() } : []
                                                                                 ^^
  ```

- Warning: `subworkflows/local/fastq_assembly/main.nf:65:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter { it[0].single_end }
                        ^^
  ```

- Warning: `subworkflows/local/fastq_assembly/main.nf:68:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_reads.filter { !it[0].single_end }.map { meta, reads -> [meta, [reads[0]], [reads[1]]] }
                                     ^^
  ```

- Warning: `subworkflows/local/fastq_fasta_iterative_consensus/main.nf:24:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_consensus_allsteps = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fasta_iterative_consensus/main.nf:25:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fasta_iterative_consensus/main.nf:26:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fasta_map_consensus/main.nf:27:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions     = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fasta_map_consensus/main.nf:28:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc      = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fasta_map_consensus/main.nf:29:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_dedup_bam    = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fasta_map_consensus/main.nf:30:52`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_reads_in     = ch_reference_reads.map{meta, ref, reads -> [meta,reads] }
                                                     ^^^
  ```

- Warning: `subworkflows/local/fastq_fasta_map_consensus/main.nf:38:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc   = ch_multiqc.mix(MAP_READS.out.mqc.collect{it[1]}.ifEmpty([]))
                                                              ^^
  ```

- Warning: `subworkflows/local/fastq_fasta_map_consensus/main.nf:45:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc   = ch_multiqc.mix(BAM_STATS_FILTER.out.stats.collect{it[1]}.ifEmpty([]))
                                                                       ^^
  ```

- Warning: `subworkflows/local/fastq_fasta_map_consensus/main.nf:58:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc   = ch_multiqc.mix(BAM_DEDUPLICATE.out.mqc.collect{it[1]}.ifEmpty([]))
                                                                        ^^
  ```

- Warning: `subworkflows/local/fastq_fasta_map_consensus/main.nf:71:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc   = ch_multiqc.mix(BAM_STATS_METRICS.out.mqc.collect{it[1]}.ifEmpty([]))
                                                                          ^^
  ```

- Warning: `subworkflows/local/fastq_fasta_map_consensus/main.nf:76:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_vcf        = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fasta_map_consensus/main.nf:77:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_vcf_filter = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fasta_map_consensus/main.nf:78:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_tbi        = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fasta_map_consensus/main.nf:87:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc    = ch_multiqc.mix(BAM_CALL_VARIANTS.out.mqc.collect{it[1]}.ifEmpty([]))
                                                                           ^^
  ```

- Warning: `subworkflows/local/fastq_fasta_map_consensus/main.nf:113:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_bam_out            = ch_dedup_bam_ref.map{meta,bam,ref -> [meta,bam] }
                                                            ^^^
  ```

- Warning: `subworkflows/local/fastq_fasta_mash_screen/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fastqc_umitools_trimmomatic/main.nf:36:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      save_trimmed_fail // boolean: true/false
      ^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fastqc_umitools_trimmomatic/main.nf:37:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      save_merged       // boolean: true/false
      ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fastqc_umitools_trimmomatic/main.nf:41:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fastqc_umitools_trimmomatic/main.nf:42:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fastqc_raw_html = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fastqc_umitools_trimmomatic/main.nf:43:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fastqc_raw_zip = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fastqc_umitools_trimmomatic/main.nf:53:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_umi_log = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fastqc_umitools_trimmomatic/main.nf:71:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trim_summ           = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fastqc_umitools_trimmomatic/main.nf:72:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trim_unpaired_reads = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fastqc_umitools_trimmomatic/main.nf:73:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trim_log            = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fastqc_umitools_trimmomatic/main.nf:74:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fastqc_trim_html    = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fastqc_umitools_trimmomatic/main.nf:75:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fastqc_trim_zip     = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fastqc_umitools_trimmomatic/main.nf:76:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trim_read_count     = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_kraken_host_remove/main.nf:12:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_kraken_host_remove/main.nf:13:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_kraken_kaiju/main.nf:22:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions            = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_kraken_kaiju/main.nf:23:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files       = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_kraken_kaiju/main.nf:24:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_krona_text          = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_kraken_kaiju/main.nf:25:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_raw_classifications = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/map_reads/main.nf:12:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/map_reads/main.nf:13:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/map_reads/main.nf:15:5`: Variable was declared but not used

  ```nextflow
      ch_reads = ch_reference_reads.map { meta, fasta, fastq -> [meta, fastq] }
      ^^^^^^^^
  ```

- Warning: `subworkflows/local/map_reads/main.nf:15:47`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_reads = ch_reference_reads.map { meta, fasta, fastq -> [meta, fastq] }
                                                ^^^^^
  ```

- Warning: `subworkflows/local/map_reads/main.nf:16:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_reference = ch_reference_reads.map { meta, fasta, fastq -> [meta, fasta] }
                                                           ^^^^^
  ```

- Warning: `subworkflows/local/mmseqs_annotate/main.nf:10:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing_illumina/main.nf:21:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions         = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing_illumina/main.nf:22:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files    = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing_illumina/main.nf:23:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trim_read_count  = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/scaffolds_extend_stats/main.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/scaffolds_extend_stats/main.nf:18:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_scaffolds = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/scaffolds_extend_stats/main.nf:19:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/scaffolds_extend_stats/main.nf:28:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc = ch_multiqc.mix(QUAST.out.tsv.collect { it[1] }.ifEmpty([]))
                                                          ^^
  ```

- Warning: `subworkflows/local/scaffolds_extend_stats/main.nf:52:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_coverages = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/singleton_filtering/main.nf:12:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_viralmetagenome_pipeline/main.nf:29:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_viralmetagenome_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_viralmetagenome_pipeline/main.nf:95:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_viralmetagenome_pipeline/main.nf:326:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return param ? Channel.fromPath(param, checkIfExists: true).collect() : []
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_viralmetagenome_pipeline/main.nf:330:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return dbPath && skipFlag ? Channel.fromPath(dbPath, checkIfExists: true).map { db -> [[id: dbName], db] } : Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_viralmetagenome_pipeline/main.nf:330:114`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return dbPath && skipFlag ? Channel.fromPath(dbPath, checkIfExists: true).map { db -> [[id: dbName], db] } : Channel.empty()
                                                                                                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_viralmetagenome_pipeline/main.nf:345:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, fasta, stats -> ["$meta.id\t$meta.sample\t$meta.cluster_id\t$meta.previous_step\t$stats.contig_size\t$stats.n_100"] }
                       ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_viralmetagenome_pipeline/main.nf:401:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, bam, mapped_reads ->
                       ^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_viralmetagenome_pipeline/main.nf:432:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, txt, fasta ->
                       ^^^
  ```

- Warning: `subworkflows/local/vcf_annotate/main.nf:12:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_tabix_stats/main.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_stats_samtools/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:33:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      catch (Exception ex) {
                       ^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:51:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:52:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_raw_html = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:53:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_raw_zip = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:54:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      umi_log = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:55:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_json = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:56:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_html = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:57:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_log = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:58:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_reads_fail = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:59:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_reads_merged = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:60:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_trim_html = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:61:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_trim_zip = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:62:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_read_count = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:63:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      adapter_seq = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:66:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      reads_only = reads.map { meta, reads_files, adapter_fasta -> [ meta, reads_files ] }
                                                  ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:104:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { sample_id, meta, umi_reads_files, adapter_fasta -> [meta, umi_reads_files, adapter_fasta] }
                     ^^^^^^^^^
  ```

- Warning: `workflows/viralmetagenome.nf:70:100`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def read_classifiers   = params.read_classifiers ? params.read_classifiers.split(',').collect{ it.trim().toLowerCase() } : []
                                                                                                     ^^
  ```

- Warning: `workflows/viralmetagenome.nf:71:112`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def contig_classifiers = params.precluster_classifiers ? params.precluster_classifiers.split(',').collect{ it.trim().toLowerCase() } : []
                                                                                                                 ^^
  ```

- Warning: `workflows/viralmetagenome.nf:78:5`: Variable was declared but not used

  ```nextflow
      ch_adapter_fasta   = createFileChannel(params.adapter_fasta)
      ^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/viralmetagenome.nf:124:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_ref_pool         = ch_db.reference.collect{it[1]}.ifEmpty([]).map{it -> [[id: 'reference'], it]}
                                                        ^^
  ```

- Warning: `workflows/viralmetagenome.nf:125:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_annotation_db    = ch_db.annotation.collect{it[1]}.ifEmpty([]).map{it -> [[id: 'annotation'], it]}
                                                         ^^
  ```

- Warning: `workflows/viralmetagenome.nf:148:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_blast_refdb  = ch_blastdb_out.reference.collect{it[1]}.ifEmpty([]).map{it -> [[id: 'reference'], it]}
                                                             ^^
  ```

- Warning: `workflows/viralmetagenome.nf:165:95`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files        = ch_multiqc_files.mix(PREPROCESSING_ILLUMINA.out.mqc.collect{it[1]}.ifEmpty([]))
                                                                                                ^^
  ```

- Warning: `workflows/viralmetagenome.nf:179:84`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FASTQ_KRAKEN_KAIJU.out.mqc.collect{it[1]}.ifEmpty([]))
                                                                                     ^^
  ```

- Warning: `workflows/viralmetagenome.nf:238:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_clusters_summary    = FASTA_CONTIG_CLUST.out.clusters_summary.collect{it[1]}.ifEmpty([])
                                                                                       ^^
  ```

- Warning: `workflows/viralmetagenome.nf:239:82`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_clusters_tsv        = FASTA_CONTIG_CLUST.out.clusters_tsv.collect{it[1]}.ifEmpty([])
                                                                                   ^^
  ```

- Warning: `workflows/viralmetagenome.nf:351:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mash_screen = FASTQ_FASTA_MASH_SCREEN.out.json.collect{it[1]}
                                                                    ^^
  ```

- Warning: `workflows/viralmetagenome.nf:413:83`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files      = ch_multiqc_files.mix(CONSENSUS_QC.out.mqc.collect{it[1]}.ifEmpty([]))
                                                                                    ^^
  ```

- Warning: `workflows/viralmetagenome.nf:414:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_checkv_summary     = CONSENSUS_QC.out.checkv.collect{it[1]}.ifEmpty([])
                                                                  ^^
  ```

- Warning: `workflows/viralmetagenome.nf:415:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_quast_summary      = CONSENSUS_QC.out.quast.collect{it[1]}.ifEmpty([])
                                                                 ^^
  ```

- Warning: `workflows/viralmetagenome.nf:416:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_blast_summary      = CONSENSUS_QC.out.blast.collect{it[1]}.ifEmpty([])
                                                                 ^^
  ```

- Warning: `workflows/viralmetagenome.nf:417:69`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_annotation_summary = CONSENSUS_QC.out.annotation.collect{it[1]}.ifEmpty([])
                                                                      ^^
  ```

- Warning: `workflows/viralmetagenome.nf:424:5`: Variable was declared but not used

  ```nextflow
      ch_multiqc_custom_config              = params.multiqc_config              ? channel.fromPath(params.multiqc_config, checkIfExists: true) : channel.empty()
      ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/viralmetagenome.nf:425:5`: Variable was declared but not used

  ```nextflow
      ch_multiqc_logo                       = params.multiqc_logo                ? channel.fromPath(params.multiqc_logo, checkIfExists: true) : channel.empty()
      ^^^^^^^^^^^^^^^
  ```
