function greetUser() {
    let feature_1 = document.getElementById("feature_1").value;
    let feature_2 = document.getElementById("feature_2").value;
    let feature_3 = document.getElementById("feature_3").value;
    let feature_4 = document.getElementById("feature_4").value;
    let feature_5 = document.getElementById("feature_5").value;
    let feature_6 = document.getElementById("feature_6").value;
    let feature_7 = document.getElementById("feature_7").value;
    let feature_8 = document.getElementById("feature_8").value;
    let feature_9 = document.getElementById("feature_9").value;
    let feature_10 = document.getElementById("feature_10").value;
    let feature_11 = document.getElementById("feature_11").value;
    let feature_12 = document.getElementById("feature_12").value;
    let feature_13 = document.getElementById("feature_13").value;
    let feature_14 = document.getElementById("feature_14").value;
    let feature_15 = document.getElementById("feature_15").value;
    let feature_16 = document.getElementById("feature_16").value;

    fetch('http://172.16.9.31:8080/send_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
            feature_1: feature_1,
            feature_2: feature_2,
            feature_3: feature_3,
            feature_4: feature_4,
            feature_5: feature_5,
            feature_6: feature_6,
            feature_7: feature_7,
            feature_8: feature_8,
            feature_9: feature_9,
            feature_10: feature_10,
            feature_11: feature_11,
            feature_12: feature_12,
            feature_13: feature_13,
            feature_14: feature_14,
            feature_15: feature_15,
            feature_16: feature_16, 
        })
    })
    .then(response => response.json())
    .then(data_2 => {
        document.getElementById("greetingMessage").innerText = data_2.message1;

        ctx = document.getElementById("featureImportanceChart").getContext("2d");

        data = {
            labels: data_2.label,
            datasets: [{
            label: "Feature Importance",
            data: data_2.data_1, 
            backgroundColor: ["#4CAF50", "#FF9800", "#2196F3", "#9C27B0","#4CAF50", "#FF9800", "#2196F3", "#9C27B0","#4CAF50", "#FF9800", "#2196F3", "#9C27B0","#4CAF50", "#FF9800", "#2196F3", "#9C27B0", "#4CAF50", "#FF9800"],
            }]
        };

        new Chart(ctx, {
            type: "bar",
            data: data,
            options: { responsive: true, scales: { y: { beginAtZero: true } } }
        });

    })
    .catch(error => console.error('Lỗi:', error));
}