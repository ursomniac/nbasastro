import requests
import os
from icalendar import Calendar
import recurring_ical_events 
from datetime import datetime, date, timedelta

ICS_URL = "https://calendar.google.com/calendar/ical/4ed44232216bce207ca3a81b5fa5304ebe99f3dec93491707b3543ba28b191c1%40group.calendar.google.com/public/basic.ics"

def sync():
    try:
        response = requests.get(ICS_URL, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"CONNECTION ERROR: {e}")
        return

    # 1. Parse the main calendar
    calendar = Calendar.from_ical(response.content)
    
    # 2. Define the expansion range (from today to 6 months out)
    start_date = date.today()
    end_date = start_date + timedelta(days=366)
    
    # 3. EXPAND RECURRING EVENTS
    events = recurring_ical_events.of(calendar).between(start_date, end_date)
    
    formatted_entries = []
    for event in events:
        dtstart = event.get('dtstart').dt
        
        # Format the date (YYYY-MM-DD)
        date_str = dtstart.strftime("%Y-%m-%d")
        
        # Format the time (HH:MM or --:--)
        if isinstance(dtstart, datetime):
            time_str = dtstart.strftime("%H:%M")
        else:
            time_str = "--:--"
            
        summary = str(event.get('summary'))
        formatted_entries.append(f"{date_str} | {time_str} | {summary}")

    # 4. Save the expanded list
    os.makedirs("data", exist_ok=True)
    with open("assets/calendar/calendar_nbas.txt", "w") as f:
        f.write("\n".join(formatted_entries))
    
    print(f"SUCCESS: Generated {len(formatted_entries)} upcoming events.")

if __name__ == "__main__":
    sync()

