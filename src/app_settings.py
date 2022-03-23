import data_settings
# Constants
MILLISECONDS = 1000
SECONDS = 100 * MILLISECONDS
MINUTES = 60 * SECONDS

# App framework settings
TITLE = "TSLA Trade Bot"
UPDATE_TITLE = "Updating..."

# App run settings
DEBUG = True
PORT = "8050"

# Graph timings
TSLA_PRICE_GRAPH_INTERVAL = data_settings.LOOK_BACK * MINUTES
