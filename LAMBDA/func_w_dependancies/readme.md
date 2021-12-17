You can make this thing work from Cloudshell.

[This](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html) explains it.


Create a dir where you put your code:

```
mkdir my-source-code-function
cd my-source-code-function
```

Put your lambda there:

```
vi lambda_function.py
```

Install the required packages to the `package` directory in that folder. Following example installs the `requests` library:

```
pip install --target ./package requests
```

Create a deployment package with the installed library at the root.

```
cd package
zip -r ../my-deployment-package.zip .
```
After this, there will be a zip file that contains everything from the `package` directory in the root dir where you placed the lambda.

So then we go up 1 and zip the whole thing again, this time including the lambda:

```
cd ..
zip -g my-deployment-package.zip lambda_function.py
```

In my example, things looked like so:
```
[cloudshell-user@ip-10-0-136-20 my-source-code-function]$ pwd
/home/cloudshell-user/my-source-code-function
[cloudshell-user@ip-10-0-136-20 my-source-code-function]$ ls -ltr
total 772
-rw-rw-r--  1 cloudshell-user cloudshell-user    238 Dec 17 19:09 lambda_function.py
drwxrwxr-x 13 cloudshell-user cloudshell-user   4096 Dec 17 19:11 package
-rw-rw-r--  1 cloudshell-user cloudshell-user 779846 Dec 17 19:12 my-deployment-package.zip
```

The final thing that remains is uploading the zip. We can do that from cloudshell, like so:

```
aws lambda update-function-code --function-name explore-config --zip-file fileb://my-deployment-package.zip
```