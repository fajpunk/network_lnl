import sys
import pprint
import logging

import boto3


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

num = int(sys.argv[1])
ami_id = 'ami-639bdc06'

logger.info('Connecting to AWS...')
ec2 = boto3.resource('ec2')

logger.info('Creating {} instances ({})'.format(num, ami_id))

ips = []
for i in range(num):
    name = 'individual-{}'.format(i)
    instances = ec2.create_instances(
        MinCount=1,
        MaxCount=1,
        ImageId=ami_id,
        KeyName='lnl-open-east',
        SecurityGroupIds=[
            'sg-c73625a0',
        ],
        InstanceType='t2.micro',
        SubnetId='subnet-a1e3209c'
    )
    instance = instances[0]
    instance.wait_until_running()
    instance.create_tags(Tags=[{'Key': 'Name', 'Value': name}])
    instance.reload()
    logger.info('Created instance {} with public ip: {}'.format(name, instance.public_ip_address))
    ips.append(instance.public_ip_address)
pprint.pprint(ips)
