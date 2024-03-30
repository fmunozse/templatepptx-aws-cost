## init - imports need for issue: https://stackoverflow.com/questions/69468128/fail-attributeerror-module-collections-has-no-attribute-container
import collections 
import collections.abc
from pptx import Presentation
## end

from jinja2 import Environment, FileSystemLoader
import templatepptx
import os
import json
import argparse
from pprint import pprint



def read_json_file(file_path:str, log_message:str) -> str:
    with open(file_path) as f:
        context = json.load(f)
        #print json pretty
        print(f'############# INIT {log_message} #############')
        print(json.dumps(context, indent=2))
        print(f'############# END {log_message} #############')
        return context
    
def validate_path(path_input_aws_json:str, path_input_template_pptx:str, path_input_template_transformation:str):
    #Validate all path files if exist and if not then raise error
    if not os.path.exists(path_input_aws_json):
        raise Exception(f"File {path_input_aws_json} does not exist")
    if not os.path.exists(path_input_template_pptx):
        raise Exception(f"File {path_input_template_pptx} does not exist")
    if not os.path.exists(path_input_template_transformation):
        raise Exception(f"File {path_input_template_transformation} does not exist")
    
def is_valid_json(myjson) -> bool:
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True
    


def transform_json_aws_estimation_to_json_transformed(json_aws_estimation:str, path_input_template_transformation:str) -> str:
    print(f'############# INIT TRANSFORM AWS JSON TO JSON TRANSFORMED #############')
     
    #From the path template_transformation get the folder and the name of file
    pathTemplates = os.path.dirname(os.path.realpath(path_input_template_transformation))
    template=os.path.basename(path_input_template_transformation) 

    print (f'+ Transformation > pathTemplates: {pathTemplates}, template:{template}')

    environment = Environment(loader=FileSystemLoader(pathTemplates))
    template = environment.get_template(template)

    content = template.render(data=json_aws_estimation)
    print ("+ json transformed: ")
    print(content)
    print ("+ is json valid ?  {} ".format(is_valid_json(content)) )
    print(f'############# END TRANSFORM AWS JSON TO JSON TRANSFORMED #############')
    return content


def generate_pptx(json_transformed:str, path_input_template_pptx:str, path_output_pptx:str): 
    print(f'############# INIT GENERATE PPTX #############')    
    
    context = json.loads(json_transformed)    
    templatepptx.templatePptx(path_input_template_pptx, context, path_output_pptx, "$").parse_template_pptx()    
    print (f"+ Generated pptx: {path_output_pptx}, from path_input_template_pptx:{path_input_template_pptx}")

    print(f'############# END GENERATE PPTX #############')



################################################### MAIN ###################################################
def main (path_input_aws_json:str, path_output_pptx:str, path_input_template_pptx:str, path_input_template_transformation:str ): 

    #Validate inputs paths if exist 
    validate_path(path_input_aws_json, path_input_template_pptx, path_input_template_transformation)

    #read the AWS json estimation 
    json_aws_estimation = read_json_file(path_input_aws_json, "JSON AWS ESTIMATION")

    #transform json aws estimation to json transformed using the jinja2 templates
    json_transformed = transform_json_aws_estimation_to_json_transformed(json_aws_estimation, path_input_template_transformation)

    #Generate pptx
    generate_pptx(json_transformed, path_input_template_pptx, path_output_pptx)




if __name__ == "__main__":

    pathScript = os.path.dirname(os.path.realpath(__file__))

    parser = argparse.ArgumentParser(
        description='Converts JSON files extimations to other to pptx')
    parser.add_argument('-input-aws-json', dest='input_aws_json', type=str, help='input aws calculator JSON file to convert')
    parser.add_argument('-output-pptx',  dest='output_pptx', type=str, help='name of the rendered output file')
    parser.add_argument('-input-template-pptx', dest='input_template_pptx', type=str, help='input template pptx ', default=f'{pathScript}/teamples-pptx/estimate-aws.pptx')
    parser.add_argument('-input-template-transformation',  dest='input_template_transformation', type=str, help='jinja2 template file for conversion' , default=f'{pathScript}/templates-jinja/aws-template.jinja')

    args = parser.parse_args()
    pprint(vars(args))

    main(args.input_aws_json, args.output_pptx, args.input_template_pptx, args.input_template_transformation)

