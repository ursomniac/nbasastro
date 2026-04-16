function getNextMeeting() {
    const now = new Date();
    function findFirstWednesday(date) {
        let d = new Date(date.getFullYear(), date.getMonth(), 1);
        while (d.getDay() !== 3) { d.setDate(d.getDate() + 1); }
        d.setHours(18, 0, 0, 0);
        return d;
    }
    let meetingDate = findFirstWednesday(now);
    if (now > meetingDate) {
        let nextMonth = new Date(now.getFullYear(), now.getMonth() + 1, 1);
        meetingDate = findFirstWednesday(nextMonth);
    }
    const options = { weekday: 'long', month: 'long', day: 'numeric' };
    document.getElementById('next-meeting-text').innerText = meetingDate.toLocaleDateString('en-US', options);
}
getNextMeeting();
