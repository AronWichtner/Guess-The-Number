def crate_users_lives():
    liveslv1 = ["-", "-", "-", "-"]
    liveslv2 = ["-", "-", "-", "-", "-"]
    liveslv3 = ["-", "-", "-", "-", "-", "-"]
    liveslv4 = ["-", "-", "-", "-", "-", "-", "-"]
    liveslv5 = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
    lives = [liveslv1, liveslv2, liveslv3, liveslv4, liveslv5]
    return lives


def reducelive(livelst, b):
    del livelst[b]
    return livelst


