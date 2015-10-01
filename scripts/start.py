import sys
import logging

import boto3


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

amis = {
    'base': 'ami-53531436',
    'no_icmp': 'ami-0f75326a',
    'no_udp': 'ami-bb7037de',
    'docker_base': 'ami-2952154c',
    'individual': '',
}

kind = sys.argv[1]
ami_id = amis[kind]

logger.info('Connecting to AWS...')
ec2 = boto3.resource('ec2')

logger.info('Creating instance: {} ({})'.format(kind, ami_id))
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
instance.create_tags(Tags=[{'Key': 'Name', 'Value': kind}])
instance.reload()
logger.info('Created instance with public ip: {}'.format(instance.public_ip_address))
