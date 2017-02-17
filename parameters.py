# Name of output file
filename = "dates.csv"

# Number of articles to use from each issue
num_articles = 1

# Which issue number to sample in each volume
issue = 1

# Number of volumes to use
num_volumes = 12  # latest 12 volumes, roughly 6 months

latest_volume = 836  # same for both ApJ and ApJL - issues run in parallel

volume_list = range(latest_volume-num_volumes+1,latest_volume+1)
