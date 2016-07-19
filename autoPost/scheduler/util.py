__author__ = 'sharvija'

FREQUENCIES=(
    ("hourly", "Hourly"),
    ("weekly", "Weekly"),
    ("minutly", "Minutly"),
    ("daily", "Daily"),
    ("yearly", "Yearly")

)

valid_frequencies = ["hourly", "weekly", "minutly", "daily", "yearly"]

SCHDULER_TYPE = (
    ("interval", "Interval"),
    ("cron", "Cron")
)

SCH_ACTIONS=(
    ("tweet", "tweet"),
    ("search", "search"),
    ("follow", "follow")

)


REST_METHODS=(
    ("GET", "GET"),
    ("POST", "POST"),
    ("PUT", "PUT"),
    ("DELETE", "DELETE"),
    ("HEAD", "HEAD")
)