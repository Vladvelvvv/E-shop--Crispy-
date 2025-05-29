function showPassword() {
    var passwordField = document.getElementById("password");
    var eyeicon = document.getElementById("eyeicon")
    
    if (passwordField.type == "password"){
        passwordField.type = "text";
        eyeicon.src = '{% static "3. profile\source\icons\eye-close.png" %}';
    }
    else{
        passwordField.type = "password";
        eyeicon.src = '{% static "3. profile\source\icons\eye-open.png" %}';
    }
}  