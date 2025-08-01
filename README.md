# Daleel.ai - Interactive Streamlit Prototype

This prototype demonstrates the core user journeys and value proposition of Daleel.ai, an intelligent hiring platform.

**Note:** This is a high-fidelity prototype. All data is mocked, and complex features like AI matching and LinkedIn scraping are simulated to showcase the intended functionality.

## Setup Instructions

1.  **Clone the repository.**
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Users:**
    *   Open `config.yaml`.
    *   Change the `key` under `cookies` to a new random string.
    *   To create your own users, run the included `generate_keys.py` script and copy the output into the `credentials` section of `config.yaml`.

4.  **(Optional) Configure OpenAI:**
    *   To enable the AI Job Description generator, you need an OpenAI API key.
    *   Create a file `.streamlit/secrets.toml` in the project root.
    *   Add your key to the file like this: `OPENAI_API_KEY="sk-..."`

## How to Run

Open your terminal in the project folder and run:

```bash
streamlit run 1_🏠_Home.py
```

## User Journeys to Test

### 1. Talent Journey
*   **Sign Up** as a new Talent user (e.g., using a `gmail.com` address).
*   **Login** with one of the pre-configured talent accounts (e.g., user: `nora_talent`, pass: `pass123`).
*   Navigate to the **Talent Dashboard**.
*   Go through the **"Build Your Twin"** tab:
    *   Upload a sample PDF resume.
    *   "Scrape" a LinkedIn profile (this is simulated).
    *   Rate past experiences.
*   Go to the **"Assessments"** tab to complete the simulated technical and cultural tests.

### 2. Employer Journey
*   **Sign Up** as an Employer. Notice the validation that requires a corporate email domain.
*   **Login** with the pre-configured employer account (e.g., user: `acme_admin`, pass: `pass123`).
*   Navigate to the **Employer Dashboard**.
*   In the **"Hire New Talent"** tab, create a new job request.
*   Click **"Find Top 5 Matches"** to run the simulated matching engine.
*   Review the curated list of candidates and see how their "Digital Twin" data is displayed.