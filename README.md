

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
* sudo nano /etc/fuse.conf
* `user_allow_other`
* mkdir ~/s3bucket
* s3fs my-bucket-name ~/s3bucket -o passwd_file=${HOME}/.passwd-s3fs -o url=https://s3.us-east-2.amazonaws.com -o endpoint=us-east-2 -o use_path_request_style -o allow_other
* s3fs my-bucket-name ~/s3bucket -o passwd_file=~/.passwd-s3fs -o url=https://s3.amazonaws.com -o use_path_request_style
* sudo /home/ubuntu/s3fs_tutorial/venv/bin/python -m streamlit run app.py --server.port 80


# file support 
#### To count the number of files inside ~/s3bucket/1x1_try2, use:
`find ~/s3bucket/1x1_try2 -type f | wc -l`
#### To output all filenames from ~/s3bucket/1x1_try2 into a file for comparison, use:
`ls ~/s3bucket/1x1_try2 > file_list_1x1_try2.txt`
#### To move a file from 1x1_try2 to ~/s3bucket, use:
`mv ~/s3bucket/1x1_try2/filename ~/s3bucket/`
#### If you need full paths, use:
`find ~/s3bucket/1x1_try2 -type f > file_list_1x1_try2.txt`
#### compare it with another folder's file list using diff
`diff file_list_1x1_try2.txt file_list_other_folder.txt`
#### To move all files from ~/s3bucket/1x1_try2/ to ~/s3bucket/, use:
`mv ~/s3bucket/1x1_try2/* ~/s3bucket/`
