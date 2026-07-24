> _Regenerated after Veer-QA flagged the first draft._

Fixing the two QA-flagged issues — restoring the dropped 07-21 O2Ring SpO2 discrepancy to the memory block, and reframing today's protein overage as a repeat pattern with an actual trim offered rather than a shrug. Here's the corrected full brief.

---

**2026-07-24 — Friday. Biotin: SKIP today (Tue/Thu/Sat only).**

## 🧠 COACH PANEL

🏋️ **Head Coach:** BB peak 68 (garmin/daily/2026-07-24.md) lands in the 60–74 tier — 3 sets, weights cut 10–20%, lateral raises held locked at 25lb; Upper is the call (see session selection below), not calendar-Friday-Lower.
🔋 **Recovery Scientist:** TR dropped 70→66 and HRV flipped Balanced(68ms)→Unbalanced(65ms) overnight — day 1 of a fresh instance, well short of the 3-day override threshold, but worth watching tomorrow.
😴 **Sleep & Breathing:** 6.7h (399m, score 84) is 1h shorter than last night despite deeper sleep (Deep 87m vs 73m) — architecture quality up, duration down; O2Ring gap now 3+ nights, last real data 07-21.
🧬 **Longevity Scientist:** Vigorous minutes sitting at 49 this week vs the 75+ target — behind pace; fisetin next window is Aug 1-2, confirm stock before then.
🧪 **Hormonal Specialist:** Weight untracked 2 days running (Omada gap 07-23, 07-24) — last confirmed 173.7 lb (07-22), mid-band; RHR steady at 52 both days, no elevation signal.
🥗 **Nutritionist:** Friday dinner rotation (chicken + sardines) plus a fully-run legume/breakfast/lunch stack projects to ~200g protein against the 160-165g training-day ceiling — same over-target pattern as 07-21, trim option below.
🦵 **Movement Coach:** Last Lower session 07-22 (corrective block, right-side priority, completed) — Upper today means the right-knee corrective work waits until the next Lower day; no gap created.
💎 **Aesthetics Coach:** Upper trailing-week frequency is 1x (07-21) vs Lower's 2x (07-17, 07-22) — today's Upper call also closes that gap and serves the V-taper priority.

## Weight

**Not available in today's data pull** (Omada — no reading 07-23 or 07-24). Last confirmed: **173.7 lb** on 2026-07-22 — CARRIED FROM 07-22, NOT TODAY'S ACTUAL READING. Sits mid-band (172–175).

## Recovery Scorecard

| Metric | Yesterday (07-23) | Today (07-24) | Delta | Source |
|---|---|---|---|---|
| Body Battery (start→peak) | 8 → 79 | 6 → 68 | peak −11 | garmin/daily/2026-07-23.md / 2026-07-24.md |
| RHR | 52 bpm | 52 bpm | 0 | same |
| HRV status | BALANCED (68ms) | UNBALANCED (65ms) | flipped negative | same |
| Sleep duration | 7.7h (464m) | 6.7h (399m) | −1.0h | same |
| Sleep score | 83 | 84 | +1 | same |
| Stress avg | 37 | 22 | −15 | same |
| Steps | 13,091 | 187 | −12,904 | same |
| Training Readiness | 70 | 66 | −4 | same |
| O2Ring score | not available in today's data pull | not available in today's data pull | n/a | O2Ring section (no PDF) |
| O2Ring drops/hr | not available in today's data pull | not available in today's data pull | n/a | same |
| SpO2 lowest (wrist) | 85% | 85% | 0 | garmin/daily/2026-07-23.md / 2026-07-24.md |
| Time <90% | not available in today's data pull | not available in today's data pull | n/a | not tracked by Garmin field |

**Pattern (3 lines max):**
- HRV flipped Balanced→Unbalanced overnight (68→65ms) as BB peak also fell 79→68 — a normal post-hike dip, day 1, not yet a concern.
- Sleep volume down 1h but deep sleep up 14 min (73m→87m) — quality compensating partially for duration.
- Wrist SpO2 low held flat at 85% both nights; O2Ring (the trustworthy instrument per measurement science) has no data for 3+ nights running.

## Active Flags

- **CRITICAL — Pulmonologist:** referral submitted Jun 1, 2026 — **53 days unscheduled** as of today. Standing #1 item.
- HRV flipped to Unbalanced today (HRV_UNBALANCED_12, garmin/daily/2026-07-24.md) — day 1 of a new instance after 07-23's Balanced reading. Override needs 3+ consecutive days; does **not** fire.
- **Pipeline discrepancy:** the HRV persistence computation reports streak=0 ending today, but today is actually Unbalanced following a Balanced day, so the correct streak is 1. Override conclusion is unaffected either way (1 day is far under the 3-day threshold) — flagging as a counter bug to fix, not a training-call risk.
- **Pipeline discrepancy:** this morning's 06:30 healthcheck reports veer-data.json's today-block as blank for training_readiness/body_battery_peak/rhr/sleep_score, but the source markdown (garmin/daily/2026-07-24.md) is fully populated with all four. The markdown is authoritative for this brief; the JSON export step needs a fix so downstream consumers aren't fed nulls.
- O2Ring gap: no PDF for 3+ nights, last real data 07-21 (score 6.9). **Unresolved:** 07-21 night's lowest SpO2 has been recorded two different ways in history (81% vs 85%) — needs source-PDF reverification before citing to a pulmonologist.
- Anaerobic load shortage — 4th+ consecutive day below target (Ana 55 vs 133–400, garmin/daily/2026-07-24.md).
- Vigorous intensity minutes: 49 this week vs 75+/week target — behind pace.
- Weight pipeline: Omada not available 07-23 or 07-24, two consecutive missed pulls.
- Inventory: chicken breast (lunch + Friday dinner anchor) and dry garbanzo (Friday legume) still ❔ unconfirmed in INVENTORY.md — canned garbanzo is the backup if dry wasn't soaked Thursday night.

## Training Call

**Override checklist — all five checked, none fire:**
- **A. Training Readiness:** 66 MODERATE, not Low → clear.
- **B. Acute Load:** 267, well under the 450–500 deload threshold → clear.
- **C. Recovery Time:** 0.0h → clear.
- **D. HRV persistence:** Unbalanced today is day 1 of a fresh instance (see pipeline note above) — need 3+ consecutive days to latch → clear.
- **E. Load Focus explicit warning:** none present; "ANAEROBIC_SHORTAGE" is informational, not a scale-back warning → clear.

**Body Battery tier:** peak 68 → **60–74 band → 3 sets, weights cut 10–20%** across variable lifts; lateral raises stay locked at 25lb regardless of tier.

**Session selection — reasoned from actual training history, not the calendar:**
1. Last Upper: 07-21 (3 days ago, 72h+ — fully past the 48h MPS window). Last Lower: 07-22 (2 days ago, ~48h — right at the edge, still technically inside the repair window).
2. Trailing 7-day frequency (07-17→07-24): Lower = 2x (07-17, 07-22, already at the 2x/week target). Upper = 1x (07-21, behind pace).
3. Upper wins on both counts — more fully recovered AND behind on frequency. Lower would be the second Lower-adjacent stimulus inside the tightest recovery window while Upper has had none in 3 days.
4. V-taper priority breaks any remaining tie toward Upper (lateral delts/back width = the highest-ROI aesthetic lever), and the open anaerobic-load shortage flag also favors a real strength session today.
5. No layoff re-entry needed — Upper was trained 3 days ago at full weights, so this is a standard progression session, not a re-entry.

**Call: Upper Body, 3 sets, weights cut 10–20% off standard, lateral raises locked at 25lb.** This diverges from the calendar-default (Friday = Lower) — Lower already hit its weekly frequency target and is still inside its tightest recovery window; Upper is both more recovered and behind on frequency.

## Full Training Plan — Upper Body (BB 60–74 tier: 3 sets, weights cut 10–20%)

**Warmup:** Treadmill 5–7 min, incline 4–5, speed 2.8–3.0 mph.

| # | Exercise | Standard Weight | Today's Weight (cut) | Sets × Reps | Notes |
|---|---|---|---|---|---|
| 1 | Lateral Raises | 25lb (11kg) | **25lb (11kg) — LOCKED, no cut** | 3 × 12 | Always first. Shoulders DOWN, away from ears. Garmin logs as "Face Pull." |
| 2 | Rear Delt Machine | 90lb (41kg) | 75lb (34kg) — cut 17% | 3 × 10 | |
| 3 | Incline DB Press | 50lb (23kg) | 40lb (18kg) — cut 20% | 3 × 10 | Shoulders down throughout. |
| 4 | Converging Chest Press | 105lb (48kg) | 90lb (41kg) — cut 14% | 3 × 10 | Garmin logs as "Bench Press." |
| 5 | Lat Pulldown | 145lb (66kg) | 125lb (57kg) — cut 14% | 3 × 10 | Assisted chin-up is a valid sub if machine's busy. |
| 6 | DB Curls | 25lb (11kg) | 20lb (9kg) — cut 20% | 3 × 12 | |
| 7 | Tricep Pushdown | 42.5lb (19kg) | 35lb (16kg) — cut 18% | 3 × 10 | |
| 8 | Push-ups | Bodyweight | Bodyweight | 2–3 sets to failure | |
| 9 | Incline Treadmill Finisher | Incline 10 | Incline 10, speed 3.0 mph (BB<80, not 3.2–3.5) | 20 min | Never skip. |

Log as Strength Training, Forerunner 970, Auto Set Detection + Auto Rest Timer ON. Celtic sea salt pinch post-finisher (training day).

## Protein Target + Full Meal Plan

**Training day target: 160–165g muscle protein.** Carb decision: **sweet potato 200g added at dinner** — two triggers fire: (1) Acute Load 267 ≥200 on a genuinely moderate-to-hard trailing window, and (2) yesterday's numbers came in soft after Thursday's hike (HRV, BB peak, TR, sleep duration all down) — the correction goes on today's training day per the soft-numbers protocol.

**⚠️ Protein check before serving:** running the full plan below as written totals **≈200g — roughly 35–40g over the 165g ceiling, the same pattern flagged on 07-21 (over-target with the carb still needed, not a one-off).** Past ~2.2g/kg the excess just gets burned for energy — it isn't buying extra muscle. **Trim option: cut lunch chicken 160g→150g and skip the Siggi's yogurt** — brings the day to ≈182g, closer to the ceiling while keeping every anchor intact. Take the trim unless you're deliberately banking extra food today.

**Inventory check (INVENTORY.md):** chicken breast and dry garbanzo are both ❔ unconfirmed. If chicken is out → substitute turkey, shrimp, or salmon 150g+ (never egg whites/legumes alone). If dry garbanzo wasn't soaked Thursday night → use canned, well-rinsed, as backup.

**BREAKFAST (training day):**
1. ACV — 1 tbsp in water
2. Goat bone broth + lemon — 240ml warm
3. Whole eggs — 3
4. Breakfast bowl (prepped overnight): sprouted oats 50g + Isopure whey 1 scoop + collagen 1–2 scoops (with the berries below for vitamin C) + almond milk 200ml + egg whites 6 tbsp + frozen berries 220g + dried cranberries 20g + chia seeds 10g + walnuts 15g + pumpkin seeds 10g
5. Add fresh this morning only: Brazil nut 1 whole, bee pollen 5g, broccoli microgreens 1 tbsp raw on top last second
6. Kefir — 100ml
7. 10-min walk

**LUNCH:**
- ACV — 1 tbsp in water, before meal
- Spinach 100g + broccoli 150g — eat first
- Chicken breast — **150g cooked (trimmed from 160g)** — primary anchor
- Garbanzo — 100g cooked, fiber side (canned rinsed backup if dry not soaked)
- Seaweed sheets — 2–3 sheets, eaten with the vegetable course
- Avocado — half, or olive oil 1 tbsp drizzle, after protein
- Turmeric + black pepper, together. Garlic 2 cloves.
- Kimchi — 35g, cold, last
- Broccoli microgreens — 1 tbsp raw, on top, absolute last
- **Skip Siggi's/Greek yogurt today (trim)** — or include 150g if you want the extra protein and are fine tracking closer to 200g
- 10-min walk after

**DINNER (Friday rotation — chicken + sardines):**
- Psyllium husk — 5g in warm water, before meal, drink within 60 sec
- ACV — 1 tbsp in water
- Spinach 80g + zucchini or yellow squash 150g — eat first
- Chicken breast — 150g cooked
- Sardines — half tin
- Garbanzo — remaining 80–100g cooked
- **Sweet potato — 200g** (carb trigger fired, see above)
- Avocado — half, after protein
- Sesame oil — finishing drizzle, off heat
- Olive oil + garlic + turmeric + black pepper
- Kimchi — 30g, cold, last
- Broccoli microgreens — 1 tbsp raw, absolute last
- 10-min walk after
- Dark chocolate (Hu Salty Dark) — 3 bites, before 8 PM
- Jojo's chocolate blocks — 3 blocks, locked evening ritual, not counted toward protein
- Mastic gum — 20–30 min after

## Full Supplement Schedule

**Morning with breakfast:**
- Creatine 5g
- D3 + K2 (Solaray) 5000 IU
- Omega-3 (Nordic Naturals) 2 caps
- Beef Liver — 2 caps (training day)
- B12 sublingual 5000mcg — hold 30 sec under tongue
- CoQ10 Ubiquinol 100mg
- **Biotin — SKIP today** (Tue/Thu/Sat only)
- **Fisetin — SKIP today** (1st–2nd of month only; next window Aug 1–2, 2026)
- Probiotic (Garden of Life 50B) — separate, empty stomach

**Before dinner:** Psyllium husk 5g in warm water, within 60 sec.

**With dinner:** Zinc Picolinate (Solgar) 22mg + Thorne Copper 2mg — always together.

**9:30 PM:** Magnesium Glycinate (Jarrow) 240mg + Tart Cherry Juice 60ml (not 8oz) + KSM-66 600mg (cycle active, break starts Sept 7, 2026 — do not reorder before then).

## Hour-by-Hour Schedule

- **6:00 AM** — wake, ACV + bone broth
- **6:15 AM** — breakfast bowl + eggs + kefir + morning supplements
- **6:30 AM** — 10-min walk
- **9:30–11:30 AM** — Upper Body session (warmup → 9 exercises → finisher)
- **12:30 PM** — lunch + 10-min walk
- **3:30 PM** — light activity / mastic gum from lunch
- **6:30 PM** — psyllium husk, then dinner + 10-min walk
- **7:45 PM** — dark chocolate + Jojo's blocks (before 8 PM cutoff)
- **9:30 PM** — magnesium, tart cherry, KSM-66
- **10:00 PM** — screens off
- **10:30 PM** — lights out, full sleep protocol (nose strip, mouth tape, O2Ring on thumb vibration off, earplugs, back sleeping)

## The One Thing

**Call the pulmonologist's office today — 53 days unscheduled is the longest this has gone.** Everything else in this brief is optimization; this is the one open item with real medical weight (T90 evidence, OSA-driven HRV/testosterone suppression) sitting untouched.



**Files read:** MEMORY.md, DAILY_RULES.md, PROTOCOLS.md (locked meal/supplement/workout section), KNOWLEDGE_BASE.md, MEASUREMENT_SCIENCE.md, INVENTORY.md, garmin/daily/2026-07-18.md, garmin/daily/2026-07-19.md, garmin/daily/2026-07-20.md, garmin/daily/2026-07-21.md, garmin/activities/2026-07-21-strength-workout.md, garmin/activities/2026-07-21-treadmill-running.md, garmin/daily/2026-07-22.md, garmin/activities/2026-07-22-lower.md, garmin/activities/2026-07-22-treadmill-running.md, garmin/daily/2026-07-23.md, garmin/activities/2026-07-23-coconino-county-hiking.md, garmin/daily/2026-07-24.md, Omada weight source (not available today), O2Ring source (not available today), pipeline healthcheck output (06:30).


---

## 🧠 VEER-QA (original flag)

⚠️ **VEER-QA: PASS WITH NOTE**

**Verified:** All headline numbers trace to source (TR 66, BB 6→68, HRV 65ms Unbalanced, RHR 52, sleep 6.7h/84, SpO2 low 85% — all match garmin/daily/2026-07-24.md). Weight correctly labeled as carried from 07-22, not today's. Training call is properly reasoned from history (Upper 72h recovered + 1x trailing frequency + V-taper) not the Friday-Lower calendar; all five override checks walked and genuinely clear; BB 68 → 60–74 tier applied with cuts of 14–20% on every variable lift and lateral raises correctly held locked at 25 lb. The plan caught two real pipeline contradictions the right way — the HRV streak counter reading 0 when today's Unbalanced status makes it 1 (flagged, correctly noted override is clear either way), and the healthcheck's "blank JSON" claim contradicting a fully populated source markdown. No phantom foods, no rice, carb trigger legitimately fired (Acute Load 267 ≥200 + soft next-day numbers), pulmonologist at day 53, biotin SKIP stated, weights in lb and kg, times in 12-hour.

**Carry-forward notes for the specialists:**

1. **Dropped open item in the regenerated MEMORY.md:** the unresolved 07-21 O2Ring lowest-SpO2 discrepancy (81% vs 85%, needs source-PDF reverification) was in the prior memory's open items and vanished from the replacement block. That's an active data-integrity question feeding the pulmonologist evidence — restore it on the next rebuild.

2. **Protein ~200g is accepted too casually.** The plan invokes "ceiling not floor" while running ~35–40g over the ceiling. Whole-food overage is better than a redundant shake (the 07-21 lesson), but the honest framing is that this is a repeat of the over-target pattern, not "expected and fine" — a one-line trim option (e.g., lunch chicken 160g→150g, skip the Siggi's) should have been offered rather than normalizing it.

Neither error would mislead Veer on today's decisions — the plan stands.