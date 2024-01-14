from slack_bolt import WebClient
import os
import logging



def handle_email(body, client, logger):
    logger.info(body)

    email = body["actions"][0]["value"]
    print(f"email: {email}")

    # open a view with a form to send an email
    response = client.views_open(
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
                    "block_id": f"send-email-body-{email}",
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

    logger.info(response)
    print(response)