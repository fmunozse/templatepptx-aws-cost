## init - imports need for issue: https://stackoverflow.com/questions/69468128/fail-attributeerror-module-collections-has-no-attribute-container
import collections 
import collections.abc
from pptx import Presentation
## end

import templatepptx
import os


input_pptx = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"examples\examplePresentations\ExampleTables.pptx")
output_pptx = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"examples\examplePresentations\ExampleTables-Output.pptx")
context = {
    "random_key" : "random_value",
         "relationship_test" : [ 
             { "id" : "1", "first_name" : "Duncan", "last_name" : "Junior" }, 
             { "id" : "2", "first_name" : "Jessica", "last_name" : "Jones" } 
          ],         
         "relationship_people" : [ 
             { "id" : "3", "first_name" : "Duncan", "last_name" : "Junior" }, 
             { "id" : "4", "first_name" : "Jessica", "last_name" : "Jones" } 
          ]
    }


templatepptx.templatePptx(input_pptx, context, output_pptx, "$").parse_template_pptx()