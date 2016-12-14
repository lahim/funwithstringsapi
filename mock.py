# -*- coding: utf-8 -*-
__author__ = 'mkr'


class Mock(object):
    from models import User

    users = (
        User.create(username="user1", token='52ba1bd6255e81ae8de725dbf46f217743c302f4'),
        User.create(username="user2", token='3d361f0042faf1751d1b1d561e22bbcecc8198ae'),
        User.create(username="user3", token='907a7400146b2a4c27ec7f49fb3952dfb55a6e7f'),
        User.create(username="user4", token='e80f6ef9785b003f286dfbdcdadf80eaa8f59b8c'),
        User.create(username="user5", token='bffa00ecae58dab1e85313fa9f7968164424792b'),
        User.create(username="user6", token='86320f899fa096b53252e103c5956bc46f348061'),
    )
