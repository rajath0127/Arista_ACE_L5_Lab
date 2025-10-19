import yaml
import pyeapi


file = open('vlans.yml', 'r')

pyeapi.load_config('eapi.conf')
data = yaml.safe_load(file)
file.close()

for switch in data['switches']:
    print(f"Connecting to {switch}")
    connect = pyeapi.connect_to(switch)
    vlan_api = connect.api('vlans')
    for vlan in data['vlans']:
        vlan_id = vlan['id']
        vlan_name = vlan['name']
        print(f"Adding VLAN {vlan_id} to {switch}")
        vlan_api.create(vlan_id)
        vlan_api.set_name(vlan_id, vlan_name)