#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A slackbot that responds to commands.
This uses the Slack RTM (Real Time Messaging) API.
Required environment variables (example only, these are not real tokens).
Get these from the Slack account settings that you are connecting to.
   BOT_USER_ID = 'U20981S736'
   BOT_USER_TOKEN = 'xoxb-106076235608-AbacukynpGahsicJqugKZC'
"""
__author__ = 'Clinton Johnson & Jen Browning'
BOT_NAME = 'my-little-slackbot'
BOT_CHAN = '#bot-test'

import logging
import time
import datetime
import argparse
import signal
import os
import thread
from slackclient import SlackClient
# instantiate Slack client
slack_client = SlackClient(os.environ.get('xoxb-421405103765-605284427574-AOQ9lCjAJMUVtMOZxQQvcpk2'))
# slackbot's user ID in Slack: value is assigned after the bot starts up
bot_id = 'varys-my-dragon'

exit_flag = False
bot_commands = {
    'help': 'Returns list of helpful commands to use'
    'ping': 'Show the uptime of the bot'
    'exit': 'Stops running active bot'
    #May add more as time progresses
}


def config_logger():
    """Setup logging configuration"""
    pass


def command_loop(bot):
    """Process incoming bot commands"""
    slack_client = SlackClient(bot_user_token)
    if slack_client.rtm_connect(auto_reconnect=True):
        print "Successfully connected, listening for events"
     while True:
         incoming_events = slack_client.rtm_read()
         command = parse_bot_mention(incoming_events) #this method returns the command issued to the bot in specific
         if command:
             handle_command_thread = Thread(target=handle_bot_command, args=(command))
             handle_command_thread.start()
         time.sleep(1) #RTM read delay of 1 sec
         else:
             print "Connection failed"


def signal_handler(sig_num, frame):
    """Handles OS signals SIGTERM and SIGINT."""
    global exit_flag
    signals = dict((key, value) for value, key in reversed(sorted(signal.__dict__.items()))
                if value.startswith('SIG') and not value.startswith('SIG_'))
    logger.warning('Received OS Signal: {}'.format(signals[sig_num]))

    # only exit if it is a sigterm or sigint
    if sig_num == signal.SIGINT or sig_num == signal.SIGTERM:
        exit_flag = True


class SlackBot:

    def __init__(self, bot_user_token, home_channel, bot_id=None):
        self.sc = SlackClient(bot_user_token)
        self.bot_id = bot_id
        self.home = home_channel

    def __repr__(self):
        return "Point(sc=%s, home=%s, bot_id=%s)" % (self.sc, self.bot_id, self.home)
    my_object = Slackbot()
    print my_object

    def __str__(self):
        return "(%s, %s, %s)" % (self.sc, self.bot_id, self.home)

    def __enter__(self):
        """Implement this method to make this a context manager"""
        welcome_message = "Greetings how may I assist you?"
        if self.sc.server.connected:
            logger.info('Bot connected')
        else:
            logger.info('Bot connected')
            self.sc.rtm_connect()
        self.post_command_message(welcome_message, self.home)
        return self


    def __exit__(self, type, value, traceback):
        """Implement this method to make this a context manager"""
        logger.info('Now exiting bot.  Goodbye!')

    def post_message(self, msg, chan=BOT_CHAN):
        """Sends a message to a Slack Channel"""
        logger.info('Sent response to channel: {}'.format(channel))
        self.sc.rtm_send_message(channel, mess)

    def handle_command(self, raw_cmd, channel):
        """Parses a raw command string from the bot"""
        pass


def main():
    pass


if __name__ == '__main__':
    main()