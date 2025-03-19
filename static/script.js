function toggleChat() {
    let chatWindow = document.getElementById("chatWindow");
    if (chatWindow.style.display === "none" || chatWindow.style.display === "") {
        chatWindow.style.display = "flex";
    } else {
        chatWindow.style.display = "none";
    }
}

function sendMessage() {
    let userInput = document.getElementById("userInput").value;
    let chatBody = document.getElementById("chatBody");

    if (userInput.trim() === "") return;

    // Append user message with avatar
    let userMessageContainer = document.createElement("div");
    userMessageContainer.classList.add("message", "user-message");

    let userAvatar = document.createElement("img");
    userAvatar.src = "/static/user.png"; // Replace with actual user image path
    userAvatar.classList.add("avatar", "user-avatar");

    let userText = document.createElement("span");
    userText.innerText = userInput;

    userMessageContainer.appendChild(userText);
    userMessageContainer.appendChild(userAvatar);
    chatBody.appendChild(userMessageContainer);

    chatBody.scrollTop = chatBody.scrollHeight;
    document.getElementById("userInput").value = "";

    // Fetch response from Flask backend
    fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        let botMessageContainer = document.createElement("div");
        botMessageContainer.classList.add("message", "bot-message");

        let botAvatar = document.createElement("img");
        botAvatar.src = "/static/Text new.png"; // Replace with actual bot image path
        botAvatar.classList.add("avatar", "bot-avatar");

        let botText = document.createElement("span");
        botText.innerText = data.response;

        botMessageContainer.appendChild(botAvatar);
        botMessageContainer.appendChild(botText);
        chatBody.appendChild(botMessageContainer);

        chatBody.scrollTop = chatBody.scrollHeight;
    })
    .catch(error => {
        console.error("Error:", error);
        let errorMessageContainer = document.createElement("div");
        errorMessageContainer.classList.add("message", "bot-message");
        errorMessageContainer.innerText = "Bot: Sorry, there was an error. Please try again!";
        chatBody.appendChild(errorMessageContainer);
        chatBody.scrollTop = chatBody.scrollHeight;
    });
}
