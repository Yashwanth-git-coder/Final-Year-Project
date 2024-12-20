document.getElementById('send-button').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keypress', function (e) {
  if (e.key === 'Enter') sendMessage();
});

function sendMessage() {
  const userInput = document.getElementById('user-input');
  const messageText = userInput.value.trim();

  if (messageText === '') return;

  displayMessage(messageText, 'user-message');
  userInput.value = '';

  // Simulate sending the message to the backend and receiving a response
  fetch('/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ message: messageText }),
})
  .then((response) => response.json())
  .then((data) => {
    displayMessage(data.response, 'ai-message');
  })
  .catch((error) => {
    console.error('Error:', error);
    displayMessage('Something went wrong. Please try again.', 'ai-message');
  });
}

function displayMessage(text, className) {
  const messagesDiv = document.getElementById('messages');
  const messageDiv = document.createElement('div');
  messageDiv.classList.add('message', className);
  messageDiv.textContent = text;
  messagesDiv.appendChild(messageDiv);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}
