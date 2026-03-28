import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os

COLORS = {
    "ai":       "#7F77DD",
    "non_ai":   "#1D9E75",
    "positive": "#3B8BD4",
    "negative": "#E24B4A",
    "neutral":  "#888780",
    "accent":   "#EF9F27",
}

def set_style():
    mpl.rcParams.update({
        "figure.facecolor":   "white",
        "axes.facecolor":     "white",
        "axes.spines.top":    False,
        "axes.spines.right":  False,
        "axes.grid":          True,
        "axes.grid.axis":     "y",
        "grid.alpha":         0.3,
        "grid.linestyle":     "--",
        "font.size":          11,
        "axes.titlesize":     13,
        "axes.titleweight":   "bold",
        "figure.dpi":         120,
    })

def load_data():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base, "data", "tech_layoffs_2026_tracker.csv")
    df = pd.read_csv(path, parse_dates=["layoff_date"])
    df["ai_cited"]  = df["ai_cited"].astype(bool)
    df["month_num"] = df["layoff_date"].dt.month
    df["stock_up"]  = (df["stock_change_day_pct"] > 0).astype(int)
    return df

def save_chart(fig, name):
    base   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    folder = os.path.join(base, "outputs")
    os.makedirs(folder, exist_ok=True)
    fig.savefig(os.path.join(folder, f"{name}.png"), dpi=150, bbox_inches="tight")
    print(f"Saved → outputs/{name}.png")

def dataset_summary(df):
    print("=" * 50)
    print("  Tech Layoffs 2026 — Dataset Summary")
    print("=" * 50)
    print(f"  Rows            : {len(df)}")
    print(f"  Total jobs cut  : {df['jobs_cut'].sum():,}")
    print(f"  AI-cited        : {df['ai_cited'].sum()} / {len(df)}")
    print(f"  Date range      : {df['layoff_date'].min().date()} → {df['layoff_date'].max().date()}")
    print(f"  Missing values  : {df.isnull().sum().sum()}")
    print("=" * 50)