import random
from lxml import etree

WIDTH = 2500
HEIGHT = 1080

NB_STARS = 1000
MIN_SIZE_STARS = 2
MAX_SIZE_STARS = 4
COLOR_PROBA = 0.3

NB_PLANETS = 5
DISTANCE_PLANET = 150

MIN_SIZE_PLANET = 50
MAX_SIZE_PLANET = 200

RING_PROBA = 0.3
MIN_RING = 2
MAX_RING = 5

MIN_NB_MOONS = 1
MAX_NB_MOONS = 5
MIN_SIZE_MOON = 5
MAX_SIZE_MOON = 30
DISTANCE_MOON = 15
MOON_PROBA = 0.2

COLOR_PALETTE = ['#E5BEED', '#7D5C65', '#7C90DB', '#DA3E52', '#F2E94E']


def sun_size(height):
    return int(height * 0.75)


def sun_x(height):
    return int(height * (-0.358))  # calcul du ratio


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


sun_size = sun_size(HEIGHT)
sun_x = sun_x(HEIGHT)
sun_y = int(HEIGHT / 2)
print(sun_size, sun_x, sun_y)

root = etree.Element('svg', width=str(WIDTH), height=str(HEIGHT), xmlns='http://www.w3.org/2000/svg')

########## BACKGROUND
background_group = etree.SubElement(root, 'g')
title = etree.SubElement(background_group, 'title').text = 'background'
rect = etree.SubElement(background_group, 'rect', x='-1', y='-1', width=str(WIDTH + 2), height=str(HEIGHT + 2),
                        id='background', fill='#000000')

########## STARS
stars_group = etree.SubElement(root, 'g')
title = etree.SubElement(stars_group, 'title').text = 'stars'

for i in range(NB_STARS):
    star_x = random.randint(0, WIDTH)
    star_y = random.randint(0, HEIGHT)
    star_size = random.randint(MIN_SIZE_STARS, MAX_SIZE_STARS)

    star = etree.SubElement(stars_group, 'ellipse')

    star.set('cx', str(star_x))
    star.set('cy', str(star_y))
    star.set('rx', str(star_size))
    star.set('ry', str(star_size))

    if random.random() < COLOR_PROBA:
        color = random.choice(COLOR_PALETTE)
    else:
        color = '#000000'

    star.set('fill', '{}'.format(color))
    star.set('stroke', 'none')
    star.set('fill-opacity', '{}'.format(random.random()))

########## STAR
sun_group = etree.SubElement(root, 'g')
title = etree.SubElement(sun_group, 'title').text = 'sun'

sun = etree.SubElement(sun_group, 'ellipse', cx=str(sun_x), cy=str(sun_y), rx=str(sun_size), ry=str(sun_size), id='sun',
                       fill='#000000', stroke='#ffffff')
sun.set('stroke-width', '2')

last_celestial = (sun_x, sun_size)

########## PLANETS
planets = []

for i in range(NB_PLANETS):

    planet_group = etree.Element('g')
    title = etree.SubElement(planet_group, 'title').text = 'planet_{}'.format(i)

    rand_size = random.randint(MIN_SIZE_PLANET, MAX_SIZE_PLANET)
    planet_x = calculate_pos_x(last_celestial[0], last_celestial[1], rand_size)
    planet_y = int(HEIGHT / 2)

    print(planet_x, planet_y)

    planet = etree.SubElement(planet_group, 'ellipse', id='planet_{}'.format(i))

    planet.set('cx', str(planet_x))
    planet.set('cy', str(planet_y))
    planet.set('rx', str(rand_size))
    planet.set('ry', str(rand_size))

    planet.set('fill', '#000000')
    planet.set('stroke', '#ffffff')
    planet.set('stroke-width', '2')

    if random.random() < RING_PROBA:
        rings = create_ring(planet_x, planet_y, rand_size)
        for ring in rings:
            planet_group.append(ring)

    if random.random() < MOON_PROBA:
        for moon in create_moons(planet_x, planet_y):
            planet_group.append(moon)

    planets.append(planet_group)
    last_celestial = (planet_x, rand_size)

planets_group = etree.SubElement(root, 'g')
title = etree.SubElement(planets_group, 'title').text = 'planets'

for planet in planets:
    planets_group.append(planet)

########## SAVING
data = etree.tostring(root, pretty_print=True).decode('utf8')
file_res = open('test.svg', 'w')
file_res.write(data)
