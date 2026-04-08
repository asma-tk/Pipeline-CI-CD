import requests
import streamlit as st
import os

st.set_page_config(
	page_title="Iris Predictor",
	page_icon="🌸",
	layout="wide",
)

st.markdown(
	"""
	<style>
	  .hero {
		  padding: 1.2rem 1.4rem;
		  border-radius: 14px;
		  background: linear-gradient(90deg, #4f46e5 0%, #7c3aed 100%);
		  color: white;
		  margin-bottom: 1rem;
	  }
	  .result-card {
		  border-radius: 14px;
		  padding: 1rem 1.2rem;
		  background: #f1f5f9;
		  border: 1px solid #e2e8f0;
	  }
	</style>
	""",
	unsafe_allow_html=True,
)

st.markdown(
	"""
	<div class="hero">
	  <h2 style="margin:0;">🌸 Prédiction de plante Iris</h2>
	  <p style="margin:0.4rem 0 0 0;">Entre les mesures de la fleur et obtiens la classe + le nom d'espèce.</p>
	</div>
	""",
	unsafe_allow_html=True,
)

with st.sidebar:
	st.header("⚙️ Configuration")
	default_api_url = os.getenv("BACKEND_API_URL", "http://127.0.0.1:8000/predict")
	api_url = st.text_input("URL API backend", value=default_api_url)
	st.caption("Assure-toi que FastAPI tourne sur le port 8000.")

left_col, right_col = st.columns([1.2, 1])

with left_col:
	st.subheader("Mesures de la fleur")
	sepal_length = st.slider("SepalLengthCm", 4.0, 8.5, 5.8, 0.1)
	sepal_width = st.slider("SepalWidthCm", 2.0, 4.5, 3.0, 0.1)
	petal_length = st.slider("PetalLengthCm", 1.0, 7.0, 4.3, 0.1)
	petal_width = st.slider("PetalWidthCm", 0.1, 2.8, 1.3, 0.1)

	payload = {
		"sepal_length": sepal_length,
		"sepal_width": sepal_width,
		"petal_length": petal_length,
		"petal_width": petal_width,
	}

	if st.button("🔮 Prédire l'espèce", use_container_width=True):
		try:
			response = requests.post(api_url, json=payload, timeout=10)
			response.raise_for_status()
			result = response.json()

			species_name = str(result.get("species_name", "unknown")).capitalize()
			prediction_id = result.get("prediction", "?")

			with right_col:
				st.subheader("Résultat")
				st.markdown(
					f"""
					<div class="result-card">
					  <h3 style="margin:0;">✅ Espèce prédite : {species_name}</h3>
					  <p style="margin:0.5rem 0 0 0;">ID de classe : <strong>{prediction_id}</strong></p>
					</div>
					""",
					unsafe_allow_html=True,
				)
				st.info(
					"0 = Setosa | 1 = Versicolor | 2 = Virginica"
				)
		except requests.exceptions.RequestException as error:
			st.error(f"Impossible d'appeler l'API: {error}")
		except ValueError:
			st.error("Réponse JSON invalide reçue depuis l'API.")

with right_col:
	st.subheader("Aide")
	st.write("L'API attend les champs suivants :")
	st.code(
		"""{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}""",
		language="json",
	)