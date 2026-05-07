from playwright.sync_api import sync_playwright
import json
import re

def scrape_program(page, url):
    page.goto(url)
    page.wait_for_load_state("networkidle")
    page.click("a[href='#coursestextcontainer']")
    page.wait_for_timeout(2000)

    container = page.query_selector("#coursestextcontainer")
    if not container:
        return []

    courses = []
    rows = container.query_selector_all("tr")

    for row in rows:
        code_el = row.query_selector("td.codecol")
        credits_el = row.query_selector("td.hourscol")
        cells = row.query_selector_all("td")

        if not code_el or not credits_el or len(cells) < 3:
            continue

        code = code_el.inner_text().strip()
        title = cells[1].inner_text().strip()
        credits_text = credits_el.inner_text().strip()

        # Skip rows that aren't real courses (e.g. "or" rows, headers)
        if not re.match(r'^[A-Z]{2,4}\s\d{3}', code):
            continue

        # Remove footnote numbers from title
        title = re.sub(r'\.\s*\d+$', '.', title).strip().rstrip('.')

        credits_match = re.search(r'\d+', credits_text)
        if not credits_match:
            continue

        courses.append({
            "code": code,
            "name": title,
            "credits": int(credits_match.group())
        })

    return courses

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    programs = {
        "cs_major": {
            "url": "https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/computer-science/computer-science-major-bsc/",
            "name": "Computer Science Major (B.Sc.)",
            "totalRequired": 63
        },
        "cs_honours": {
            "url": "https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/computer-science/computer-science-honours-bsc/",
            "name": "Computer Science Honours (B.Sc.)",
            "totalRequired": 75
        },
        "biology_major": {
            "url": "https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/biology/biology-major-bsc/",
            "name": "Biology Major (B.Sc.)",
            "totalRequired": 59
        },
        "chemistry_major": {
            "url": "https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/chemistry/chemistry-major-bsc/",
            "name": "Chemistry Major (B.Sc.)",
            "totalRequired": 59
        },
        "psychology_major": {
            "url": "https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/psychology/psychology-major-bsc/",
            "name": "Psychology Major (B.Sc.)",
            "totalRequired": 54
        }
    }

    result = {}
    for key, info in programs.items():
        print(f"Scraping {info['name']}...")
        courses = scrape_program(page, info["url"])
        print(f"  Found {len(courses)} courses")
        for c in courses:
            print(f"  {c}")
        result[key] = {
            "name": info["name"],
            "totalRequired": info["totalRequired"],
            "courses": courses
        }

    browser.close()

    with open("data/programs.json", "w") as f:
        json.dump(result, f, indent=2)

    print("\nSaved to data/programs.json")