
const msg = document.getElementById("MSG"); 
const name = document.getElementById("name");
const Email = document.getElementById("email");
const password = document.getElementById("password");
const password2 = document.getElementById("password2");
const agree = document.getElementById("Agree");
const register = document.getElementById("Register");

register.onclick = function()
{
    if(agree.checked)
    {
        if(name.value == '')
        {
            msg.textContent = `You must enter your name!`
            msg.style.color = "red";
        }
        else if(Email.value == '')
        {
            msg.textContent = `You must enter your email !`
            msg.style.color = "red";
        }
        else if(password.value == '')
        {
            msg.textContent = `You must enter a password!`
            msg.style.color = "red";
        }
        else if(password.value != password2.value)
        {
            msg.textContent = `password not match, enter the password again`;
            msg.style.color = "red";
            password2.value = '';
        }
        else
        {
            
        } 
    }
    else
    {
        msg.textContent = `You have to agree to the terms & conditions!`;
        msg.style.color = "red";
    }
}