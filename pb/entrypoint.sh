#!/bin/sh
set -e # exit on any non-zero status (error)
DIR=$(dirname $0) #where this script lives

# this entrypoint script checks that all required setup is done
# if not done, does it
# and then proceeds to execute the main "command" for this container
if [ -n "$LS_VERSION" ]; then
  if [ ! -x "litestream" ]; then
    url="https://github.com/benbjohnson/litestream/releases/download/v${LS_VERSION}/litestream-v${LS_VERSION}-linux-amd64.tar.gz"
    echo "Downloading ... ${url}"
    wget -q "$url" -O - | tar -zxvf -
  fi
  FILE=$DIR/pb_data/data.db
  if [ ! -f $FILE ]; then
    echo "No database found, restoring from replica if exists"
    ./litestream restore -if-replica-exists $FILE
  fi
  # only if we are the "master" (prod), then ...
  if [ "$LS_REPLICATION_MASTER" = "1" ]; then
    # Prefix the command, so that litestream wraps it.
    # Below, use $* (one string) instead of $@ (separate)
    set -- $DIR/litestream replicate -exec "$*"
  fi
fi

if [ ! -x "pocketbase" ]; then
  url="https://github.com/pocketbase/pocketbase/releases/download/v${PB_VERSION}/pocketbase_${PB_VERSION}_linux_amd64.zip"
  echo "Downloading ... ${url}"
  wget -q "$url" -O /tmp/pb.zip
  unzip /tmp/pb.zip pocketbase
fi

exec "$@"