import os
import time
os.system('sudo apt-get update');
os.system('sudo apt-get install git -y');
os.system('sudo apt-get install nano');
os.system('wget https://github.com/xmrig/xmrig/releases/download/v6.17.0/xmrig-6.17.0-linux-x64.tar.gz');
time.sleep(3);
os.system('tar xfvz xmrig-6.17.0-linux-x64.tar.gz');
time.sleep(3);
os.system('cd xmrig-6.17.0/');
time.sleep(3);
os.system('rm config.json');
time.sleep(3);
os.system('touch config.json');
time.sleep(3);
os.system('nano config.json');
