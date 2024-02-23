<template>
    <form @submit.prevent="submitForm">
        <h1 class="LoginHeader">Login </h1>
        <label>Username:</label>
        <input type="username" required v-model="username">

        <label>Password:</label>
        <input type="password" required v-model="password">

        <div class="submit">
            <button>Login</button>
        </div>

        <div class="registerClient">
            <p>
                Don't have an account? <a href="#">Register</a>
            </p>
        </div>
    </form>

</template>
 
<script>
export default {
    data() {
        return {
            username: '',
            password: ''
        }
    },
    methods: {
        submitForm() {
            console.log('The form has been submitted')
        }
    }
}
</script>

<style scoped>

.LoginHeader {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 40px;
}
 form {
    max-width: 420px;
    margin: 30px auto;
    background: white;
    text-align: left;
    padding: 40px;
    border-radius: 10px;
 }
 label {
    color: #aaa;
    display: inline-block;
    margin: 25px 0 15px;
    font-size: 0.6em;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: bold;
 }
 input {
    display: block;
    padding: 10px 6px;
    width: 100%;
    box-sizing: border-box;
    border: none;
    border-bottom: 1px solid #ddd;
    color: #555;
 }
 button {
    background: #0b6dff;
    border: 0;
    padding: 10px 20px;
    margin-top: 20px;
    color: white;
    border-radius: 20px;
 }
 .submit {
    text-align: center;
 }
 .registerClient {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    text-align: center;
    margin-top: 20px;
 }

 body {
  margin: 0;
  background: #eee;
}
</style>