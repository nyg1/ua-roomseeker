// This project is licenced under the MIT licence.

/**
 * Main JavaScript file, contains most of the functionality for the app.
 */


/**
 * All building names, and day of week mappings.
 */
const buildings = [
    "AF", "BS", "BUS", "C", "CAB", "CCIS", "CSC", "ECHA", "ED", "ESB",
    "ETLC", "HC", "HUB","MEC", "NRE", "SAB", "SUB", "T", "TEL", "TL", "V", "VVC"
];

const week = ["M", "T", "W", "R", "F"];


/**
 *  Button link object. Turns any element into a button that redirects
 *  to a given url.
 */
var button_link = new Vue({
    el: '.button-link',
    methods: {
        clicked: function(url) {
            window.location.href = url;
        }
    }
});


/** 
 *  Seeker object. Main app functionality. Given a time and building, queries
 *  the database for available rooms.
 */
var seeker = new Vue({
    el: '#seeker',
    data: {
        time: init_time(),
        building: "",
        day: init_day(),
        building_options: buildings,
        day_options: week,
        msg: ""
    },
    methods: {
        convert_time: function (time) {
            // Convert time input to minutes since day started.
            var hours = parseInt(time.substr(0, 2));
            var minutes = parseInt(time.substr(3, 5));

            return 60 * hours + minutes;
        },
        validate: function(time, building, day) {
            // Validate time/day/building values.
            if (building === "" || building === undefined || building === null) return {valid: false, msg: "Please choose a building."};
            else if (time === "" || time === undefined || time === null) return {valid: false, msg: "Please choose a time."};
            else if (day === "" || day === undefined || day === null) return {valid: false, msg: "Please choose a day of the week."};

            var converted = this.convert_time(time);
            if (converted < 420 || converted >= 1200) return {valid: false, msg: "Please choose a time from 7:00 AM to 8:00 PM."};

            // If the previous checks all pass, the values are valid.
            return {valid: true, msg: ""};
        },
        submitted: function () {
            // Submits query and prints the results.
            var res = this.validate(this.time, this.building, this.day);
            this.msg = res.msg;

            if (res.valid) {
                // TODO: Submit the query to the right API.
                console.log("day: " + this.day + ", time: " + this.time + ", building: " + this.building);
                results.queried = true;
            } else {
                // Stop displaying query results as the last query was invalid.
                results.queried = false;
            }
        }
    }
});


var results = new Vue({
    el: "#results",
    data: {
        queried: false,
        values: [
            {room: "ETLC 1-005", times: "7:00 AM - 9:00 AM"},
            {room: "ETLC 1-007", times: "8:00 AM - 9:30 AM"},
            {room: "ETLC 2-002", times: "10:00 AM - 6:00 PM"},
            {room: "ETLC 2-005", times: "11:00 AM - 1:00 PM"}
        ]
    }
});


/**
 * Get initial day and time values based on the computer's clock.
 */
function init_day() {
    return week[Math.max(0, Math.min(4, new Date().getDay() - 1))];
}

function init_time() {
    let hours = new Date().getHours();
    let minutes = Math.min(30, new Date().getMinutes());

    // Get lower bound for current time.
    if (minutes < 30) minutes = 0;
    if (hours < 7) hours = 7;
    else if (hours > 20) hours = 20;

    // Format and return the time.
    return String(hours).padStart(2, '0') + ":" + String(minutes).padStart(2, '0');
}