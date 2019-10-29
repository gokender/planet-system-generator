import configargparse

import generation
import utils

__VERSION__ = '0.4.0'

def main():

    parser = configargparse.ArgParser(default_config_files=['config.ini'])
    parser.add('--width', required=False, type=int, help='SVG width')
    parser.add('--height', required=False, type=int, help='SVG height')
    parser.add('--color_palette', required=False, action='append', help='list of colors for stars')
    parser.add('--font_size', required=False, type=int, help='font size for planet name')

    parser.add('--nb_stars', required=False, type=int, help='number of stars')
    parser.add('--min_size_stars', required=False, type=int, help='minimal star size')
    parser.add('--max_size_stars', required=False, type=int, help='maximal star size')
    parser.add('--color_proba', required=False, type=float, help='probability of coloured star')

    parser.add('--nb_planets', required=False, type=int, help='number of planets')
    parser.add('--distance_planet', required=False, type=int, help='distance in pixel between each planet')
    parser.add('--min_size_planet', required=False, type=int, help='minimal planet size')
    parser.add('--max_size_planet', required=False, type=int, help='maximal planet size')

    parser.add('--ring_proba', required=False, type=float, help='probability of a ringed planet')
    parser.add('--min_ring', required=False, type=int, help='minimal number of rings')
    parser.add('--max_ring', required=False, type=int, help='maximal number of rings')

    parser.add('--moon_proba', required=False, type=float, help='probability for a planet to have moons')
    parser.add('--distance_moon', required=False, type=int, help='distance between each moon')
    parser.add('--min_nb_moons', required=False, type=int, help='minimal number of moon')
    parser.add('--max_nb_moons', required=False, type=int, help='maximal number of moon')
    parser.add('--min_size_moon', required=False, type=int, help='minimal size of moon')
    parser.add('--max_size_moon', required=False, type=int, help='maximal size of moon')

    parser.add('--id', required=False, help='random seed for generation')
    parser.add('-f', '--filename', default='solar_system.svg', required=False, help='file name to save')
    parser.add('-v', '--version', action='version', version=__VERSION__)

    options = parser.parse_args()
    #print(options)
    #print(parser.format_values())

    if options.id is None:
        options.id = utils.generate_id(5, options.nb_planets)
        #print(options.id)

    print('Generating planetary system "{}"'.format(options.id))
    generation.generate(options)


if __name__ == '__main__':
    main()
