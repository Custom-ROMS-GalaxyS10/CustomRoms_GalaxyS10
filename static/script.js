fetch("/api/roms")
.then(res => res.json())
.then(data => {
    const container = document.getElementById("container");

    for (let device in data) {
        let box = document.createElement("div");
        box.className = "box";

        box.innerHTML = `<h2>${device}</h2>`;

        if (data[device].length === 0) {
            box.innerHTML += "<p>Pusto</p>";
        } else {
            data[device].forEach(file => {
                box.innerHTML += `<p>📦 ${file}</p>`;
            });
        }

        container.appendChild(box);
    }
});