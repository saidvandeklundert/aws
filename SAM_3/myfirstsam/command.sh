# create an s3 bucket
aws s3 mb s3://said-my-first-sam

# package cloudformation packate
aws cloudformation package --s3-bucket said-my-first-sam --template-file template.yaml --output-template-file gen/template-generated.yaml

#deploy

aws cloudformation deploy --template-file gen/template-generated.yaml --stack-name my-first-sam --capabilities CAPABILITY_IAM 