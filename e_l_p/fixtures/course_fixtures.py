

curriculum_mutation_query = {'query': 'mutation{ createCurriculumPackage(name:"python package", description:"This is a python package") { curriculum { name description } } }' }

curriculum_mutation_response = b'{"data":{"createCurriculumPackage":{"curriculum":{"name":"python package","description":"This is a python package"}}}}'


curriculum_query = {"query": "{ curriculumPackages{ name description } }"}

curriculum_query_response = b'{"data":{"curriculumPackages":[{"name":"python package","description":"This is a python package"}]}}'
