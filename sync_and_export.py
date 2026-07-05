#!/usr/bin/env python3
"""
Cloud sync script — runs in GitHub Actions.
Pulls today's Garmin data, merges with existing veer-data.json, writes updated file.
No Omada pull (MFA blocks it in CI) — carries last known weight forward.
"""

import json, sys
from datetime import date, datetime
from pathlib import Path

TODAY     = date.today()
VEER_DATA = Path("veer-data.json")
TOKEN_FILE = Path.home() / ".garmin_tokens.json"


def pull_garmin() -> dict | None:
    try:
        from garminconnect import Garmin
    except ImportError:
        print("garminconnect not installed"); return None

    try:
        client = Garmin()
        client.login(str(TOKEN_FILE))
    except Exception as e:
        print(f"Garmin login failed: {e}"); return None

    ds = TODAY.isoformat()
    try:
        stats = client.get_stats(ds)
        bb    = client.get_body_battery(ds, ds)
        sleep = client.get_sleep_data(ds)
        tr    = client.get_training_readiness(ds)
    except Exception as e:
        print(f"Garmin fetch failed: {e}"); return None

    # Body battery: list of [timestamp, level] — find peak
    bb_peak  = max((x[1] for x in (bb or []) if x[1] is not None), default=None)
    bb_start = min((x[1] for x in (bb or []) if x[1] is not None), default=None)

    # Sleep seconds
    sleep_s = None
    sleep_score = None
    if sleep:
        daily = sleep.get("dailySleepDTO", {})
        sleep_s     = daily.get("sleepTimeSeconds")
        sleep_score = daily.get("sleepScore") or daily.get("sleepScores", {}).get("overall", {}).get("value")

    # Training readiness
    tr_val = None
    if tr:
        if isinstance(tr, list) and tr:
            tr_val = tr[0].get("score") or tr[0].get("trainingReadinessScore")
        elif isinstance(tr, dict):
            tr_val = tr.get("score") or tr.get("trainingReadinessScore")

    row = {
        "training_readiness": tr_val or stats.get("trainingReadinessScore"),
        "body_battery_start": bb_start or stats.get("bodyBatteryLowest"),
        "body_battery_peak":  bb_peak  or stats.get("bodyBatteryHighest"),
        "rhr":                stats.get("restingHeartRate"),
        "sleep_h":            round(sleep_s / 3600, 1) if sleep_s else None,
        "sleep_score":        sleep_score,
        "hrv_status":         stats.get("hrvStatus", "Unknown"),
        "hrv_streak":         0,
    }
    print(f"Garmin: TR={row['training_readiness']} BB={row['body_battery_start']}->{row['body_battery_peak']} RHR={row['rhr']} Sleep={row['sleep_h']}h/{row['sleep_score']}")
    return row


def upsert(arr, date_str, val_key, val):
    if val is None:
        return arr
    for e in arr:
        if e.get("date") == date_str:
            e[val_key] = val
            return arr
    arr.append({"date": date_str, val_key: val})
    arr.sort(key=lambda x: x.get("date", ""))
    return arr


def main():
    existing = {}
    if VEER_DATA.exists():
        try:
            existing = json.loads(VEER_DATA.read_text())
        except Exception:
            pass

    today_row = pull_garmin()
    if today_row is None:
        print("ERROR: could not pull Garmin data"); sys.exit(1)

    # Preserve existing hrv_status if Garmin didn't return one
    if today_row.get("hrv_status") in (None, "Unknown", ""):
        today_row["hrv_status"] = existing.get("today", {}).get("hrv_status", "Unknown")

    bb_arr = existing.get("body_battery", [])
    if today_row.get("body_battery_peak") is not None:
        bb_arr = upsert(bb_arr, TODAY.isoformat(), "v", today_row["body_battery_peak"])

    out = {
        "generated":    datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S") + "Z",
        "today":        today_row,
        "weight":       existing.get("weight", []),
        "body_battery": bb_arr,
        "hrv":          existing.get("hrv", []),
        "o2":           existing.get("o2", []),
    }
    if existing.get("coaches"):
        out["coaches"] = existing["coaches"]
    if existing.get("coaches_generated"):
        out["coaches_generated"] = existing["coaches_generated"]

    VEER_DATA.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"veer-data.json written for {TODAY.isoformat()}")


if __name__ == "__main__":
    main()
