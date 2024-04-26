import xmltodict

file = 'data.xml'

with open(file, 'r') as f:
    data = f.read()

tree = xmltodict.parse(data)

for dia in tree['root']['prediccion']['dia']:
    print(dia)