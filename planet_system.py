import configargparse

import generation
import utils

__VERSION__ = '0.3.0'

# TODO:Change config.ini structure


def main():

    parser = configargparse.ArgParser(default_config_files=['config2.ini'])
    parser.add('--width', required=False, type=int, help='config file path')
    parser.add('--height', required=False, type=int, help='path to genome file')
    parser.add('--color_palette', required=False, action='append', help='path to genome file')
    parser.add('--font_size', required=False, type=int, help='path to genome file')

    parser.add('--nb_stars', required=False, type=int, help='config file path')
    parser.add('--min_size_stars', required=False, type=int, help='path to genome file')
    parser.add('--max_size_stars', required=False, type=int, help='path to genome file')
    parser.add('--color_proba', required=False, type=float, help='path to genome file')

    parser.add('--nb_planets', required=False, type=int, help='path to genome file')

    parser.add('--id', required=False, help='path to genome file')
    parser.add('-f', '--filename', default='solar_system.svg', required=False, help='path to genome file')
    parser.add('-v', '--version', action='version', version=__VERSION__)

    options = parser.parse_args()
    print(options)
    #print(parser.format_values())

    if options.id is None:
        options.id = utils.generate_id(5, options.nb_planets)
        print(options.id)

    print(options)
    #generation.generate(options.id)


if __name__ == '__main__':
    main()
