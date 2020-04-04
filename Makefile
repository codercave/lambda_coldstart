deploy:
	aws cloudformation package \
		--template-file template.yaml \
		--output-template-file packaged-template.yaml \
		--s3-bucket ${CODERCAVE_BUCKET} \
		--profile caveman

	$(info [+] Deploying 'codercave-lambda_coldstart')
	aws cloudformation deploy \
		--template-file packaged-template.yaml \
		--stack-name codercave-lambda-coldstart \
		--capabilities CAPABILITY_IAM \
		--profile caveman

delete:
	aws cloudformation delete-stack \
		--stack-name codercave-lambda-coldstart \
		--profile caveman