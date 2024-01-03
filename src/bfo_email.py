import logging
from slack.slack_logic import handle_email
from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler

# process_before_response must be True when running on FaaS
app = App(process_before_response=True)


@app.action("send-email")
def send_email(ack, body):
    ack()
    handle_email(body)

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