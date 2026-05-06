# McGill-Planner

# McGill Planner 🎓

A lightweight, browser-based degree planning tool for McGill University students. Track your required courses, monitor your credit progress, and estimate your GPA — all in one place, with no account or login required.

**Live site:** [cvil-it.github.io/McGill-Planner](https://cvil-it.github.io/McGill-Planner/)

---

## Features

- **Major selection** — Choose your program from a dropdown; the course list updates automatically to show your required courses.
- **Course checklist** — Check off courses as you complete them, with credit values displayed for each.
- **Credit progress tracker** — See how many credits you've completed out of your program's total requirement, with a live percentage.
- **GPA calculator** — Assign a grade to each completed course and get a running GPA estimate based on McGill's grading scale.
- **Auto-save** — Your progress is saved automatically to your browser's local storage — no account needed.
- **Multiple profiles** — Save and switch between different profiles (e.g., different semesters or what-if scenarios).

---

## Getting Started

No installation needed. Just visit the live site:

👉 **[cvil-it.github.io/McGill-Planner](https://cvil-it.github.io/McGill-Planner/)**

1. Select your major from the dropdown.
2. Check off courses you've completed.
3. Optionally assign a grade to each course to track your GPA.
4. Save your progress as a named profile to revisit later.

---

## Running Locally

If you want to run or modify the project locally:

```bash
git clone https://github.com/cvil-it/McGill-Planner.git
cd McGill-Planner
```

Then open `index.html` in your browser — no build step or server required.

---

## Adding or Editing Programs

Course data is defined directly in `index.html` inside the `programs` JavaScript object. Each program entry looks like this:

```js
"cs-major": {
  name: "Computer Science Major",
  totalRequired: 60,
  courses: [
    { code: "COMP 202", name: "Foundations of Programming", credits: 3 },
    { code: "COMP 250", name: "Introduction to Computer Science", credits: 3 },
    // ...
  ]
}
```

To add a new major, add a new key to the `programs` object and a corresponding `<option>` in the `#major-select` dropdown.

---

## Tech Stack

- **HTML / CSS / JavaScript** — no frameworks or dependencies
- **localStorage** — for client-side persistence
- **GitHub Pages** — for hosting

---

## Contributing

Pull requests are welcome! If you'd like to add support for a new McGill program or fix course data, feel free to open a PR.

1. Fork the repo
2. Create a branch (`git checkout -b add-program-name`)
3. Make your changes
4. Open a pull request

---

## Disclaimer

This tool is **not affiliated with McGill University**. Course requirements are maintained manually and may not reflect the latest academic calendar. Always verify your program requirements with the [McGill eCalendar](https://www.mcgill.ca/study/courses/ecalendar).

---

## License

MIT
