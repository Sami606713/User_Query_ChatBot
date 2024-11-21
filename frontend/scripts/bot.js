// Function to show loading state
function showLoading() {
    document.getElementById('loading-bar').style.display = 'block';
}

// Function to hide loading state
function hideLoading() {
    document.getElementById('loading-bar').style.display = 'none';
}

// Function to append user and bot messages dynamically
function appendMessage(message, sender) {
    let messageDiv = document.createElement('div');
    
    // Add different classes depending on the sender
    if (sender === 'user') {
        messageDiv.classList.add('user-message');
        messageDiv.innerText = message; // Plain text message
    } else if (sender === 'bot') {
        messageDiv.classList.add('bot-message');
        messageDiv.innerHTML = message; // Bot message can have HTML content
    }

    // Append the message to the chat body
    document.getElementById('chat-body').appendChild(messageDiv);

    // Scroll chat body to bottom to show latest message
    let chatBody = document.getElementById('chat-body');
    chatBody.scrollTop = chatBody.scrollHeight;
}

// Event listener for send button
document.getElementById('send-btn').addEventListener('click', function() {
    let userInput = document.getElementById('user-input').value;

    // If user input is not empty, process the message
    if (userInput.trim() !== "") {
        appendMessage(userInput, 'user'); // Append user message
        get_response(userInput)
        // appendMessage("How can I help you?", 'bot'); // Bot's immediate response

        // Clear the input field
        document.getElementById('user-input').value = '';
    }
});

// Function to fetch the bot's response from the server
function get_response(user_query) {
    console.log("Getting Data...");
    
    let options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify({
            "query": user_query
        })
    };

    // Fetch request to your API
    fetch("http://127.0.0.1:8000/response", options)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            let text = data['Response'][0];
            let video_id = data['Response'][1];
            const botResponse = `
                <div class="chat-message bot-message">
                    
                    <div class="bot-message">
                        <p>${text}</p>
                        <iframe width="360" height="200" src="https://www.youtube.com/embed/${video_id}" 
                            title="YouTube video player" frameborder="0" 
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                            referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
                        </iframe>
                    </div>
                </div>
            `;

            // Append the bot's response
            appendMessage(botResponse, 'bot');
        })
        .catch(error => {
            console.error('Error:', error);
            appendMessage("Sorry, there was an error. Please try again.", 'bot');
        });
}
