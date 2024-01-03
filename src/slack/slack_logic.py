from slack_sdk.web import WebClient
import os
import logging

slack_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])


def handle_email(body, say, logger):
    logger.info(body)
    email = body["actions"][0]["value"]

    # open a view with a form to send an email
    response = slack_client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "send-email-modal",
            "title": {
                "type": "plain_text",
                "text": "Send Email"
            },
            "submit": {
                "type": "plain_text",
                "text": "Send",
                "emoji": True
            },
            "blocks": [
                {
                    "type": "input",
                    "block_id": "send-email-body",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "to",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Body of the email"
                        }
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "To"
                    }
                }
            ]
        }
    )
