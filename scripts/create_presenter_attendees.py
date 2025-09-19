import os
import uuid
import requests
PLONE_URL = "https://2025.ploneconf.org/++api++"
AUTH_HEADER = os.environ.get("AUTHORIZATION")

if not AUTH_HEADER:
    raise RuntimeError("Please set AUTHORIZATION environment variable")

HEADERS = {
    "Accept": "application/json",
    "Authorization": AUTH_HEADER,
    "Content-Type": "application/json"
}


def get_all_items_by_type(content_type):
    """Fetch all content items of a given type using @search with fullobjects=1"""
    items = []
    start = 0
    batch_size = 100

    while True:
        params = {
            "portal_type": content_type,
            "fullobjects": 1,
            "b_size": batch_size,
            "b_start": start,
        }
        resp = requests.get(f"{PLONE_URL}/@search", headers=HEADERS, params=params)
        resp.raise_for_status()
        data = resp.json()
        batch = data.get("items", [])
        if not batch:
            break

        items.extend(batch)
        start += len(batch)
        if len(batch) < batch_size:
            break

    return items


def normalize_people(items):
    """Extract (email, first_name, last_name, @id, id) from search items"""
    people = []
    for it in items:
        email = it.get("email")
        title = it.get("title", "")
        if email:
            parts = title.strip().split()
            first_name = parts[0] if parts else ""
            last_name = " ".join(parts[1:]) if len(parts) > 1 else ""
            people.append({
                "email": email.lower(),
                "first_name": first_name,
                "last_name": last_name,
                "url": it.get("@id"),
                "id": it.get("id"),
            })
    return people


def create_attendee(container_url, first_name, last_name, email):
    """POST a new Attendee object with a UUID4 as id and return its id"""
    new_id = str(uuid.uuid4())
    payload = {
        "@type": "Attendee",
        "id": new_id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }
    resp = requests.post(container_url, headers=HEADERS, json=payload)
    resp.raise_for_status()
    data = resp.json()
    return data.get("id", new_id)


def grant_editor_role_on_presenter(presenter_url, attendee_id):
    """POST to @sharing endpoint to give Attendee Editor role"""
    presenter_url = presenter_url.replace(PLONE_URL.rsplit("/", 1)[0], PLONE_URL)
    payload = {
        "entries": [
            {
                "id": attendee_id,
                "roles": {
                    "Contributor": False,
                    "Editor": True,
                    "Reader": False,
                    "Reviewer": False
                },
                "type": "user"
            }
        ],
        "inherit": True
    }
    resp = requests.post(f"{presenter_url}/@sharing", headers=HEADERS, json=payload)
    resp.raise_for_status()


def main():
    print("Fetching all Presenters...")
    presenters = normalize_people(get_all_items_by_type("Presenter"))
    print(f"Found {len(presenters)} Presenters")

    print("Fetching all Attendees...")
    attendees = normalize_people(get_all_items_by_type("Attendee"))
    print(f"Found {len(attendees)} Attendees")

    attendee_emails = {a["email"] for a in attendees}

    missing = [p for p in presenters if p["email"] not in attendee_emails]

    print(f"\nFound {len(missing)} missing attendees to create...")

    for m in missing:
        print(f"Creating attendee: {m['first_name']} {m['last_name']} <{m['email']}>")
        attendee_id = create_attendee(
            f"{PLONE_URL}/attendees",
            m["first_name"],
            m["last_name"],
            m["email"]
        )

        print(f"Granting Editor to {attendee_id} on {m['url']}")
        grant_editor_role_on_presenter(m["url"], attendee_id)

    print("\nAll missing attendees created and given Editor on their Presenter page.")


if __name__ == "__main__":
    main()
