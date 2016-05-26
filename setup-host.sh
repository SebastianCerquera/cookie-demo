#! /bin/bash

mkdir /tmp/performance && cd /tmp/performance

wget https://github.com/scouter-project/scouter-demo/releases/download/0.0.5/demo-env1.tar.gz
tar xf demo-env1.tar.gz
cd demo-env1
bash start-tomcat.sh

cd /tmp/performance
wget http://jmeter-plugins.org/downloads/file/ServerAgent-2.2.1.zip
mkdir /tmp/performance/agent && cd /tmp/performance/agent
unzip ../ServerAgent-2.2.1.zip
./startAgent.sh --udp-port 0 --tcp-port 3450 &


