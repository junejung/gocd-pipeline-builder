from jinja2 import Template
import yaml
import os

inventory_file = open('inventory.yaml')
inventories = yaml.load(inventory_file)


with open(os.path.join('templates', 'demo_pipeline.json')) as template_file:
    template_json = template_file.read()
    template = Template(template_json)
    print template.render( INVENTORY = inventories['pipelines'][0]['portfolio']['inventory'][0]['repository']['url'] )
