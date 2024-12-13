const url = 'LAMBDA URL';

// Data to send in the body of the POST request
const postData = {
  system: "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
  user: "Compose a poem that explains the concept of recursion in programming."
}

// Make the POST request
fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',  // Set the content type to JSON
    },
    body: JSON.stringify(postData),  // Convert the JavaScript object to a JSON string
})
.then(response => response.json())  // Parse the JSON response
.then(data => {
    console.log('Success:', data);  // Log the response data
})
.catch((error) => {
    console.error('Error:', error);  // Log any errors
});
