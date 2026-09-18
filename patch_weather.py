import sys

with open('server.js', 'r') as f:
    content = f.read()

old_report = """Responding directly to the analytical focus on **"${ctx.prompt}"**:
1. **Intra-Day Volatility & The Duck-Curve Phenomenon**:"""

new_report = """Responding directly to the analytical focus on **"${ctx.prompt}"**:

${ctx.prompt.toLowerCase().includes('weather') || ctx.prompt.toLowerCase().includes('mausam') ? `### ☁️ Meteorological Impact on Commercial Operations
The commercial analysis directly correlates with recent meteorological patterns (Weather Reports):
1. **Heatwave Spikes (Extreme Demand)**: Rising ambient temperatures directly amplify cooling loads (AC/HVAC). This surge rapidly depletes base generation margins, causing **evening peak tariffs to hit the ceiling limit of ₹${maxRs}/MWh**. 
2. **Monsoon/Hydro Influx**: During rainy weather and monsoon progression, increased run-of-river hydro generation provides abundant cheap energy, which depresses the base and daytime clearing prices toward the **₹${minRs}/MWh** threshold.
3. **Cloud Cover & Solar Intermittency**: Sudden cloudy weather during daytime (Blocks 25–68) reduces solar generation, forcing the grid to rapidly procure power from the Real-Time Market (RTM), significantly increasing volatility.
` : ''}
1. **Intra-Day Volatility & The Duck-Curve Phenomenon**:"""

content = content.replace(old_report, new_report)

with open('server.js', 'w') as f:
    f.write(content)
print("Patched weather report")
