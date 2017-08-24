from model.group import Group
import random
import string
import os.path
import jsonpickle
import sys
import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def generate_str(prefix = "", maxlen = 20):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix+''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name = "", header = "", footer = "")] + [
           Group(name = generate_str("name", 10),
                 header = generate_str("header", 20),
                 footer = generate_str("footer", 20))
            for i in range(n)
            ]

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", f)

with open(file_path, "w") as out:
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))