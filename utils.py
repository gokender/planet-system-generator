import random
import string
import os

def new_pos_x(oa_cx, oa_rx, ob_rx, distance):
    """
    Calcul la prochaine position X de l'objet B en fonction de l'objet A
    :param oa_cx: position x de l'objet A
    :param oa_rx: rayon x de l'objet A
    :param ob_rx: rayon x de l'objet B
    :param distance: distance entre les objets
    :return:
    """
    return oa_cx + oa_rx + distance + ob_rx


def random_size_moons(options):

    min_nb_moons = options.min_nb_moons
    max_nb_moons = options.max_nb_moons
    min_size_moon = options.min_size_moon
    max_size_moon = options.max_size_moon

    nb_moons = random.randint(min_nb_moons, max_nb_moons)
    moons = []

    for i in range(nb_moons):
        moons.append(random.randint(min_size_moon, max_size_moon))

    moons.sort()
    return moons


def total_size_moons(moon_list, options):

    distance_moon = options.distance_moon

    distance = (len(moon_list) - 1) * distance_moon
    moons_ls = [i * 2 for i in moon_list]
    return int((sum(moons_ls) + distance) / 2 - moon_list[0])


def random_name():
    with open(os.path.join('data', 'latin_names.txt'), 'r') as infile:
        data = infile.readlines()
    return random.choice(data).strip()


def split_str(string_msg, n):
    return [string_msg[i:i + n] for i in range(0, len(string_msg), n)]


def generate_id(id_size, nb_id):
    _id = ''
    for i in range(nb_id):
        _id += ''.join(random.choices(string.ascii_lowercase + string.digits, k=id_size))
    return _id
