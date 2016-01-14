from jinja2 import Template
import os

with open(os.path.join('templates', 'demo_pipeline.json')) as template_file:
    template_json = template_file.read()
    template = Template(template_json)
    print template.render(GO_SERVER_URL='localhost:8153',
            PIPELINE_NAME='DEMO_PIPELINE')
