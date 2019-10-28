import configparser
import random
import string


def get_config(filepath='config'):
    """
    Return the config file
    :param filepath:  Path of the conf file
    :return: ConfigParser object
    """
    config = configparser.ConfigParser()
    config.read(filepath)
    return config


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


def random_size_moons():
    config = get_config()
    min_nb_moons = int(config['MOONS']['min_nb_moons'])
    max_nb_moons = int(config['MOONS']['max_nb_moons'])
    min_size_moon = int(config['MOONS']['min_size_moon'])
    max_size_moon = int(config['MOONS']['max_size_moon'])

    nb_moons = random.randint(min_nb_moons, max_nb_moons)
    moons = []

    for i in range(nb_moons):
        moons.append(random.randint(min_size_moon, max_size_moon))

    moons.sort()
    return moons


def total_size_moons(moon_list):
    config = get_config()
    distance_moon = int(config['MOONS']['distance_moon'])

    distance = (len(moon_list) - 1) * distance_moon
    moons_ls = [i * 2 for i in moon_list]
    return int((sum(moons_ls) + distance) / 2 - moon_list[0])


def random_name():
    with open('latin_names.txt', 'r') as infile:
        data = infile.readlines()
    return random.choice(data).strip()


def split_str(string, n):
    return [string[i:i + n] for i in range(0, len(string), n)]


def generate_id(id_size, nb_id):
    _id = ''
    for i in range(nb_id):
        _id += ''.join(random.choices(string.ascii_lowercase + string.digits, k=id_size))
    return _id
