function showPassword() {
    var passwordField = document.getElementById("password");
    var eyeicon = document.getElementById("eyeicon")
    
    if (passwordField.type == "password"){
        passwordField.type = "text";
        eyeicon.src = "source/icons/eye-close.png";
    }
    else{
        passwordField.type = "password";
        eyeicon.src = "source/icons/eye-open.png";
    }


    }  