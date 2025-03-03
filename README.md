

* sudo apt-get update -y
* sudo apt-get install s3fs -y
* sudo apt install python3.12-venv
* cd s3fs_tutorial
* python -m venv venv
* source venv/bin/activate
* pip install boto3 python-dotenv
* .env file
```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=us-east-1
S3_BUCKET=my-bucket-name
```
* echo "your_access_key:your_secret_key" > ~/.passwd-s3fs
* chmod 600 ~/.passwd-s3fs
* mkdir ~/s3bucket
* s3fs my-bucket-name ~/s3bucket -o passwd_file=~/.passwd-s3fs -o url=https://s3.amazonaws.com -o use_path_request_style
* sudo /home/ubuntu/test_stream_mount/venv/bin/python -m streamlit run app.py --server.port 80
