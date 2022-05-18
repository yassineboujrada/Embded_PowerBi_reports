
// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.8.1/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.8.1/firebase-analytics.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyCPeLozDHk6Sn2_KGlqZA_YWdrQQBTNNnc",
    authDomain: "db-awelk.firebaseapp.com",
    databaseURL: "https://db-awelk-default-rtdb.firebaseio.com",
    projectId: "db-awelk",
    storageBucket: "db-awelk.appspot.com",
    messagingSenderId: "37231178359",
    appId: "1:37231178359:web:b4e5fae6e61555dce7cc72",
    measurementId: "G-VX1NF3YBG7"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
