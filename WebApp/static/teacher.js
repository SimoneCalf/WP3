function func(){
    console.log("Hello from teacher.js");
      // get the email and password from the form
      let email = document.getElementById("exampleInputEmail1").value;
      let password = document.getElementById("exampleInputPassword1").value;
      console.log(email, password);

      //send the email and password to the backend
        fetch("/teacher/login", {
            method: "POST",
            body: JSON.stringify({email: email, password: password}),
            headers: {
            "Content-Type": "application/json"
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if(data.status == 200){
                window.location.href = "/teacher/dashboard";
            }
            else{
                alert("Invalid email or password");
            }
        });
   
};
