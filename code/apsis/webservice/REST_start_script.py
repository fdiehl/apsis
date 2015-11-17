__author__ = 'Frederik Diehl'

import REST_interface
import argparse


def start_rest(port=5000, validation=False, cv=5):
    print("Initializing apsis. Val is %s, cv is %s" %(validation, cv))
    print("Initialized apsis on port %s" %port)
    REST_interface.start_apsis(port, validation)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", help="Set the apsis server's port.")
    parser.add_argument("--cross_validation", help="Set the number of cvs if "
                                                   "using --validation.")
    parser.add_argument("--validation", help="Use ValidationLabAssistant",
                    action="store_true")
    args = parser.parse_args()

    validation = False
    if args.validation:
        validation = True
    cv = 5
    if args.cross_validation:
        cv = args.cross_validation
    port = 5000
    if args.port:
        port = args.port
    start_rest(port, validation, cv)