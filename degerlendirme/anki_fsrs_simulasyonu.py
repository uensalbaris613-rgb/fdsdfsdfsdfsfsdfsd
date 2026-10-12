"""FSRS-6 workload simulation for the plan's Anki regime.

Anki'nin FSRS-6 zamanlayicisiyla 180 gunluk tekrar yukunu tahmin eder.
Kullanim:  pip install fsrs  &&  python anki_fsrs_simulasyonu.py [plan37|plan37slow|plan47|rec20|all]

Assumes the learner's memory behaves like the FSRS-6 default (population) model:
recall probability at each review = FSRS retrievability at that moment.
Results are order-of-magnitude estimates; card-creation time is not included.
"""
import heapq
import random
import statistics
import sys
from datetime import datetime, timedelta, timezone

from fsrs import Card, Rating, Scheduler, State

DAYS = 180
START = datetime(2026, 1, 1, 9, 0, tzinfo=timezone.utc)

# seconds per answer (assumptions; varied in sensitivity runs)
SEC_NEW_FIRST = 20   # first exposure of a new card (front + image + audio + back)
SEC_LEARN = 9        # learning / relearning step answers
SEC_REVIEW = 8       # review-state answers


def run(new_per_day, stop_new_after=DAYS, first_recall=0.65, slow_again=False,
        seed=0, sec_review=SEC_REVIEW):
    rng = random.Random(seed)
    sched = Scheduler(enable_fuzzing=True)
    cards = []  # list of Card
    daily = []
    for d in range(DAYS):
        day_start = START + timedelta(days=d)
        day_end = day_start + timedelta(hours=15)
        now = day_start
        heap = []
        counter = 0
        # due cards from previous days
        for i, c in enumerate(cards):
            if c.due <= day_end:
                heap.append((c.due, counter, i))
                counter += 1
        heapq.heapify(heap)
        n_rev = n_learn = n_new = n_lapse = 0
        secs = 0.0
        # introduce new cards at start of the day
        n_today = new_per_day if d < stop_new_after else 0
        for _ in range(n_today):
            c = Card()
            cards.append(c)
            i = len(cards) - 1
            recalled = rng.random() < first_recall
            rating = Rating.Good if recalled else Rating.Again
            c, _ = sched.review_card(c, rating, now)
            cards[i] = c
            n_new += 1
            secs += SEC_NEW_FIRST
            now += timedelta(seconds=SEC_NEW_FIRST)
            if c.due <= day_end:
                heapq.heappush(heap, (c.due, counter, i))
                counter += 1
        # process everything due today (reviews + learning steps)
        while heap:
            due, _, i = heapq.heappop(heap)
            c = cards[i]
            if c.due != due:
                continue
            t = max(now, due)
            r = sched.get_card_retrievability(c, t)
            recalled = rng.random() < r
            in_review = c.state == State.Review
            if recalled and slow_again:
                # crude "5-second rule": a share of correct-but-slow answers graded Again
                p_slow = 0.15 if (c.stability or 0) < 10 else 0.05
                if rng.random() < p_slow:
                    recalled = False
            rating = Rating.Good if recalled else Rating.Again
            c, _ = sched.review_card(c, rating, t)
            cards[i] = c
            cost = sec_review if in_review else SEC_LEARN
            secs += cost
            now = t + timedelta(seconds=cost)
            if in_review:
                n_rev += 1
                if not recalled:
                    n_lapse += 1
            else:
                n_learn += 1
            if c.due <= day_end:
                heapq.heappush(heap, (c.due, counter, i))
                counter += 1
        daily.append(dict(day=d + 1, reviews=n_rev, learn=n_learn, new=n_new,
                          lapses=n_lapse, answers=n_rev + n_learn + n_new,
                          minutes=secs / 60.0, total_cards=len(cards)))
    return daily


def summarize(label, runs):
    def avg(key, day):
        return statistics.mean(r[day - 1][key] for r in runs)
    print(f"\n=== {label} ===")
    print("day  dueRev  learnSteps  new  answers  minutes  cards")
    for day in (30, 60, 90, 120, 141, 150, 167, 180):
        print(f"{day:>3}  {avg('reviews', day):6.0f}  {avg('learn', day):10.0f}  "
              f"{avg('new', day):3.0f}  {avg('answers', day):7.0f}  {avg('minutes', day):7.0f}  "
              f"{avg('total_cards', day):5.0f}")
    peak_day = max(range(1, DAYS + 1), key=lambda d: avg('minutes', d))
    print(f"peak minutes ~{avg('minutes', peak_day):.0f} on day {peak_day}; "
          f"mean minutes days 121-180: "
          f"{statistics.mean(avg('minutes', d) for d in range(121, 181)):.0f}")


if __name__ == "__main__":
    seeds = [1, 2, 3]
    scen = sys.argv[1] if len(sys.argv) > 1 else "all"
    if scen in ("all", "plan37"):
        summarize("Plan: 37 new/day (30 headword + ~7 opaque), all 180 days",
                  [run(37, seed=s) for s in seeds])
    if scen in ("all", "plan37stop"):
        summarize("Plan: 37 new/day, new cards stop after day 135 (5,000 cards)",
                  [run(37, stop_new_after=135, seed=s) for s in seeds])
    if scen in ("all", "plan37slow"):
        summarize("Plan: 37 new/day + '5-second rule' (slow-correct graded Again)",
                  [run(37, slow_again=True, seed=s) for s in seeds])
    if scen in ("all", "plan47"):
        summarize("Plan + Empower words: 47 new/day",
                  [run(47, seed=s) for s in seeds])
    if scen in ("all", "rec20"):
        summarize("Alternative: 20 new/day",
                  [run(20, seed=s) for s in seeds])
