def get_cl_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--logging_file", help="Log file path for Pynacea",
        default=None)
    parser.add_argument("--logging_level", help="Logging level for Pynacea")
    return parser.parse_args()
