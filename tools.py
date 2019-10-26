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
