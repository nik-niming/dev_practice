#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'niming'

import shelve

DATA_FILE = "guestbook.dat"

def save_data(name, comment,create_at):
    """
    Save the comment
    :param name:
    :param comment:
    :param create_at:
    :return:
    """

    # open the shelve module database file

    database = shelve.open(DATA_FILE)

    # if there is no greeting_list in database, create it.
    if 'greeting_list' not in database:
       greeting_list = []
    else:
        # get the greeting_list in the database
        greeting_list = database['greeting_list']

    # append the data into the list top
    greeting_list.insert(0, {'name':name,
                             'comment':comment,
                             'create_at':create_at,})

    # update the database
    database['greeting_list'] = greeting_list

    # close the database file
    database.close()

