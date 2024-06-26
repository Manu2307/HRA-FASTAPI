DEV = "dev"
ENV_NAME = DEV

FILE_HANDLER = {
    "class": "logging.handlers.TimedRotatingFileHandler",
    "filename": f"logs/{ENV_NAME}.log",
    "formatter": "default",
    "backupCount": 10,
    "when": "midnight",
    "interval": 1,
}

STREAM_HANDLER = {
    "class": "logging.StreamHandler",
    "formatter": "default",
    "stream": "ext://sys.stdout",
}

# FILE_REQ_HANDLER = {
#     "class": "logging.handlers.TimedRotatingFileHandler",
#     "filename": f"logs/{ENV_NAME}.log",
#     "formatter": "request_formatter",
#     "backupCount": 10,
#     "when": "midnight",
#     "interval": 1,
# }
#
# STREAM_REQ_HANDLER = {
#     "class": "logging.StreamHandler",
#     "formatter": "request_formatter",
#     "stream": "ext://sys.stdout",
# }


LOGGING_CONF = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "class": "logging.Formatter",
            "format": "%(asctime)s | %(module)s | %(lineno)d | %(levelname)s | %(message)s",
        },
        "request_formatter": {
            "class": "logging.Formatter",
            "format": "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
        },
    },
    # "handlers": {"log_handler": STREAM_HANDLER, "request_log_handler": STREAM_REQ_HANDLER},
    "handlers": {"log_handler": STREAM_HANDLER},
    "loggers": {
        "": {"handlers": ["log_handler"], "level": "DEBUG", "propagate": True},
        # "RequestLogger": {
        #     "handlers": ["request_log_handler"],
        #     "level": "DEBUG",
        #     "propagate": False,
        # },
    },
}
