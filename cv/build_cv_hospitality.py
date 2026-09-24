# -*- coding: utf-8 -*-
"""Build James Dillon's hospitality CV as a DOCX (part-time weekend work).

Usage:  python cv/build_cv_hospitality.py
Deps:   pip install python-docx qrcode pillow

Same layout as the software CV (see cv_style.py) but aimed at part-time
hospitality roles: customer-facing work first, technical detail cut right back.
Key Skills are deliberately transferable — each one should be evidenced by more
than a single job. This CV is for job applications and is NOT published on the
site.

    soffice --headless --outdir cv --convert-to pdf "cv/James Dillon CV - Hospitality.docx"
"""
from cv_style import HERE, PORTFOLIO_URL, CvBuilder, build_qr

OUT_PATH = HERE / "James Dillon CV - Hospitality.docx"

build_qr()
cv = CvBuilder()
# Tighter than the software CV so this fits on a single page
cv.sp_heading_before = 7
cv.sp_heading_after = 3.5
cv.sp_role_before = 4.5
cv.sp_bullet_after = 1.7
cv.sp_skill_after = 1.5

# =====================================================================
cv.header(
    name="James Dillon",
    tagline="Available weekends and after school  ·  Part-time",
    contact_line=[
        ("Letchworth, Hertfordshire", None),
        ("07821 867254", None),
        ("jamesdillon_@outlook.com", "mailto:jamesdillon_@outlook.com"),
    ],
    link_line=[
        ("linkedin.com/in/jamesdillondev", "https://www.linkedin.com/in/jamesdillondev/"),
    ],
    qr_caption=["Scan to find out", "more about me"],
)

# =====================================================================
cv.heading("Profile", first=True)
cv.paragraph(
    "Sixth form student looking for part-time hospitality work, available weekends and after school. I "
    "work in my school canteen, taking orders on the till and keeping the servery stocked and clean. "
    "Since 2022 I have also volunteered on the BBQ and bar at Balstock and the Baldock Beer Festival, "
    "serving 100+ people at a time. As an Air Cadets Sergeant I am used to turning up on time, taking "
    "responsibility and staying calm when it gets busy.",
    before=1, line=1.04)

# =====================================================================
cv.heading("Key Skills")
cv.skill_line("Customer service", "Serving the public at a school canteen and at busy community events "
                                  "— orders, cash and queues")
cv.skill_line("Tills & payments", "Entering orders accurately on a point-of-sale system and handling cash "
                                  "under time pressure")
cv.skill_line("Under pressure", "Staying calm and organised through a lunch rush, a busy event bar or a "
                                "parade night")
cv.skill_line("Teamwork", "Canteen shifts, event stalls run with small volunteer teams, and camps run "
                          "alongside other leaders")
cv.skill_line("Leadership", "Air Cadets Sergeant and Scouts Young Leader — planning and running "
                            "sessions for groups of 10–20")
cv.skill_line("Health & safety", "Keeping food areas clean and safe · Instructor First Aid (St John "
                                 "Ambulance) · fire warden trained")

# =====================================================================
cv.heading("Work Experience")

cv.role("Knights Templar School Canteen", "Canteen Assistant", "Sept 2026 – present")
cv.bullet("Take orders on the point-of-sale (POS) system through a busy lunch service, keeping the queue "
          "moving.")
cv.bullet("Restock food and drink during downtime so the servery does not run short partway through "
          "service.")
cv.bullet("Clear, clean and tidy throughout and after service, keeping the serving and seating areas neat "
          "and presentable.")

cv.role("Balstock & Baldock Beer Festival", "Event Volunteer (BBQ & Bar)", "2022 – present")
cv.bullet("Serve food and drink to 100+ members of the public, handling cash and managing queues.")
cv.bullet("Set up and pack down stalls and event equipment with a small team, adapting when things change "
          "on the day.")

cv.role("Janus Technology", "Junior Software Engineer (part-time)", "July 2025 – present")
cv.bullet("Part-time role alongside sixth form, working to a brief and meeting deadlines. Completed "
          "workplace fire warden training.")

# =====================================================================
cv.heading("Leadership & Volunteering")

cv.role("RAF Air Cadets, 248 Squadron", "Sergeant", "2022 – present")
cv.bullet("Promoted through four ranks to Sergeant, responsible for junior cadets on weekly parade nights "
          "and at public events such as Remembrance Sunday.")
cv.bullet("Methods of Instruction qualified — plan and deliver lessons to groups of 10–20.")

cv.role("Scouts and Explorers", "Young Leader", "2014 – present")
cv.bullet("Help run weekly meetings at my old Scout group, planning activities and supporting the "
          "leaders.")
cv.bullet("Help organise weekend camps — sorting equipment, giving safety briefings and running "
          "outdoor activities such as cooking and pioneering.")

cv.role("Duke of Edinburgh’s Award", "Bronze completed, Silver in progress", "2022 – present")
cv.bullet("Expeditions in North Yorkshire and the Peak District involving route planning, navigation and "
          "working as a small team over several days.")
cv.bullet("Volunteered in the local community and trained regularly to improve my running over several "
          "months.")

# =====================================================================
cv.heading("Education")

cv.role("Knights Templar School Sixth Form", "Baldock, Hertfordshire", "Sept 2024 – present")
cv.bullet([("A-Levels (predicted): ", True),
           ("Product Design A*, Computer Science A, Maths B", False)])
cv.bullet([("GCSEs: ", True),
           ("nine passes including Maths (7) and English (5), with grade 9 in Design and Technology and "
            "in Computer Science. BTEC Level 2 in Teamwork and Personal Development.", False)])

# =====================================================================
cv.heading("Qualifications & Interests")
cv.skill_line("Qualifications", "Instructor First Aid (St John Ambulance) · Methods of Instruction "
                                "· Silver Leadership · Fire Warden")
cv.skill_line("Interests", "Running (5K PB 20:35), camping and the outdoors, electronics and computing "
                           "projects")

cv.footer_note("References available on request. More about me: ", "jamesdillon.uk",
               PORTFOLIO_URL, before=3)

cv.save(OUT_PATH)
