document.querySelector('form').addEventListener('submit', function (e) {
    const name = document.getElementById('name').value;
    const message = name 
        ? `Hello, ${name}, you can vote!` 
        : `Hello, ${name}, you cannot vote.`;
    alert(message);
});
