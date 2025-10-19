import pyeapi
import yaml
import os

pyeapi.load_config('eapi.conf')

directory = "configs"
#exists = os.path.exists(directory)
if not os.path.exists(directory):
    os.makedirs(directory)

file = open('allswitches.yml', 'r')
data = yaml.safe_load(file)
file.close()

#switches = ['leaf1', 'leaf2', 'leaf3', 'leaf4', 'spine1', 'spine2', 'spine3', 'spine4', 'borderleaf1', 'borderleaf2']

for switch in data['allswitches']:
    connect = pyeapi.connect_to(switch)
    running_config = connect.get_config(as_string='True')
    path = directory+'/'+switch+'.cfg'
    file = open(path,'w')
    file.write(running_config)
    file.close()
    print(f"Backing up {switch}")