import numpy as np
import tpot
from sklearn.model_selection import StratifiedKFold

##### TODO: load the real data, below we probide an example #####
# Simulated data for CatFACS-based approach
catfacs_data_set = np.random.randint(0, 2, (100, 30))  # Non-temporal data
catfacs_data_seq = np.random.randint(0, 2, (100, 30))  # Temporal data
labels = np.random.randint(0, 2, 100)

# CatFACS-based approach
kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

tpot_classifier_set = tpot.TPOTClassifier(verbosity=2, generations=5, population_size=20)
tpot_classifier_seq = tpot.TPOTClassifier(verbosity=2, generations=5, population_size=20)

for train_idx, test_idx in kfold.split(catfacs_data_set, labels):
    tpot_classifier_set.fit(catfacs_data_set[train_idx], labels[train_idx])
    tpot_classifier_seq.fit(catfacs_data_seq[train_idx], labels[train_idx])

# Simulated data for Facial landmarks-based approach
landmarks_data_set = np.random.rand(100, 68, 2)  # Non-temporal data
landmarks_data_seq = np.random.rand(100, 68, 2)  # Temporal data
cat_ids = np.random.randint(1, 3, 100)

# Landmark-based features
def compute_geometric_features(landmarks):
    # Example feature: distance between two landmarks
    distances = np.sqrt(np.sum((landmarks[:, 0, :] - landmarks[:, 1, :]) ** 2, axis=1))
    return distances

# Compute features for all frames
geometric_features_set = compute_geometric_features(landmarks_data_set)
geometric_features_seq = compute_geometric_features(landmarks_data_seq)

# Simulate deficiency metrics
deficiency_ratios = {
    "no_face_detected": np.random.rand(100),
    "low_confidence": np.random.rand(100)
}

# Further classification with TPOT
tpot_classifier_landmarks_set = tpot.TPOTClassifier(verbosity=2, generations=5, population_size=20)
tpot_classifier_landmarks_seq = tpot.TPOTClassifier(verbosity=2, generations=5, population_size=20)

for train_idx, test_idx in kfold.split(geometric_features_set, labels):
    tpot_classifier_landmarks_set.fit(geometric_features_set[train_idx].reshape(-1, 1), labels[train_idx])
    tpot_classifier_landmarks_seq.fit(geometric_features_seq[train_idx].reshape(-1, 1), labels[train_idx])

# Quantitative measure of deficiency level
deficiency_level_no_face = np.mean(deficiency_ratios["no_face_detected"])
deficiency_level_low_confidence = np.mean(deficiency_ratios["low_confidence"])

print(f"Deficiency Level (No Face Detected): {deficiency_level_no_face}")
print(f"Deficiency Level (Low Confidence): {deficiency_level_low_confidence}")
