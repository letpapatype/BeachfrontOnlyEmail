import logging
import os
from slack.slack_logic import handle_email
from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler
from dotenv import load_dotenv

load_dotenv()

# process_before_response must be True when running on FaaS
# pass in token, signing secret, and process_before_response
app = App(token=os.environ['SLACK_BOT_TOKEN'], signing_secret=os.environ['SLACK_SIGNING_SECRET'], process_before_response=True)
logging.basicConfig(level=logging.DEBUG)


@app.action("send-email")
def send_email(ack, body, logger, client):
    ack()
    handle_email(body, client, logger)

@app.middleware  # or app.use(log_request)
def log_request(logger, body, next):
    logger.debug(body)
    return next()


SlackRequestHandler.clear_all_log_handlers()
logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG)


def lambda_handler(event, context):
    logging.info(event)
    slack_handler = SlackRequestHandler(app)
    return slack_handler.handle(event, context)


# export SLACK_SIGNING_SECRET=***
# export SLACK_BOT_TOKEN=xoxb-***

# rm -rf vendor && cp -pr ../../src/* vendor/
# pip install python-lambda
# lambda deploy --config-file aws_lambda_config.yaml --requirements requirements.txt