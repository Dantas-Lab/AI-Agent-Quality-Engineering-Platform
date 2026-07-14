const chatForm = document.getElementById("chat-form");
const messageInput = document.getElementById("message-input");
const messages = document.getElementById("messages");

chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const message = messageInput.value;

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            message: message,
            session_id: "web-session-001",
        }),
    });

    const data = await response.json();

    const sources = data.sources.length > 0
        ? data.sources.join(", ")
        : "No sources available";

    messages.innerHTML += `
        <p><strong>User:</strong> ${message}</p>
        <p><strong>Assistant:</strong> ${data.answer}</p>
        <p><strong>Sources:</strong> ${sources}</p>
        <hr>
    `;

    messageInput.value = "";
});