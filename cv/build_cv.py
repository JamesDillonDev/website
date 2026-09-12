# -*- coding: utf-8 -*-
"""Build James Dillon's CV as a DOCX.

Usage:  python cv/build_cv.py
Deps:   pip install python-docx qrcode pillow

Writes "James Dillon CV.docx" next to this script, along with the portfolio QR
code it embeds. To publish an updated CV on the site, export the DOCX to PDF
and copy both into the site:

    soffice --headless --outdir cv --convert-to pdf "cv/James Dillon CV.docx"
    cp "cv/James Dillon CV.pdf" src/lib/assets/James_Dillon_CV.pdf
"""
from pathlib import Path

import qrcode
from qrcode.constants import ERROR_CORRECT_M

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.opc.constants import RELATIONSHIP_TYPE as RT

HERE = Path(__file__).resolve().parent
PORTFOLIO_URL = "https://jamesdillon.uk"
QR_PATH = HERE / "portfolio-qr.png"
OUT_PATH = HERE / "James Dillon CV.docx"


def build_qr():
    """Regenerate the portfolio QR. Box size is deliberately large so the code
    stays crisp when the DOCX is printed."""
    qr = qrcode.QRCode(error_correction=ERROR_CORRECT_M, box_size=24, border=2)
    qr.add_data(PORTFOLIO_URL)
    qr.make(fit=True)
    qr.make_image(fill_color="black", back_color="white").convert("RGB").save(QR_PATH)


build_qr()

NAVY = RGBColor(0x1B, 0x36, 0x5D)
GREY = RGBColor(0x55, 0x5B, 0x66)
DARK = RGBColor(0x1A, 0x1A, 0x1A)
FAINT = RGBColor(0xA0, 0xA8, 0xB4)
RULE = "9BA6B8"
FONT = "Calibri"

doc = Document()

# ---------- page setup ----------
sec = doc.sections[0]
sec.page_width, sec.page_height = Inches(8.27), Inches(11.69)   # A4
sec.left_margin = sec.right_margin = Inches(0.45)
sec.top_margin = Inches(0.4)
sec.bottom_margin = Inches(0.38)
CONTENT_W = sec.page_width - sec.left_margin - sec.right_margin

# ---------- base styles ----------
normal = doc.styles["Normal"]
normal.font.name = FONT
normal.font.size = Pt(10)
normal.font.color.rgb = DARK
normal._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
pf = normal.paragraph_format
pf.space_before = Pt(0)
pf.space_after = Pt(0)
pf.line_spacing = 1.0


def set_spacing(p, before=0, after=0, line=1.0):
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.line_spacing = line
    return p


def run(p, text, size=10, bold=False, italic=False, color=DARK):
    r = p.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(size)
    r.bold = bold
    r.italic = italic
    r.font.color.rgb = color
    return r


def hyperlink(p, text, url, size=10, bold=False, color="1B365D"):
    """Insert real external hyperlink. Without this Word autoformats bare
    domains like "jamesdillon.uk" into a relative path, which resolves to a
    local file:/// URL instead of the site."""
    r_id = p.part.relate_to(url, RT.HYPERLINK, is_external=True)
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), r_id)

    r = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    # child order below is fixed by the CT_RPr schema — do not reorder
    fonts = OxmlElement("w:rFonts")
    fonts.set(qn("w:ascii"), FONT)
    fonts.set(qn("w:hAnsi"), FONT)
    rPr.append(fonts)
    if bold:
        rPr.append(OxmlElement("w:b"))
    col = OxmlElement("w:color")
    col.set(qn("w:val"), color)
    rPr.append(col)
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), str(int(size * 2)))
    rPr.append(sz)
    r.append(rPr)

    t = OxmlElement("w:t")
    t.text = text
    t.set(qn("xml:space"), "preserve")
    r.append(t)

    link.append(r)
    p._p.append(link)
    return link


def bottom_border(p, color=RULE, size=6, space=2):
    pPr = p._p.get_or_add_pPr()
    bdr = OxmlElement("w:pBdr")
    b = OxmlElement("w:bottom")
    b.set(qn("w:val"), "single")
    b.set(qn("w:sz"), str(size))
    b.set(qn("w:space"), str(space))
    b.set(qn("w:color"), color)
    bdr.append(b)
    pPr.append(bdr)


def keep_with_next(p):
    pPr = p._p.get_or_add_pPr()
    e = OxmlElement("w:keepNext")
    pPr.append(e)
    return p


def heading(text, first=False):
    p = doc.add_paragraph()
    set_spacing(p, before=0 if first else 11, after=4.5)
    r = run(p, text.upper(), size=11, bold=True, color=NAVY)
    r.font.spacing = Pt(0.9)
    bottom_border(p)
    keep_with_next(p)
    return p


def role(title, meta, date, indent=0.0):
    """Entry title on the left, date right-aligned on the same line."""
    p = doc.add_paragraph()
    set_spacing(p, before=7, after=2.5)
    p.paragraph_format.tab_stops.add_tab_stop(CONTENT_W, WD_TAB_ALIGNMENT.RIGHT)
    run(p, title, size=10.5, bold=True, color=NAVY)
    if meta:
        run(p, "  |  ", size=10, color=FAINT)
        run(p, meta, size=10, color=DARK)
    p.add_run("\t")
    run(p, date, size=9, italic=True, color=GREY)
    keep_with_next(p)
    return p


def bullet(parts, indent=0.0):
    """parts: str, or list of (text, bold) tuples."""
    p = doc.add_paragraph()
    set_spacing(p, before=0, after=3.4, line=1.02)
    p.paragraph_format.left_indent = Inches(indent + 0.17)
    p.paragraph_format.first_line_indent = Inches(-0.17)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(indent + 0.17))
    r = p.add_run("•\t")
    r.font.name = FONT
    r.font.size = Pt(10)
    r.font.color.rgb = NAVY
    r.bold = True
    if isinstance(parts, str):
        parts = [(parts, False)]
    for text, bold in parts:
        run(p, text, size=10, bold=bold)
    return p


def skill_line(label, value, label_w=1.3):
    p = doc.add_paragraph()
    set_spacing(p, before=0, after=3.6, line=1.02)
    p.paragraph_format.left_indent = Inches(label_w)
    p.paragraph_format.first_line_indent = Inches(-label_w)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(label_w))
    run(p, label, size=10, bold=True, color=NAVY)
    p.add_run("\t")
    run(p, value, size=10)
    return p


def no_cell_margins(cell):
    tcPr = cell._tc.get_or_add_tcPr()
    mar = OxmlElement("w:tcMar")
    for side in ("left", "right", "top", "bottom"):
        e = OxmlElement("w:" + side)
        e.set(qn("w:w"), "0")
        e.set(qn("w:type"), "dxa")
        mar.append(e)
    tcPr.append(mar)


# =====================================================================
# HEADER  (name + contacts | QR code)
# =====================================================================
qr_w = Inches(1.12)
right_w = Inches(2.72)
name_w = CONTENT_W - right_w

head = doc.add_table(rows=1, cols=2)
head.alignment = WD_TABLE_ALIGNMENT.LEFT
head.autofit = False
head.columns[0].width = name_w
head.columns[1].width = right_w
left, right = head.rows[0].cells
left.width = name_w
right.width = right_w
no_cell_margins(left)
no_cell_margins(right)

p = left.paragraphs[0]
set_spacing(p, after=1)
r = run(p, "James Dillon", size=25, bold=True, color=NAVY)
r.font.spacing = Pt(0.5)

p = set_spacing(left.add_paragraph(), before=0, after=5)
run(p, "Software  ·  Electronics  ·  Product Design", size=10, color=GREY)

SEP = "   •   "
p = set_spacing(left.add_paragraph(), before=0, after=1.5)
run(p, "Letchworth, Hertfordshire", size=9)
run(p, SEP, size=9, color=FAINT)
run(p, "07821 867254", size=9)
run(p, SEP, size=9, color=FAINT)
hyperlink(p, "jamesdillon_@outlook.com", "mailto:jamesdillon_@outlook.com", size=9, color="1A1A1A")

p = set_spacing(left.add_paragraph(), before=0, after=0)
hyperlink(p, "linkedin.com/in/jamesdillondev",
          "https://www.linkedin.com/in/jamesdillondev/", size=9, color="1A1A1A")
run(p, SEP, size=9, color=FAINT)
hyperlink(p, "github.com/JamesDillonDev",
          "https://github.com/JamesDillonDev", size=9, color="1A1A1A")

# QR cell: portfolio URL + caption sit to the LEFT of the QR, which stays flush right
qr_txt_w = right_w - qr_w - Inches(0.1)
qr_inner = right.add_table(rows=1, cols=2)
qr_inner.autofit = False
qr_txt_cell, qr_img_cell = qr_inner.rows[0].cells
qr_inner.columns[0].width = qr_txt_w
qr_inner.columns[1].width = qr_w + Inches(0.1)
qr_txt_cell.width = qr_txt_w
qr_img_cell.width = qr_w + Inches(0.1)
no_cell_margins(qr_txt_cell)
no_cell_margins(qr_img_cell)

p = qr_txt_cell.paragraphs[0]
set_spacing(p, before=3, after=2.5, line=0.95)
p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
hyperlink(p, "jamesdillon.uk", PORTFOLIO_URL, size=13.5, bold=True)

for line in ("Scan to view my portfolio,", "coursework and projects"):
    p = set_spacing(qr_txt_cell.add_paragraph(), before=0, after=0, line=0.95)
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run(p, line, size=8, color=GREY)

p = qr_img_cell.paragraphs[0]
set_spacing(p, after=0)
p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
p.add_run().add_picture(str(QR_PATH), width=qr_w)

# drop the now-empty placeholder paragraph the outer cell started with
right.paragraphs[0]._p.getparent().remove(right.paragraphs[0]._p)

set_spacing(doc.add_paragraph(), before=0, after=3)

# =====================================================================
heading("Profile", first=True)
p = set_spacing(doc.add_paragraph(), before=1, after=0, line=1.05)
run(p,
    "Sixth form student studying Maths, Computer Science and Product Design, looking for a software or "
    "engineering apprenticeship. I have worked part-time as a junior software engineer at Janus Technology "
    "since July 2025, building features that went out to real customers, and spent a placement at MBDA "
    "working on a Raspberry Pi guided missile project. Outside of school I build things end to end, from a "
    "self-hosted website and home server to 3D-printed electronics projects. I am also a Sergeant in the Air "
    "Cadets, so I am used to teaching, organising and being responsible for other people.")

# =====================================================================
heading("Key Skills")
skill_line("Languages", "C#, Python, JavaScript")
skill_line("Web & software", "SvelteKit, HTML/CSS; building web apps and plugins to a brief")
skill_line("Infrastructure", "Docker, Linux, self-hosting, home networking, automated image builds and deploys")
skill_line("Version control", "Git, GitHub, self-hosted GitLab")
skill_line("AI tooling", "LLM-based automation, Model Context Protocol (MCP) servers, structured knowledge bases")
skill_line("Hardware", "Raspberry Pi, Zigbee, sensors and smart devices, wiring and low-voltage installation, "
                       "hardware integration, testing and fault-finding")
skill_line("Design", "Product and concept design, CAD, 3D printing, electronics, prototyping and iterating "
                     "from a brief (A-Level Product Design, GCSE DT grade 9)")

# =====================================================================
heading("Education")

role("Knights Templar School Sixth Form", "Baldock, Hertfordshire", "Sept 2024 – present")
bullet([("A-Levels (predicted): ", True),
        ("Product Design A*, Computer Science A, Maths B", False)])
bullet([("Extended Project Qualification — A* (50/52): ", True),
        ("designed and built an automatic pet feeder, covering the research, design, electronics and build. "
         "Full write-up on my portfolio.", False)])
bullet([("GCSEs: ", True),
        ("grade 9 in Design and Technology and Computer Science; 8 in Physics and Media; 7 in Maths and "
         "Chemistry; 6 in Biology; 5 in English. Cambridge National in Enterprise and Marketing — M2 "
         "(grade A equivalent). Graded coursework is on my portfolio.", False)])

# =====================================================================
heading("Work Experience")

role("Janus Technology", "Junior Software Engineer (part-time)", "July 2025 – present")
bullet([("Support ticket automation (osTicket) — ", True),
        ("built a plugin for the open-source osTicket helpdesk that reads an incoming ticket, works out the "
         "likely problem and drafts a step-by-step reply, so common queries get a useful first response "
         "without waiting for an agent.", False)])
bullet([("Stile app for AVProEdge — ", True),
        ("added the live video preview feature to a released app that controls multiview video walls. Every "
         "draggable source now shows a real-time preview, so users can tell inputs apart before assigning "
         "them to a display.", False)])
bullet([("AI knowledge base — ", True),
        ("set up a linked Obsidian vault holding API references, example projects and in-house library notes "
         "so AI tools can pull the right context instead of the team pasting docs into a chat window. Also "
         "tested several MCP servers and wrote a custom one to connect AI tools to our self-hosted GitLab.", False)])
bullet("Worked to a brief on each project, mostly on my own but within a team, and iterated on feedback. "
       "Completed workplace fire warden training.")

role("MBDA", "Engineering Work Experience", "2026")
_b = bullet([("Miniature guided missile — ", True),
             ("worked in a team to design and program a model guided missile running on a Raspberry Pi, "
              "helping with the code, integrating the hardware, testing the system and tracking down "
              "faults. Code on GitHub at ", False)])
hyperlink(_b, "JamesDillonDev/mini-missile",
          "https://github.com/JamesDillonDev/mini-missile", size=10, color="1A1A1A")
run(_b, ".", size=10)
bullet("Rotated through systems testing and validation, materials, hardware-in-the-loop, electronics, "
       "production and project management, which showed me how a large engineering programme is delivered "
       "from concept through to implementation.")

# =====================================================================
heading("Projects")

role("jamesdillon.uk — Portfolio Website", "SvelteKit, Docker, Raspberry Pi", "2025 – present")
bullet("Built the site in SvelteKit and self-host it from a custom Docker image. Pushing to Git builds a new "
       "image that my server pulls and swaps in automatically, so a deploy takes nothing more than a git push.")
bullet("Wrote a custom in-page PDF viewer component so my coursework can be read on the site instead of "
       "having to be downloaded first.")

role("Home Assistant Smart Home", "Docker, Zigbee, Raspberry Pi", "2025 – present")
bullet("Rebuilt the family smart home around Home Assistant in Docker. Started with Tapo smart plugs for "
       "lighting, then added Wake-on-LAN control for the TV and Sonos playback.")
bullet("Moved over to Zigbee using a Sonoff dongle and motion sensors for automations like hallway lights "
       "that come on at night and switch themselves off, including planning cable routes and running "
       "low-voltage cabling safely and neatly.")
bullet("Added a wall-mounted Raspberry Pi 4 touchscreen panel so the whole house can use the system without "
       "reaching for a phone. I diagnose and fix the hardware, network and integration problems myself.")

role("Jellyfin Media Server", "Self-hosted home lab", "2025 – present")
bullet("Run a Jellyfin server holding our media and the CDs I have ripped, so the family has one central "
       "library. Set up to be reliable and simple enough that everyone can use it without my help.")

# =====================================================================
heading("Leadership & Volunteering")

role("RAF Air Cadets, 248 Squadron", "Sergeant", "2022 – present")
bullet("Promoted through four ranks to Sergeant, responsible for the training and welfare of junior cadets "
       "on weekly parade nights.")
bullet("Methods of Instruction qualified, so I plan and deliver lessons to groups of 10–20 and assess "
       "cadets afterwards. Also hold the Silver Leadership award.")
bullet("Qualified First Aid Instructor (St John Ambulance), able to teach and assess first aid as well as "
       "respond to incidents.")
bullet("Represent the squadron at public events such as Remembrance Sunday, and competed in athletics at "
       "Wing and Regional level.")

role("Scouts and Explorers", "Young Leader", "2014 – present")
bullet("Help run weekly meetings at my old Scout group, planning activities, keeping sessions on track and "
       "supporting the leaders.")
bullet("Help organise weekend camps and residentials: sorting equipment, giving safety briefings and running "
       "outdoor activities.")
bullet("Volunteer on the BBQ and bar at Balstock and the Baldock Beer Festival, serving 100+ members of the "
       "public, handling cash and keeping a busy food station clean and safe.")

role("Duke of Edinburgh’s Award", "Bronze completed, Silver in progress", "2022 – present")
bullet("Expeditions in North Yorkshire and the Peak District involving route planning, navigation and "
       "teamwork, volunteering in the local community, and a cybersecurity club covering online safety and "
       "ethical hacking.")

# =====================================================================
heading("Qualifications, Awards & Interests")
skill_line("Qualifications", "Instructor First Aid, St John Ambulance · Methods of Instruction · "
                             "BTEC Level 2 in Teamwork and Personal Development (GCSE equivalent) · "
                             "Air Cadets Silver Leadership · Fire Warden (valid to 2027)")
skill_line("Awards", "EPQ A* (50/52) · Gold medal, Wing-level athletics · GCSE grade 9 in Design "
                     "and Technology and in Computer Science")
skill_line("Interests", "Running (5K PB 20:35), home lab and self-hosting, 3D printing and electronics projects")

p = set_spacing(doc.add_paragraph(), before=9, after=0)
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run(p, "Full write-ups, coursework and source code: ", size=8.5, color=GREY)
hyperlink(p, "jamesdillon.uk", PORTFOLIO_URL, size=8.5, bold=True)

doc.save(OUT_PATH)
print("saved", OUT_PATH)
