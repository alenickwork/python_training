from model.group import Group
testdata = [
    Group(name = "name1", header = "header1", footer = "footer1"),
    Group(name = "name2", header = "header2", footer = "footer2"),
]

# import random
# import string

# def generate_str(prefix = "", maxlen = 20):
#     symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
#     return prefix+''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# testdata = [Group(name = "", header = "", footer = "")] + [
#            Group(name = generate_str("name", 10),
#                  header = generate_str("header", 20),
#                  footer = generate_str("footer", 20))
#             for i in range(5)
#             ]

