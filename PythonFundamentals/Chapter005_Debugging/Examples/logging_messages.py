import logging


def main() -> None:
    logger: logging.Logger = logging.getLogger(__name__)

    # logging.basicConfig(filename="log_example.log", level=logging.DEBUG,
    #                     format=" %(asctime)s - %(levelname)s - %(message)s")

    logging.basicConfig(level=logging.DEBUG,
                        format=" %(asctime)s - %(levelname)s - %(message)s")

    logger.debug("Some minor code and debugging details.")

    logger.info("An event happened.")

    logger.warning("Something could go wrong.")

    logger.error("An error has occurred.")

    logger.critical(
        "The program is unable to recover and will now terminate!")

    logging.disable(logging.DEBUG)

    logger.debug("This will never be logged")


if (__name__ == "__main__"):
    main()
