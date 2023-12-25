from slack_sdk.web import WebClient
import logging


def handle_app_mentions(body, say, logger):
    logger.info(body)
    say("What's up?")