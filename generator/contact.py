from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import sys
import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def generate_str(prefix = "", maxlen = 20):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix+''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="",
                       middlename="",
                       lastname="",
                       nickname="",
                       title="",
                       company="",
                       address="",
                       home_phone="",
                       mobile_phone="",
                       work_phone="",
                       fax="",
                       email_prior="",
                       email_2="",
                       email_3="",
                       homepage="",
                       address_secondary="",
                       phone_secondary="",
                       notes="")] + [
    Contact(firstname=generate_str("firstname", random.randint(5,10)),
                       middlename=generate_str("middlename", random.randint(5,10)),
                       lastname=generate_str("lastname", random.randint(5,10)),
                       nickname=generate_str("nickname", random.randint(5,10)),
                       title=generate_str("title", random.randint(5,10)),
                       company=generate_str("company", random.randint(5,10)),
                       address=generate_str("address", random.randint(5,10)),
                       home_phone=generate_str("home_phone", random.randint(5,10)),
                       mobile_phone=generate_str("mobile_phone", random.randint(5,10)),
                       work_phone=generate_str("work_phone", random.randint(5,10)),
                       fax=generate_str("fax", random.randint(5,10)),
                       email_prior=generate_str("email_prior", random.randint(5,10)),
                       email_2=generate_str("email_2", random.randint(5,10)),
                       email_3=generate_str("email_3", random.randint(5,10)),
                       homepage=generate_str("homepage", random.randint(5,10)),
                       address_secondary=generate_str("address_secondary", random.randint(5,10)),
                       phone_secondary=generate_str("phone_secondary", random.randint(5,10)),
                       notes=generate_str("notes", random.randint(5,10)))
            for i in range(n)
            ]

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", f)

with open(file_path, "w") as out:
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))