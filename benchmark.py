from __future__ import annotations

from csv import writer
from pathlib import Path
from statistics import mean
import timeit
from typing import TypedDict


OUTPUT_DIR = Path("benchmark_results")
CSV_PATH = OUTPUT_DIR / "results.csv"
TOTALS_SVG_PATH = OUTPUT_DIR / "totals.svg"
SPEEDUP_SVG_PATH = OUTPUT_DIR / "speedup.svg"
REPEAT_COUNT = 5


class BenchmarkCase(TypedDict):
    title: str
    left_name: str
    left_stmt: str
    left_number: int
    right_name: str
    right_stmt: str
    right_number: int


class BenchmarkRow(TypedDict):
    benchmark: str
    variant: str
    mean_seconds: float
    runs: int
    samples_seconds: list[float]


BENCHMARKS: list[BenchmarkCase] = [
    {
        "title": "List comprehension vs for loop",
        "left_name": "List comprehension",
        "left_stmt": "[x * 2 for x in range(20000)]",
        "left_number": 300,
        "right_name": "For loop with append",
        "right_stmt": """
result = []
for x in range(20000):
    result.append(x * 2)
""",
        "right_number": 300,
    },
    {
        "title": "String join vs string +=",
        "left_name": "String join",
        "left_stmt": """
words = ["python"] * 20000
result = "".join(words)
""",
        "left_number": 200,
        "right_name": "String +=",
        "right_stmt": """
result = ""
for _ in range(20000):
    result += "python"
""",
        "right_number": 20,
    },
    {
        "title": "Dict lookup vs list search",
        "left_name": "Dict lookup",
        "left_stmt": """
data = {i: i * 2 for i in range(50000)}
for i in range(20000):
    value = data[i]
""",
        "left_number": 120,
        "right_name": "List search",
        "right_stmt": """
data = list(range(20000))
for i in range(400):
    value = 19999 in data
""",
        "right_number": 120,
    },
    {
        "title": "Set membership vs list membership",
        "left_name": "Set membership",
        "left_stmt": """
data = set(range(20000))
for i in range(20000):
    value = i in data
""",
        "left_number": 120,
        "right_name": "List membership",
        "right_stmt": """
data = list(range(20000))
for i in range(2000):
    value = i in data
""",
        "right_number": 20,
    },
]


def run_timer(stmt: str, number: int) -> tuple[list[float], float]:
    samples = timeit.repeat(stmt, repeat=REPEAT_COUNT, number=number)
    return samples, mean(samples)


def save_csv(rows: list[BenchmarkRow]) -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    with CSV_PATH.open("w", newline="", encoding="utf-8") as file:
        csv_writer = writer(file)
        csv_writer.writerow(
            ["benchmark", "variant", "mean_seconds", "runs", "samples_seconds"]
        )
        for row in rows:
            csv_writer.writerow(
                [
                    row["benchmark"],
                    row["variant"],
                    f"{row['mean_seconds']:.6f}",
                    row["runs"],
                    ",".join(f"{sample:.6f}" for sample in row["samples_seconds"]),
                ]
            )


def make_bar_chart(
    filename: Path,
    title: str,
    labels: list[str],
    values: list[float],
    color: str,
    value_suffix: str,
) -> None:
    width = 1080
    height = 640
    margin_left = 280
    margin_right = 80
    margin_top = 70
    margin_bottom = 50
    bar_gap = 18
    bar_height = 32
    usable_width = width - margin_left - margin_right
    max_value = max(values) if values else 1.0
    scale = usable_width / max_value if max_value else 1.0

    bars = []
    label_items = []
    value_items = []

    for index, (label, value) in enumerate(zip(labels, values, strict=True)):
        y = margin_top + index * (bar_height + bar_gap)
        bar_width = max(value * scale, 1.0)
        bars.append(
            f'<rect x="{margin_left}" y="{y}" width="{bar_width:.2f}" '
            f'height="{bar_height}" fill="{color}" rx="4" />'
        )
        label_items.append(
            f'<text x="{margin_left - 14}" y="{y + 21}" text-anchor="end">{label}</text>'
        )
        value_items.append(
            f'<text x="{margin_left + bar_width + 10:.2f}" y="{y + 21}">'
            f"{value:.3f}{value_suffix}</text>"
        )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">
<style>
text {{
  font-family: Arial, sans-serif;
  font-size: 14px;
  fill: #1f2937;
}}
.title {{
  font-size: 24px;
  font-weight: bold;
}}
.subtitle {{
  font-size: 13px;
  fill: #4b5563;
}}
</style>
<rect width="100%" height="100%" fill="#ffffff" />
<text x="{margin_left}" y="36" class="title">{title}</text>
<text x="{margin_left}" y="58" class="subtitle">Average of {REPEAT_COUNT} runs</text>
<line x1="{margin_left}" y1="{margin_top - 10}" x2="{margin_left}" y2="{height - margin_bottom}" stroke="#9ca3af" />
{''.join(bars)}
{''.join(label_items)}
{''.join(value_items)}
</svg>
"""
    filename.write_text(svg, encoding="utf-8")


def main() -> None:
    rows: list[BenchmarkRow] = []
    total_labels: list[str] = []
    total_values: list[float] = []
    speedup_labels: list[str] = []
    speedup_values: list[float] = []

    for benchmark in BENCHMARKS:
        left_samples, left_mean = run_timer(
            benchmark["left_stmt"], benchmark["left_number"]
        )
        right_samples, right_mean = run_timer(
            benchmark["right_stmt"], benchmark["right_number"]
        )

        print(benchmark["title"])
        print(f"  {benchmark['left_name']}:  {left_mean:.6f} s")
        print(f"  {benchmark['right_name']}: {right_mean:.6f} s")
        print(f"  Speedup: {right_mean / left_mean:.2f}x\n")

        rows.extend(
            [
                {
                    "benchmark": benchmark["title"],
                    "variant": benchmark["left_name"],
                    "mean_seconds": left_mean,
                    "runs": benchmark["left_number"],
                    "samples_seconds": left_samples,
                },
                {
                    "benchmark": benchmark["title"],
                    "variant": benchmark["right_name"],
                    "mean_seconds": right_mean,
                    "runs": benchmark["right_number"],
                    "samples_seconds": right_samples,
                },
            ]
        )

        total_labels.extend(
            [
                f"{benchmark['title']} / {benchmark['left_name']}",
                f"{benchmark['title']} / {benchmark['right_name']}",
            ]
        )
        total_values.extend([left_mean, right_mean])
        speedup_labels.append(benchmark["title"])
        speedup_values.append(right_mean / left_mean)

    save_csv(rows)
    make_bar_chart(
        TOTALS_SVG_PATH,
        "Benchmark totals, seconds",
        total_labels,
        total_values,
        "#2563eb",
        " s",
    )
    make_bar_chart(
        SPEEDUP_SVG_PATH,
        "Relative speedup of the faster approach",
        speedup_labels,
        speedup_values,
        "#059669",
        "x",
    )

    print(f"Saved CSV results to: {CSV_PATH}")
    print(f"Saved chart to: {TOTALS_SVG_PATH}")
    print(f"Saved chart to: {SPEEDUP_SVG_PATH}")


if __name__ == "__main__":
    main()
