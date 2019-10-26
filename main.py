import random
from lxml import etree

import tools

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

    return (sun_group, sun_x, sun_size)


def generate_moons():
    pass


def generate_rings():
    pass


def generate_planets(sun_pos_x, sun_size):
    last_celestial = (sun_pos_x, sun_size)
    planets = []

    for i in range(NB_PLANETS):
        random_size = random.randint(MIN_SIZE_PLANET, MAX_SIZE_PLANET)
        planet_x = tools.new_pos_x(last_celestial[0], last_celestial[1], random_size, DISTANCE_PLANET)
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
        # TODO: ADD MOONS
        # TODO: ADD NAMES

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
