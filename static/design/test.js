// var form = document.querySelector("form");
// var log = document.querySelector("#log");

// form.addEventListener("submit", function(event) {
//   var data = new FormData(form);
//   var output = "";
//   for (const entry of data) {
//     output = entry[0] + "=" + entry[1] + "\r";
//   };
//   log.innerText = output;
//   event.preventDefault();
// }, false);

// var show_pass=document.getElementById("show_password")
// var password_input=document.getElementById("password")

// show_pass.onclick = () => {
//     const type = password_input.getAttribute("type") === "password" ? "text" : "password";
//     password_input.setAttribute("type", type);
  
// }

//////////////////////    fech api for actualisation

// document.getElementById('select_nav').addEventListener("click", e => {
//     fetch("http://127.0.0.1:3000/dashbord", {
//         method: "POST",
//         headers: {
//           "Accept": "application/json",
//           "Content-Type": "application/json"
//         },
//         body: JSON.stringify({
//           c_check:String(e.target.innerText)
//         })
//       })
//       .then(res => {
//         if (!res.ok) {
//           throw Error(res.status);
//         }

//         return res.json();
//       })
//       .then(({data: {val}}) => {
//         console.log(val);
//         const res = document.querySelector(".result");
//         res.innerText = `client got: ${val}`;
//       })
//       .catch(err => console.error(err))
//     ;
//   })
// ;