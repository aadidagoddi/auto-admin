document.getElementById("submit-btn").addEventListener("click", submitBusiness);

function submitBusiness() {
  const description = document.getElementById("desc").value;

  fetch("http://127.0.0.1:8000/business", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ description }),
  })
    .then((res) => res.json())
    .then((data) => {
      alert(data.message);
      window.location.href = "dashboard.html"; // redirect to dashboard
    })
    .catch((err) => console.error("Error submitting business:", err));
}
