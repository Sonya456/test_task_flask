document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: '/api/events',  // Nowa trasa dla FullCalendar
        eventClick: function(info) {
            window.location.href = '/event/' + info.event.id;
        }
    });

    calendar.render();
});

