#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'niming'

import shelve
from datetime import datetime

from flask import Flask, request, render_template, redirect, escape, Markup

application = Flask(__name__)

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

def load_data():
    """
    Return the comment data saved before

    :return: greeting_list
    """

    # open the shelve module database file
    database = shelve.open(DATA_FILE)

    # get the greeting_list. if not, just return empty list.
    greeting_list = database.get('greeting_list',[])

    # close the database file
    database.close()

    return greeting_list

@application.route('/')
def index():
    """Top page
    Use template to show the page
    """
    greeting_list = load_data()

    return render_template("index.html", greeting_list = greeting_list)


@application.route('/post', methods=['post'])
def post():
    """Comment's target url
    """

    # get the comment data
    name = request.form.get('name') # name
    comment = request.form.get('comments') # comment
    create_at = datetime.now() # comment time

    # save the date
    save_data(name, comment, create_at)

    # redirect to the top page
    return redirect('/')


@application.template_filter('nl2br')
def nl2br_filter(s):
    """
    transform the new line in comment to <br> tag.
    :param s:
    :return:
    """

    return escape(s).replace('\n',Markup('</br>'))

@application.template_filter('datetime_fmt')
def datetime_fmt(dt):
    """
    the filter of making datetime to be shown friendly.

    for demo
    :param datetime:
    :return:
    """

    return dt.strftime('%Y%m%d %H%:%M:%S')


if __name__ == '__main__':
   # save_data("test","test comment", datetime.now())

    # Run application when the IP address is 127.0.0.1 and the port is 5000
    application.run('127.0.0.1', 5000, debug=True)

