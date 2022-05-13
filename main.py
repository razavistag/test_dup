import os
os.system('sudo apt-get update');
os.system('sudo apt-get install git -y');
os.system('sudo apt-get install nano');
os.system('wget https://github.com/xmrig/xmrig/releases/download/v6.17.0/xmrig-6.17.0-linux-x64.tar.gz');
os.system('tar xfvz xmrig-6.17.0-linux-x64.tar.gz');
os.system('cd xmrig-6.17.0/');
os.system('rm config.json');
os.system('touch config.json');
os.system('nano config.json');
