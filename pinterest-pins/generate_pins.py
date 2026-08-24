#!/usr/bin/env python3
"""Generate Pinterest pin images (1000x1500 PNG) from SVG templates.
Requires: pip install cairosvg
"""
import textwrap
from html import escape
from pathlib import Path

import cairosvg

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)

BRAND = "#0e7c6b"
BRAND_SOFT = "#e6f4f1"
INK = "#1c2733"
INK_SOFT = "#4a5a6a"
WHITE = "#fdfdfb"

PINS = [
    # (filename, headline, subtext, article_slug)
    ("lang-apps-01", "5 AI Language Apps\nCompared (2026)", "Babbel vs Duolingo vs Busuu vs Pimsleur — honest pros & cons before you subscribe.", "best-ai-language-learning-apps-2026"),
    ("lang-apps-02", "Best App to Learn\nSpanish or French\nwith AI", "We tested the AI conversation features — here's what's real vs marketing hype.", "best-ai-language-learning-apps-2026"),
    ("lang-apps-03", "Duolingo Max vs\nBabbel: AI Features\nCompared", "Video Call AI vs Babbel Speak — which one actually helps you speak?", "best-ai-language-learning-apps-2026"),

    ("babbel-review-01", "Babbel Review:\nIs It Worth It\nin 2026?", "Real pricing, hidden auto-renewal traps, and who should skip it.", "babbel-review-2026"),
    ("babbel-review-02", "Babbel Pricing\nExplained\n(Don't Pay Full Price)", "The Lifetime deal discount trick nobody tells you about.", "babbel-review-2026"),
    ("babbel-review-03", "Babbel Languages\nRanked: Which\nCourses Are Good?", "Spanish and French are deep. Turkish and Norwegian? Not so much.", "babbel-review-2026"),

    ("vs-duolingo-01", "Babbel vs Duolingo:\nWhich Teaches\nYou More?", "One builds habits. One builds fluency. Here's how to pick.", "babbel-vs-duolingo"),
    ("vs-duolingo-02", "Free vs Paid\nLanguage App:\nDuolingo or Babbel?", "Should you pay for Babbel or stick with Duolingo's free tier?", "babbel-vs-duolingo"),
    ("vs-duolingo-03", "AI Conversation\nPractice Compared", "Babbel Speak vs Duolingo Max — we tested both AI conversation partners.", "babbel-vs-duolingo"),

    ("coursera-01", "Is Coursera Plus\nWorth $399/Year?", "The 30-second math that decides if you should subscribe.", "coursera-plus-review"),
    ("coursera-02", "Coursera Plus:\nWhat's Actually\nIncluded in 2026", "Google certificates? Yes. Stanford courses? Often no.", "coursera-plus-review"),
    ("coursera-03", "Coursera Plus vs\nBuying Courses\nIndividually", "Break-even calculator: when the subscription actually pays off.", "coursera-plus-review"),

    ("tts-01", "5 Best AI\nText-to-Speech Apps\nfor Studying", "Speechify vs ElevenLabs vs free options — honest comparison.", "best-text-to-speech-apps-for-studying"),
    ("tts-02", "Free Text-to-Speech\nApp for Students\n(No Subscription)", "Try this before paying for Speechify.", "best-text-to-speech-apps-for-studying"),
    ("tts-03", "Best App for\nADHD & Dyslexia\nReading Support", "Text-to-speech tools that actually help you focus and retain.", "best-text-to-speech-apps-for-studying"),

    ("surfer-01", "Surfer SEO Review:\nWorth It for\nBloggers?", "The vendor's own data on whether Content Score actually predicts rankings.", "surfer-seo-review"),
    ("surfer-02", "Surfer SEO Pricing\n& Alternatives\n(2026)", "Is there a cheaper option? We compared it to NeuronWriter.", "surfer-seo-review"),
    ("surfer-03", "SEO Content Score:\nDoes It Really\nWork?", "We looked at Surfer's own correlation study — here's what it says.", "surfer-seo-review"),

    ("aws-cert-01", "Best Online Courses\nfor AWS\nCertification 2026", "Pluralsight vs AWS Skill Builder vs Udemy — the cheapest real path compared.", "best-aws-certification-courses-2026"),
    ("aws-cert-02", "AWS Certification:\nThe Real Cost\n(Not the Marketing Price)", "Course + exam + retake buffer — what you'll actually pay.", "best-aws-certification-courses-2026"),
    ("aws-cert-03", "Cheapest Way to Get\nAWS Solutions\nArchitect Certified", "The $12 Udemy course thousands of people actually pass with.", "best-aws-certification-courses-2026"),

    ("vs-pluralsight-01", "Coursera vs\nPluralsight for\nTech Careers", "Credentials or hands-on labs? Match the platform to what you're proving.", "coursera-vs-pluralsight"),
    ("vs-pluralsight-02", "Which Skill\nPlatform Actually\nGets You Hired?", "We compared certificate recognition vs real skill-building.", "coursera-vs-pluralsight"),
    ("vs-pluralsight-03", "Coursera vs\nPluralsight: Which\nfor Cloud Certs?", "Hands-on labs vs university-style courses for AWS/Azure/GCP prep.", "coursera-vs-pluralsight"),

    ("coursera-price-01", "Coursera Pricing\n2026: Every Plan\nExplained", "Plus, Specializations, certificates — what each actually costs.", "coursera-pricing-2026"),
    ("coursera-price-02", "Did Coursera Prices\nGo Up in 2026?\n(The Real Answer)", "Most articles get this wrong. Here's what actually changed.", "coursera-pricing-2026"),
    ("coursera-price-03", "Coursera Financial\nAid: How It\nActually Works", "The application process explained honestly, no fake approval stats.", "coursera-pricing-2026"),

    ("coursera-certs-01", "Best Coursera\nCertificates for\nCareer Changers", "Google vs IBM vs Meta vs Microsoft — honest completion times.", "coursera-career-certificates-2026"),
    ("coursera-certs-02", "Do Coursera\nCertificates Actually\nGet You Hired?", "Coursera says 75%. Independent research found something different.", "coursera-career-certificates-2026"),
    ("coursera-certs-03", "Google Certificate\nReview: Real Timeline\n& Cost", "3-6 months advertised. Here's what it actually takes.", "coursera-career-certificates-2026"),

    ("coursera-edx-01", "Coursera vs edX:\nWhich Is Cheaper\nfor You?", "One bills monthly until you finish. The other you buy once.", "coursera-vs-edx"),
    ("coursera-edx-02", "edX Isn't the\nHarvard Non-Profit\nAnymore", "Sold to 2U in 2021, restructured in 2024 — what actually changed.", "coursera-vs-edx"),
    ("coursera-edx-03", "Take Coursera &\nedX Courses Free\n(Audit Explained)", "Both platforms let you audit. Neither will tell you about it.", "coursera-vs-edx"),
]


def wrap_svg_text(text, x, y, font_size, fill, weight="700", line_height=1.15, anchor="start"):
    lines = text.split("\n")
    tspans = "".join(
        f'<tspan x="{x}" dy="{0 if i == 0 else font_size * line_height}">{escape(line)}</tspan>'
        for i, line in enumerate(lines)
    )
    return (
        f'<text x="{x}" y="{y}" font-family="Georgia, serif" font-size="{font_size}" '
        f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{tspans}</text>'
    )


def wrap_plain(text, width_chars):
    return "\n".join(textwrap.wrap(text, width_chars))


def make_svg(headline, subtext):
    headline_svg = wrap_svg_text(headline, 70, 260, 76, WHITE, weight="700", line_height=1.08)
    subtext_wrapped = wrap_plain(subtext, 34)
    subtext_svg = wrap_svg_text(subtext_wrapped, 70, 1180, 34, INK, weight="400", line_height=1.4)

    return f"""<svg width="1000" height="1500" viewBox="0 0 1000 1500" xmlns="http://www.w3.org/2000/svg">
  <rect width="1000" height="1500" fill="{WHITE}"/>
  <rect width="1000" height="820" fill="{BRAND}"/>
  <rect x="0" y="780" width="1000" height="8" fill="{INK}"/>
  <text x="70" y="120" font-family="-apple-system, sans-serif" font-size="30" font-weight="700"
        fill="{WHITE}" letter-spacing="1">LEARNSTACK</text>
  {headline_svg}
  <rect x="70" y="900" width="120" height="6" fill="{BRAND}"/>
  {subtext_svg}
  <text x="70" y="1420" font-family="-apple-system, sans-serif" font-size="28" font-weight="700"
        fill="{BRAND}">yameyaku.com &#8594;</text>
</svg>"""


def main():
    for filename, headline, subtext, slug in PINS:
        svg = make_svg(headline, subtext)
        svg_path = OUT / f"{filename}.svg"
        svg_path.write_text(svg, encoding="utf-8")
        png_path = OUT / f"{filename}.png"
        cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), output_width=1000, output_height=1500)
        print(f"{filename}.png -> links to /{slug}/")
    print(f"\nGenerated {len(PINS)} pins in {OUT}")


if __name__ == "__main__":
    main()
