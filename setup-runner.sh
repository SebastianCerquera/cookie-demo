#! /bin/bash

mkdir /tmp/performance && cd /tmp/performance

wget http://www-eu.apache.org/dist//jmeter/binaries/apache-jmeter-3.0.tgz
tar xf apache-jmeter-3.0.tgz

wget http://jmeter-plugins.org/downloads/file/JMeterPlugins-Standard-1.4.0.zip
mkdir /tmp/performance/plugin && cd /tmp/performance/plugin
unzip ../JMeterPlugins-Standard-1.4.0.zip
cp lib/ext/JMeterPlugins-Standard.jar /tmp/performance/apache-jmeter-3.0/lib/ext/JMeterPlugins-Standard.jar

echo "172.37.0.27   mine.demo.com" >> /etc/hosts

# mkdir /tmp/performance/plans && cd mkdir /tmp/performance/plans
# wget localhost:9000/baseline.jmx
# wget localhost:9000/peak.jmx
