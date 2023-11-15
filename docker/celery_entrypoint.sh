#!/bin/sh

echo "--> Waiting for db to be ready"
./wait-for-it.sh db:5432

echo "--> Starting celery process"
celery -A tracktrace.tasks worker -l info --without-gossip --without-mingle --without-heartbeat
