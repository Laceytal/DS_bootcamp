num_of_steps = 3

report_template = (
    "We made {total} observations by tossing a coin: {tails} were tails and {heads} were heads. "
    "The probabilities are {tails_frac:.2f}% and {heads_frac:.2f}%, respectively. "
    "Our forecast is that the next {steps} observations will be: {pred}."
)

log_file = "analytics.log"

telegram_url = "TG_URL"
telegram_chat_id = "TG_CHAG_ID"  # id чата/канала
