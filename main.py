import json
import os


# ============================================================
# SMARTTRIP
# MINI AUTONOMOUS TRAVEL AGENT
# ============================================================

MEMORY_FILE = "memory.json"


# ============================================================
# TRAVEL DATABASE
# ============================================================

DESTINATIONS = {

    "Mysuru": {

        "description": "Heritage city, palaces, temples, zoo and museums",

        "places": [

            {
                "name": "Mysuru Palace",
                "type": "Heritage",
                "cost": 100
            },

            {
                "name": "Mysuru Zoo",
                "type": "Wildlife",
                "cost": 120
            },

            {
                "name": "St. Philomena's Church",
                "type": "Church",
                "cost": 0
            },

            {
                "name": "Payana Vintage Car Museum",
                "type": "Museum",
                "cost": 75
            },

            {
                "name": "Chamundi Hills",
                "type": "Temple / Viewpoint",
                "cost": 0
            },

            {
                "name": "Karanji Lake",
                "type": "Nature",
                "cost": 60
            },

            {
                "name": "Mysuru Railway Museum",
                "type": "Museum",
                "cost": 50
            },

            {
                "name": "Jaganmohan Palace",
                "type": "Museum / Art",
                "cost": 100
            },

            {
                "name": "Mysuru Sand Sculpture Museum",
                "type": "Museum",
                "cost": 80
            },

            {
                "name": "Devaraja Market",
                "type": "Shopping",
                "cost": 0
            },

            {
                "name": "Kukkarahalli Lake",
                "type": "Nature",
                "cost": 0
            },

            {
                "name": "Lalitha Mahal Palace",
                "type": "Heritage",
                "cost": 0
            },

            {
                "name": "Ranganathittu Bird Sanctuary",
                "type": "Wildlife",
                "cost": 100
            },

            {
                "name": "Brindavan Gardens",
                "type": "Garden",
                "cost": 50
            }
        ],

        "hotels": [

            {
                "name": "Budget Lodge - Railway Station Area",
                "price": 1000
            },

            {
                "name": "Budget Hotel - Bus Stand Area",
                "price": 1200
            },

            {
                "name": "Aishwarya Residency",
                "price": 1300
            },

            {
                "name": "Hotel Roopa",
                "price": 1600
            },

            {
                "name": "Ashray Residency",
                "price": 1400
            },

            {
                "name": "Hotel Garden City",
                "price": 1500
            }
        ]
    },


    "Goa": {

        "description": "Beaches, forts, churches and nightlife",

        "places": [

            {
                "name": "Baga Beach",
                "type": "Beach",
                "cost": 0
            },

            {
                "name": "Calangute Beach",
                "type": "Beach",
                "cost": 0
            },

            {
                "name": "Fort Aguada",
                "type": "Heritage",
                "cost": 50
            },

            {
                "name": "Basilica of Bom Jesus",
                "type": "Church",
                "cost": 0
            },

            {
                "name": "Dudhsagar Falls",
                "type": "Nature",
                "cost": 500
            },

            {
                "name": "Panaji",
                "type": "City",
                "cost": 0
            },

            {
                "name": "Anjuna Beach",
                "type": "Beach",
                "cost": 0
            },

            {
                "name": "Vagator Beach",
                "type": "Beach",
                "cost": 0
            }
        ],

        "hotels": [

            {
                "name": "Budget Beach Guest House",
                "price": 1200
            },

            {
                "name": "Goa Budget Stay",
                "price": 1500
            },

            {
                "name": "Calangute Budget Hotel",
                "price": 1800
            },

            {
                "name": "Panaji Budget Hotel",
                "price": 1700
            }
        ]
    },


    "Bengaluru": {

        "description": "Technology city, parks, palaces and museums",

        "places": [

            {
                "name": "Lalbagh Botanical Garden",
                "type": "Nature",
                "cost": 30
            },

            {
                "name": "Cubbon Park",
                "type": "Nature",
                "cost": 0
            },

            {
                "name": "Bangalore Palace",
                "type": "Heritage",
                "cost": 300
            },

            {
                "name": "Vidhana Soudha",
                "type": "Heritage",
                "cost": 0
            },

            {
                "name": "ISKCON Temple",
                "type": "Temple",
                "cost": 0
            },

            {
                "name": "Bannerghatta Biological Park",
                "type": "Wildlife",
                "cost": 100
            },

            {
                "name": "Visvesvaraya Museum",
                "type": "Science Museum",
                "cost": 100
            },

            {
                "name": "Ulsoor Lake",
                "type": "Nature",
                "cost": 0
            }
        ],

        "hotels": [

            {
                "name": "Bengaluru Budget Lodge",
                "price": 1000
            },

            {
                "name": "City Budget Hotel",
                "price": 1400
            },

            {
                "name": "Central Bengaluru Hotel",
                "price": 1800
            }
        ]
    },


    "Hyderabad": {

        "description": "Historic monuments, food and culture",

        "places": [

            {
                "name": "Charminar",
                "type": "Heritage",
                "cost": 50
            },

            {
                "name": "Golconda Fort",
                "type": "Heritage",
                "cost": 50
            },

            {
                "name": "Hussain Sagar Lake",
                "type": "Nature",
                "cost": 0
            },

            {
                "name": "Salar Jung Museum",
                "type": "Museum",
                "cost": 50
            },

            {
                "name": "Birla Mandir",
                "type": "Temple",
                "cost": 0
            },

            {
                "name": "Nehru Zoological Park",
                "type": "Wildlife",
                "cost": 100
            }
        ],

        "hotels": [

            {
                "name": "Hyderabad Budget Stay",
                "price": 1200
            },

            {
                "name": "Charminar Budget Hotel",
                "price": 1300
            },

            {
                "name": "City Budget Hotel",
                "price": 1500
            }
        ]
    },


    "Chennai": {

        "description": "Beaches, temples, museums and culture",

        "places": [

            {
                "name": "Marina Beach",
                "type": "Beach",
                "cost": 0
            },

            {
                "name": "Fort St. George",
                "type": "Heritage",
                "cost": 50
            },

            {
                "name": "Kapaleeshwarar Temple",
                "type": "Temple",
                "cost": 0
            },

            {
                "name": "Government Museum",
                "type": "Museum",
                "cost": 50
            },

            {
                "name": "Santhome Basilica",
                "type": "Church",
                "cost": 0
            },

            {
                "name": "Guindy National Park",
                "type": "Nature",
                "cost": 30
            }
        ],

        "hotels": [

            {
                "name": "Chennai Budget Lodge",
                "price": 1000
            },

            {
                "name": "Marina Budget Hotel",
                "price": 1400
            },

            {
                "name": "City Budget Hotel",
                "price": 1600
            }
        ]
    },


    "Mangaluru": {

        "description": "Beaches, temples, churches and coastal food",

        "places": [

            {
                "name": "Panambur Beach",
                "type": "Beach",
                "cost": 0
            },

            {
                "name": "Tannirbhavi Beach",
                "type": "Beach",
                "cost": 0
            },

            {
                "name": "St. Aloysius Chapel",
                "type": "Church",
                "cost": 20
            },

            {
                "name": "Kadri Manjunath Temple",
                "type": "Temple",
                "cost": 0
            },

            {
                "name": "Sultan Battery",
                "type": "Heritage",
                "cost": 20
            },

            {
                "name": "Pilikula Biological Park",
                "type": "Wildlife",
                "cost": 100
            }
        ],

        "hotels": [

            {
                "name": "Mangaluru Budget Lodge",
                "price": 1000
            },

            {
                "name": "City Budget Hotel",
                "price": 1300
            },

            {
                "name": "Beach Area Budget Stay",
                "price": 1600
            }
        ]
    },


    "Pondicherry": {

        "description": "French architecture, beaches and peaceful streets",

        "places": [

            {
                "name": "Promenade Beach",
                "type": "Beach",
                "cost": 0
            },

            {
                "name": "Sri Aurobindo Ashram",
                "type": "Spiritual",
                "cost": 0
            },

            {
                "name": "Basilica of the Sacred Heart",
                "type": "Church",
                "cost": 0
            },

            {
                "name": "Paradise Beach",
                "type": "Beach",
                "cost": 200
            },

            {
                "name": "French Quarter",
                "type": "Heritage",
                "cost": 0
            },

            {
                "name": "Auroville",
                "type": "Tourism",
                "cost": 0
            }
        ],

        "hotels": [

            {
                "name": "Pondicherry Budget Lodge",
                "price": 1000
            },

            {
                "name": "White Town Budget Hotel",
                "price": 1600
            },

            {
                "name": "Beach Budget Stay",
                "price": 1400
            }
        ]
    }
}


# ============================================================
# TRANSPORT DATABASE
# ============================================================

TRANSPORT = {

    "Bengaluru-Mysuru": 600,
    "Bengaluru-Goa": 1800,
    "Bengaluru-Hyderabad": 1600,
    "Bengaluru-Chennai": 1200,
    "Bengaluru-Mangaluru": 1000,
    "Bengaluru-Pondicherry": 1100
}


# ============================================================
# MEMORY
# ============================================================

def load_memory():

    if os.path.exists(MEMORY_FILE):

        with open(MEMORY_FILE, "r") as file:
            return json.load(file)

    return {
        "previous_destinations": [],
        "preferences": [],
        "travel_style": "budget"
    }


def save_memory(memory):

    with open(MEMORY_FILE, "w") as file:

        json.dump(
            memory,
            file,
            indent=4
        )


# ============================================================
# SHOW DESTINATIONS
# ============================================================

def show_destinations():

    print("\n")
    print("=" * 70)
    print("AVAILABLE DESTINATIONS")
    print("=" * 70)

    number = 1

    for destination, data in DESTINATIONS.items():

        print(
            f"\n{number}. {destination}"
        )

        print(
            f"   {data['description']}"
        )

        print(
            f"   Tourist places available: "
            f"{len(data['places'])}"
        )

        number += 1


# ============================================================
# SHOW ALL PLACES
# ============================================================

def show_places(destination):

    data = DESTINATIONS[destination]

    print("\n")
    print("=" * 70)
    print(f"PLACES AVAILABLE IN {destination.upper()}")
    print("=" * 70)

    for i, place in enumerate(data["places"], 1):

        print(
            f"{i}. {place['name']}"
        )

        print(
            f"   Type: {place['type']}"
        )

        print(
            f"   Approx. entry cost: ₹{place['cost']}"
        )


# ============================================================
# SHOW HOTELS
# ============================================================

def show_hotels(destination):

    data = DESTINATIONS[destination]

    print("\n")
    print("=" * 70)
    print(f"HOTEL OPTIONS IN {destination.upper()}")
    print("=" * 70)

    for i, hotel in enumerate(data["hotels"], 1):

        print(
            f"{i}. {hotel['name']}"
        )

        print(
            f"   Approx. price: ₹{hotel['price']} / night"
        )

        print(
            "   Type: Budget-friendly accommodation"
        )


# ============================================================
# TRANSPORT TOOL
# ============================================================

def transport_tool(source, destination):

    key = f"{source}-{destination}"

    if key in TRANSPORT:

        return TRANSPORT[key]

    # Reverse route

    reverse_key = f"{destination}-{source}"

    if reverse_key in TRANSPORT:

        return TRANSPORT[reverse_key]

    # Default estimate

    return 1500


# ============================================================
# HOTEL TOOL
# ============================================================

def hotel_tool(destination):

    hotels = DESTINATIONS[destination]["hotels"]

    # Cheapest hotel

    cheapest = min(
        hotels,
        key=lambda x: x["price"]
    )

    return cheapest


# ============================================================
# PLACE SELECTION TOOL
# ============================================================

def place_tool(destination, days, preference):

    places = DESTINATIONS[destination]["places"]

    selected = []

    preference = preference.lower()

    # First select places matching preference

    for place in places:

        if preference in place["type"].lower():

            selected.append(place)

    # Fill remaining places

    for place in places:

        if place not in selected:

            selected.append(place)

        if len(selected) >= days * 2:

            break

    return selected


# ============================================================
# COST CALCULATION
# ============================================================

def calculate_cost(
    transport_cost,
    hotel_cost,
    places,
    days,
    people
):

    transport_total = transport_cost * people

    hotel_total = hotel_cost * (days - 1)

    entry_total = sum(
        place["cost"]
        for place in places
    ) * people

    food_cost = 400 * days * people

    local_transport = 150 * days * people

    total = (
        transport_total
        + hotel_total
        + entry_total
        + food_cost
        + local_transport
    )

    return int(total)


# ============================================================
# CREATE ITINERARY
# ============================================================

def create_itinerary(
    destination,
    places,
    days
):

    itinerary = []

    place_index = 0

    for day in range(1, days + 1):

        if day == 1:

            activities = []

            for _ in range(2):

                if place_index < len(places):

                    activities.append(
                        places[place_index]["name"]
                    )

                    place_index += 1

            itinerary.append(
                f"Day {day}: "
                + " → ".join(activities)
            )

        elif day == days:

            activities = []

            for _ in range(2):

                if place_index < len(places):

                    activities.append(
                        places[place_index]["name"]
                    )

                    place_index += 1

            itinerary.append(
                f"Day {day}: "
                + " → ".join(activities)
                + " → Return"
            )

        else:

            activities = []

            for _ in range(2):

                if place_index < len(places):

                    activities.append(
                        places[place_index]["name"]
                    )

                    place_index += 1

            itinerary.append(
                f"Day {day}: "
                + " → ".join(activities)
            )

    return itinerary


# ============================================================
# DISPLAY PLAN
# ============================================================

def display_plan(
    destination,
    hotel,
    transport,
    places,
    itinerary,
    total,
    budget
):

    print("\n")
    print("=" * 70)
    print("                 SMARTTRIP FINAL PLAN")
    print("=" * 70)

    print(
        f"\nDestination : {destination}"
    )

    print(
        f"Transport   : Approx. ₹{transport} per person"
    )

    print(
        f"Hotel       : {hotel['name']}"
    )

    print(
        f"Hotel cost  : Approx. ₹{hotel['price']} per night"
    )

    print("\nPLACES TO VISIT")
    print("-" * 70)

    for place in places:

        print(
            f"• {place['name']} "
            f"({place['type']}) - ₹{place['cost']}"
        )

    print("\nDAY-WISE ITINERARY")
    print("-" * 70)

    for day in itinerary:

        print(
            f"• {day}"
        )

    print("\nESTIMATED TRIP COST")
    print("-" * 70)

    print(
        f"Estimated cost : ₹{total}"
    )

    print(
        f"Your budget    : ₹{budget}"
    )

    if total <= budget:

        print(
            "\n✓ The trip is within your budget."
        )

    else:

        print(
            f"\n✗ Budget exceeded by ₹{total - budget}"
        )


# ============================================================
# RE-PLANNING
# ============================================================

def replan(
    destination,
    hotel,
    transport,
    places,
    days,
    people,
    budget
):

    print("\n")
    print("=" * 70)
    print("                 RE-PLANNING")
    print("=" * 70)

    print(
        "\nAgent detected that the trip is over budget."
    )

    print(
        "Searching for cheaper alternatives..."
    )

    # Choose fewer paid attractions

    free_places = [
        place for place in places
        if place["cost"] == 0
    ]

    paid_places = [
        place for place in places
        if place["cost"] > 0
    ]

    # Keep free places first

    new_places = free_places

    # Add only one low-cost attraction

    if paid_places:

        cheapest = min(
            paid_places,
            key=lambda x: x["cost"]
        )

        new_places.append(
            cheapest
        )

    # Use cheapest hotel

    cheapest_hotel = hotel

    hotels = DESTINATIONS[destination]["hotels"]

    cheapest_hotel = min(
        hotels,
        key=lambda x: x["price"]
    )

    # Recalculate

    new_total = calculate_cost(
        transport,
        cheapest_hotel["price"],
        new_places,
        days,
        people
    )

    print(
        "\n✓ Re-planning completed."
    )

    print(
        f"New hotel: {cheapest_hotel['name']}"
    )

    print(
        f"New estimated cost: ₹{new_total}"
    )

    return (
        cheapest_hotel,
        new_places,
        new_total
    )


# ============================================================
# HUMAN APPROVAL
# ============================================================

def human_approval():

    print("\n")
    print("=" * 70)
    print("                 HUMAN APPROVAL")
    print("=" * 70)

    print(
        "\nThe agent has completed the travel plan."
    )

    while True:

        choice = input(
            "\nDo you approve this plan? "
            "(yes/no): "
        ).lower()

        if choice == "yes":

            print(
                "\n✓ Human approval received."
            )

            print(
                "✓ Travel plan approved."
            )

            return True

        elif choice == "no":

            print(
                "\n✗ User rejected the plan."
            )

            return False

        else:

            print(
                "Please enter yes or no."
            )


# ============================================================
# MAIN AGENT
# ============================================================

def run_agent():

    print("\n")
    print("=" * 70)
    print("          SMARTTRIP - MINI AUTONOMOUS TRAVEL AGENT")
    print("=" * 70)

    # --------------------------------------------------------
    # SHOW ALL OPTIONS FIRST
    # --------------------------------------------------------

    show_destinations()

    print("\n")
    print("=" * 70)
    print("IMPORTANT: AVAILABLE INFORMATION")
    print("=" * 70)

    print(
        "\nThe agent has destination, tourist place, "
        "hotel and approximate cost information."
    )

    # --------------------------------------------------------
    # USER INPUT
    # --------------------------------------------------------

    source = input(
        "\nStarting city: "
    ).strip()

    destination = input(
        "Destination: "
    ).strip()

    # Check destination

    if destination not in DESTINATIONS:

        print(
            "\nSorry, destination is not available."
        )

        print(
            "Please select one of the destinations shown above."
        )

        return

    days = int(
        input(
            "Number of days: "
        )
    )

    people = int(
        input(
            "Number of people: "
        )
    )

    budget = int(
        input(
            "Total budget (₹): "
        )
    )

    preference = input(
        "What do you prefer? "
        "(heritage/beach/nature/church/museum/wildlife): "
    ).strip()

    # --------------------------------------------------------
    # GOAL
    # --------------------------------------------------------

    print("\n")
    print("=" * 70)
    print("1. GOAL")
    print("=" * 70)

    print(
        f"\nPlan a {days}-day trip from {source} "
        f"to {destination} for {people} people "
        f"within ₹{budget}."
    )

    # --------------------------------------------------------
    # MEMORY
    # --------------------------------------------------------

    print("\n")
    print("=" * 70)
    print("2. MEMORY")
    print("=" * 70)

    memory = load_memory()

    if destination not in memory["previous_destinations"]:

        memory["previous_destinations"].append(
            destination
        )

    if preference not in memory["preferences"]:

        memory["preferences"].append(
            preference
        )

    save_memory(memory)

    print(
        "\nPrevious destinations:",
        memory["previous_destinations"]
    )

    print(
        "Previous preferences:",
        memory["preferences"]
    )

    print(
        "\n✓ User preference saved."
    )

    # --------------------------------------------------------
    # SHOW DESTINATION INFORMATION
    # --------------------------------------------------------

    show_places(destination)

    show_hotels(destination)

    # --------------------------------------------------------
    # PLANNING
    # --------------------------------------------------------

    print("\n")
    print("=" * 70)
    print("3. PLANNING")
    print("=" * 70)

    print(
        "\nAgent is creating a budget-friendly itinerary..."
    )

    # --------------------------------------------------------
    # TRANSPORT
    # --------------------------------------------------------

    print("\n[TOOL] Checking transport...")

    transport = transport_tool(
        source,
        destination
    )

    print(
        f"Approximate transport cost: ₹{transport} "
        f"per person"
    )

    # --------------------------------------------------------
    # HOTEL
    # --------------------------------------------------------

    print("\n[TOOL] Finding cheapest suitable hotel...")

    hotel = hotel_tool(
        destination
    )

    print(
        f"Selected hotel: {hotel['name']}"
    )

    print(
        f"Approximate price: ₹{hotel['price']} per night"
    )

    # --------------------------------------------------------
    # PLACES
    # --------------------------------------------------------

    print("\n[TOOL] Selecting tourist places...")

    places = place_tool(
        destination,
        days,
        preference
    )

    print(
        f"✓ Selected {len(places)} places."
    )

    # --------------------------------------------------------
    # COST
    # --------------------------------------------------------

    total = calculate_cost(
        transport,
        hotel["price"],
        places,
        days,
        people
    )

    # --------------------------------------------------------
    # OBSERVATION
    # --------------------------------------------------------

    print("\n")
    print("=" * 70)
    print("4. OBSERVATION")
    print("=" * 70)

    print(
        f"\nEstimated cost: ₹{total}"
    )

    print(
        f"Budget: ₹{budget}"
    )

    # --------------------------------------------------------
    # REASONING + RE-PLANNING
    # --------------------------------------------------------

    if total > budget:

        print(
            "\n✗ Trip is above the user's budget."
        )

        print(
            "\n5. REASONING"
        )

        print(
            "The agent decided to reduce "
            "paid attractions and accommodation cost."
        )

        (
            hotel,
            places,
            total
        ) = replan(
            destination,
            hotel,
            transport,
            places,
            days,
            people,
            budget
        )

    else:

        print(
            "\n✓ Trip is already within budget."
        )

    # --------------------------------------------------------
    # ITINERARY
    # --------------------------------------------------------

    itinerary = create_itinerary(
        destination,
        places,
        days
    )

    # --------------------------------------------------------
    # FINAL PLAN
    # --------------------------------------------------------

    display_plan(
        destination,
        hotel,
        transport,
        places,
        itinerary,
        total,
        budget
    )

    # --------------------------------------------------------
    # HUMAN APPROVAL
    # --------------------------------------------------------

    approved = human_approval()

    if approved:

        print("\n")
        print("=" * 70)
        print("                 ACTION COMPLETED")
        print("=" * 70)

        print(
            "\n✓ SmartTrip Agent successfully completed the task."
        )

        print(
            "✓ Plan generated."
        )

        print(
            "✓ Budget checked."
        )

        print(
            "✓ User approval received."
        )

    else:

        print(
            "\nAgent stopped because human approval was not given."
        )


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":

    run_agent()