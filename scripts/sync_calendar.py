import requests
import os
from icalendar import Calendar
import recurring_ical_events
from datetime import datetime, date, timedelta

ICS_SOURCES = [
    {
        "url": "https://calendar.google.com/calendar/ical/nbasastro%40gmail.com/public/basic.ics",
        "tag": "NBAS"
    },
    {
        "url": "https://calendar.google.com/calendar/ical/3b32e873531bab30292740da69ae860281131db1ff6ae69874f6f6924dc275af%40group.calendar.google.com/public/basic.ics",
        "tag": "LOCAL"
    }
]

def sync():
    start_date = date.today()
    end_date = start_date + timedelta(days=366)
    all_entries = []

    for source in ICS_SOURCES:
        try:
            response = requests.get(source["url"], timeout=10)
            response.raise_for_status()
        except Exception as e:
            print(f"CONNECTION ERROR ({source['tag']}): {e}")
            continue

        calendar = Calendar.from_ical(response.content)
        events = recurring_ical_events.of(calendar).between(start_date, end_date)

        for event in events:
            dtstart = event.get('dtstart').dt
            date_str = dtstart.strftime("%Y-%m-%d")
            if isinstance(dtstart, datetime):
                time_str = dtstart.strftime("%H:%M")
            else:
                time_str = "--:--"
            summary = str(event.get('summary'))
            location = str(event.get('location', ''))
            all_entries.append(f"{date_str} | {time_str} | {source['tag']} | {summary} | {location}")

    # Sort all events by date
    all_entries.sort()

    os.makedirs("assets/calendar", exist_ok=True)
    with open("assets/calendar/calendar_nbas.txt", "w") as f:
        f.write("\n".join(all_entries))

    print(f"SUCCESS: Generated {len(all_entries)} upcoming events.")

if __name__ == "__main__":
    sync()
