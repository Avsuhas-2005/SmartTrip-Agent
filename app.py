from flask import Flask, render_template, request

from smarttrip_data import (
    DESTINATIONS,
    get_destinations,
    generate_trip
)


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    trip = None
    error = None

    if request.method == "POST":

        try:
            source = request.form.get(
                "source",
                ""
            ).strip()

            destination = request.form.get(
                "destination",
                ""
            ).strip()

            days = int(
                request.form.get("days", 1)
            )

            people = int(
                request.form.get("people", 1)
            )

            budget = int(
                request.form.get("budget", 0)
            )

            preference = request.form.get(
                "preference",
                "All"
            )

            valid_preferences = {
                "All",
                "Nature",
                "History",
                "Culture",
                "Beach",
                "Museum",
                "Shopping"
            }

            if not source:
                raise ValueError(
                    "Please enter your starting location."
                )

            if destination not in DESTINATIONS:
                raise ValueError(
                    "Please select a valid destination."
                )

            if not 1 <= days <= 14:
                raise ValueError(
                    "Trip duration must be between 1 and 14 days."
                )

            if not 1 <= people <= 20:
                raise ValueError(
                    "Number of travellers must be between 1 and 20."
                )

            if budget <= 0:
                raise ValueError(
                    "Please enter a budget greater than zero."
                )

            if preference not in valid_preferences:
                raise ValueError(
                    "Please select a valid travel preference."
                )

            trip = generate_trip(
                source=source,
                destination=destination,
                days=days,
                people=people,
                budget=budget,
                preference=preference
            )

        except ValueError as exception:
            error = str(exception)

    return render_template(
        "index.html",
        destinations=get_destinations(),
        trip=trip,
        error=error
    )


if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )