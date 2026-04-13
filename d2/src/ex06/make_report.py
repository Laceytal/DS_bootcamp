import sys
import config
from analytics import Research


if __name__ == "__main__":
    reader = Research(sys.argv[1])

    try:
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
            pred=f"{pred_tails} решка и {pred_heads} орла"
        )

        print(report)
        analytics.save_file(report, "report", "txt")
        reader.send_to_telegram("Отчёт успешно создан")

    except Exception as e:
        print("Ошибка:", e)
        reader.send_to_telegram("Отчёт не создан из-за ошибки")
