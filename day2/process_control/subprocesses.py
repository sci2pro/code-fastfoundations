""""""
import os
import shlex
import subprocess
import sys
import time


def simplest_way():
    process = subprocess.run(
        # shlex.split("sleep 10")
        shlex.split("""echo '''He said, "She said, 'No!'"'''""")
    )
    print(f"{process = }")
    print(f"{process.args = }")
    print(f"{process.returncode = }")
    print(f"{process.stdout = }")
    print(f"{process.stderr = }")


def create_subprocess():
    # https://docs.python.org/3/library/subprocess.html#popen-constructor
    print(f"{os.getpid() = }")  # the process id for this module's process
    process = subprocess.Popen(
        shlex.split(
            "python /Users/paulkorir/PycharmProjects/code-fastfoundations/"
            "day2/process_control/simple_task.py"
        ),
        stdin=subprocess.PIPE,  # necessary to communicate the input value
        stdout=subprocess.PIPE,  # necessary to retrieve the output values
        stderr=subprocess.PIPE  # ditto
    )
    print(f"{process.pid = }")
    stdout, stderr = process.communicate(input=b"2\n0.3333333\n10\n")  # send input; receive output; bytes
    print(f"{process = }")
    print(f"{stdout = }")
    print(f"{stderr = }")
    print(f"{process.returncode = } 👍")  # exit code


def stop_subprocess():
    print(f"{os.getpid() = }")
    process = subprocess.Popen(
        shlex.split("sleep 1000")
    )
    print(f"{process.pid = }")
    print(f"Parent will now sleep for 5s...")
    time.sleep(5)
    print(f"Hmm... This is taking too long!")
    print(f"{process.poll() = } (None = 'still running')")
    time.sleep(5)
    print(f"That's it! I've had it!")
    process.kill()
    stdout, stderr = process.communicate()
    print(f"{stdout = }")
    print(f"{stderr = }")
    print(f"{process.returncode = } 😵")  # exit code


def main():
    # simplest_way()
    # create_subprocess()
    stop_subprocess()
    return 0


if __name__ == '__main__':
    sys.exit(main())
