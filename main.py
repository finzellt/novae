"""Entry point for the Nova Catalog
"""


def main(args, clargs, log):
    from .novacatalog import NovaCatalog
    from astrocats.catalog.argshandler import ArgsHandler

    # Create an `ArgsHandler` instance with the appropriate argparse machinery
    args_handler = ArgsHandler(log)
    # Parse the arguments to get the configuration settings
    args = args_handler.load_args(args=args, clargs=clargs)
    # Returns 'None' if no subcommand is given
    if args is None:
        return

    print(args)
    catalog = NovaCatalog(args, log)

    # Run the subcommand given in `args`
    args_handler.run_subcommand(args, catalog)

    return
