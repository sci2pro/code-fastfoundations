import sys


def working_with_gzip_files():
    import gzip
    # read
    with gzip.open(
            "dir1/dir3/dir4/our_deepest_fear.txt.gz",
            mode='rt',
            encoding='utf-8'
    ) as g:
        text = g.read()
        print(type(text))
    # write
    with gzip.open(
            "dir1/dir3/dir4/youth.txt.gz",
            'wb'
    ) as g:  # a binary file
        # g.write("It takes a very long time to become young.\n") # TypeError
        # g.write("― Pablo Picasso\n") # TypeError
        g.write("It takes a very long time to become young.\n".encode('utf-8'))
        g.write("― Pablo Picasso\n".encode('utf-8'))
    with gzip.open(
            "dir1/dir3/dir4/youth.txt.gz"
    ) as g:
        print(g.read())


def read_json_file():
    import json
    import datetime
    import requests  # view documentation https://requests.readthedocs.org
    response = requests.get("http://api.geneontology.org/api/bioentity/NCBIGene%3A84570")
    print(f"{type(response) = }")  # a requests.models.Response object
    print(f"{response.status_code = } 👍")  # 200 is OK
    print(f"{response.text = }")
    data = json.loads(response.text)  # actually, response.json() does this already!
    print(f"{data = }")
    print(f"{type(data) = }")  # OMG!
    # now we can modify it
    data['retrieved'] = datetime.datetime.now().isoformat()
    # then we write it out
    with open("NCBIGene:84570.json", 'w') as j:
        json.dump(data, j, indent=4)


def working_with_binary_data():
    import random
    import struct
    import zlib
    random.seed(1234)  # seeding the RNG
    data = [random.random() for _ in range(10)]  # get <count> rands
    print(f"{data = }")
    print(f"{type(data[0]) = }")
    bin_data = struct.pack(f'<10f', *data)
    print(f"{bin_data = }")
    data2 = struct.unpack(f'<10f', bin_data)
    print(f"{data2 = }")

    str_data = ','.join(map(str, data))  # convert numbers to strings with commas between
    print(f"str_data:     [{len(str_data)} bytes]\n\t* {str_data[:100]}...")
    print(f"bin_data:     [{len(bin_data)} bytes]\n\t* {bin_data[:100]}...")
    zip_bin_data = zlib.compress(bin_data)
    print(f"zip_bin_data: [{len(zip_bin_data)} bytes]\n\t* {zip_bin_data[:100]}...")


def compressing_binary_data():
    import random
    import struct
    import zlib
    random.seed(1234)  # seeding the RNG
    data = [random.random() for _ in range(10)]  # get <count> rands
    print(f"{data = }")
    bin_data = struct.pack(f'<10f', *data)
    print(f"{bin_data = }")
    zip_bin_data = zlib.compress(bin_data)
    print(f"{zip_bin_data = }")
    bin_data2 = zlib.decompress(zip_bin_data)
    data2 = struct.unpack(f'<10f', bin_data2)
    print(f"{data2 = }")


def convert_gtf_to_gz():
    import gzip
    with open("Homo_sapiens.GRCh38.107.shuffled_and_truncated.gtf") as f, gzip.open(
            "Homo_sapiens.GRCh38.107.shuffled_and_truncated_zipped.gtf.gz", 'wb') as g:
        for row in f:
            g.write(row.encode('utf-8'))

    with gzip.open("Homo_sapiens.GRCh38.107.shuffled_and_truncated_zipped.gtf.gz") as g:
        for row in g:
            print(row)

    import pathlib
    uncompressed_path = pathlib.Path("Homo_sapiens.GRCh38.107.shuffled_and_truncated.gtf")
    print(f"{uncompressed_path.stat() = }")
    print(f"{uncompressed_path.stat().st_size = }")
    compressed_path = pathlib.Path("Homo_sapiens.GRCh38.107.shuffled_and_truncated_zipped.gtf.gz")
    print(f"{compressed_path.stat() = }")
    print(f"{compressed_path.stat().st_size = }")
    print(f"compression ratio: {uncompressed_path.stat().st_size / compressed_path.stat().st_size}")
    print(f"space saving: {(1 - compressed_path.stat().st_size / uncompressed_path.stat().st_size) * 100:.4f}%")


def binary_float_and_ints():
    import struct
    import random
    int_data = [random.randint(0, 200) for _ in range(1000)]  # get <count> rands
    float_data = [random.random() for _ in range(1000)]  # get <count> rands
    bin_data = struct.pack("<1000i", *int_data)
    bin_data += struct.pack("<1000f", *float_data)
    return bin_data


def revert_to_actual_from_binary(bin_data):
    import struct
    int_data = struct.unpack("<1000i", bin_data[:4000])
    print(f"{int_data[-10:]}")
    print(f"{len(bin_data[4001:]) = }")
    float_data = struct.unpack("<1000f", bin_data[4000:])
    print(f"{float_data[-10:]}")


def main():
    # working_with_gzip_files()
    # read_json_file()
    # working_with_binary_data()
    # compressing_binary_data()
    # convert_gtf_to_gz()
    bin_data = binary_float_and_ints()
    actual_data = revert_to_actual_from_binary(bin_data)
    return 0


if __name__ == '__main__':
    sys.exit(main())
