import weasyprint
from weasyprint import HTML

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Personal Style Analysis</title>
    <style>
        @page {
            size: A4;
            margin: 25mm 20mm;
            background-color: #faf8f5;
        }
        *, *::before, *::after {
            box-sizing: border-box;
        }
        body {
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            color: #2c2c2c;
            margin: 0;
            padding: 0;
            line-height: 1.6;
        }
        .header {
            text-align: center;
            margin-bottom: 40px;
            padding-bottom: 20px;
            border-bottom: 2px solid #e0dcd3;
        }
        h1 {
            font-family: 'Georgia', serif;
            font-size: 26pt;
            color: #1a1a1a;
            margin: 0 0 10px 0;
            letter-spacing: 1.5px;
        }
        .subtitle {
            font-size: 14pt;
            font-style: italic;
            color: #666;
        }
        h2 {
            font-family: 'Georgia', serif;
            font-size: 16pt;
            color: #3b2f2f;
            border-left: 4px solid #b75d32;
            padding-left: 10px;
            margin-top: 30px;
            margin-bottom: 20px;
        }
        h3 {
            font-size: 12pt;
            color: #1b4332;
            margin-bottom: 10px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        p, li {
            font-size: 11pt;
            color: #444;
        }
        .section {
            margin-bottom: 35px;
        }
        .flex-container {
            display: table;
            width: 100%;
            border-collapse: separate;
            border-spacing: 15px 0;
            margin-left: -15px;
        }
        .col {
            display: table-cell;
            width: 50%;
            background-color: #ffffff;
            padding: 20px;
            border: 1px solid #e0dcd3;
            border-radius: 4px;
            vertical-align: top;
        }
        ul {
            margin-top: 0;
            padding-left: 20px;
            margin-bottom: 0;
        }
        li {
            margin-bottom: 8px;
        }
        .color-box {
            display: inline-block;
            width: 14px;
            height: 14px;
            margin-right: 8px;
            vertical-align: middle;
            border: 1px solid #d1d1d1;
            border-radius: 2px;
        }
        .highlight {
            font-weight: bold;
            color: #b75d32;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>PERSONAL STYLE ANALYSIS</h1>
        <div class="subtitle">Curated Profile for Lucky</div>
    </div>

    <div class="section">
        <h2>1. Color Profile Overview</h2>
        <p>Your defining characteristics align beautifully with the <span class="highlight">Deep Autumn</span> season. Your features are most complemented by rich, warm, earthy tones that mirror the natural, grounded colors of late autumn.</p>
        <ul>
            <li><strong>Undertone:</strong> Warm Neutral. You possess a balance of warm and cool tones, but lean slightly towards the warm spectrum, giving your complexion a natural richness.</li>
            <li><strong>Contrast Level:</strong> Medium Contrast. There is a balanced, harmonious transition between your skin, hair, and eye colors without extreme starkness.</li>
        </ul>
    </div>

    <div class="section">
        <h2>2. Palette Recommendations</h2>
        <div class="flex-container">
            <div class="col">
                <h3>Suits You Best</h3>
                <p style="font-size: 10pt; margin-bottom: 15px;">These shades enhance your natural warmth and harmonize with your medium contrast.</p>
                <ul style="list-style-type: none; padding-left: 0;">
                    <li><span class="color-box" style="background-color: #1b4332;"></span> Deep Teal & Forest Green</li>
                    <li><span class="color-box" style="background-color: #556b2f;"></span> Olive Green</li>
                    <li><span class="color-box" style="background-color: #c15b2c;"></span> Burnt Orange & Rust</li>
                    <li><span class="color-box" style="background-color: #d4af37;"></span> Mustard Yellow</li>
                    <li><span class="color-box" style="background-color: #1a2a40;"></span> Navy & Deep Blue</li>
                    <li><span class="color-box" style="background-color: #672626;"></span> Burgundy & Maroon</li>
                    <li><span class="color-box" style="background-color: #4a3020;"></span> Dark Chocolate Brown</li>
                </ul>
            </div>
            <div class="col">
                <h3>Colors to Limit</h3>
                <p style="font-size: 10pt; margin-bottom: 15px;">Pastels and highly cool-toned colors may wash out your warm neutral undertone.</p>
                <ul style="list-style-type: none; padding-left: 0;">
                    <li><span class="color-box" style="background-color: #ffb6c1;"></span> Light Pink & Lavender</li>
                    <li><span class="color-box" style="background-color: #add8e6;"></span> Bright & Baby Blue</li>
                    <li><span class="color-box" style="background-color: #98ff98;"></span> Mint Green</li>
                    <li><span class="color-box" style="background-color: #ffffe0;"></span> Pale Yellow</li>
                    <li><span class="color-box" style="background-color: #d3d3d3;"></span> Light Grey</li>
                    <li><span class="color-box" style="background-color: #ffffff;"></span> Stark White</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="section" style="page-break-inside: avoid;">
        <h2>3. Hairstyle Analysis</h2>
        <p>Your facial structure and natural hair texture are maximized by styles that offer volume on top while keeping the sides neatly tapered. Embracing your natural wave and texture yields the most flattering and effortless results.</p>
        
        <div class="flex-container" style="margin-bottom: 20px;">
            <div class="col">
                <h3>Top Recommendations</h3>
                <ul>
                    <li><strong>Textured Top:</strong> Adds excellent vertical dimension.</li>
                    <li><strong>Side & Middle Parts:</strong> Frames your face symmetrically.</li>
                    <li><strong>Quiff:</strong> Brings structured, intentional volume.</li>
                    <li><strong>Tapered Crop:</strong> Clean, modern, and low-maintenance.</li>
                    <li><strong>Messy Waves:</strong> Capitalizes perfectly on natural texture.</li>
                </ul>
            </div>
            <div class="col">
                <h3>Styles to Avoid</h3>
                <ul>
                    <li><strong>Long Fringe:</strong> Obscures your facial features.</li>
                    <li><strong>Curly Shag:</strong> Can lack the necessary sharp structure.</li>
                    <li><strong>Man Bun:</strong> Pulls volume away from the top.</li>
                    <li><strong>Slick Back (Flat):</strong> Diminishes volume and flattens natural texture.</li>
                </ul>
            </div>
        </div>
        
        <div style="background-color: #ffffff; padding: 15px; border-left: 4px solid #1b4332; border-radius: 4px;">
            <h3 style="margin-top: 0;">Core Styling Principles</h3>
            <ul style="margin-bottom: 0;">
                <li><strong>Volume on Top:</strong> Ensure hair height is concentrated at the top to perfectly balance facial proportions.</li>
                <li><strong>Tapered Sides:</strong> Keep the sides shorter to emphasize the volume and texture above.</li>
                <li><strong>Routine & Tools:</strong> Rely on light styling products. Use a blow dryer to assist in building volume, and schedule regular trims to maintain the sharp structure of tapered cuts.</li>
            </ul>
        </div>
    </div>
</body>
</html>
"""

# Generate the PDF file
HTML(string=html_content).write_pdf('Lucky_Personal_Style_Analysis.pdf')
