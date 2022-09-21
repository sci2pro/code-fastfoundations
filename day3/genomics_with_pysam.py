import sys

import pysam


def pysam_read_sam_file():
    samfile = pysam.AlignmentFile("genomics_workout/SRR20334685/SRR20334685.sam", "r")
    count = 0
    for read in samfile:
        if count > 10:
            break
        print(f"{read = }")  # https://pysam.readthedocs.io/en/latest/api.html#pysam.AlignedSegment
        count += 1
        # print(f"{read.bin = }")
        # print(f"{read.cigarstring = }")
        # print(f"{read.get_aligned_pairs() = }")
    samfile.close()


def pysam_read_bam_file():
    with pysam.AlignmentFile("genomics_workout/SRR20334685/SRR20334685.final.bam") as bamfile:
        # fetch by region
        for read in bamfile.fetch("I", 1000, 2000):
            print(f"{read = }")  # https://pysam.readthedocs.io/en/latest/api.html#pysam.AlignedSegment
            print(f"{read.get_forward_sequence() = }")
            print(f"{len(read.get_forward_sequence())}")
            print(f"{read.get_forward_qualities() = }")
            print(f"{read.get_reference_positions() = }")


def pysam_get_pileup():
    with pysam.AlignmentFile("genomics_workout/SRR20334685/SRR20334685.final.bam") as bamfile:
        # reads associated with positions
        for pileup_column in bamfile.pileup("I", 1750, 1751):
            # print(f"{pileup_column = }") # https://pysam.readthedocs.io/en/latest/api.html#pysam.PileupColumn
            print(f"{pileup_column.get_num_aligned() = }")
            print(f"{pileup_column.get_query_sequences() = }")
            print(f"{pileup_column.get_query_positions() = }")
            print(f"{pileup_column.get_query_qualities() = }")


def htseq_read_fastq():
    import HTSeq
    import itertools
    with HTSeq.FastqReader("genomics_workout/SRR20334685/SRR20334685.fastq") as fastq_file:
        for read in itertools.islice(fastq_file, 10):
            print(f"{read = }")  # https://htseq.readthedocs.io/en/master/refoverview.html
            print(f"{read.qual = }")  # https://htseq.readthedocs.io/en/master/refoverview.html


def main():
    # pysam_read_sam_file()
    # pysam_read_bam_file()
    # pysam_get_pileup()
    htseq_read_fastq()
    return 0


if __name__ == '__main__':
    sys.exit(main())
