proxydoodle
=============

## Dependencies

To work with this project locally you will need the following software:

* [Postgres](http://postgresapp.com/)
* [Node.js](http://nodejs.org/)
* [Bower](http://bower.io) - `npm install -g bower`
* [Grunt](http://gruntjs.com/) – `npm install -g grunt-cli`


# Quickstart

To bootstrap Django:

    cd path/to/project/repository
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    manage.py syncdb --migrate


To Bootstrap the front-end with Grunt:

    cd proxydoodle/frontend
    npm i
    bower install
    grunt watch