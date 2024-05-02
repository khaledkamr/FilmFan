const users = {
    "kk@gmail.com": "0000", 
    "ak@gmail.com": "1111", 
    "ad@gmail.com": "2222"
};
 

const msg = document.getElementById("CodeMSG"); 
let forget = document.getElementById("forget");
const login = document.getElementById("login");
const Email = document.getElementById("email");
const password = document.getElementById("password");
const rememberMe = document.getElementById("Rememberme");

forget.onclick = function()
{
    msg.textContent = `We sent code to your Email, please enter the code instead of the password`;
    msg.style.color = "black";
}

login.onclick = function()
{
    if(Email.value in users && users[Email.value] == password.value)
    {
        msg.textContent = `login successfully✅`;
        msg.style.color = "green";
        location.href = "{% url 'home' %}";
    }
    else
    {
        msg.textContent = `something went wrong, please try again!`;
        msg.style.color = "red";
        Email.value = '';
        password.value = '';
    }
}
    

