from pathlib import Path

import joblib
import mlflow
from mlflow.exceptions import MlflowException
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split

#prepare the data
data = load_iris()
X = data.data
y = data.target 

#split the data
x_train, x_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

#tran the model
model = RandomForestClassifier()
model.fit(x_train, y_train)

#make predictions
y_pred = model.predict(x_test)

#evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")

mlflow.sklearn.autolog(log_models=False)
tracking_uri = "http://localhost:5000"
mlflow.set_tracking_uri(tracking_uri)

model_output_path = Path(__file__).resolve().parent.parent / "model" / "model.pkl"
model_output_path.parent.mkdir(parents=True, exist_ok=True)
joblib.dump(model, model_output_path)
print(f"Model saved at: {model_output_path}")

try:
    mlflow.set_experiment("Iris_Classification")
    with mlflow.start_run(run_name="RandomForest-iris"):
        f1 = f1_score(y_test, y_pred, average="weighted")

        mlflow.log_metric("test_accuracy", accuracy)
        mlflow.log_metric("test_f1", f1)
        mlflow.log_metrics({"error": 1 - accuracy})
        mlflow.log_artifact(str(model_output_path), artifact_path="model-pkl")
    print("MLflow: logs envoyés avec succès")
except MlflowException as error:
    print(f"MLflow indisponible ({tracking_uri}) : {error}")
except Exception as error:
    print(f"MLflow ignoré suite à une erreur inattendue : {error}")
