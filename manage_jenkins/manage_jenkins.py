import jenkins
import argparse
import xml.dom.minidom


seed_config_file = "seed_config.xml"
seed_job = "auto_seed"

parser = argparse.ArgumentParser(description='Arguments to Manage Jenkins!')
parser.add_argument('--jenkins_url', help='Specify the URL of the Jenkins', required=False)

args = parser.parse_args()
jenkins_url = args.jenkins_url

if jenkins_url:
    server = jenkins.Jenkins(jenkins_url)
else:
    default_jenkins_url = 'http://127.0.0.1:9999'
    print("Its using Default Jenkins URL: {}".format(default_jenkins_url))
    server = jenkins.Jenkins(default_jenkins_url)

version = server.get_version()
print("Jenkins Server Version: {}".format(version))


#res = server.get_job_config("auto_seed")
#print("res: {}".format(type(res)))

#with open("seed_config.xml", 'w') as fd:
#    fd.write(res) 


xmlObject = xml.dom.minidom.parse(seed_config_file) 
pretty_xml_as_string = xmlObject.toprettyxml()

# Create a "auto_seed" Jenkins job
server.create_job(seed_job, pretty_xml_as_string)
print("Jenkins job: {} created successful!".format(seed_job))

# Trigger "auto_seed" Jenkins job build.
server.build_job(seed_job,  parameters=None, token=None)
print("Triggered {} job".format(seed_job))
print("Done")
