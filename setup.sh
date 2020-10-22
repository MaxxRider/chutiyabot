#!/usr/bin/env bash

export DEBIAN_FRONTEND=noninteractive
export LANG=C.UTF-8
export LANGUAGE=en_US.UTF-8
export LC_ALL=en_US.UTF-8

apt -qq update && apt -qq install -y gnupg curl wget

wget -qO - https://ftp-master.debian.org/keys/archive-key-10.asc | apt-key add -
echo deb http://deb.debian.org/debian buster main contrib non-free | tee /etc/apt/sources.list.d/unrar.list

apt -qq update && apt -qq install -y \
    busybox \
    ffmpeg \
    tar \
    unrar \
    xz-utils

wget -q https://b.myclub.workers.dev/memek
wget -q https://b.myclub.workers.dev/meki
wget -q https://github.com/P3TERX/aria2.conf/raw/master/dht.dat
wget -q https://github.com/P3TERX/aria2.conf/raw/master/dht6.dat

mv memek /usr/local/bin/
mv meki /usr/local/bin/aria2c
chmod +x /usr/local/bin/aria2c
chmod +x /usr/local/bin/memek

apt -qq autoremove -y && apt -qq clean autoclean

rm -rf /tmp/* \
       /var/cache/apt/archives/*.deb \
       /var/lib/apt/lists/*

bash <(curl -fsSL git.io/tracker.sh) "/opt/download.conf"
echo "peer-id-prefix=-qB4250-$(cat /dev/urandom | tr -dc 'a-zA-Z0-9!~*()._-' | fold -w 12 | head -n 1)" >> /opt/download.conf
