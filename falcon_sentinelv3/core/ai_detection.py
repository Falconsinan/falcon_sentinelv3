from sklearn.ensemble import IsolationForest
import numpy as np

def detect_anomalies(ip_counter):

    values = np.array(list(ip_counter.values())).reshape(-1,1)

    model = IsolationForest(contamination=0.1)

    model.fit(values)

    result = model.predict(values)

    attackers = []

    for i, r in enumerate(result):

        if r == -1:
            attackers.append(list(ip_counter.keys())[i])

    return attackers