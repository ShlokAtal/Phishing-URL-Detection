const urlInput = document.getElementById("urlInput");
const scanButton = document.getElementById("scanButton");

const resultSection = document.getElementById("resultSection");

const riskScore = document.getElementById("riskScore");
const riskLevel = document.getElementById("riskLevel");
const riskMeter = document.getElementById("riskMeter");

const prediction = document.getElementById("prediction");
const predictionIcon = document.getElementById("predictionIcon");
const predictionDescription = document.getElementById("predictionDescription");

const scannedUrl = document.getElementById("scannedUrl");
const modelProbability = document.getElementById("modelProbability");
const analysisRiskLevel = document.getElementById("analysisRiskLevel");

const reasonsList = document.getElementById("reasonsList");
const scanAgain = document.getElementById("scanAgain");

scanButton.addEventListener("click", scanURL);

urlInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        scanURL();
    }
});

async function scanURL() {
    const url = urlInput.value.trim();
    if (!url) {
        urlInput.focus();
        return;
    }

    scanButton.disabled = true;
    scanButton.innerHTML = "ANALYZING <span>...</span>";

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify({
                url: url
            })
        });
        if (!response.ok) {
            throw new Error("Prediction request failed.");
        }
        const data = await response.json();
        displayResult(data);

    } catch (error) {
        console.error(error);
        alert(
            "Unable to analyze the URL. Make sure the FastAPI server is running."
        );
    } finally {
        scanButton.disabled = false;
        scanButton.innerHTML = 'ANALYZE <span>→</span>';

    }
}
function displayResult(data) {

    resultSection.classList.remove("hidden");

    const score = Number(data.risk_score) || 0;
    const probability = Number(data.model_probability) || 0;
    riskScore.textContent = `${score.toFixed(1)}%`;
    modelProbability.textContent = `${probability.toFixed(1)}%`;
    riskLevel.textContent = String(
        data.risk_level || "Unknown"
    ).toUpperCase();

    analysisRiskLevel.textContent = String(
        data.risk_level || "Unknown"
    ).toUpperCase();

    riskMeter.style.width = `${Math.min(score, 100)}%`;
    prediction.textContent = String(
        data.prediction || "Unknown"
    ).toUpperCase();

    scannedUrl.textContent = data.url || "";
    if (data.prediction === "Phishing") {
        predictionIcon.textContent = "!";
        predictionDescription.textContent =
            "This URL shows characteristics associated with phishing.";
        predictionIcon.style.color = "var(--danger)";
        predictionIcon.style.background =
            "rgba(255, 92, 112, 0.10)";
        predictionIcon.style.borderColor =
            "rgba(255, 92, 112, 0.20)";
        riskMeter.style.background = "var(--danger)";

    } else {
        predictionIcon.textContent = "✓";
        predictionDescription.textContent =
            "No major suspicious characteristics detected.";
        predictionIcon.style.color = "var(--accent)";
        predictionIcon.style.background =
            "rgba(53, 214, 163, 0.10)";
        predictionIcon.style.borderColor =
            "rgba(53, 214, 163, 0.20)";
        riskMeter.style.background = "var(--accent)";

    }
    displayReasons(data.reasons);
    resultSection.scrollIntoView({
        behavior: "smooth",
        block: "start"
    });

}

function displayReasons(reasons) {
    reasonsList.innerHTML = "";
    if (!reasons || reasons.length === 0) {
        const message = document.createElement("div");
        message.className = "no-reasons";
        message.textContent =
            "No major suspicious URL characteristics detected.";
        reasonsList.appendChild(message);
        return;

    }

    reasons.forEach(function(reason) {
        const item = document.createElement("div");
        item.className = "reason-item";
        item.textContent = reason;
        reasonsList.appendChild(item);

    });

}
scanAgain.addEventListener("click", function() {

    resultSection.classList.add("hidden");
    urlInput.value = "";
    urlInput.focus();
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

});