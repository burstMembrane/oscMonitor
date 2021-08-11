#!/osc/bin/python3
# binds to specific port and ip combination parsed in as args,
# then logs all recieved osc messages to the console using a custom logger

import argparse
import math
import logging
from pythonosc import dispatcher
from pythonosc import osc_server
from colorama import init
from colorama import Fore, Back, Style
import sys
init()

logging.basicConfig(
    format='[ %(asctime)s.%(msecs)03d ] %(message)s', level=logging.DEBUG, datefmt="%d-%m-%y %H:%M:%S")


def log_osc(address, *args):

    logging.info(
        "{}[ {} ] {}{}: {}{} {}[{}] {}".format(Fore.CYAN, ':'.join(args[0]), Fore.GREEN, address, Fore.RED, str(args[1]), Fore.BLUE, type(args[1]).__name__, Style.RESET_ALL))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1", help="Listener IP address")
    parser.add_argument("--port",
                        type=int, default=5005, help="OSC Port", required=True)
    parser.add_argument("--address",
                        type=str, default="/*", help="OSC Address to listen for")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map(args.address, log_osc, args.ip, str(args.port))

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    logging.info("{} Listening on {}:{} {}".format(Fore.GREEN,
                                                   server.server_address[0], server.server_address[1], Style.RESET_ALL))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("{}Quitting...{}".format(Fore.RED, Style.RESET_ALL))
        sys.exit(0)
