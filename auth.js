// auth.js - Frontend Logic

const SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbyKUrP28dEY_Ma2EirPSf7VwGjQBzKo09Bpm5riLzHth0a7bE4uildUq7-2v_Ri7icy/exec';

// Form Toggling
function toggleForm(formId) {
    document.getElementById('login-form').classList.add('hidden');
    document.getElementById('signup-form').classList.add('hidden');
    document.getElementById('forgot-form').classList.add('hidden');
    
    document.getElementById('alert-box').style.display = 'none';
    
    setTimeout(() => {
        document.getElementById(formId + '-form').classList.remove('hidden');
    }, 100);
}

// Alert Handling
function showAlert(message, type) {
    const alertBox = document.getElementById('alert-box');
    alertBox.textContent = message;
    alertBox.className = 'alert alert-' + type + ' fade-in';
    alertBox.style.display = 'block';
    
    setTimeout(() => {
        alertBox.style.display = 'none';
    }, 5000);
}

// Set Loading State
function setLoading(buttonId, isLoading) {
    const btn = document.getElementById(buttonId);
    if (!btn) return;
    if (isLoading) {
        btn.classList.add('loading');
        btn.disabled = true;
    } else {
        btn.classList.remove('loading');
        btn.disabled = false;
    }
}

// Handle Form Submission via Google Apps Script JSONP
function handleAuth(event, action) {
    event.preventDefault();

    const btnId = 'btn-' + action;
    setLoading(btnId, true);
    document.getElementById('alert-box').style.display = 'none';

    // We generate a unique callback function name to avoid collisions
    const callbackName = 'handleResponse_' + Date.now();
    const script = document.createElement('script');
    
    let url = `${SCRIPT_URL}?callback=${callbackName}&t=${Date.now()}`;

    // Variables for parameters
    let phone, password, name, classCode;

    if (action === 'login') {
        phone = document.getElementById('login-phone').value.trim();
        password = document.getElementById('login-password').value.trim();
        url += `&action=login&phone=${encodeURIComponent(phone)}&password=${encodeURIComponent(password)}`;
    } else if (action === 'signup') {
        name = document.getElementById('signup-name').value.trim();
        email = document.getElementById('signup-email') ? document.getElementById('signup-email').value.trim() : "";
        phone = document.getElementById('signup-phone').value.trim();
        classCode = document.getElementById('signup-code').value.trim();
        password = document.getElementById('signup-password').value.trim();
        // The old backend uses "register" as the action
        url += `&action=register&name=${encodeURIComponent(name)}&email=${encodeURIComponent(email)}&phone=${encodeURIComponent(phone)}&classCode=${encodeURIComponent(classCode)}&password=${encodeURIComponent(password)}`;
    } else if (action === 'forgot') {
        phone = document.getElementById('forgot-phone').value.trim();
        password = document.getElementById('forgot-password').value.trim();
        // The old backend uses "reset" as the action
        url += `&action=reset&phone=${encodeURIComponent(phone)}&password=${encodeURIComponent(password)}`;
    }

    window[callbackName] = function(data) {
        setLoading(btnId, false);
        
        if (action === 'login') {
            if (data.success) {
                // Successful login
                sessionStorage.setItem('isLoggedIn', 'true');
                if(data.name) sessionStorage.setItem('userName', data.name);
                
                showAlert("Sign in successful! Redirecting...", "success");
                setTimeout(() => {
                    window.location.href = 'intro.html';
                }, 1000);
            } else {
                showAlert("Incorrect Phone Number or Password.", "error");
            }
        } else if (action === 'signup') {
            if (data.success) {
                showAlert("Registration Successful! You can now sign in.", "success");
                setTimeout(() => {
                    document.getElementById('signup-form').reset();
                    toggleForm('login');
                }, 2000);
            } else {
                showAlert("Registration failed: " + (data.error || "Unknown error"), "error");
            }
        } else if (action === 'forgot') {
            if (data.success) {
                showAlert("Password Reset Successful! Log in with your new password.", "success");
                setTimeout(() => {
                    document.getElementById('forgot-form').reset();
                    toggleForm('login');
                }, 2000);
            } else {
                showAlert("Update failed. Phone number might not exist or be incorrect.", "error");
            }
        }

        // Cleanup the script tag
        try {
            document.body.removeChild(script);
            delete window[callbackName];
        } catch(e) {}
    };

    // Error handling for network failure - note JSONP doesn't give precise error codes
    script.onerror = function() {
        setLoading(btnId, false);
        showAlert("Failed to connect to the server. Please try again.", "error");
    };

    // Append script to trigger the request
    script.src = url;
    document.body.appendChild(script);
}
