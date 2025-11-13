# Generates a 2x3 GitHub README HTML grid with hover effects
from html import escape

projects = [
    {
        "title": "Simulating the Universe using Diffusion",
        "image": "Figures/Condition Diffusion N-body to Hydro Arch (1).jpg",
        "description": "Master's Project: Using Generative AI for Cosmology",
        "stack": "Python · TensorFlow · Generative AI",
        "link": "https://github.com/ChamodKalupahana/simulating_the_universe_using_GANs",
        "color": "rgba(255,165,0,0.5)"
    },
    {
        "title": " GPT-2 Logit Lens",
        "image": "Figures/gpt_2_logit_lens/donald_trump.png",
        "description": "Exploratory, Probe-Based Study at GPT-2 Hidden States",
        "stack": "Python · PyTorch · Mechanistic Interpretability",
        "link": "https://chamodkalupahana.github.io/GPT-2-Tuned-Logit-Lens/",
        "color": "rgba(100,149,237,0.5)"
    },
    {
        "title": "Cham-GPT",
        "image": "Figures/cham_gpt/feeling_shitty.jpeg",
        "description": "LLM Chatbot for talking to a AI version of me",
        "stack": "Phython · TensorFlow · NLP",
        "link": "https://github.com/ChamodKalupahana/Cham-GPT",
        "color": "rgba(255,140,0,0.5)"
    },
    {
        "title": "Compare Astronomical Objects",
        "image": "Figures/compare_astro_objects/betelgeuse.png",
        "description": "Passion project for showing the scale of the universe",
        "stack": "Next.js · Typescript · Firebase",
        "link": "https://compare-astronomical-objects.web.app/",
        "color": "rgba(255,192,203,0.5)"
    },
    {
        "title": "AI Incidents Forecasting",
        "image": "Figures/ai_incidents_forecasting/total_incidents.jpg",
        "description": "Apart Research Hackathon",
        "stack": "Python · Poisson Regression · Monte Carlo Simulations",
        "link": "https://apartresearch.com/project/ai-incidents-forecasting-w92p",
        "color": "rgba(144,238,144,0.5)"
    },
    {
        "title": "The Class Plan",
        "image": "Figures/class_plan/phone.png",
        "description": "ICN: Muti-platform app for pilates instructors",
        "stack": "Swift · Kotlin · Java",
        "link": "https://www.theclassplan.com/",
        "color": "rgba(135,206,250,0.5)"
    }
]

def generate_html(projects, columns=3, img_width=260):
    """
    Returns a GitHub-README-safe HTML table (no JS, no inline CSS that gets stripped).
    - projects: list of dicts with keys: title, image, description, stack, link
    - columns: how many columns per row (default 3)
    - img_width: <img width="..."> attribute (allowed by GitHub)
    """
    rows = [projects[i:i+columns] for i in range(0, len(projects), columns)]
    parts = ['<div align="center">', '<table>']

    for row in rows:
        parts.append('  <tr>')
        for p in row:
            title = escape(p.get('title', 'Untitled'))
            image = escape(p.get('image', ''))
            desc  = escape(p.get('description', ''))
            stack = escape(p.get('stack', ''))
            link  = escape(p.get('link', ''))

            parts.append(f'    <td align="center" width="{100 // columns}%">')
            if link:
                parts.append(f'      <a href="{link}">')
            if image:
                parts.append(f'        <img src="{image}" width="{img_width}" alt="{title}"/><br/>')
            parts.append(f'        <b>{title}</b>')
            if link:
                parts.append('      </a>')
            parts.append('      <br/>')
            if desc:
                parts.append(f'      <sub>{desc}</sub><br/>')
            if stack:
                parts.append(f'      <sub><i>{stack}</i></sub>')
            parts.append('    </td>')

        # Pad remaining cells to keep the row width consistent
        if len(row) < columns:
            for _ in range(columns - len(row)):
                parts.append(f'    <td align="center" width="{100 // columns}%">&nbsp;</td>')

        parts.append('  </tr>')

    parts.extend(['</table>', '</div>'])
    return "\n".join(parts)

if __name__ == "__main__":
    html_output = generate_html(projects, columns=2, img_width=400)
    with open("portfolio_section.html", "w") as f:
        f.write(html_output)
    print("✅ HTML generated! Copy 'portfolio_section.html' into your README.md")