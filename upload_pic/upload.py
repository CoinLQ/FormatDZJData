import boto3
from boto3.session import Session
import os
import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
REDIS_KEY='jobs'

aws_key = ""
aws_secret = ""
def call_back(c):
    global yes_or_no
    yes_or_no = c

session = Session(aws_access_key_id=aws_key,
    aws_secret_access_key=aws_secret, region_name='cn-north-1')
s3 = session.resource('s3')
s3_client = s3.meta.client

def uploadPicFile(img_path):
    img_path = img_path.replace('\\','/')
    keyList = img_path.split("/")
    length = len(keyList)
    numberString = keyList[length-2]
    try:
        number = (int)(numberString)
    except Exception as e: 
        print('error:',numberString)
        number = -1
    if number > 0:
        key = "YB/" + keyList[length-2] +"/" +keyList[length-1]
        try:
            s3.client.get_object_acl(Bucket='lqdzj-image', Key=key)
        except:
            s3_client.upload_file(img_path, 'lqdzj-image', Key=key, Callback=call_back)
    else:
        print('upload pic error!')

def main():
    while True:
        item = r.blpop(REDIS_KEY)
        path = item[1]
        print(path)
        uploadPicFile(path)

if __name__=='__main__': 
    main()
    
    
