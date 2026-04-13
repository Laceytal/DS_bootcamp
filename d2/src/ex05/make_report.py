import sys
from analytics import Research
import config


if __name__ == "__main__":
    path = sys.argv[1]
    reader = Research(path)
    data = reader.file_reader()
    analytics = Research.Analytics(data)

    heads, tails = analytics.counts()
    frac_heads, frac_tails = analytics.fractions(heads, tails)
    predictions = analytics.predict_random(config.num_of_steps)

    pred_heads = sum(row[0] for row in predictions)
    pred_tails = sum(row[1] for row in predictions)

    report = config.report_template.format(
        total=len(data),
        heads=heads,
        tails=tails,
        heads_frac=frac_heads,
        tails_frac=frac_tails,
        steps=config.num_of_steps,
        pred=f"{pred_tails} tails и {pred_heads} heads"
    )

    print(report)

    analytics.save_file(report, "report", "txt")
