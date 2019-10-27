import random

MIN_NB_MOONS = 1
MAX_NB_MOONS = 5
MIN_SIZE_MOON = 5
MAX_SIZE_MOON = 30
DISTANCE_MOON = 15


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
    nb_moons = random.randint(MIN_NB_MOONS, MAX_NB_MOONS)
    moons = []

    for i in range(nb_moons):
        moons.append(random.randint(MIN_SIZE_MOON, MAX_SIZE_MOON))

    moons.sort()
    return moons


def total_size_moons(moon_list):
    distance = (len(moon_list) - 1) * DISTANCE_MOON
    moons_ls = [i * 2 for i in moon_list]
    return int((sum(moons_ls) + distance) / 2 - moon_list[0])


def random_name():
    with open('latin_names.txt', 'r') as infile:
        data = infile.readlines()
    return random.choice(data).strip()
