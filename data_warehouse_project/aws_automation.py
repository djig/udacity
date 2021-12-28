import boto3
import sys
import configparser
import json
import pandas as pd
import pprint
from botocore.exceptions import ClientError

config = configparser.ConfigParser()

#  Retrive all config variables from config file
config.read_file(open('dwh.cfg'))
KEY                    = config.get('AWS','KEY')
SECRET                 = config.get('AWS','SECRET')
SESSION                 = config.get('AWS','SESSION')

DB_CLUSTER_TYPE       = config.get("CLUSTER_CONFIG","CLUSTER_TYPE")
DB_NUM_NODES          = config.get("CLUSTER_CONFIG","NUM_NODES")
DB_NODE_TYPE          = config.get("CLUSTER_CONFIG","NODE_TYPE")

HOST                  = config.get("CLUSTER_CONFIG","CLUSTER_NAME")   
DB_NAME               = config.get("CLUSTER","DB_NAME")
DB_USER               = config.get("CLUSTER","DB_USER")
DB_PASSWORD           = config.get("CLUSTER","DB_PASSWORD")
DB_PORT               = config.get("CLUSTER","DB_PORT")
IAM_ROLE_NAME      = config.get("CLUSTER_CONFIG", "IAM_ROLE_NAME")


#  crate instances of ec2, s3, redshift, iam
ec2 = boto3.resource('ec2',
                       region_name="us-west-2",
                       aws_access_key_id=KEY,
                       aws_secret_access_key=SECRET
                       ,
                       aws_session_token=SESSION
                    )

s3 = boto3.resource('s3',
                       region_name="us-west-2",
                       aws_access_key_id=KEY,
                       aws_secret_access_key=SECRET
                       ,
                       aws_session_token=SESSION
                   )

iam = boto3.client('iam',aws_access_key_id=KEY,
                     aws_secret_access_key=SECRET,
                     aws_session_token=SESSION,
                     region_name='us-west-2'
                  )

redshift = boto3.client('redshift',
                       region_name="us-west-2",
                       aws_access_key_id=KEY,
                       aws_secret_access_key=SECRET,
                       aws_session_token=SESSION
                       )


def check_cluster_exists(cluster_identifier):
    """
    Check if cluster exists
    input: cluster_identifier
    output: True or False
    """
    clusters = redshift.describe_clusters()
    print(len(clusters['Clusters']))
    if len(clusters['Clusters']) > 0:
        try:
            redshift.describe_clusters(ClusterIdentifier=HOST)['Clusters']
            return True
        except ClientError as e:
            return False
    else:
        return False


def test_aws_s3():
    """
    Test if s3 bucket exists
    """
    sampleDbBucket =  s3.Bucket("udacity-dend")
    for obj in sampleDbBucket.objects.filter(Prefix="song_data/A/B/C/TRABCEI128F424C983.json"):
        json_content = json.loads(obj.get()['Body'].read().decode('utf-8'))
        print(json_content)

def test_aws_redshift():
    print(redshift.describe_clusters())


def create_iam_role(role_name):
    """
        Create IAM role for Redshift
        Attach S3ReadOnlyAccess policy to it
        input: role_name
    """ 
    try:
        print("1.1 Creating a new IAM Role") 
        dwhRole = iam.create_role(
            Path='/',
            RoleName=role_name,
            Description = "Allows Redshift clusters to call AWS services on your behalf.",
            AssumeRolePolicyDocument=json.dumps(
                {'Statement': [{'Action': 'sts:AssumeRole',
                'Effect': 'Allow',
                'Principal': {'Service': 'redshift.amazonaws.com'}}],
                'Version': '2012-10-17'})
        )    
    except Exception as e:
        print(e)
    print("1.2 Attaching Policy")
    iam.attach_role_policy(RoleName=IAM_ROLE_NAME,
                       PolicyArn="arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
                      )['ResponseMetadata']['HTTPStatusCode']

    print("1.3 Get the IAM role ARN")
    roleArn = iam.get_role(RoleName=IAM_ROLE_NAME)['Role']['Arn']
    print(roleArn)
def generate_cluster():
    """
        Create Redshift cluster
    """
    try:
        roleArn = iam.get_role(RoleName=IAM_ROLE_NAME)['Role']['Arn']
        response = redshift.create_cluster(        
            #HW
            ClusterType=DB_CLUSTER_TYPE,
            NodeType=DB_NODE_TYPE,
            NumberOfNodes=int(DB_NUM_NODES),

            #Identifiers & Credentials
            DBName=DB_NAME,
            ClusterIdentifier=HOST,
            MasterUsername=DB_USER,
            MasterUserPassword=DB_PASSWORD,
            
            #Roles (for s3 access)
            IamRoles=[roleArn]  
        )
    except Exception as e:
        print(e)
def open_tcp_port(port, myClusterProps):
    """
        Open TCP port
        input: port
    """
    try:
        vpc = ec2.Vpc(id=myClusterProps['VpcId'])
        defaultSg = list(vpc.security_groups.all())[0]
        print(defaultSg)
        print(list(vpc.security_groups.all()))
        defaultSg.authorize_ingress(
            GroupName=defaultSg.group_name,
            CidrIp='0.0.0.0/0',
            IpProtocol='TCP',
            FromPort=int(port),
            ToPort=int(port)
        )
    except Exception as e:
        print(e)

def delete_iam_role():
    """
        Delete IAM role
    """
    try:
        iam.detach_role_policy(RoleName=IAM_ROLE_NAME, PolicyArn="arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess")
        iam.delete_role(RoleName=IAM_ROLE_NAME)
    except Exception as e:
        print(e)

def create_cluster():
    """
        Create IAM role for Redshift
        Create Redshift cluster
        Print cluster properties
    """
    create_iam_role(IAM_ROLE_NAME)
    generate_cluster()
    get_cluster_endpoint_role_arn()

def delete_cluster():
    """
        Delete Redshift cluster
    """
    redshift.delete_cluster( ClusterIdentifier=HOST,  SkipFinalClusterSnapshot=True)
    get_cluster_endpoint_role_arn()

def get_cluster_endpoint_role_arn():
    """
        Get cluster endpoint and role ARN
    """
    try:
        if len(redshift.describe_clusters(ClusterIdentifier=HOST)['Clusters']) > 0:
            myClusterProps = redshift.describe_clusters(ClusterIdentifier=HOST)['Clusters'][0]
            open_tcp_port(DB_PORT, myClusterProps)
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(myClusterProps)
            print('***********  status of cluser: ************ ')
            print(myClusterProps['ClusterStatus'])
            print('*********************** ')
            if myClusterProps['ClusterStatus'] == 'available':
                DWH_ENDPOINT = myClusterProps['Endpoint']['Address']
                DWH_ROLE_ARN = myClusterProps['IamRoles'][0]['IamRoleArn']
                print("DWH_ENDPOINT :: ", DWH_ENDPOINT)
                print("DWH_ROLE_ARN :: ", DWH_ROLE_ARN)
        else:
            print("Cluster not found")
    except Exception as e:
        print("Cluster not found")
def main():
    """
        Main function for status, create, delete of cluster with IAM role, s3 access and redshift DB
    """
    run_mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if run_mode == 'create':
        if check_cluster_exists(HOST):
            get_cluster_endpoint_role_arn()
        else:
            print("**************** Creating cluster ********************")
            create_cluster()
            print("**************** Creating cluster ********************")
    elif run_mode == 'status':
        print("Getting cluster endpoint and role arn")
        if check_cluster_exists(HOST):
            get_cluster_endpoint_role_arn()
        else:
            print("Cluster not found")
    elif run_mode == 'delete':
        if check_cluster_exists(HOST):
            print("**************** Deleting cluster ********************")
            delete_cluster()
            delete_iam_role()
            print("**************** Deleting cluster ********************")
        else:
            print("Cluster not found")
        
    else:
        print("Getting cluster endpoint and role arn")
        get_cluster_endpoint_role_arn()

if __name__ == "__main__":
    main()
