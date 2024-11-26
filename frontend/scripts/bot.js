// DOM elements
const chatbotIcon = document.querySelector('.chatbot-icon');
const chatbotContainer = document.querySelector('.chatbot-container');
const closeIcon = document.querySelector('.close-icon');
const sendButton = document.getElementById('send-btn');
const userInput = document.getElementById('user-input');

// Show chatbot on icon click
chatbotIcon.addEventListener('click', () => {
    chatbotContainer.style.display = 'flex';
    chatbotIcon.style.display = 'none';
});

// Close chatbot on close icon click
closeIcon.addEventListener('click', () => {
    chatbotContainer.style.display = 'none';
    chatbotIcon.style.display = 'flex';
});

// Show loading state
function showLoading() {
    const chatBody = document.getElementById('chat-body');
    const loadingBar = document.createElement('div');
    loadingBar.className = 'loading-bar';
    loadingBar.id = 'loading-bar'; // To ensure we can hide it later
    loadingBar.innerHTML = `
        <div class="progress"></div>
        <span>Loading...</span>
    `;
    chatBody.appendChild(loadingBar);
    chatBody.scrollTop = chatBody.scrollHeight; // Scroll to bottom
}

// Hide loading state
function hideLoading() {
    const loadingBar = document.getElementById('loading-bar');
    if (loadingBar) {
        loadingBar.remove();
    }
}

// Append messages to the chat
function appendMessage(message, sender) {
    const chatBody = document.getElementById('chat-body');
    const messageDiv = document.createElement('div');
    messageDiv.className = sender === 'user' ? 'user-message' : 'bot-message';
    messageDiv.innerHTML = message;
    chatBody.appendChild(messageDiv);
    chatBody.scrollTop = chatBody.scrollHeight;
}

// Send message event
sendButton.addEventListener('click', () => {
    showLoading();
    const userQuery = userInput.value.trim();
    if (userQuery) {
        appendMessage(userQuery, 'user');
        userInput.value = '';
        
        getResponse(userQuery);
    }
});

// Fetch bot response
function getResponse(query) {
    console.log("Getting Data...");
    
    fetch("http://127.0.0.1:8000/response", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query })
    })
        .then(res => res.json())
        .then(data => {
            const botResponse = `
            <p>${parseResponse(data.Response[0])}</p>
            <iframe width="360" height="200" src="https://www.youtube.com/embed/${data.Response[1]}" 
            frameborder="0" allowfullscreen></iframe>`;
            appendMessage(botResponse, 'bot');
            hideLoading();
        })
        .catch(err => {
            console.error(err);
            appendMessage("Sorry, there was an error. Please try again.", 'bot');
            hideLoading();
        });
}
// Function to parse response
function parseResponse(response) {
    // Replace links and formats appropriately
    const formattedText = response
        .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>") // Bold text
        .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank">$1</a>'); // Links
    
    return formattedText; // Return parsed text
}

