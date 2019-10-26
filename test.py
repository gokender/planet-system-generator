import random
from lxml import etree

WIDTH = 1000
HEIGHT = 1000

MIN_NB_MOONS = 1
MAX_NB_MOONS = 5
MIN_SIZE_MOON = 5
MAX_SIZE_MOON = 30
DISTANCE_MOON = 15


def generate_size_moons():
    nb_moons = random.randint(MIN_NB_MOONS, MAX_NB_MOONS)
    print(nb_moons)

    moons = []

    for i in range(nb_moons):
        moons.append(random.randint(MIN_SIZE_MOON, MAX_SIZE_MOON))

    moons.sort()
    print(moons)

    return moons


def total_size_moons(moon_list):
    distance = (len(moon_list) - 1) * DISTANCE_MOON
    moons_ls = [i * 2 for i in moon_list]
    return int((sum(moons_ls) + distance) / 2 - moon_list[0])


def calculate_pos_x2(oax, oarx, obrx):
    return oax + oarx + DISTANCE_MOON + obrx


root = etree.Element('svg', width=str(WIDTH), height=str(HEIGHT), xmlns='http://www.w3.org/2000/svg')

########## BACKGROUND
background_group = etree.SubElement(root, 'g')
title = etree.SubElement(background_group, 'title').text = 'background'
rect = etree.SubElement(background_group, 'rect', x='-1', y='-1', width=str(WIDTH + 2), height=str(HEIGHT + 2),
                        id='background', fill='#000000')

planet_x = int(WIDTH / 2)
planet_y = int(HEIGHT / 2)
rand_size = 100

planet = etree.SubElement(root, 'ellipse', id='planet')

planet.set('cx', str(planet_x))
planet.set('cy', str(planet_y))
planet.set('rx', str(rand_size))
planet.set('ry', str(rand_size))

planet.set('fill', '#000000')
planet.set('stroke', '#ffffff')
planet.set('stroke-width', '2')

rand_size = 20

moons = generate_size_moons()
moons = [20, 25, 30]

diff_pos_moon = total_size_moons(moons)
list_moons = []
previous_moon = ()
cpt = 0
for moo in moons:
    if cpt == 0:
        moon = etree.Element('ellipse', id='moon_{}'.format(cpt))
        moon.set('cx', str(planet_x - diff_pos_moon))
        moon.set('cy', str(0.75 * HEIGHT))
        moon.set('rx', str(moo))
        moon.set('ry', str(moo))

        moon.set('fill', '#000000')
        moon.set('stroke', '#ffffff')
        moon.set('stroke-width', '2')

        list_moons.append(moon)
        previous_moon = (planet_x - diff_pos_moon, moo)
    else:
        moon_value = calculate_pos_x2(previous_moon[0], previous_moon[1], moo)

        moon = etree.Element('ellipse', id='moon_{}'.format(cpt))
        moon.set('cx', str(moon_value))
        moon.set('cy', str(0.75 * HEIGHT))
        moon.set('rx', str(moo))
        moon.set('ry', str(moo))

        moon.set('fill', '#000000')
        moon.set('stroke', '#ffffff')
        moon.set('stroke-width', '2')

        list_moons.append(moon)
        previous_moon = (moon_value, moo)

    cpt += 1

for m in list_moons:
    root.append(m)

data = etree.tostring(root, pretty_print=True).decode('utf8')
file_res = open('moon.svg', 'w')
file_res.write(data)


def calculate_pos_x(oax, oarx, obrx):
    return oax + oarx + DISTANCE_PLANET + obrx


def calculate_pos_x2(oax, oarx, obrx):
    return oax + oarx + DISTANCE_MOON + obrx


def create_ring(cx, cy, ray):
    rings = []
    nb_rings = random.randint(MIN_RING, MAX_RING)
    rotation_rings = random.randint(0, 360)
    print(nb_rings)

    for i in range(nb_rings):
        cpt = i * 5
        path = 'M{pos_x},{pos_y} a{distor},{distor2} 0 1,0 {ray},0'.format(pos_x=cx - ray, pos_y=cy - cpt,
                                                                           distor=(2 * ray) + cpt, distor2=15 + cpt,
                                                                           ray=2 * ray)

        ring = etree.Element('path')
        ring.set('d', path)
        ring.set('fill', 'none')
        ring.set('stroke', '#ffffff')
        ring.set('stroke-width', '1.5')
        ring.set('transform', 'rotate({} {},{})'.format(rotation_rings, cx, cy))
        rings.append(ring)

    return rings


def get_first_position_x(cx, nb_moons):
    total_size = 0
    moons_dict = {}
    moons = []

    for i in range(nb_moons):
        distance = i * DISTANCE_MOON
        rand_size = random.randint(MIN_SIZE_MOON, MAX_SIZE_MOON)
        total_size += rand_size + distance

        moons.append(rand_size)

    moons_dict['first_pos_x'] = int(cx - (total_size / 2))
    moons_dict['moons'] = moons
    print(moons_dict)

    return moons_dict


def create_moons(cx, cy):
    nb_moons = 2
    moons_dict = get_first_position_x(cx, nb_moons)
    previous_moon = (moons_dict['first_pos_x'] - moons_dict['moons'][0], moons_dict['moons'][0])
    moons = []

    for moon in moons_dict['moons']:
        moon_x = calculate_pos_x2(previous_moon[0], previous_moon[1], moon)
        moon_y = int(0.75 * HEIGHT)
        rand_moon_size = moon

        print('MOON')
        print(moon_x, moon_y, rand_moon_size)

        moon = etree.Element('ellipse')
        moon.set('id', 'moon')
        moon.set('cx', str(moon_x))
        moon.set('cy', str(moon_y))
        moon.set('rx', str(rand_moon_size))
        moon.set('ry', str(rand_moon_size))

        moon.set('fill', '#000000')
        moon.set('stroke', '#ffffff')
        moon.set('stroke-width', '1.5')

        moons.append(moon)

        previous_moon = (moon_x, rand_moon_size)

    return moons
