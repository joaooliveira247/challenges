## Promps

### Index.html
```plaintext
Create a semantic HTML5 structure for CO2 emissions calculator;

HEADER:
- Title with leaf emoji: "🌿 Calculadora de Emissão de CO₂"
- subtitle explaining the purpose

MAIN FORM(id="calculator-form"):
- Origin Input (id="manual-distance") labeled "Inserir distância manualmente"
- Destination input (id="destination") sharing the same datalist
- Distance input (id="distance", type="number", readonly) that will be auto-filled
- Transport mode selector with 4 radio buttons in a visual grid:
  - bicycle, car(checked/default), bus, truck
  - Each wrapped in label with emoji icon and text in portuguese
  - Use name="transport" and values: bicycle, car, bus, truck
- Submit button with text "Calcular Emissão"

RESULT SECTIONS (all hidden by default with class="hidden")
- Section id="results" with emprty div id="resykts-content"
- Section id="comparison" with empty div id="comparison-content"
- Section id="carbon-credits" with empty div="carbon-credits-content"

FOOTER
- Credits text: "Developed with Gemini."
```