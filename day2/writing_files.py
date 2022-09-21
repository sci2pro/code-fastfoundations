import sys


def writing_to_text_files():
    with open("my_fancy_file.txt", 'w') as f:
        f.write("1")  # no newline at the end
        f.write("2")  # no newline at the end
        f.write("3")  # no newline at the end
        f.write("4\n")  # now we add a new line
        f.write("5\n")  # again
    with open("my_fancy_file.txt") as f:
        print(f"{f.read() = }")
    lines_of_text = [
        "Knowledge is power.",
        "Power to do evil... or power to do good.",
        "Power itself is not evil.",
        "So knowledge itself is not evil.",
        "― Veronica Roth, Allegiant",
    ]
    with open("power_quote.txt", 'w') as f:
        f.writelines(map(lambda s: s + '\n', lines_of_text))
    with open("power_quote.txt") as f:
        print(f.readlines())


def creating_and_modifying_paths():
    import pathlib
    import datetime
    my_path = pathlib.Path("dir7/new_file.txt")  # a non-existent path
    col1 = 80
    print(f"{str(my_path.absolute()):{col1}}: {my_path.exists() = }")
    # with my_path.open('w') as f: # FileNotFoundError
    #     print(f"{datetime.datetime.now() = }\n", file=f) # another way to write to a file
    my_path.parent.mkdir()  # need to create the parent first
    print(f"{str(my_path.parent.absolute()):{col1}}: {my_path.parent.exists() = }")
    with my_path.open('w') as f:  # write
        print(f"{datetime.datetime.now() = }\n", file=f)  # another way to write to a file
    print(f"{str(my_path.absolute()):{col1}}: {my_path.exists() = }")
    # my_path.parent.rmdir() # FileExistsError
    my_path.unlink()
    print(f"{str(my_path.absolute()):{col1}}: {my_path.exists() = }")
    my_path.parent.rmdir()
    print(f"{str(my_path.parent.absolute()):{col1}}: {my_path.parent.exists() = }")


def parsing_text_files():
    with open("Homo_sapiens.GRCh38.107.abinitio.gtf") as f:
        for row in f:  # files are iterators
            print(row.strip())  # remove trailing \n
    with open("Homo_sapiens.GRCh38.107.abinitio.gtf") as f:
        for row in f:
            cols = row.strip().split("\t")
            print(cols)


def file_with_random_text():
    import pathlib
    my_path = pathlib.Path("dir1/dir3/dir5/some_random_random.txt")
    my_path.parent.mkdir(exist_ok=True)
    with my_path.open('w') as f:
        f.write('some random text in a random file\n')


def parse_gtf_file():
    import re
    with open("Homo_sapiens.GRCh38.107.abinitio.gtf") as f:
        for row in f:
            if not re.search(r"^\s*#", row):  # use a regular expression
                # also, simpler would be 'if row[0] != "#"' but this can by bypassed easily if a space is present
                cols = row.strip().split("\t")
                if cols[2] == 'exon':  # now filter only exons
                    print(cols)


def fixing_the_broken_code():
    data = range(10)
    with open("file.txt", 'w') as f:
        for d in data:
            f.write(str(d) + "\n")  # we should make d a string; we can't use the + operator between int and str


def separate_by_chromosome():
    """We need each chromosome to have its own file. The most straightforward solution is to collect the data into
    individual lists then write them later. We can organise all our lists into a single dictionary of
    chromosome to lists of lines like follows:

    my_data = {
        '1': [<rows for chromosome 1>],
        '2': [<rows for chromosome 2>],
        ...
    }
    """
    import re
    my_data = dict()
    with open("Homo_sapiens.GRCh38.107.shuffled_and_truncated.gtf") as f:
        for row in f:
            if not re.search(r"^\s*#", row):
                # first we get the columns using strip then split
                cols = row.strip().split("\t")
                # next we check if the chromosome is in the dictionary
                # if it is not we make a new list with the row unchanged
                # if it is then we append at the end of the existing list
                if cols[0] not in my_data:  # col[0] is the chromosome
                    my_data[cols[0]] = [row]  # keep the newlines so that we just write to file later
                else:
                    # .append() because my_data[cols[0]] is a list
                    my_data[cols[0]].append(row)
    # once we are done we can write to files
    for chromosome, rows in my_data.items():  # the key is the name of the chromosome; values is the list of rows
        # make a new filename with the chromosome as part of it
        with open(f"Homo_sapiens.GRCh38.107.shuffled_and_truncated.{chromosome}.gtf", 'w') as f:
            for row in rows:
                f.write(row)  # each row still has the newlines at the end


def separate_by_gene_id():
    """Our code here will be more or less the same as in 'separate_by_chromosome' only that we now group in the
    dictionary by 'gene_id' (same for 'transcript_id')

    The main difference here is that we now have to do a second layer of processing to get the gene_id or
    transcript_id.

    The last column is special. Everything from 'gene_id' to the end is one column. The characters ';<space>' are
    the sub-column delimiters.

    Therefore, we need to split this again as follows:

    subcols = cols[8].split('; ')
    gene_str = subcols[0] # e.g. 'gene_id "ENSG00000130396"'

    This has to be further split to get the actual gene id. Fortunately, Ensembl gene IDs have a fixed length so
    we can extract this using a slice.

    gene_id = gene_str[9:-1] # exclude the last '"' character

    """
    import re
    my_data = dict()
    with open("Homo_sapiens.GRCh38.107.shuffled_and_truncated.gtf") as f:
        for row in f:
            if not re.search(r"^\s*#", row):
                # first we get the columns using strip then split
                cols = row.strip().split("\t")
                subcols = cols[8].split('; ')
                gene_str = subcols[0]
                gene_id = gene_str[9:-1]
                print(gene_id)
                # next we check if the gene_id is in the dictionary
                # if it is not we make a new list with the row unchanged
                # if it is then we append at the end of the existing list
                if gene_id not in my_data:  # col[0] is the gene_id
                    my_data[gene_id] = [row]  # keep the newlines so that we just write to file later
                else:
                    # .append() because my_data[cols[0]] is a list
                    my_data[gene_id].append(row)
    # once we are done we can write to files
    for gene_id, rows in my_data.items():  # the key is the name of the gene_id; values is the list of rows
        # make a new filename with the gene_id as part of it
        with open(f"Homo_sapiens.GRCh38.107.shuffled_and_truncated.{gene_id}.gtf", 'w') as f:
            for row in rows:
                f.write(row)  # each row still has the newlines at the end

def get_exons_by_gene():
    """Here we will use a dictionary to get all the exons associated with a particular gene
    based on the gene/transcript ID. We will do this for gene but you can modify the function
    to work for transcripts.

    For each exon, we can add a column of the exon length then we can print the longest
    exon for each gene.

    Because the file is truncated most of the genes/transcripts will only have one exon. If you run
    this with the full GTF file then you will get much more meaningful data.
    """
    import re
    # first, we compile exons by gene
    # to do this we need to be able to identify the gene id
    exons_by_gene_id = dict()
    with open("Homo_sapiens.GRCh38.107.shuffled_and_truncated.gtf") as f:
        for row in f:
            if not re.search(r"^\s*#", row): # only non-comments
                cols = row.strip().split('\t')
                # as before, we need to extract the gene_id from the last column
                # the last column has subcolumns separated by '; ' (note: two characters)
                subcols = cols[8].split('; ')
                # again, because Ensembl IDs are fixed length we can use slicing of the string for the gene ID
                gene_id = subcols[0][9:-1]
                if cols[2] == 'exon': # now we only get exons
                    start_pos = int(cols[3])
                    end_pos = int(cols[4])
                    if gene_id not in exons_by_gene_id:
                        # we will collect the exons into a list of tuples
                        # (length, row)
                        exons_by_gene_id[gene_id] = [(end_pos - start_pos, row)]
                    else:
                        exons_by_gene_id[gene_id] += [(end_pos - start_pos, row)]
    # now we can print the longest exons for each gene
    for gene_id, exons in exons_by_gene_id.items(): # 'exons' is a list of exons
        # this is how we can sort using sorted:
        # the second argument to sorted is which field/attribute to sort by
        # here we use a lambda to point to the length of the exon
        # which is the first item in the tuple (length, row)
        # we use reverse=True so that the longest is sorting is longest->shortest
        sorted_exons = sorted(exons, key=lambda e: e[0], reverse=True)
        # we can now get the longest: index 0
        longest_exon = sorted_exons[0][1]
        print(f"{gene_id}\t{longest_exon.strip()}")
        # exercise: write this to a file


def main():
    # writing_to_text_files()
    # creating_and_modifying_paths()
    # parsing_text_files()
    # file_with_random_text()
    # parse_gtf_file()
    # separate_by_chromosome()
    # separate_by_gene_id()
    get_exons_by_gene()
    return 0


if __name__ == '__main__':
    sys.exit(main())
