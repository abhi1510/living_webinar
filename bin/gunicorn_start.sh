#!/bin/bash
  
NAME="living_webinar"                                           # Name of the application
DJANGODIR=/home/ubuntu/living_webinar/web                       # Django project directory
SOCKFILE=/home/ubuntu/living_webinar/run/app.sock               # we will communicte using this unix socket
USER=ubuntu                                                     # the user to run as
NUM_WORKERS=3                                                   # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=web.settings.production                  # which settings file should Django use
DJANGO_WSGI_MODULE=web.wsgi                                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source ../../lw_venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
exec /home/ubuntu/lw_venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-