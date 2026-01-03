window.addEventListener("load", loadBusinesses);

async function loadBusinesses() {
  try {
    const res = await fetch("http://127.0.0.1:8000/businesses");
    const businesses = await res.json();

    const list = document.getElementById("business-list");
    list.innerHTML = "";

    businesses.forEach((b) => {
      const li = document.createElement("li");
      li.textContent = `#${b.id}: ${b.description}`;
      list.appendChild(li);
    });
  } catch (err) {
    console.error("Failed to load businesses:", err);
  }
}
