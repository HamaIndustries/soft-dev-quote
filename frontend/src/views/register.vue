<template>
    <div class="regisPage">
        <h1 class="regisHeader">Registration</h1>
        <form class="regisForm" @submit.prevent="handleSubmit"> 
            <label>Company Name: </label>
            <input type="text" required v-model="companyName">


            <label>Create Username: </label>
            <input type="text" required v-model="username">

            <label>Create Password: </label>
            <input type="password" required v-model="password">
            <div v-if="passwordError" class="pwError">{{ passwordError }}</div>

            <label>Confirm Password: </label>
            <input type="password" required v-model="confirmPassword">

            <button type="submit" class="createAccount">Create Account</button>
        </form>

    </div>
</template>

<script>
export default {
    data() {
        return {
            companyName: "",
            username: "",
            password: "",
            confirmPassword: "",
            passwordError: ""
        };
    },

    methods: {
        handleSubmit() {
            if (this.password.length < 5) {
                this.passwordError = "Password must be at least 5 characters long";
                return;
            }
            if (this.password !== this.confirmPassword) {
                this.passwordError = "Passwords do not match!";
                return;
            }
            this.passwordError = "";
            console.log("regis form submitted")
        }
    }



}


</script>

<style>

.body {
    color: #333;
    background-color: #eef2f3;
}

.regisPage {
    text-align: center;
}

.pwError {
    color: black;
    margin-top: 10px;
    font-size: bold;
    font-weight:400;
}

.regisHeader {
    padding-left: 30px;
    font-family: Avenir, Arial, Helvetica, sans-serif;
    font-size: bold;
    margin-bottom: 20px;
    font-weight: 550;
    font-size: 40px;
    color: white;
    letter-spacing: 3px;
}
.regisForm {
    width: 600px;
    text-align: left;
    margin-left: 30px;
    background: white;
    padding:40px;
    border-radius: 15px;
}

.createAccount {
    border: 0;
    padding: 10px 15px;
    font-family: Avenir, Arial, Helvetica, sans-serif;
    margin-top: 35px;
    margin-left: 130px;
    background:lightskyblue;
    color: white;
    border-radius: 20px;
    font-weight: 520;
    font-size:25px;
    transition: 0.3s;
    letter-spacing: 1px;

}
.createAccount:hover {
    background: darkcyan;
}



label {
    color: #aaa;
    display: inline-block;
    margin: 25px 0 15px;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-weight: bold;
}

input {
    display: block;
    padding: 10px 6px;
    width: 100%;
    box-sizing: border-box;
    border: none;
    border-bottom: 1px solid #ddd;
    color: rgb(68, 38, 38);
}

</style>

