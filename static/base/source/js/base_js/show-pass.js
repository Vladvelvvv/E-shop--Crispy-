function showPassword() {
    var passwordField = document.getElementById("password");
    var eyeicon = document.getElementById("eyeicon")
    
    if (passwordField.type == "password"){
        passwordField.type = "text";
        eyeicon.src = '..\base\source\files\base_files\password-eye\eye-close.png';
    }
    else{
        passwordField.type = "password";
        eyeicon.src = '..\base\source\files\base_files\password-eye\eye-open.png';
    }
}  