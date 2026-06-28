# Dominion Protocol

A Deep Space Nine-themed Python project built across seven seasons as a structured programming curriculum. It starts as a terminal-based patrol briefing and grows into a fully playable combat simulator with a live Dominion War data pipeline.

---

## What It Is

Dominion Protocol is two things running in parallel:

**game.py** — a turn-based combat game set aboard the USS Defiant during the Dominion War. The player commands the Defiant against escalating threats: Maquis raiders, Klingon warships, Jem'Hadar fighters, and Dominion battleships. Combat uses weapon loadouts, crew abilities, shield mechanics, and warp factor-based escape calculations.

**ops.py** — a Starfleet Operations dashboard that tracks mission data, classifies threats, logs combat outcomes to a SQLite database, and generates intelligence reports and battle charts via Pandas and Matplotlib.

The two systems are connected: combat outcomes from game.py feed into the ops.py ledger, and ship upgrades built in ops.py apply directly to the Defiant's stats.

---

## Project Structure

The project is built in seven seasons, each adding new Python concepts and new game mechanics. `game.py` is the cumulative file — it grows with every season. `season_N.py` files are the exam builds: written from scratch at the end of each season to prove the concepts are understood.

| Season | Chapters | What It Adds |
|--------|----------|--------------|
| 1 | 1–2 | USS Rio Grande patrol briefing — variables, strings, f-strings |
| 2 | 3–4 | Mission generator, patrol log — lists, loops |
| 3 | 5–6 | Defiant arrives. Hit/miss logic, enemy profiles, crew bonuses |
| 4 | 7–8 | Fully playable combat — user input, while loops, functions |
| 5 | 9–10 | Ship, crew, and enemies as classes — save/load ship state |
| 6 | 11 + Pandas | Full test suite, Pandas integration, Dominion War opens |
| 7 | 15–17 | Live data pipeline — APIs, SQLite, Matplotlib intelligence charts |

---

## Stack

- Python 3
- Pandas
- Matplotlib
- SQLite (`sqlite3`)
- Requests (API calls)

---

## Why This Project Exists

This is a portfolio project built during a career transition into clinical data engineering. The skills demonstrated here — data pipelines, SQL, testing, APIs, object-oriented design — map directly to production data engineering work in regulated environments.

The DS9 theme is intentional. A project you're invested in is a project you finish.

---

## Current Status

Season 1 complete — USS Rio Grande patrol briefing operational.
