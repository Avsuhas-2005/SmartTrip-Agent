import json
import os
from datetime import datetime


# File used to store previous trip plans
MEMORY_FILE = "memory.json"


# Destination information
DESTINATIONS = {
    "Mysuru": {
        "description": "Explore royal palaces, gardens, museums and cultural attractions.",
        "travel_cost": 800,
        "food_per_person": 500,
        "local_transport_per_day": 400,
        "attractions": [
            {
                "name": "Mysuru Palace",
                "category": "History",
                "cost": 100
            },
            {
                "name": "Mysuru Zoo",
                "category": "Nature",
                "cost": 100
            },
            {
                "name": "St. Philomena's Church",
                "category": "Culture",
                "cost": 0
            },
            {
                "name": "Payana Vintage Car Museum",
                "category": "Museum",
                "cost": 200
            },
            {
                "name": "Chamundi Hills",
                "category": "Nature",
                "cost": 0
            },
            {
                "name": "Karanji Lake",
                "category": "Nature",
                "cost": 50
            },
            {
                "name": "Mysuru Railway Museum",
                "category": "Museum",
                "cost": 50
            },
            {
                "name": "Jaganmohan Palace",
                "category": "History",
                "cost": 100
            },
            {
                "name": "Sand Sculpture Museum",
                "category": "Museum",
                "cost": 80
            },
            {
                "name": "Devaraja Market",
                "category": "Shopping",
                "cost": 0
            },
            {
                "name": "Kukkarahalli Lake",
                "category": "Nature",
                "cost": 0
            },
            {
                "name": "Brindavan Gardens",
                "category": "Nature",
                "cost": 50
            }
        ],

        "hotels": [
            {
                "name": "Budget Guest House",
                "type": "Budget",
                "price": 900
            },
            {
                "name": "City Comfort Hotel",
                "type": "Standard",
                "price": 1800
            },
            {
                "name": "Royal Stay Hotel",
                "type": "Premium",
                "price": 3500
            }
        ]
    },

    "Goa": {
        "description": "Enjoy beaches, coastal views, markets and Portuguese heritage.",
        "travel_cost": 2500,
        "food_per_person": 700,
        "local_transport_per_day": 700,
        "attractions": [
            {
                "name": "Baga Beach",
                "category": "Beach",
                "cost": 0
            },
            {
                "name": "Calangute Beach",
                "category": "Beach",
                "cost": 0
            },
            {
                "name": "Fort Aguada",
                "category": "History",
                "cost": 0
            },
            {
                "name": "Basilica of Bom Jesus",
                "category": "Culture",
                "cost": 0
            },
            {
                "name": "Dudhsagar Falls",
                "category": "Nature",
                "cost": 500
            },
            {
                "name": "Anjuna Flea Market",
                "category": "Shopping",
                "cost": 0
            }
        ],

        "hotels": [
            {
                "name": "Beachside Budget Stay",
                "type": "Budget",
                "price": 1200
            },
            {
                "name": "Coastal Comfort Hotel",
                "type": "Standard",
                "price": 2500
            },
            {
                "name": "Luxury Beach Resort",
                "type": "Premium",
                "price": 6000
            }
        ]
    },

    "Bengaluru": {
        "description": "Discover gardens, museums, technology attractions and city life.",
        "travel_cost": 500,
        "food_per_person": 600,
        "local_transport_per_day": 500,
        "attractions": [
            {
                "name": "Lalbagh Botanical Garden",
                "category": "Nature",
                "cost": 50
            },
            {
                "name": "Cubbon Park",
                "category": "Nature",
                "cost": 0
            },
            {
                "name": "Bengaluru Palace",
                "category": "History",
                "cost": 300
            },
            {
                "name": "Visvesvaraya Industrial Museum",
                "category": "Museum",
                "cost": 100
            },
            {
                "name": "ISKCON Temple",
                "category": "Culture",
                "cost": 0
            },
            {
                "name": "Vidhana Soudha Viewpoint",
                "category": "History",
                "cost": 0
            }
        ],

        "hotels": [
            {
                "name": "City Budget Lodge",
                "type": "Budget",
                "price": 1000
            },
            {
                "name": "Business Comfort Hotel",
                "type": "Standard",
                "price": 2200
            },
            {
                "name": "Premium City Hotel",
                "type": "Premium",
                "price": 5000
            }
        ]
    },

    "Hyderabad": {
        "description": "Experience historic monuments, museums and famous local cuisine.",
        "travel_cost": 1800,
        "food_per_person": 650,
        "local_transport_per_day": 600,
        "attractions": [
            {
                "name": "Charminar",
                "category": "History",
                "cost": 30
            },
            {
                "name": "Golconda Fort",
                "category": "History",
                "cost": 50
            },
            {
                "name": "Salar Jung Museum",
                "category": "Museum",
                "cost": 50
            },
            {
                "name": "Hussain Sagar Lake",
                "category": "Nature",
                "cost": 0
            },
            {
                "name": "Chowmahalla Palace",
                "category": "History",
                "cost": 150
            },
            {
                "name": "Birla Mandir",
                "category": "Culture",
                "cost": 0
            }
        ],

        "hotels": [
            {
                "name": "Budget City Inn",
                "type": "Budget",
                "price": 1100
            },
            {
                "name": "Comfort Residency",
                "type": "Standard",
                "price": 2300
            },
            {
                "name": "Luxury City Suites",
                "type": "Premium",
                "price": 5000
            }
        ]
    },

    "Chennai": {
        "description": "Explore beaches, temples, museums and South Indian culture.",
        "travel_cost": 1800,
        "food_per_person": 600,
        "local_transport_per_day": 550,
        "attractions": [
            {
                "name": "Marina Beach",
                "category": "Beach",
                "cost": 0
            },
            {
                "name": "Kapaleeshwarar Temple",
                "category": "Culture",
                "cost": 0
            },
            {
                "name": "Fort St. George",
                "category": "History",
                "cost": 100
            },
            {
                "name": "Government Museum",
                "category": "Museum",
                "cost": 75
            },
            {
                "name": "Santhome Cathedral Basilica",
                "category": "Culture",
                "cost": 0
            },
            {
                "name": "Elliot's Beach",
                "category": "Beach",
                "cost": 0
            }
        ],

        "hotels": [
            {
                "name": "Budget Chennai Stay",
                "type": "Budget",
                "price": 1000
            },
            {
                "name": "City Comfort Residency",
                "type": "Standard",
                "price": 2200
            },
            {
                "name": "Premium Marina Hotel",
                "type": "Premium",
                "price": 4500
            }
        ]
    },

    "Mangaluru": {
        "description": "Visit coastal beaches, temples, churches and scenic viewpoints.",
        "travel_cost": 1200,
        "food_per_person": 550,
        "local_transport_per_day": 500,
        "attractions": [
            {
                "name": "Panambur Beach",
                "category": "Beach",
                "cost": 0
            },
            {
                "name": "Tannirbhavi Beach",
                "category": "Beach",
                "cost": 0
            },
            {
                "name": "St. Aloysius Chapel",
                "category": "Culture",
                "cost": 0
            },
            {
                "name": "Kadri Manjunath Temple",
                "category": "Culture",
                "cost": 0
            },
            {
                "name": "Pilikula Nisargadhama",
                "category": "Nature",
                "cost": 100
            },
            {
                "name": "Sultan Battery",
                "category": "History",
                "cost": 0
            }
        ],

        "hotels": [
            {
                "name": "Coastal Budget Lodge",
                "type": "Budget",
                "price": 900
            },
            {
                "name": "Seaside Comfort Hotel",
                "type": "Standard",
                "price": 2000
            },
            {
                "name": "Premium Coastal Resort",
                "type": "Premium",
                "price": 4200
            }
        ]
    },

    "Pondicherry": {
        "description": "Enjoy French-style streets, beaches, cafes and peaceful attractions.",
        "travel_cost": 2000,
        "food_per_person": 650,
        "local_transport_per_day": 550,
        "attractions": [
            {
                "name": "Promenade Beach",
                "category": "Beach",
                "cost": 0
            },
            {
                "name": "White Town",
                "category": "Culture",
                "cost": 0
            },
            {
                "name": "Auroville Visitor Centre",
                "category": "Culture",
                "cost": 150
            },
            {
                "name": "Sri Aurobindo Ashram",
                "category": "Culture",
                "cost": 0
            },
            {
                "name": "Paradise Beach",
                "category": "Beach",
                "cost": 200
            },
            {
                "name": "Pondicherry Museum",
                "category": "Museum",
                "cost": 50
            }
        ],

        "hotels": [
            {
                "name": "French Quarter Budget Stay",
                "type": "Budget",
                "price": 1200
            },
            {
                "name": "White Town Comfort Hotel",
                "type": "Standard",
                "price": 2600
            },
            {
                "name": "Premium Heritage Resort",
                "type": "Premium",
                "price": 5500
            }
        ]
    }
}


def get_destinations():
    """Return the available destination names."""
    return list(DESTINATIONS.keys())


def get_hotel(destination, budget):
    """Choose a sample hotel based on the available budget per night."""

    hotels = DESTINATIONS[destination]["hotels"]

    affordable_hotels = [
        hotel for hotel in hotels
        if hotel["price"] <= budget
    ]

    if affordable_hotels:
        return affordable_hotels[-1]

    return hotels[0]


def select_attractions(destination, preference, days):
    """Select attractions based on the user's interests."""

    attractions = DESTINATIONS[destination]["attractions"]

    if preference == "All":
        selected = attractions[:]
    else:
        selected = [
            attraction
            for attraction in attractions
            if attraction["category"] == preference
        ]

        # Include other attractions if the preferred category
        # does not have enough options.
        if len(selected) < days * 2:
            for attraction in attractions:
                if attraction not in selected:
                    selected.append(attraction)

    # Select approximately two attractions per day.
    maximum = min(len(selected), days * 2)

    return selected[:maximum]


def create_itinerary(attractions, days):
    """Create a simple day-by-day itinerary."""

    itinerary = []

    for day in range(1, days + 1):
        first_index = (day - 1) * 2

        daily_attractions = attractions[
            first_index:first_index + 2
        ]

        if not daily_attractions:
            daily_attractions = [
                {
                    "name": "Explore the city at your own pace",
                    "category": "Leisure",
                    "cost": 0
                }
            ]

        itinerary.append({
            "day": day,
            "morning": daily_attractions[0]["name"],
            "afternoon": (
                daily_attractions[1]["name"]
                if len(daily_attractions) > 1
                else "Free time and local exploration"
            )
        })

    return itinerary


def calculate_costs(
    destination,
    days,
    people,
    hotel,
    attractions
):
    """Calculate estimated trip expenses."""

    destination_info = DESTINATIONS[destination]

    travel = destination_info["travel_cost"] * people

    accommodation = hotel["price"] * days

    food = (
        destination_info["food_per_person"]
        * people
        * days
    )

    local_transport = (
        destination_info["local_transport_per_day"]
        * days
    )

    sightseeing = sum(
        attraction["cost"]
        for attraction in attractions
    )

    total = (
        travel
        + accommodation
        + food
        + local_transport
        + sightseeing
    )

    return {
        "travel": travel,
        "accommodation": accommodation,
        "food": food,
        "local_transport": local_transport,
        "sightseeing": sightseeing,
        "total": total
    }


def save_trip_memory(trip):
    """Save generated trip information in a local JSON file."""

    try:
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "r", encoding="utf-8") as file:
                memories = json.load(file)
        else:
            memories = []

        memories.append({
            "destination": trip["destination"],
            "days": trip["days"],
            "people": trip["people"],
            "budget": trip["budget"],
            "created_at": datetime.now().isoformat(
                timespec="seconds"
            )
        })

        # Keep only the latest 50 plans.
        memories = memories[-50:]

        with open(MEMORY_FILE, "w", encoding="utf-8") as file:
            json.dump(memories, file, indent=4)

    except (OSError, json.JSONDecodeError):
        # The website can still work if memory storage fails.
        pass


def generate_trip(
    source,
    destination,
    days,
    people,
    budget,
    preference
):
    """Generate a trip plan with estimated expenses."""

    destination_info = DESTINATIONS[destination]

    # Estimate accommodation budget per night.
    hotel_budget_per_night = budget / days

    hotel = get_hotel(
        destination,
        hotel_budget_per_night
    )

    attractions = select_attractions(
        destination,
        preference,
        days
    )

    costs = calculate_costs(
        destination,
        days,
        people,
        hotel,
        attractions
    )

    adjusted = False

    # If the estimate exceeds the total budget,
    # switch to the cheapest sample hotel.
    if costs["total"] > budget:
        cheapest_hotel = min(
            destination_info["hotels"],
            key=lambda item: item["price"]
        )

        cheaper_costs = calculate_costs(
            destination,
            days,
            people,
            cheapest_hotel,
            attractions
        )

        if cheaper_costs["total"] < costs["total"]:
            hotel = cheapest_hotel
            costs = cheaper_costs
            adjusted = True

    # If the plan still exceeds the budget,
    # remove paid sightseeing options where possible.
    if costs["total"] > budget:
        free_attractions = [
            attraction
            for attraction in attractions
            if attraction["cost"] == 0
        ]

        if free_attractions:
            attractions = free_attractions

            costs = calculate_costs(
                destination,
                days,
                people,
                hotel,
                attractions
            )

            adjusted = True

    itinerary = create_itinerary(
        attractions,
        days
    )

    trip = {
        "source": source,
        "destination": destination,
        "description": destination_info["description"],
        "days": days,
        "people": people,
        "budget": budget,
        "hotel": hotel,
        "attractions": attractions,
        "itinerary": itinerary,
        "costs": costs,
        "adjusted": adjusted,
        "within_budget": costs["total"] <= budget
    }

    save_trip_memory(trip)

    return trip