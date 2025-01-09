from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import os
import logging

# 正常情况日志级别使用 INFO，需要定位时可以修改为 DEBUG，此时 SDK 会打印和服务端的通信信息
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 初始化配置信息
config = CosConfig(
    Region=os.getenv("COS_REGION"),
    SecretId=os.getenv("COS_SECRET_ID"),
    SecretKey=os.getenv("COS_SECRET_KEY"),
    Scheme="https"
)
client = CosS3Client(config)

# 上传文件到 COS
with open("nextselfbuild.tar.gz", "rb") as fp:
    response = client.put_object(
        Bucket=os.getenv("COS_BUCKET_NAME"),
        Body=fp,
        Key="nextselfbuild.tar.gz",
        StorageClass="STANDARD",
        EnableMD5=False
    )
    print(response["ETag"])
