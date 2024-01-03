FROM amazon/aws-lambda-python:3.10

ENV SLACK_BOT_TOKEN = ""
ENV SLACK_SIGNING_SECRET = ""

COPY ./src ${LAMBDA_TASK_ROOT}

WORKDIR ${LAMBDA_TASK_ROOT}

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --target ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "bfo_email.lambda_handler" ]
