import random
import string

def randomize_it(value, type = "str"):
    if value == "random":
        if type == "str":
            return generate_str()
        if type == "year":
            return str(random.randint(1990,2017))
        if type == "day_of_month":
            return str(random.randint(1,28))
        if type == "month":
            month_dict={1:"January",
                        2:"Febuary",
                        3:"March",
                        4:"April",
                        5:"May",
                        6:"June",
                        7:"July",
                        8:"August",
                        9:"September",
                        10:"October",
                        11:"November",
                        12:"December"}
            return month_dict[random.randint(1, 12)]
    else:
        return value

def generate_str():
    return ''.join([random.choice(string.ascii_letters+string.digits) for i in range(random.randrange(20))])