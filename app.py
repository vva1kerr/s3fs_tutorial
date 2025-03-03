import streamlit as st
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os
import boto3

load_dotenv()

st.title("s3fs mount")

aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region = os.getenv("AWS_REGION")
bucket = os.getenv("S3_BUCKET")

# Initialize S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=region
)

# Example: List bucket objects
response = s3.list_objects_v2(Bucket=bucket)
for obj in response.get('Contents', []):
    st.write(obj['Key'])





