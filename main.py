import random

from lxml import etree

import utils

WIDTH = 2800
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

# COLOR_PALETTE = ['#E5BEED', '#7D5C65', '#7C90DB', '#DA3E52', '#F2E94E']
COLOR_PALETTE = ['#e57376', '#eba772', '#72b2f1', '#d3addf', '#aac6a6', '#d7ffda', '#e6d700']
FONT_SIZE = 25

def generate_background():
    """
    Fonction permettant d'ajouter un background
    :return: etree.Element
    """
    background_group = etree.Element('g')
    etree.SubElement(background_group, 'title').text = 'background'

    background = etree.SubElement(background_group, 'rect', id='background')
    background.set('x', '-1')
    background.set('y', '-1')
    background.set('width', str(WIDTH + 2))
    background.set('height', str(HEIGHT + 2))

    background.set('fill', '#000000')

    return background_group


def generate_stars():
    """
    Fonction permettant d'ajouter des étoiles
    :return: etree.Element
    """
    stars_group = etree.Element('g')
    etree.SubElement(stars_group, 'title').text = 'stars'

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

    return stars_group


def generate_sun():
    """
    Fonction permettant de créer un soleil
    :return: etree.Element
    """
    sun_size = int(HEIGHT * 0.75)
    sun_x = int(HEIGHT * (-0.358))  # TODO: Calcul du ratio
    sun_y = int(HEIGHT / 2)

    print(sun_size, sun_x, sun_y)  # Delete logs

    sun_group = etree.Element('g')
    etree.SubElement(sun_group, 'title').text = 'sun'
    sun = etree.SubElement(sun_group, 'ellipse', id='sun')

    sun.set('cx', str(sun_x))
    sun.set('cy', str(sun_y))
    sun.set('rx', str(sun_size))
    sun.set('ry', str(sun_size))

    sun.set('stroke-width', '2')
    sun.set('fill', '#000000')
    sun.set('stroke', '#ffffff')

    return sun_group, sun_x, sun_size


def generate_moons(planet_cx):
    moons = utils.random_size_moons()
    diff_pos_moon = utils.total_size_moons(moons)
    # moons = [20, 25, 30]
    list_moons = []
    last_moon = ()

    cpt = 0
    for moo in moons:
        if cpt == 0:
            moon_value = planet_cx - diff_pos_moon
        else:
            moon_value = utils.new_pos_x(last_moon[0], last_moon[1], moo, DISTANCE_MOON)

        moon = etree.Element('ellipse', id='moon_{}'.format(cpt))
        moon.set('cx', str(moon_value))
        moon.set('cy', str(0.75 * HEIGHT))  # TODO: Change into ratio
        moon.set('rx', str(moo))
        moon.set('ry', str(moo))

        moon.set('fill', '#000000')
        moon.set('stroke', '#ffffff')
        moon.set('stroke-width', '2')

        list_moons.append(moon)
        last_moon = (moon_value, moo)
        cpt += 1

    return list_moons


def generate_rings(cx, cy, ray):
    rings = []
    nb_rings = random.randint(MIN_RING, MAX_RING)
    rotation_rings = random.randint(0, 360)

    for i in range(nb_rings):
        cpt = i * 5
        path = 'M{pos_x},{pos_y} a{distortion1},{distortion2} 0 1,0 {ray},0'.format(pos_x=cx - ray, pos_y=cy - cpt,
                                                                                    distortion1=(2 * ray) + cpt,
                                                                                    distortion2=15 + cpt,
                                                                                    ray=2 * ray)
        ring = etree.Element('path')
        ring.set('d', path)
        ring.set('fill', 'none')
        ring.set('stroke', '#ffffff')
        ring.set('stroke-width', '1.5')
        ring.set('transform', 'rotate({} {},{})'.format(rotation_rings, cx, cy))
        rings.append(ring)

    return rings


def generate_names(planet_cx):
    random_name = utils.random_name()
    planet_name = etree.Element('text', id='planet_name')

    planet_name.set('x', str(planet_cx))
    planet_name.set('y', str(0.90 * HEIGHT))
    planet_name.set('font-family', 'Helvetica')
    planet_name.set('style', 'text-anchor: middle')
    planet_name.set('font-size', str(FONT_SIZE))

    planet_name.set('fill-opacity', 'null')
    planet_name.set('fill', '#ffffff')
    planet_name.set('stroke-width', '0')

    planet_name.text = random_name

    return planet_name


def generate_planets(sun_pos_x, sun_size_r):
    last_celestial = (sun_pos_x, sun_size_r)
    planets = []

    for i in range(NB_PLANETS):
        random_size = random.randint(MIN_SIZE_PLANET, MAX_SIZE_PLANET)
        planet_x = utils.new_pos_x(last_celestial[0], last_celestial[1], random_size, DISTANCE_PLANET)
        planet_y = int(HEIGHT / 2)

        # print(planet_x, planet_y)

        planet_group = etree.Element('g')
        etree.SubElement(planet_group, 'title').text = 'planet_{}'.format(i)
        planet = etree.SubElement(planet_group, 'ellipse', id='planet_{}'.format(i))

        planet.set('cx', str(planet_x))
        planet.set('cy', str(planet_y))
        planet.set('rx', str(random_size))
        planet.set('ry', str(random_size))

        planet.set('fill', '#000000')
        planet.set('stroke', '#ffffff')
        planet.set('stroke-width', '2')

        # TODO: ADD RINGS
        if random.random() < RING_PROBA:
            for ring_svg in generate_rings(planet_x, planet_y, random_size):
                planet_group.append(ring_svg)

        # TODO: ADD MOONS
        if random.random() < MOON_PROBA:
            for moon_svg in generate_moons(planet_x):
                planet_group.append(moon_svg)
        # TODO: ADD NAMES
        planet_group.append(generate_names(planet_x))

        planets.append(planet_group)
        last_celestial = (planet_x, random_size)

    return planets


background_svg = generate_background()
stars_svg = generate_stars()
sun_svg, sun_x, sun_size = generate_sun()
planets_list_svg = generate_planets(sun_x, sun_size)

root = etree.Element('svg', width=str(WIDTH), height=str(HEIGHT), xmlns='http://www.w3.org/2000/svg')

root.append(background_svg)
root.append(stars_svg)
root.append(sun_svg)

for planet_svg in planets_list_svg:
    root.append(planet_svg)

########## SAVING
data = etree.tostring(root, pretty_print=True).decode('utf8')
file_res = open('solar_system.svg', 'w')
file_res.write(data)
