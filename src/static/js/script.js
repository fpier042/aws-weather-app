document.addEventListener('DOMContentLoaded', function() {
    console.log('Weather Dashboard loaded');
    function updateTime() {
        const now = new Date();
        const options = { 
            weekday: 'long', year: 'numeric', month: 'long', day: 'numeric',
            hour: 'numeric', minute: 'numeric', hour12: true
        };
        document.getElementById('current-time').textContent = now.toLocaleDateString('en-US', options);
    }
    updateTime();
    setInterval(updateTime, 60000);
});