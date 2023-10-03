import json
import os
from vars import *

d=open('example_request.json','r')
t=d.read()
d.close()

example_request=json.loads(t)

d=open('branchnames.txt','r')
t=d.read()
d.close()

branchnames=[l.strip() for l in t.split('\n') if l!='']

for branchname in branchnames:
	thisrequest=dict(example_request)
	thisrequest['ServiceName']=branchname
	thisrequest['SourceConfiguration']['CodeRepository']['SourceCodeVersion']['Value']=branchname
	thisrequest['SourceConfiguration']['CodeRepository']['RepositoryUrl']=repositoryurl
	thisrequest['SourceConfiguration']['AuthenticationConfiguration']['ConnectionArn']=connectionarn
	d=open('tmp/%s.json' %branchname,'w')
	d.write(json.dumps(thisrequest,indent=2))
	d.close()
	execstr="aws apprunner create-service --cli-input-json file://tmp/%s.json" %branchname
	print(execstr)
	v=os.system(execstr)
	print(v)