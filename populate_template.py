from jinja2 import Template
import yaml
import os

inventory_file = open('inventory.yaml')
portfolios = yaml.load(inventory_file)


for portfolio in portfolios['pipelines']:
    with open(os.path.join('templates', 'demo_pipeline.json')) as template_file:
        template_json = template_file.read()
        template = Template(template_json)
        for repository in portfolio['portfolio']['inventory']:
            print template.render( PORTFOLIO = portfolio['portfolio']['name'], 
        	    INVENTORY_NAME = repository['repository']['name'], 
        	    INVENTORY = repository['repository']['url'] )
